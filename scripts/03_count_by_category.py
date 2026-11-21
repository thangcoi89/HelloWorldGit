# -*- coding: utf-8 -*-
"""03 - Count model elements per category and print the result (read-only).

Optional: set CSV_PATH to also export. It will overwrite that file, so use a new name.
"""
from collections import Counter
from pyrevit import revit
from Autodesk.Revit.DB import FilteredElementCollector

CSV_PATH = None  # e.g. r"C:\Temp\category_count_261120.csv"

doc = revit.doc

# WhereElementIsNotElementType() skips types, keeping placed instances only.
elements = FilteredElementCollector(doc).WhereElementIsNotElementType().ToElements()

counts = Counter()
for el in elements:
    if el.Category is not None:      # some elements have no category
        counts[el.Category.Name] += 1

for name, n in counts.most_common():
    print("{:<40} {:>6}".format(name, n))

if CSV_PATH:
    import sys, os
    sys.path.append(os.path.join(os.path.dirname(__file__), "..", "lib"))
    from helpers import write_csv
    write_csv(CSV_PATH, ["Category", "Count"], counts.most_common())
    print("Saved: {}".format(CSV_PATH))
