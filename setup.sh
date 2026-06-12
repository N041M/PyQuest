#!/usr/bin/env bash
#
# Back-compat wrapper. The real, intuitive command is:
#
#     python3 play.py setup
#
# It installs the optional shell shortcuts and prints a themed summary. This
# script just forwards to it so old habits (./setup.sh) keep working.
#
ROOT="$(cd "$(dirname "$0")" && pwd)"
exec python3 "$ROOT/play.py" setup
