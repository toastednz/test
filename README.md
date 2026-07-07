# ⚽ World Cup 2026 Flag Game

A talking flag game for little kids — all **48 teams** of the FIFA World Cup 2026.

A flag appears, the game asks *"What country is this?"* out loud, and your child
**says the country's name into the microphone**. Get it right → cheering, confetti,
and the next flag. After two tries the game gently says the answer and asks the
child to repeat it, then moves on.

## How to play

1. Open `index.html` in **Chrome or Edge** (they have the best speech recognition).
   Double-clicking the file works, or host it anywhere (e.g. GitHub Pages).
2. Press **Play** and allow the microphone when the browser asks.
3. Kid looks, kid says the name, game does the rest. No reading needed —
   everything is spoken aloud.

### Grown-up corner (bottom-right)

- **✔️ got it** — mark the answer correct if the mic mis-heard
- **⏭️ skip** — move to the next flag
- **🔊 / 🔇** — sound on/off

## Notes

- Flags are embedded in `flags-data.js`, so the game works offline too
  (only the optional Gemini backup judge needs internet).
- Optionally, a Google AI Studio key in `index.html` (`CONFIG.GEMINI_KEY`) adds a
  backup judge for tricky kid-pronunciations. Only add a key on a private copy,
  and restrict it in Google Cloud Console — the game works fine without it.
- Recognition language follows the browser's language (falls back to `en-US`);
  change `CONFIG.LANG` in `index.html` if needed.
