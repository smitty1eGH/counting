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
def events(url):
  return f'{url}calendar/v2/events'
  
def test_events(auth, events):
  r = requests.get(events, auth=auth)
  x = r.json()
  for y in x['data']:
    print(json.dumps(y,indent=4))








