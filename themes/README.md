# Making a theme

A theme is a small **palette**: it maps a dozen named *roles* (success, failure,
frames, ids, …) to **256-colour codes**, so switching themes retunes every hue in
the UI at once. Built-in themes are `neon` (the default), `amber`, `forest`, and
`mono`; your own are just JSON files dropped in this folder — no code, no
restart needed.

## Make one in four steps

1. **Copy a starting point.** The quickest start is to copy a built-in's shape:

   ```bash
   cp themes/ocean.json themes/sunset.json
   ```

   The file name (without `.json`) is the theme's name — this makes a theme
   called `sunset`.

2. **Pick colours.** Every value is a 256-colour code, `0`–`255`. Print the whole
   palette in *your* terminal (colours vary by terminal, so choose in the one
   you'll use) and read off the numbers you like:

   ```bash
   for i in $(seq 0 255); do printf '\033[38;5;%sm%4d' "$i" "$i"; done; echo
   ```

3. **Edit the roles** (table below). You only need the ones you want to change —
   anything you omit inherits from `neon`, so a two-line file is valid:

   ```json
   { "cyan": 39, "ramp": [45, 39, 33, 27, 75, 81] }
   ```

4. **Preview it live** and iterate:

   ```bash
   theme sunset            # or: python3 start.py theme sunset
   ```

   Switching applies immediately. Tweak the JSON, run `theme sunset` again, and
   watch it change. Your theme also appears in the `theme` list and the `begin`
   menu next to the built-ins.

## The roles

Every value is one 256-colour code (`0`–`255`), except `ramp`.

| Role | Colours… |
|---|---|
| `cyan` | the **structure**: frames, headers, labels (the dominant UI hue) |
| `byellow` | puzzle **ids and titles** (the bright highlight) |
| `bcyan` | the **"you are here"** marker and the active title |
| `green` / `red` | **success** / **failure** |
| `bgreen` / `bred` | bright success / failure (e.g. `CHECK PASSED`) |
| `yellow` | **hints** |
| `magenta` | **mode** / **solution** |
| `blue` | **file paths** |
| `white` | strong, emphasised text |
| `gray` | dim, secondary text |
| `ramp` | a list of **6** codes for the logo's top-to-bottom **gradient** |

For the logo `ramp`, pick six codes that step smoothly from one end of a hue to
the other (light→dark, or one colour→a neighbour); the built-ins are good
references.

## A complete example

[`ocean.json`](ocean.json) sets every role — a good template to copy:

```json
{
  "cyan": 39, "byellow": 81, "bcyan": 51,
  "green": 48, "red": 203, "bgreen": 84, "bred": 210,
  "yellow": 117, "magenta": 75, "blue": 45,
  "white": 231, "gray": 244,
  "ramp": [51, 45, 39, 33, 27, 75]
}
```

## Good to know

- **Build on a built-in.** Because omitted roles inherit `neon`, the easiest
  theme is one that overrides just a few roles. To re-tune a *different* base,
  copy that built-in's values out of `engine/theme.py` (`THEMES`) first.
- **Override a built-in.** Name your file after one (`themes/neon.json`) to
  replace it.
- **You can't break anything.** Codes are clamped to `0`–`255`, a malformed or
  non-JSON file is skipped silently, and any missing/invalid role falls back to
  `neon`. The worst case is a theme that just looks like `neon`.
- **No colour, no problem.** On a terminal without colour support the UI is
  monochrome and themes simply have no visible effect.

See the [main README](../README.md) for the `theme` command and persistence (your
choice is saved in `settings.json`).
