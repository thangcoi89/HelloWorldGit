# HelloWorldGit
Hi there!
I'm new to Github, I 'm playing Skyrim SE (Nord Race), I joined Thief Guild and I like Rouge build stype.
I want to learn Revit API and coding for Revit

## Revit scripting starter
Read-only learning scripts for [pyRevit](https://github.com/pyrevitlabs/pyRevit). Revit version: [TBC].

| Script | What it shows |
|---|---|
| `scripts/01_hello_revit.py` | Revit version, document title |
| `scripts/02_list_levels.py` | `FilteredElementCollector`, feet to mm |
| `scripts/03_count_by_category.py` | Count elements per category, optional CSV |
| `scripts/04_read_parameters.py` | Read a parameter from the selection |

Shared code is in `lib/helpers.py`. Notes go in `docs/learning-log.md`.

### How to run
1. Install pyRevit and open a test model in Revit.
2. In pyRevit, add this repo's `scripts` folder as an extension/script path, or paste a script into the pyRevit Python shell.
3. Run a script and read the output window.
