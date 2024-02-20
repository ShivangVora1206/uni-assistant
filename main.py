import requests
import json
from config import config
from filters import filters

# semester 52  -> winter 2024/25
# abscchlussgruppe 4 -> Master
# bewerbungsfreigabe (boolean) -> application release status
# datamap -> data/list[0]/list
# uni_name -> data/list[0]/list[n]/hochschuleName
# degree_name -> data/list[0]/list[n]/studienfachName
# degree_type -> data/list[0]/list[n]/abschlussName
# degree_group -> data/list[0]/list[n]/abschlussgruppeName

def fetch_auth_token(username, password):
    url = config['auth_url']
    payload = json.dumps({
        "data": {
        "email": username,
        "passwort": password
        }})
    
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    config['auth_token'] = response.headers['Authorization']
    print("Auth Token Found -> ", '\033[1;30;45m',  response.headers['Authorization'], '\033[0;0m')

def fetch_data(url, payload, auth_token):
    if not auth_token:
        print('No auth token found')
        return
    headers = {'Authorization': auth_token, 'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    return json.loads(response.text)

def parse_data(data, uni_name_filter=None, degree_name_filter=None, degree_type_filter=None):
    out = []
    print("Total Elements", data['totalElements'])
    data = data['data']['list'][0]['list']
    for uni in data:

        if uni_name_filter and uni['hochschuleName'] not in uni_name_filter:
            continue

        if degree_type_filter and uni['abschlussgruppeName'] not in degree_type_filter:
            continue

        if degree_name_filter:
            flag = False
            for term in degree_name_filter:
                if term in uni['studienfachName']:
                    flag = True
                    break
            if not flag: continue
        
        
        uni_name = uni['hochschuleName']
        degree_name = uni['studienfachName']
        degree_type = uni['abschlussgruppeName']
        release_status = uni['bewerbungsfreigabe']
        
        if release_status:
            print('\033[1;30;42m', uni_name, '\033[0;0m', '|', '\033[1;30;43m', degree_name,  '\033[0;0m', '|',  '\033[1;30;44m', degree_type,  '\033[0;0m')
        else:
            print('\033[1;30;41m', uni_name, '\033[0;0m', '|', '\033[1;30;41m', degree_name,  '\033[0;0m', '|',  '\033[1;30;41m', degree_type,  '\033[0;0m')
        out.append({'uni_name': uni_name, 'degree_name' : degree_name, 'degree_type' : degree_type, 'release_status' : release_status.__str__()})
    return out

def find_diff(item_list, file_name):

    with open(file_name, 'rb') as f:
        old_data = json.load(f)
        if old_data:
            print("Difference ->")
            for item in item_list:
                if item not in old_data:
                    print('\033[1;30;45m', item['uni_name'], '\033[0;0m', '|', '\033[1;30;43m', item['degree_name'],  '\033[0;0m', '|',  '\033[1;30;44m', item['degree_type'],  '\033[0;0m')
        else:
            print("No old data found")


fetch_auth_token(config['username'], config['password'])
parsed_output = parse_data(fetch_data(config['data_url'], json.dumps(config['data_payload']), config['auth_token']), uni_name_filter=filters['uni_names'], degree_name_filter=filters['degree_names'], degree_type_filter=filters['degree_types'])
find_diff(parsed_output, config['local_db'])
with open(config['local_db'], 'w') as f:
    f.write(json.dumps(parsed_output))
