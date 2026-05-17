"""Queue handler — BUG: divide by zero when queue is empty."""

import time


def average_throughput(messages_sent, elapsed_seconds):
    """Compute messages per second."""
    # BUG: division by zero when elapsed_seconds is 0 (first tick)
    return messages_sent / elapsed_seconds


def queue_health(queue_size, processed):
    if queue_size == 0:
        return "idle"
    return f"{processed}/{queue_size} processed"
