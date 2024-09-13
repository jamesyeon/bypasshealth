# Directions 5 API
# 출발지-목적지 간의 경로 정보를 요청하고 응답으로 경로 데이터 배열을 반환 

# importing the requests library
import requests, json

def naver_map_api_call(startX, startY, endX, endY):
	url = "https://naveropenapi.apigw.ntruss.com/map-direction/v1/driving"

	# Adding a payload
	start = startX+","+startY
	end = endX+","+endY
	payload = {"start": start, "goal":end, "option":"trafast"}
	apikeys = {"secret"}

	# A get request to the API
	response = requests.get(url, params=payload, headers=apikeys)

	# Print the response
	response_json = response.json()

	print(response_json["code"])
	print(response_json["message"])
	print(response_json["currentDateTime"])

	distance = response_json["route"]["trafast"][0]["summary"]["distance"] 
	distance = round(int(distance)/1000) 
	print(distance)
	time = response_json["route"]["trafast"][0]["summary"]["duration"] 
	time = round(int(time)/1000/60) 
	print(time)
	fuelPrice = response_json["route"]["trafast"][0]["summary"]["fuelPrice"]
	toll = response_json["route"]["trafast"][0]["summary"]["tollFare"]
	fare = int(fuelPrice)+int(toll)
	print(fuelPrice,toll)
	
	return distance, time, fare


# 좌표 데이터 파일 읽어오기
infile = open("points_list.txt", "r", encoding='UTF8')
for line in infile:
	line = line.rstrip()
	x = line.split()
	startX = x[2]
	startY = x[3]
	endX = x[4]
	endY = x[5]
	distance, time, fare = naver_map_api_call(startX, startY, endX, endY)
	print(x[0], x[1], distance,"km", time,"분", fare,"원")
	
infile.close() 


