#!/bin/env python3
print("Content-Type: text/html")
print()

import requests, time, sys, json

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country": "Myanmar"}

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "bc48047875mshf4d1668b9910304p1eeff8jsn109f6bb01cc3"
    }
request = requests.get(url, headers=headers, params=querystring)
if request.status_code == 200:
	response = json.loads(request.text)
	f = open('home.106a6c241b8797f52e1e77317b96a201.html', 'r').read()
	print(f.format(results=response['results'],country=response['parameters']['country'], cases_total=response['response'][0]['cases']['total'], cases_recovered=response['response'][0]['cases']['recovered'], cases_critical=response['response'][0]['cases']['critical'], cases_new=response['response'][0]['cases']['new'], cases_active=response['response'][0]['cases']['active'],deaths_new=response['response'][0]['deaths']['new'], deaths_total=response['response'][0]['deaths']['total'], date=response['response'][0]['day'], year=time.strftime("%Y")))