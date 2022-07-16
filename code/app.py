

import json

def handler(event, context):

    obj = {'firstname':"abdelali", 'lastname':"jadelmoula"}
    print(event)
    return {
    'statusCode': 200,
    'headers': {'Content-Type': 'application/json'},
    'body': json.dumps(obj)
       }

   
