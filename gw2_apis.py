from urllib.parse import quote
import urllib.request
import json

gw2spidy_api = 'http://www.gw2spidy.com/api/v0.9/json/'
official_api = 'https://api.guildwars2.com/v1/'

# Helper methods

def _response(url):
	#print(url)
	response = urllib.request.urlopen(url).read()
	obj = json.loads(response.decode('utf-8'))
	return obj

def _official_response(json,**params):
	url = official_api + json + '?' + '&'.join(str(argument) + '=' + quote(str(value)) for argument, value in params.items())
	return _response(url)

def _gw2spidy_response(*args,**params):
	url = gw2spidy_api
	url += '/'.join(map(str,args))
	url += '?' + '&'.join(str(argument) + '=' + quote(str(value)) for argument, value in params.items())
	return _response(url)


# Official API

    # Dynamic Events

# Returns the current status of events for a specific world.
def events(world_id = None, map_id = None, event_id = None):
	params = {}
	if world_id != None:
		params['world_id'] = str(world_id)

	if map_id != None:
		params['map_id'] = map_id

	if event_id != None:
		params['event_id'] = event_id

	return _official_response('events.json',**params)

# Returns a list of localized event names.
def event_names(lang = 'en'):
	return _official_response('event_names.json',lang=lang)

# Returns a list of localized map names.
def map_names(lang = 'en'):
	return _official_response('map_names.json',lang=lang)	

# Returns a list of localized world names.
def world_names(lang = 'en'):
	return _official_response('world_names.json',lang=lang)

# Returns detailed information about events.
def event_details(event_id = None, lang = 'en'):
	if event_id != None:
		return _official_response('event_details.json',event_id = event_id, lang = lang)
	else:
		return _official_response('event_details.json', lang = lang)


	# Guilds

# Returns detailed information about a guild.
def guild_details(guild_id = None, guild_name = None):
	if guild_id != None:
		return _official_response('guild_details.json',guild_id = guild_id)
	else:
		return _official_response('guild_details.json',guild_name = guild_name)


	# Items

# Returns a list of discovered items.
def items():
	return _official_response('items.json')

# Returns detailed information about an item.
def item_details(item_id,lang = 'en'):
	return _official_response('item_details.json', item_id = item_id, lang = lang)

# Returns a list of discovered recipes.
def recipes():
	return _official_response('recipes.json')

# Returns detailed information about a recipe.
def recipe_details(recipe_id):
	return _official_response('recipe_details.json',recipe_id = str(recipe_id))


	# Map Information

# Returns a list of continents and information about each continent.
def continents():
	return _official_response('continents.json')

# Returns a list of maps in the game.
def maps(map_id = None, lang = 'en'):
	if map_id != None:
		return _official_response('maps.json',map_id = map_id, lang = lang)
	else:
		return _official_response('maps.json',lang = lang)

# Returns detailed information about a map floor
def map_floor(continent_id,floor,lang = 'en'):
	return _official_response('map_floor.json',continent_id = continent_id, floor = floor, lang = lang)

	# World vs World

# Returns the currently running WvW matches.
def wvw_matches():
	return _official_response('wvw/matches.json')

# Returns details about a WvW match.
def wvw_match_details(match_id):
	return _official_response('wvw/match_details.json',match_id = match_id)

# Returns a list of WvW objective names.
def wvw_objective_names(lang = 'en'):
	return _official_response('wvw/objective_names.json',lang=lang)

	# Miscellaneous
# Returns the current build id.
def build():
	return _official_response('build.json')

# Returns a list of dyes in the game.
def colors(lang = 'en'):
	return _official_response('colors.json',lang = lang)

def files():
	return _official_response('files.json')


# gw2spidy API



print(guild_details(guild_id = '251BA489-7EB7-4095-8DD5-7C419E24C24F'))
print(wvw_matches())





