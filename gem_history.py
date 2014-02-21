import datetime
import gw2_apis.spidy as spidy
from gw2_db import gw2_db

def gem_price_update():

        current_price = spidy.gem_price()['result']

        current = {
                'date':datetime.datetime.utcnow(),
                'gold_to_gem': current_price['gold_to_gem'],
                'gem_to_gold': current_price['gem_to_gold'],
        }

        db = gw2_db()
        db.gemHistory.insert(current)

        print('Gem Price Saved:',current)

gem_price_update()
