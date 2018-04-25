import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "taiga_contrib_issue_colouring.settings")
sys.path.insert(0, "../../taiga-back/")

from tests.fixtures import *

import pytest
import django

def pytest_configure(config):
    django.setup()
