import ftp
import json
from jsonschema import validate

schema = {
    "host" : "string",
    "login" : "string",
    "password" : "string",
    "dir" : "string",
    "files" : {
        "type" : "string"
    }
}

try:
    validate(json.load(open('settings.json')), schema)
except Exception as e:
    print(e)

data = json.load(open('settings.json'))
for file in data['files']:
    ftp.copy(data['host'], data['login'], data['password'], data['dir'], file)