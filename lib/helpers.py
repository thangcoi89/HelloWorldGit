# -*- coding: utf-8 -*-
"""Shared helpers for the Revit learning scripts (pyRevit, IronPython 2.7 / CPython 3 safe)."""
import csv
import io

FEET_TO_MM = 304.8  # Revit stores lengths internally in feet


def get_doc():
    """Return (uidoc, doc) for the active Revit document. Works inside pyRevit."""
    from pyrevit import revit  # imported here so py_compile works outside Revit
    return revit.uidoc, revit.doc


def ft_to_mm(value_ft):
    """Convert internal feet to millimetres."""
    return value_ft * FEET_TO_MM


def write_csv(path, header, rows):
    """Write rows to a CSV file (UTF-8). Overwrites 'path', so pass a new file name."""
    with io.open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        w.writerows(rows)
