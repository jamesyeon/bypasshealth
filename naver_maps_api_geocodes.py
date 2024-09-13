# Geocoding API
# 지번 도로명을 좌표값으로 반환 

# importing the requests library
import datetime, requests, json, urllib

def naver_map_api_call(address):
	url = "https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode"

	payload = {"query":address}
	apikeys = {"secret"}

	# A get request to the API
	response = requests.get(url, params=urllib.parse.urlencode(payload), headers=apikeys)

	# Print the response
	response_json = response.json()

	print(response_json["status"]);
	print(response_json["addresses"][0]["roadAddress"]);
	print(response_json["addresses"][0]["x"]);
	print(response_json["addresses"][0]["y"]);
	
	return response_json["addresses"][0]["x"], response_json["addresses"][0]["y"]

# 주소 데이터 파일 읽어오기
infile = open("address_list.txt", "r", encoding='UTF8')
for line in infile:
	address = line.rstrip()
	now = datetime.datetime.now()
	x,y = naver_map_api_call(address)
	print(now)
	print(address, x, y)
	
infile.close() 

