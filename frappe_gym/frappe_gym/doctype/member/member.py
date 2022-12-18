# Copyright (c) 2022, Agile.co.za and contributors
# For license information, please see license.txt
import frappe
from frappe.utils import cint, cstr, getdate
import dateutil
from frappe import _
from frappe.model.document import Document

class Member(Document):
	# add a virtual docfield which checks for active gym plans - used to control what buttons are displayed in desk
	@property
	def age(self):
		if not self.dob:
			return
		dob = getdate(self.dob)
		age = dateutil.relativedelta.relativedelta(getdate(), dob)
		return age

	@property
	def	has_plan(self):
		today = getdate()
		membership = frappe.db.get_all(
			"Gym Membership",
			fields=["member"],
			filters={"member": self.name,
					"end_date": ['>', today]}
		)
		if membership and membership[0]:
			return True
		else:
			return False

	# set the full name of member based on their first and last names
	def set_full_name(self):
		if self.last_name:
			self.full_name = " ".join(filter(None, [self.first_name, self.last_name]))
		else:
			self.full_name = self.first_name

	# create a new user based on the member settings 
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
		user.add_roles("Gym Member")
		self.db_set("user_id", user.name)

    # Concatenate names to build full name
	def validate(self):
		self.set_full_name()

    # create a frappe user if requested
	def on_update(self):
		if not self.user_id and self.email and self.invite_user:
			self.create_website_user()	

		
def get_age(self):
	age = self.age
	if not age:
		return
	age_str = f'{str(age.years)} {_("Year(s)")} {str(age.months)} {_("Month(s)")} {str(age.days)} {_("Day(s)")}'
	return age_str

def get_timeline_data(doctype, member):
	"""
	Return Members timeline data from measurement activity
	"""
	member_timeline_data = dict(
		frappe.db.sql(
			"""
		SELECT
			unix_timestamp(signs_date), count(*)
		FROM
			`tabMember Measurements`
		WHERE
			member=%s
			and `signs_date` > date_sub(curdate(), interval 1 year)
		GROUP BY signs_date""",
			member,
		)
	)

	return member_timeline_data