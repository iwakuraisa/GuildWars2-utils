import threading
import gw2_apis.spidy as spidy

def periodic_gem_price():
	print(spidy.gem_price()['result'])
	threading.Timer(15*60,periodic_gem_price).start()

periodic_gem_price()