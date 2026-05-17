import pytest
from app.templates import render


def test_render_missing_template_key():
    """Test that render handles missing template keys gracefully."""
    # This test proves the bug: render() should handle missing keys
    # Currently raises KeyError, should return None or raise custom error
    
    with pytest.raises(KeyError):
        # Attempt to render a template that doesn't exist
        render("nonexistent_template", {"name": "Test"})