'''
'http://www.gw2spidy.com/api/v0.9/json/recipe/3025'
'''
from response import response
import json

gw2spidy_api = 'http://www.gw2spidy.com/api/v0.9/json/'
official_api = 'https://api.guildwars2.com/v1/'

with open('parsed_data/recipe_dict.json') as recipe_dict_file:
	recipe_dict = json.load(recipe_dict_file)

def recipe_list():
	return response(official_api+'recipes.json')['recipes']

def recipe_detail(recipe_id):
	return response(official_api+'recipe_details.json?recipe_id='+str(recipe_id))

def find_recipe(item_id):
	item_id = str(item_id)
	if item_id in recipe_dict:
		return str(recipe_dict[item_id])
	else:
		return None

def full_recipe(recipe_id):
	ingredients = recipe_detail(recipe_id)['ingredients']
	for ingredient in ingredients:
		ingredient_recipe_id = find_recipe(ingredient['item_id'])
		if ingredient_recipe_id != None:
			print(recipe_detail(ingredient_recipe_id))
		else:
			print("No recipe found for item: ",ingredient)


'''
print(recipe_detail(3025))
print(find_recipe(12494))
print(full_recipe(3025))
'''
