"""Command-line interface.

    python -m nzcpi nowcast [--quarter 2026Q2] [--uncovered seasonal|carry]
                            [--top N] [--csv out.csv] [--refresh]
    python -m nzcpi backtest [--start 2018Q1] [--uncovered seasonal|carry]
                             [--csv out.csv] [--refresh]
"""

from __future__ import annotations

import argparse
import sys

import numpy as np

from .model import BottomUpCPI, parse_quarter, quarter_label


def _fmt(x, nd=2):
    return "n/a" if x is None else f"{x:+.{nd}f}"


def cmd_nowcast(args) -> int:
    model = BottomUpCPI(refresh=args.refresh)
    qp = parse_quarter(args.quarter) if args.quarter else None
    r = model.estimate(qp, uncovered=args.uncovered, hist_years=args.hist_years)

    print(f"\nBottom-up CPI estimate — {quarter_label(r.quarter)}")
    print("=" * 46)
    print(f"Quarterly change : {_fmt(r.qoq_pct)} %")
    print(f"Annual change    : {_fmt(r.annual_pct)} %")
    if r.actual_qoq_pct is not None:
        print(f"Official (actual): {_fmt(r.actual_qoq_pct)} %  "
              f"(error {r.qoq_pct - r.actual_qoq_pct:+.2f} pp)")
    print(f"Basket priced from monthly Stats NZ data: {r.covered_weight_pct:.1f}%")
    if 0 < r.months_available < 3:
        print(f"NOTE: only {r.months_available} of 3 months of monthly data "
              f"published so far for {quarter_label(r.quarter)} — partial-quarter estimate.")
    uncov = r.detail[r.detail.source != "spi"]
    print(f"Remaining {uncov.weight_pct.sum():.1f}% of basket assumed via "
          f"'{args.uncovered}' rule.")

    top = r.detail.head(args.top).copy()
    print(f"\nLargest contributions ({args.top} of {len(r.detail)} components):")
    print(f"{'component':<44} {'src':<8} {'wgt%':>6} {'qoq%':>7} {'contr pp':>9}")
    for _, row in top.iterrows():
        print(f"{row['name'][:44]:<44} {row.source:<8} {row.weight_pct:>6.2f} "
              f"{row.qoq_pct:>7.2f} {row.contribution_pp:>9.3f}")

    if args.csv:
        r.detail.to_csv(args.csv, index=False)
        print(f"\nFull component table written to {args.csv}")
    return 0


def cmd_backtest(args) -> int:
    model = BottomUpCPI(refresh=args.refresh)
    start = parse_quarter(args.start)
    bt = model.backtest(start=start, uncovered=args.uncovered,
                        hist_years=args.hist_years)
    if bt.empty:
        print("No quarters to backtest.")
        return 1
    err = bt["error_pp"]
    print(f"\nBacktest ({args.uncovered} rule) — {bt.quarter.iloc[0]} to "
          f"{bt.quarter.iloc[-1]}, {len(bt)} quarters")
    print("=" * 56)
    print(bt.to_string(index=False))
    print("-" * 56)
    print(f"MAE  {err.abs().mean():.3f} pp   RMSE {np.sqrt((err ** 2).mean()):.3f} pp"
          f"   max|err| {err.abs().max():.3f} pp")
    n8 = min(8, len(bt))
    print(f"Last {n8} quarters MAE: {err.tail(n8).abs().mean():.3f} pp")
    if args.csv:
        bt.to_csv(args.csv, index=False)
        print(f"Backtest table written to {args.csv}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="nzcpi",
                                description="Bottom-up NZ CPI nowcast from public Stats NZ data")
    sub = p.add_subparsers(dest="cmd", required=True)

    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--uncovered", choices=["seasonal", "carry"],
                        default="seasonal",
                        help="treatment of basket items with no monthly source")
    common.add_argument("--hist-years", type=int, default=5,
                        help="years of history for the seasonal rule")
    common.add_argument("--refresh", action="store_true",
                        help="re-download source data even if cached")
    common.add_argument("--csv", help="write detail table to CSV")

    pn = sub.add_parser("nowcast", parents=[common],
                        help="estimate one quarter (default: first unpublished)")
    pn.add_argument("--quarter", help="e.g. 2026Q2")
    pn.add_argument("--top", type=int, default=15,
                    help="components to display")
    pn.set_defaults(func=cmd_nowcast)

    pb = sub.add_parser("backtest", parents=[common],
                        help="compare estimates with published CPI")
    pb.add_argument("--start", default="2018Q1")
    pb.set_defaults(func=cmd_backtest)

    args = p.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
