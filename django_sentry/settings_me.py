import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

from .settings import *

sentry_sdk.init(
    dsn="<your sentry.io ID, it's free for developer>",
    integrations=[DjangoIntegration()]
)


INSTALLED_APPS.append('django_sentry.sentry_test')
