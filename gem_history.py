import threading, time
import gw2_apis.spidy as spidy
import json

with open('parsed_data/gem_history.json','r+') as gem_history_file:
	try:
		gem_history = json.load(gem_history_file)
	except Exception:
		gem_history = {}

def periodic_gem_price_update():
	with open('parsed_data/gem_history.json','w') as gem_history_file:
		current_price = spidy.gem_price()['result']
		current_time = str(time.time())
		print(current_time,current_price)
		gem_history[current_time] = current_price
		json.dump(gem_history,gem_history_file)

	threading.Timer(60*15,periodic_gem_price_update).start()

periodic_gem_price_update()