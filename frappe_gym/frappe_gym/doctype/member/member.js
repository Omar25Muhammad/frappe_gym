// Copyright (c) 2022, Agile.co.za and contributors
// For license information, please see license.txt

frappe.ui.form.on("Member", {
    // show the age of the member based on date of birth
    onload: function (frm) {
        if (frm.doc.dob) {
            $(frm.fields_dict['age_html'].wrapper).html(`${__('AGE')} : ${get_age(frm.doc.dob)}`);
        } else {
            $(frm.fields_dict['age_html'].wrapper).html('');
        }
    },

    refresh: function (frm) {
        // allow the creation of a membership plan of one doesn't exist
        if (frm.doc.has_plan == 0) {
            frm.add_custom_button(
                "Create Membership",
                () => {
                    let dialog = new frappe.ui.Dialog({
                        title: "Select Plan",
                        fields: [
                            {
                                fieldtype: "Link",
                                fieldname: "plan",
                                label: "Membership Plan",
                                options: "Membership Types",
                            },
                            {
                                fieldtype: "Date",
                                fieldname: "start_date",
                                label: "Start Date",
                                default: "Today",
                            },
                        ],
                        primary_action_label: "Create Plan",
                        primary_action: (data) => {
                            let { member } = data;
                            let plan = dialog.get_value('plan');
                            let start_date = dialog.get_value('start_date');
                            let notes = dialog.get_value('notes');
                            frappe.new_doc("Gym Membership", {
                                member: frm.doc.name,
                                plan: plan,
                                start_date: start_date,
                                status: "Created",
                                notes: notes
                            });
                        },
                    });
                    dialog.show();
                },
            );
        } else {
            frm.add_custom_button(
                "Assign Trainer",
                () => {
                    let dialog = new frappe.ui.Dialog({
                        title: "Assign Trainer",
                        fields: [
                            {
                                fieldtype: "Link",
                                fieldname: "trainer",
                                label: "Select Trainer",
                                options: "Trainer"
                            },
                            {
                                fieldtype: "Date",
                                fieldname: "assigned_date",
                                label: "Start Date",
                                default: "Today",
                            },
                        ],
                        primary_action_label: "Select Trainer",
                        primary_action: (data) => {
                            let { trainerdata } = data;
                            let trainer = dialog.get_value("trainer");
                            let assigned_date = dialog.get_value("assigned_date")
                            frappe.new_doc("Gym Trainer Subscription", {
                                member: frm.doc.name,
                                trainer: trainer,
                                assigned_date: assigned_date
                            });
                        },
                    });
                    dialog.show();
                },
            );
        }


    }
});

// calculate age
let get_age = function (birth) {
    let ageMS = Date.parse(Date()) - Date.parse(birth);
    let age = new Date();
    age.setTime(ageMS);
    let years = age.getFullYear() - 1970;
    return years + ' Year(s) ' + age.getMonth() + ' Month(s) ' + age.getDate() + ' Day(s)';
};
