frappe.ready(function () {

	var data = {{ frappe.form_dict.name | json
}};
frappe.web_form.set_value('member', data);

frappe.web_form.on('member', (field, value) => {
	frappe.web_form.set_df_property('member', 'hidden', 1);
})

});