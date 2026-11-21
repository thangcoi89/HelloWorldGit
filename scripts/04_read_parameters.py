# -*- coding: utf-8 -*-
"""04 - Read a parameter from the selected elements (read-only)."""
from pyrevit import revit, forms

PARAM_NAME = "Mark"  # change to any instance parameter name

doc = revit.doc
selection = revit.get_selection()

if not selection:
    forms.alert("Select one or more elements first.", exitscript=True)

for el in selection.elements:
    p = el.LookupParameter(PARAM_NAME)   # returns None if not found
    if p is None:
        value = "[parameter not found]"
    else:
        value = p.AsValueString() or p.AsString()
    print("Id {} | {} | {} = {}".format(
        el.Id.IntegerValue, el.Category.Name if el.Category else "-", PARAM_NAME, value))
