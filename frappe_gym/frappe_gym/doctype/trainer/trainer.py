# Copyright (c) 2022, Agile.co.za and contributors
# For license information, please see license.txt
import frappe
from frappe import _
from frappe.model.document import Document

class Trainer(Document):

	# create a new user based on the trainer settings 
	def create_website_user(self):
		users = frappe.db.get_all(
			"User",
			fields=["email", "mobile_no"],
			or_filters={"email": self.email, "mobile_no": self.mobile},
		)
		if users and users[0]:
			frappe.throw(
				_(
					"User exists with Email {}, Mobile {}<br>Please check email / mobile or disable 'Invite as User' to skip creating User"
				).format(frappe.bold(users[0].email), frappe.bold(users[0].mobile_no)),
				frappe.DuplicateEntryError,
			)

		user = frappe.get_doc(
			{
				"doctype": "User",
				"first_name": self.first_name,
				"last_name": self.last_name,
				"email": self.email,
				"user_type": "Website User",
				"gender": self.sex,
				"phone": self.phone,
				"mobile_no": self.mobile,
				"birth_date": self.dob,
			}
		)
		user.flags.ignore_permissions = True
		user.enabled = True
		user.send_welcome_email = False
		user.add_roles("Gym Trainer")
		self.db_set("user_id", user.name)

    # create a frappe user if requested
	def on_update(self):
		if not self.user_id and self.email and self.invite_user:
			self.create_website_user()	
