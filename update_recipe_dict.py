'''
This script mantains a file which contains a map relating an item to its
recipe.
Running this takes a long time.
'''

import gw2_recipe
import json
from concurrent.futures import ThreadPoolExecutor

recipe_list = gw2_recipe.recipes()
print(recipe_list)

recipe_dict = {}

for recipe in recipe_list:
	detail = gw2_recipe.recipe_detail(recipe)
	output_item_id = detail['output_item_id']
	recipe_dict[output_item_id] = recipe
	print("Adding entry:",output_item_id,recipe)


def recipe_tuple(recipe_id):
	detail = gw2_recipe.recipe_detail(recipe_id)
	output_item_id = detail['output_item_id']
	print("Adding entry:",output_item_id,recipe_id)
	return (output_item_id,recipe_id)
	

with ThreadPoolExecutor(8) as executor:
    results = executor.map(recipe_tuple, recipe_list)
    recipe_dict = dict(results)

with open("parsed_data/recipe_dict.json","w") as recipe_dict_file:
	json.dump(recipe_dict,recipe_dict_file)



