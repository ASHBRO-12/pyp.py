import random
import time

def getRandomDate(starDate, endDate):
    print("Printing random date between", starDate, "and", endDate)
    randomGenerator = random.random()
    dateFormat = '%d/%m/%Y'
    starttime = time.mktime(time.strptime(starDate, dateFormat))
    endtime = time.mktime(time.strptime(endDate, dateFormat))
    randomTime = starttime + randomGenerator * (endtime - starttime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print("Random Date = ", getRandomDate("1/1/2009", "7/6/2025"))