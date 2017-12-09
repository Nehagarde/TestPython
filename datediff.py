# Difference bewtween two dates


import datetime
import time

tommorow = datetime.datetime(2017,12,12,0,0,0)
today = datetime.datetime.now()

diff=tommorow-today
print(type(diff))
print(diff)
print(diff.days)
print(diff.total_seconds())


#time 

listoftimes=[]
for i in range(10):
    listoftimes.append(datetime.datetime.now())
    time.sleep(2)

for eachitem in listoftimes:
    print(eachitem)