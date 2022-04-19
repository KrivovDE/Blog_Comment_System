from split_settings.tools import include, optional

include(
    "components/base.py",
    "components/database.py",
    "components/apps.py",
    "components/middleware.py",
    "components/logger.py",
    "components/drf.py",
    "components/other.py",
    optional("local_settings.py"),
)
