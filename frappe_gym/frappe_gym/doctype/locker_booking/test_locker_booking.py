# Copyright (c) 2022, Warren Eiserman and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestLockerBooking(FrappeTestCase):
	def test_cant_book_an_occupied_locker(self):
		test_locker = frappe.get_doc({
			"doctype" : "Locker",
			"location" : "Test Location"
		}).insert()

		self.assertEqual(test_locker.available, True)

		


