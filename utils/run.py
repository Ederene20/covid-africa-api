import scripts.scraper as sp
import scripts.formatter_json as fj
from app.Country import Country

# first we get from the scraper and format it

data = fj.formatter(sp.scraper())

try:
    #save in db
    Country.create(
        
    )