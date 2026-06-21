# PyQuest documentation

Start by what you're trying to do.

## I want to *use* PyQuest (learn Python)
- **[../README.md](../README.md)** — install-free quick start, the command
  reference, difficulty modes, how saving works.
- **[../GETTING_STARTED.md](../GETTING_STARTED.md)** — a guided first session,
  step by step.

## I want to *author* content (puzzles & projects)
- **[SCHEMA.md](SCHEMA.md)** — every file and field: `meta.json`, `tests.py`
  and the `T` helpers, hints, dodges, the **projects** track (`kind`, debug
  puzzles, low-guidance capstones), and the `category` tier.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — the workflow, ground rules, and the
  audit gate every change must pass.
- **[SIDESTEP_PLAYBOOK.md](SIDESTEP_PLAYBOOK.md)** — how to make a lesson
  *unavoidable*, not just its output — the anti-cheat discipline.

## I want to *understand or change the engine*
- **[ARCHITECTURE.md](ARCHITECTURE.md)** — the prose design reference: the five
  concerns, the invariants, the module map, and how validation works. Read it
  before adding a feature.
- **[architecture/](architecture/README.md)** — the same design as **UML**
  (Mermaid) diagrams, led by a single **[master class
  diagrams](architecture/README.md#0-master-diagrams-every-module--class)**,
  then focused per-area pages:
  [engine-core](architecture/engine-core.md) ·
  [toolkit](architecture/toolkit.md) ·
  [commands](architecture/commands.md) ·
  [visuals](architecture/visuals.md) ·
  [audit](architecture/audit.md).

## I want to *translate or theme* it
- **[../lang/README.md](../lang/README.md)** — language packs (interface +
  textbook); English is the default and fallback.
- **[../themes/README.md](../themes/README.md)** — custom colour themes.

---

The course is **142 puzzles across 16 chapters**, grouped into **Core**
(Ch 1–14), **Advanced** (Ch 15), and **Projects** (Ch 16+). The single source of
truth for behaviour is `tools/audit.py` — there is no separate test suite.
