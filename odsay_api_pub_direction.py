# importing the requests library
import datetime
import requests
import json

def odsay_call(startX, startY, endX, endY):

	url = "https://api.odsay.com/v1/api/searchPubTransPathT"

	# 시외구간 호출
	payload = {"SX":startX,"SY":startY,"EX":endX,"EY":endY,"SearchType":"1","apiKey":"secret"}

	# A get request to the API
	response = requests.get(url, params=payload)

	# Print the response
	response_json = response.json()
	
	pathType = response_json["result"]["path"][0]["pathType"]
	print("pathType:",pathType)
	term_time = response_json["result"]["path"][0]["info"]["totalTime"]
	print(term_time)
	term_fare = response_json["result"]["path"][0]["info"]["totalPayment"]
	print(term_fare)
	transitCount = response_json["result"]["path"][0]["info"]["transitCount"]
	
	term_startX = response_json["result"]["path"][0]["subPath"][0]["startX"]
	term_startY = response_json["result"]["path"][0]["subPath"][0]["startY"]
	if transitCount == 1:
		term_endX = response_json["result"]["path"][0]["subPath"][0]["endX"]
		term_endY = response_json["result"]["path"][0]["subPath"][0]["endY"]
	elif transitCount == 2:
		term_endX = response_json["result"]["path"][0]["subPath"][1]["endX"]
		term_endY = response_json["result"]["path"][0]["subPath"][1]["endY"]
	
	# 출발지 시내구간 호출
	payload = {"SX":startX,"SY":startY,"EX":term_startX,"EY":term_startY,"apiKey":"e6At4tHLpQIuO6JuccF97vRs9zHGy8hCJLNxKL/LoA8"}

	# A get request to the API
	response = requests.get(url, params=payload)

	# Print the response
	response_json = response.json()
	pathType = response_json["result"]["path"][0]["pathType"]
	print("pathType:",pathType)
	start_time = response_json["result"]["path"][0]["info"]["totalTime"]
	print(start_time)
	if pathType >= 1 and pathType <= 3:
		start_fare = response_json["result"]["path"][0]["info"]["payment"]
	else:
		start_fare = response_json["result"]["path"][0]["info"]["totalPayment"]
	print(start_fare)
	
	# 도착지 시내구간 호출
	payload = {"SX":term_endX,"SY":term_endY,"EX":endX,"EY":endY,"apiKey":"e6At4tHLpQIuO6JuccF97vRs9zHGy8hCJLNxKL/LoA8"}

	# A get request to the API
	response = requests.get(url, params=payload)

	# Print the response
	response_json = response.json()
	pathType = response_json["result"]["path"][0]["pathType"]
	print("pathType:",pathType)
	end_time = response_json["result"]["path"][0]["info"]["totalTime"]
	print(end_time)
	if pathType >= 1 and pathType <= 3:
		end_fare = response_json["result"]["path"][0]["info"]["payment"]
	else:
		end_fare = response_json["result"]["path"][0]["info"]["totalPayment"]
	print(end_fare)
	
	return term_time+start_time+end_time, term_fare+start_fare+end_fare 

# 좌표 데이터 파일 읽어오기
infile = open("points_list.txt", "r", encoding='UTF8')
for line in infile:
	line = line.rstrip()
	x = line.split()
	startX = x[2]
	startY = x[3]
	endX = x[4]
	endY = x[5]
	now = datetime.datetime.now()
	time, fare = odsay_call(startX, startY, endX, endY)
	print(now)
	print(x[0], x[1], time,"분", fare,"원")
	
infile.close() 

