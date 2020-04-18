import requests
import json
import xmltodict

url = 'http://openapi.11st.co.kr/openapi/OpenApiService.tmall'

params = {'key' : '02be8f6c94d855c354a8037f61789649', 
        'pageSize': 200, 'apiCode': "ProductSearch", 'keyword': "의류/잡화"}
response = requests.get(url = url, params = params)

data = json.dumps(xmltodict.parse(response.text), ensure_ascii=False, indent=4)
# print(data)

with open('data.json', 'w') as outfile:
    outfile.write(data)