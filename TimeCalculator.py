
def add_time(start, duration, day = None):

    starthr = int(start.split(":")[0])
    startmin = int(start.split(":")[1].split()[0])
    AMPM = start.split(":")[1].split()[1]

    durationhr = int(duration.split(":")[0])
    durationmin = int(duration.split(":")[1])

    week_days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]

    reshr = 0
    addedday = 0
    newAMPM = AMPM
    strday = ""

    #Calculate minutes
    addedhr = (startmin + durationmin) / 60
    resmin = (addedhr - int(addedhr)) * 60

    #Calculate hours
    addedday = addedday + (durationhr / 24)
    addedhr = addedhr + ((addedday - int(addedday)) * 24)
    reshr = reshr + int(addedhr) + starthr

    if reshr >= 12 and AMPM == "PM":
        reshr = reshr - 12
        if reshr == 0:
            reshr = 12
        addedday = int(addedday) + 1
        newAMPM = "AM"

    if reshr >= 12 and AMPM == "AM":
        reshr = reshr - 12
        if reshr == 0:
            reshr = 12

    if addedday > 1:
        stradded = " (" + str(int(addedday)) + " days later)"
    elif addedday == 1:
        stradded = " (next day)"
    else:
        stradded = ""

    if day != None:
        a = week_days.index(day) + int(addedday)
        strday = ", " + week_days[a]

    return str(reshr) + ":" + str('{:02d}'.format(int(resmin))) + " " + newAMPM + strday + stradded

print(add_time("10:10 PM", "3:30"))
