# Custom themes

How to add your own colour theme — see the [README](../README.md) for the
`theme` command itself.

Drop a JSON file in this folder to add your own colour theme. The file name
(without `.json`) becomes the theme name, so `themes/ocean.json` gives you a
theme called `ocean`. Select it with:

```
theme ocean          # or: python3 start.py theme ocean
```

Your presets show up in `theme` and in the `begin` menu alongside the built-in
themes (`neon`, `amber`, `forest`, `mono`), and can also override a built-in by
using the same name.

## Format

Every value is a **256-colour code** (an integer 0–255). Map any of these roles:

| Role | Used for |
|---|---|
| `cyan` | frames, headers, labels (the structural colour) |
| `byellow` | puzzle ids and titles (the bright highlight) |
| `bcyan` | the "you are here" marker / active title |
| `green` | success |
| `red` | failure |
| `yellow` | hints |
| `magenta` | mode / solution |
| `blue` | file paths |
| `white` | strong text |
| `gray` | secondary / dim text |
| `bgreen`, `bred` | bright success / failure |
| `ramp` | a list of **6** codes for the logo's top-to-bottom gradient |

Anything you leave out inherits from the built-in `neon` theme, so a minimal
preset is fine:

```json
{
  "cyan": 39,
  "ramp": [45, 39, 33, 27, 75, 81]
}
```

A 256-colour chart is one search away ("ANSI 256 color codes"). Malformed files
are skipped silently, so a typo won't break PyQuest.
