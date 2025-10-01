import os

os.environ.setdefault(
    "TWISTED_REACTOR",
    "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
)

try:
    from twisted.internet import asyncioreactor
    asyncioreactor.install()
except Exception:
    pass
