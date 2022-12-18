# Copyright (c) 2022, Warren Eiserman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestGymSettings(FrappeTestCase):
	# The Gym Settings contain important settings used across application
	# make sure the configuration exists and email is set
	def check_gym_configuration_has_been_set(self):
		settings = frappe.get_doc("Gym Settings")
		self.assertIsNotNone(settings.email)

