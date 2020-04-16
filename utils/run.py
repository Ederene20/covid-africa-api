import scripts.scraper as sp
import scripts.formatter_json as fj
import sqlite3

# first we get from the scraper and format it

data = fj.formatter(sp.scraper())
print(data)
conn = sqlite3.connect('countriestats.db')

c = conn.cursor()

for key in data.keys():
    name = key
    case_number = int(data[key]['case_number'])
    case_death = int(data[key]['case_death'])
    case_recovered = int(data[key]['case_recovered'])

    c.execute(
        "INSERT INTO countries VALUES(?,?,?,?)", [name, case_number, case_death, case_recovered])
    conn.commit()
