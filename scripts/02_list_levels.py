# -*- coding: utf-8 -*-
"""02 - List all Levels with elevation in mm (read-only)."""
from pyrevit import revit
from Autodesk.Revit.DB import FilteredElementCollector, Level

doc = revit.doc

# FilteredElementCollector is the core way to query elements.
levels = FilteredElementCollector(doc).OfClass(Level).ToElements()

# Elevation is in feet internally: convert to mm.
for lvl in sorted(levels, key=lambda l: l.Elevation):
    print("{:<30} {:>10.0f} mm".format(lvl.Name, lvl.Elevation * 304.8))
