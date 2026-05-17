"""Notification dispatcher — BUG: None template not checked."""

from app.templates import get_template


def send_notification(user_id, template_key, vars):
    """Render and dispatch a notification."""
    template = get_template(template_key)
    # BUG: AttributeError when template_key doesn't exist (returns None)
    rendered = template.format(**vars)
    return {"to": user_id, "body": rendered}
