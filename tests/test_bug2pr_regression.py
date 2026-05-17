import pytest
from app.pricing import average_price


def test_average_price_handles_empty_cart():
    """Regression test: average_price should handle zero count without ZeroDivisionError."""
    # This would raise ZeroDivisionError before the fix
    result = average_price(0, 0)
    assert result == 0  # or whatever the fixed behavior returns
    
    # Also test with non-zero total but zero count
    result = average_price(100, 0)
    assert result == 0  # or handle appropriately