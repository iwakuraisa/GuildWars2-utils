import urllib.request
import json

gw2spidy_api = 'http://www.gw2spidy.com/api/v0.9/json/'
official_api = 'https://api.guildwars2.com/v1/'

# Helper methods

def _response(url):
	response = urllib.request.urlopen(url).read()
	obj = json.loads(response.decode('utf-8'))
	return obj

def _official_response(json,**params):
	url = official_api + json + '?' + '&'.join(str(argument) + '=' + str(value) for argument, value in params.items())
	return _response(url)

def _gw2spidy_response(*args,**params):
	url = gw2spidy_api
	url += '/'.join(args)
	url += '?' + '&'.join(str(argument) + '=' + str(value) for argument, value in params.items())
	return _response(url)


# Official API

    # Dynamic Events

def events(world_id = None, map_id = None, event_id = None):
	params = {}
	if world_id != None:
		params['world_id'] = world_id

	if map_id != None:
		params['map_id'] = map_id

	if event_id != None:
		params['event_id'] = event_id

	return _official_response('events.json',**params)

def event_names(lang = 'en'):
	return _official_response('event_names.json',lang=lang)

def map_names(lang = 'en'):
	return _official_response('map_names.json',lang=lang)	

def world_names(lang = 'en'):
	return _official_response('world_names.json',lang=lang)

def event_details(event_id,lang='en'):
	return _official_response('event_details.json',event_id = event_id, lang = lang)

    # Guilds

def guild_deatils():
	pass


    # Items



def recipes():
	return _official_response('recipes.json')

def recipe_detail(recipe_id):
	return _official_response('recipe_details.json',recipe_id = str(recipe_id))


# gw2spidy API



print(events(map_id=15, world_id=1007))





