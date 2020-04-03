import requests, time, sys, json
from hashlib import sha1

url = "https://covid-193.p.rapidapi.com/statistics"

querystring = {"country": "Myanmar"}

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "bc48047875mshf4d1668b9910304p1eeff8jsn109f6bb01cc3"
    }

print("[*] Searching query for %s ... \n" % querystring['country'])

hash_req = ""
try:
	while True:
		request = requests.get(url, headers=headers, params=querystring)
		if not hash_req: pass
		if hash_req != sha1(request.text.encode()).hexdigest():
			if request.status_code == 200:
				response = json.loads(request.text)
				print('[+] Started at <%s>' % time.strftime('%H:%M:%S %p'))
				print('\t[+] Country : %s' % response['parameters']['country'])
				print('\t[+] Results : %d\n' % response['results'])
				if response['results'] != 0:
					print('\t[!] Cases ~>')
					print('\t\t @~ New : %s' % response['response'][0]['cases']['new'])
					print('\t\t @~ Active : %d' % response['response'][0]['cases']['active'])
					print('\t\t @~ Critical : %d' % response['response'][0]['cases']['critical'])
					print('\t\t @~ Recovered : %d' % response['response'][0]['cases']['recovered'])
					print('\t\t @~ Total : %d' % response['response'][0]['cases']['total'])
					print('\t[!!] Deaths ~>')
					print('\t\t @~ New : %s' % response['response'][0]['deaths']['new'])
					print('\t\t @~ Total : %s' % response['response'][0]['deaths']['total'])
					print('\t[-] %s' % response['response'][0]['day'])
					print('\t[-] %s' % response['response'][0]['time'])
				print('[+] Finished at <%s> \n\n' % time.strftime('%H:%M:%S %p'))
				hash_req = sha1(request.text.encode()).hexdigest()
		else:
			pass
except KeyboardInterrupt:
	print('[!] Exiting...')
	sys.exit(0)