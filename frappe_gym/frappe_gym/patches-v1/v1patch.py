import frappe

# This patch updates the Gym Settings with additional email address
def execute():
    # Get the updated version of the Doctype
     frappe.reload_doc("frappe_gym", "doctype", "Gym Settings")
     settings = frappe.get_doc("Gym Settings")

    # Did we find the attribute? If not set it the same as settings email
     if not hasattr(settings,"finance_email"):
        frappe.set_value("Gym Settings", "Gym Settings", "finance_email", settings.email)
        