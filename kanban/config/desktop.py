# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from frappe import _

def get_data():
	return {
		"Kanban": {
			"color": "red",
			"icon": "octicon octicon-file-directory",
			"type": "module",
			"label": _("Kanban")
		}
	}
