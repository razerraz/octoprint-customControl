# coding=utf-8
from __future__ import absolute_import

__author__ = "Marc Hannappel <sunpack@web.de>"
__license__ = 'GNU Affero General Public License http://www.gnu.org/licenses/agpl.html'
__copyright__ = "Copyright (C) 2014 The OctoPrint Project - Released under terms of the AGPLv3 License"

from octoprint.settings import settings

import octoprint.plugin

class CustomControlPlugin(octoprint.plugin.SettingsPlugin,
						  octoprint.plugin.TemplatePlugin,
						  octoprint.plugin.AssetPlugin):

	def get_settings_defaults(self):
		return dict(
			controls = []
			)

	def get_template_configs(self):
		if "editorcollection" in self._plugin_manager.enabled_plugins:
			return [
				dict(type="plugin_editorcollection_EditorCollection", template="customControl_hookedsettings.jinja2", custom_bindings=True)
			]
		else:
			return [
				dict(type="settings", template="customControl_hookedsettings.jinja2", custom_bindings=True)
			]

	def on_settings_save(self, data):
		s = settings()
		s.set(["controls"], data["controls"])

	def get_assets(self):
		return dict(
			js=[
				"js/customControl.js",
				"js/customControlDialog.js",
			],
			css=["css/customControls.css"],
			less=["less/customControls.less"]
		)

# If you want your plugin to be registered within OctoPrint under a different name than what you defined in setup.py
# ("OctoPrint-PluginSkeleton"), you may define that here. Same goes for the other metadata derived from setup.py that
# can be overwritten via __plugin_xyz__ control properties. See the documentation for that.
__plugin_name__ = "CustomControl"
__plugin_license__ = "AGPLv3"
__plugin_implementation__ = CustomControlPlugin()
