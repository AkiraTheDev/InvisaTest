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



#print(getDegreesBetween("1:30"))