import requests
import json

def get_flights():
	# creates a list of tuples containg the required data, from the line scraped = csv[9].strip('/"'),csv[13].strip('/"')
	# headers taken from pyflightdata
	# url UAE is airline code and number is epoch time of request
	spoofHeaders={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:28.0) Gecko/20100101 Firefox/28.0', 'Method':'POST', 'Origin':'https://www.flightradar24.com', 'Referer':'https://www.flightradar24.com'}
	url = 'https://data-live.flightradar24.com/zones/fcgi/feed.js?airline=!UAE&_=1513938553691'
	result = requests.put(url,headers=spoofHeaders)
	raw = result.content
	data = json.loads(str(raw))
	return data
	
data = get_flights()
# data is a dictionary of lists
print data

# all I want is aircraft and flight number
ignoreList = ('version', 'full_count')
for each in data.keys():
	if each not in ignoreList:
		ent = data[each]
		print '{} - {}'.format(ent[9], ent[13])

