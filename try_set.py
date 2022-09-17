import random
import datetime


rand_list = {random.randint(0, 100000000) for x in range(1000000)}
checked_list = [random.randint(0, 100000000) for x in range(100)]

start = datetime.datetime.now()

for temp in checked_list:
    if temp in rand_list:
        print(f"temp: {temp} in rand_list")

finish = datetime.datetime.now()
recode = (finish - start).total_seconds()
print(recode)