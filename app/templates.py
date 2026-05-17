"""Notification templates — BUG: missing template var."""

TEMPLATES = {
    "welcome": "Hi {name}, welcome to our service!",
    "order_confirmed": "Order #{order_id} for ${amount} confirmed.",
}


def get_template(key):
    """Look up a template by key."""
    return TEMPLATES.get(key)


def render(key, vars):
    """Render a template — BUG: KeyError when a {var} is missing from vars dict."""
    template = TEMPLATES[key]
    # BUG: .format(**vars) raises KeyError if template references a var not in vars
    return template.format(**vars)
