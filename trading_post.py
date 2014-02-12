from urllib.parse import quote
import urllib.request
import urllib.parse
import json

gem_exchange_api = 'https://exchange-live.ncplatform.net/ws/rates.json?id=undefined&coins=1000000'

def _test_response():

	values = {'id':'undefined','coins':'1000000'}
	data = urllib.parse.urlencode(values).encode('utf8')
	headers = {'Accept':'*/*', 
	'Accept-Charset':'iso-8859-1,*,utf-8',
	'Accept-Encoding': 'deflate',
	'Accept-Language': 'en',
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1003.1 Safari/535.19 Awesomium/1.7.1',
	'Cookie': 's=210C9666-D06E-468E-B997-B53A85AC46B6',
	'Referer': 'https://exchange-live.ncplatform.net/',
	'X-Requested-With': 'XMLHttpRequest',
	'Connection': 'keep-alive',
	'Host': 'exchange-live.ncplatform.net',}

	request = urllib.request.Request(url = gem_exchange_api, headers = headers)

	response = urllib.request.urlopen(request).read().decode('utf-8')
	json_obj = json.loads(response)

	return json_obj

print(_test_response()['results'])