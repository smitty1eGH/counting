from datetime import datetime
import json

import pytest
import requests
from   requests.auth import HTTPBasicAuth

from   instance.planning_center_notes import application_id, secret

def filter_batch(batches, ref_date):
  '''BATCHES is a JSON object list of batch info, ref_date is the target creation date.
  '''
  for d in batches['data']:
    t=datetime.fromisoformat(d["attributes"]["created_at"])
    if t.date()==ref_date.date():
      return d

@pytest.fixture
def ref_date():
  return datetime(2023, 11, 10)

@pytest.fixture
def auth():
  return HTTPBasicAuth(application_id, secret)

@pytest.fixture
def url():
  return 'https://api.planningcenteronline.com/'

@pytest.fixture
def batch_groups(url):
  return f'{url}giving/v2/batch_groups'

@pytest.mark.skip
def test_services_check():
  url   = 'https://api.planningcenteronline.com/services/v2/'
  basic =  HTTPBasicAuth(application_id, secret    )
  r     =  requests.get( url           , auth=basic)
  print(r.json())
  
def test_batch_groups( batch_groups, auth, ref_date):
  ''' 1. Get batch groups and find target date
      2. Determine batches in group
      3. Get donations. We're confident, (but need to check) that 
         0=checks and 1=cash

for z in y['data']:
  print((z["relationships"]["person"]["data"]["id"],z["attributes"]["payment_check_number"],z["attributes"]["amount_cents"]/100 ))
         
  x={ "links": { "self": "https://api.planningcenteronline.com/giving/v2/batches/322/donations"},
   "data":[{"type"                      : "Donation",
            "id"                        : "203534247",
            "attributes" :              {
                "amount_cents"          :  5500,
                "amount_currency"       : "USD",
                "completed_at"          :  null,
                "created_at"            : "2023-11-12T00:52:24Z",
                "fee_cents"             :  0,
                "fee_currency"          : "USD",
                "payment_brand"         :  null,
                "payment_check_dated_at": "2023-10-31",
                "payment_check_number"  :  10874,
                "payment_last4"         :  null,
                "payment_method"        : "check",
                "payment_method_sub"    :  null,
                "payment_status"        : "pending",
                "received_at"           : "2023-11-12T05:00:00Z",
                "refundable"            :  false,
                "refunded"              :  false,
                "updated_at"            : "2023-11-12T00:52:24Z"},
            "relationships": { "batch"             : { "data": { "type": "Batch"        , "id": "322"            }},
                               "campus"            : { "data":    null                                            },
                               "person"            : { "data": { "type": "Person"       , "id": "127660139"      }},
                               "payment_source"    : { "data": { "type": "PaymentSource", "id": "planning_center"}},
                               "labels"            : { "data":    []                                              },
                               "recurring_donation": { "data":    null                                           }},
            "links"        : { "self"              :   "https://api.planningcenteronline.com/giving/v2/donations/203534247",
                               "html"              :   "https://giving.planningcenteronline.com/donations/203534247"}}],
    "included": [],
    "meta"    : {"total_count" :   7, "count" : 7,
                 "can_order_by": ["created_at"    ,"updated_at" ,"received_at","completed_at"],
                 "can_query_by": ["payment_method","received_at","created_at" ,"updated_at"   ,"completed_at","fund_id"],
                 "can_include" : [ "designations" ,"labels"     , "note"      , "refund"     ],
                 "parent"      : { "id": "322"    ,"type"       : "Batch"     }}
}
  '''
  # 1.
  r     = requests.get(batch_groups, auth=auth)
  x     = r.json()
  batch = filter_batch(r.json(), ref_date)
  
  # 2.
  r     = requests.get(f"{batch['links']['self']}/batches", auth=auth)
  b2    = r.json()
  
  # 3.
  CHECKS=0
  data  = requests.get(f"{b2['data'][CHECKS]['links']['self']}/donations", auth=auth)
  d2    = data.json()
  for z in d2['data']:
    print((z["relationships"]["person"]["data"]["id"]
          ,z["attributes"   ]["payment_check_number"]
          ,z["attributes"   ]["amount_cents"        ]/100 ))

  
