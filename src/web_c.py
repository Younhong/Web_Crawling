import requests
import json
import xmltodict

keyword = input("Enter keyword: ")

### If you enter anything other than clothes, exit
if (keyword != '의류'):
        exit(0)

url = 'http://openapi.11st.co.kr/openapi/OpenApiService.tmall'

params = {'key' : 'use your own key', 
        'pageSize': 200, 'apiCode': "ProductSearch", 'keyword': keyword}
response = requests.get(url = url, params = params)

data = json.dumps(xmltodict.parse(response.text), ensure_ascii=False, indent=4)
# print(data)

with open('data.json', 'w') as outfile:
    outfile.write(data)