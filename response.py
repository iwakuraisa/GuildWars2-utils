import urllib.request
import json

def response(url):
	response = urllib.request.urlopen(url).read()
	obj = json.loads(response.decode('utf-8'))
	return obj