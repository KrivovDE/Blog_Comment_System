django_apps = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

thirds_apps = ["rest_framework", "mptt"]

project_apps = [
    "posts",
    "comments",
]

INSTALLED_APPS = django_apps + thirds_apps + project_apps
