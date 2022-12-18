from frappe import _


def get_data():
	return {
		"heatmap": True,
		"heatmap_message": _(
			"Member Measurements"
		),
		"fieldname": "member",
		"transactions": [
			{
				"label": _("Membership Details"),
				"items": ["Gym Membership", "Gym Trainer Subscription"],
			},
            {
				"label": _("Health Tracking"),
				"items": ["Member Measurements"],
			},
			{
				"label": _("Bookings"),
				"items": ["Class Booking", "Locker Booking"],
			}
		],
	}