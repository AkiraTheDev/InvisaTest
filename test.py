import string

degreesPerHour = 360 / 12
degreesPerMin = 360 / 60

def getDegreesBetween(timeStr):
    numbers = timeStr.split(":")
    hour = int(numbers[0])
    minutes = int(numbers[1])

    hourDegrees = hour * degreesPerHour
    minDegrees = minutes * degreesPerMin

    angle = max(hourDegrees, minDegrees) - min(hourDegrees, minDegrees)
    return angle



def degreesUnitTest():
    time = "1:30"
    print("Testing with time: ", time)
    result = getDegreesBetween(time)
    if(result != 150):
        print("Failed: Expected 150 but returned ", result)
    else:
        print("Succeded: Returned ", result)


#degreesUnitTest()

import datetime

def dateToDay(dateStr):
    numbers = dateStr.split("/")
    month = int(numbers[0])
    day = int(numbers[1])
    year = int(numbers[2])

    givenDate = datetime.date(year, month, day)
    startDate = datetime.date(1300,1,1)
    #startDay = "Friday"

    diffInDays = (givenDate - startDate).days
    weekNum = diffInDays % 7
    switcher = {
        0:"Friday"
        1:"Saturday"
        2:"Sunday"
        3:"Monday"
        4:"Tuesday"
    }

dateToDay("1/1/1301")
