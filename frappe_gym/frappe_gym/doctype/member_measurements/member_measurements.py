# Copyright (c) 2022, Warren Eiserman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class MemberMeasurements(Document):
	# Calculate BMI
	def before_save(self):
		if self.height:
			self.bmi = (self.weight / (self.height * self.height))
