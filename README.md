# notification-worker

A background notification dispatcher with intentional bugs for Bug2PR demos.

## Bugs in this repo

- `app/dispatcher.py` — AttributeError on None template
- `app/queue_handler.py` — Division by zero in throughput calculation
- `app/templates.py` — KeyError on missing template variable
