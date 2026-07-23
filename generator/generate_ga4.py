# Event Types
EVENTS = [
"session_start", "page_view", "user_engagement", "scroll", "view_item", "select_item", "begin_checkout", "purchase", "appointment_start", "appointment_booking", "newsletter_signup", "catalog_download", "watch_registration", "login", "account_creation"
]
# Traffic Sources
TRAFFIC = [
("google","organic"), ("bing","organic"), ("facebook","social"), ("instagram","social"), ("linkedin","social"), ("newsletter","email"), ("direct","none")
]
# Devices
DEVICES = [
("desktop","Chrome","Windows"), ("desktop","Edge","Windows"), ("mobile","Safari","iOS"), ("mobile","Chrome","Android"), ("tablet","Safari","iPadOS")
]
# User Generator
COUNTRIES = [
("France","Paris","Île-de-France"), ("France","Lyon","Auvergne-Rhône-Alpes"), ("Spain","Madrid","Madrid"), ("Spain","Barcelona","Catalonia"), ("Italy","Rome","Lazio"), ("Germany","Berlin","Berlin"), ("Switzerland","Geneva","Geneva"), ("USA","New York","New York")
]

# User Generator
from faker import Faker
import random

fake = Faker()

def generate_user():
    return {
        "user_pseudo_id": fake.uuid4(),
        "user_id": fake.uuid4() if random.random()<0.4 else None
    }

# Event Parameters
def build_event_params(event):

    return [
        {
            "key":"page_location",
            "value":{
                "string_value":"https://mb.com/"+event,
                "int_value":None,
                "double_value":None
            }
        },
        {
            "key":"engagement_time_msec",
            "value":{
                "string_value":None,
                "int_value":12000,
                "double_value":None
            }
        }
    ]

# Item Generator
WATCHES=[
"Classique", "Tradition", "Marine", "Type XX"
]

def item():
    import random
    return [{
        "item_id":"WATCH"+str(random.randint(1,20)),
        "item_name":random.choice(WATCHES),
        "price":random.randint(5000,50000),
        "quantity":1
    }]

# Generate One Event
def event(user):
    import random,time
    traffic=random.choice(TRAFFIC)
    device=random.choice(DEVICES)
    geo=random.choice(COUNTRIES)
    name=random.choice(EVENTS)
    return{
        "event_date":"20260722",
        "event_timestamp":int(time.time()*1000000),
        "event_name":name,
        "user_pseudo_id":user["user_pseudo_id"],
        "user_id":user["user_id"],
        "platform":"WEB",
        "stream_id":"123456",
        "traffic_source":{
            "source":traffic[0],
            "medium":traffic[1],
            "name":"summer"
        },
        "geo":{
            "country":geo[0],
            "city":geo[1],
            "region":geo[2]
        },
        "device":{
            "category":device[0],
            "browser":device[1],
            "operating_system":device[2]
        },
        "event_params":build_event_params(name),
        "items":item() if name in ["purchase","view_item"] else []
    }

# Generate Daily File
rows=[]
for i in range(100000):
    user=generate_user()
    rows.append(event(user))























