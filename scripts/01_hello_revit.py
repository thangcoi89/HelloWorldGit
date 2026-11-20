# -*- coding: utf-8 -*-
"""01 - Hello Revit: print the Revit version and the active document title."""
from pyrevit import revit, script

output = script.get_output()
doc = revit.doc                      # the active Document
app = doc.Application                # the Revit Application object

output.print_md("**Hello Revit!**")
print("Revit version : {}".format(app.VersionName))
print("Document      : {}".format(doc.Title))
print("Is workshared : {}".format(doc.IsWorkshared))
