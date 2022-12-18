// Copyright (c) 2022, Agile.co.za and contributors
// For license information, please see license.txt

frappe.ui.form.on("Gym Membership", {
    length: function (frm) {
        frm.set_value(
            "end_date",
            frappe.datetime.add_days(frm.doc.start_date, frm.doc.length)
        );
    },
    start_date: function (frm) {
        frm.set_value(
            "end_date",
            frappe.datetime.add_days(frm.doc.start_date, frm.doc.length)
        );
    },
    refresh: function (frm) {
        frm.set_query("plan", function () {
            return {
                filters: {
                    active: 1,
                },
            };
        });
    },
});
