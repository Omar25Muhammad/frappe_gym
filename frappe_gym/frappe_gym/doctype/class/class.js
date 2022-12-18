// Copyright (c) 2022, Warren Eiserman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Class", {
    refresh(frm) {
        if(!frm.is_dirty()) {
        frm.add_custom_button(
            "Add Booking",
            () => {
                let dialog = new frappe.ui.Dialog({
                    title: "Select Member to Book",
                    fields: [
                        {
                            fieldtype: "Link",
                            fieldname: "member",
                            label: "Member",
                            options: "Member",
                        },
                    ],
                    primary_action_label: "Book Class",
                    primary_action: (data) => {
                        console.log(data);
                        let { member } = data;
                        frappe.new_doc("Class Booking", {
                            class: frm.doc.name,
                            member: member,
                            status: "Confirmed"
                        });
                    },
                });

                dialog.show();
            },
        );
        }
    },
});
