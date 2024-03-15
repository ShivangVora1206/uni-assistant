config = {
    "data_url" : "https://mya-backend.uni-assist.de/services/semesterangebot",
    "auth_url" : "https://mya-backend.uni-assist.de/services/nutzer/login",
    "data_payload" : {
    "start": 0,
    "limit": 2000,
    "filter": {
        "volltext": "",
        "semester": [52],
        "hochschule": [],
        "bundesland": [],
        "studienfach": [],
        "abschlussgruppe": [4]
    }
},
    "username":"your username here",
    "password":"your password here",
    "auth_token":"",
    "local_db":"local.json"
}
