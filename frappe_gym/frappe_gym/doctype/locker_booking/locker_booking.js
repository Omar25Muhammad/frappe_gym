// Copyright (c) 2022, Warren Eiserman and contributors
// For license information, please see license.txt

frappe.ui.form.on("Locker Booking", {
    // only show locker locations which are available
    refresh: function (frm) {
        frm.set_query("locker", function () {
            return {
                filters: {
                    is_group: 0,
                    available: 1,
                },
            };
        });
    }
})
