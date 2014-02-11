from urllib.parse import quote
import urllib.request
import json

gw2spidy_api = 'http://www.gw2spidy.com/api/v0.9/json/'
official_api = 'https://api.guildwars2.com/v1/'

# Helper functions

def _response(url):
	# print(url)
	response = urllib.request.urlopen(url).read()
	obj = json.loads(response.decode('utf-8'))
	return obj

def _gw2spidy_response(*args, **params):
	url = gw2spidy_api
	url += '/'.join(map(str, args))
	url += '?' + '&'.join(str(argument) + '=' + quote(str(value)) for argument, value in params.items())
	return _response(url)

# gw2spidy API

# Type List
def types():
	return _gw2spidy_response('types')

# Discipline List
def disciplines():
	return _gw2spidy_response('disciplines')

# Rarity List
def rarities():
	return _gw2spidy_response('rarities')

# Full Item List
def all_items(item_type = 'all'):
	return _gw2spidy_response('all-items', item_type)

# Item List (will be deprecated)
# TODO eliminate pagination
def items(item_type = 'all', page = '1', sort_trending = 'sale', *filter_ids):
	ids = ','.join(filter_ids)
	return _gw2spidy_response('items', item_type, page, sort_trending = sort_trending, filter_ids = ids)

# Item Data
def item(item_id):
	return _gw2spidy_response('item', item_id)

# Item Listings
# TODO eliminate pagination
def listings(item_id, sell_or_buy = 'sell', page = '1'):
	return _gw2spidy_response('listings', item_id, sell_or_buy, page)

# Item Search
# TODO eliminate pagination
def item_search(name, page = '1'):
	return _gw2spidy_response('item-search', quote(name), page)

# Recipe List
def recipes(item_type = 'all', page = '1'):
	return _gw2spidy_response('recipes', item_type, page)

# Recipe Data
def recipe(recipe_id):
	return _gw2spidy_response('recipe', recipe_id)

# Current Gem Price
def gem_price():
	return _gw2spidy_response('gem-price')

# Gem Price History (not implemented)


#print(types())
#print(disciplines())
#print(rarities())
#print(all_items('2')['count'])
#print(item(12494))
#print(items(5))
#print(listings(12494))
#print(item_search('dilled'))
#print(recipes(5))
#print(recipe(3025))
#print(gem_price())