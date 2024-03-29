# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "kanban"
app_title = "Kanban"
app_publisher = "Alec Ruiz-Ramon"
app_description = "Kanban view to plug-into various doctypes, especially Projects and CRM"
app_icon = "octicon octicon-file-directory"
app_color = "red"
app_email = "alec.ruizramon@me.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kanban/css/kanban.css"
# app_include_js = "/assets/kanban/js/kanban.js"

# include js, css files in header of web template
# web_include_css = "/assets/kanban/css/kanban.css"
# web_include_js = "/assets/kanban/js/kanban.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "kanban.install.before_install"
# after_install = "kanban.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kanban.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kanban.tasks.all"
# 	],
# 	"daily": [
# 		"kanban.tasks.daily"
# 	],
# 	"hourly": [
# 		"kanban.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kanban.tasks.weekly"
# 	]
# 	"monthly": [
# 		"kanban.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "kanban.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kanban.event.get_events"
# }

