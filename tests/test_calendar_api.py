from datetime import datetime
import json

import pytest
import requests
from   requests.auth import HTTPBasicAuth

from   instance.planning_center_notes import application_id, secret

@pytest.fixture
def auth():
  return HTTPBasicAuth(application_id, secret)

@pytest.fixture
def url():
  return 'https://api.planningcenteronline.com/'

@pytest.fixture
def events():
  return 'calendar/v2/events'