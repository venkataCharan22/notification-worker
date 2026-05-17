try:
    # risky operation
    result = perform_operation()
except SpecificException as e:
    logger.error(f'Operation failed: {e}')
    # Handle gracefully
    result = fallback_value()
finally:
    cleanup_resources()