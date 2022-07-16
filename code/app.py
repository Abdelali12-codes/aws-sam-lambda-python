

import json

def handler(event, context):

    obj = {'firstname':"abdelali", 'lastname':"jadelmoula"}
    print(event)
    return  json.dumps(obj)

   
