

import json
import os


def handler(event, context):

    obj = {'firstname':"abdelali", 'lastname':"jadelmoula"}
    print(event)
    print(f"the databasename is {os.environ.get('databaseName')} and dbuser is {os.environ.get('databaseUser')}")
    return  json.dumps(obj)

   
