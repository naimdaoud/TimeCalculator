
def add_time(start, duration, day = None):

    starthr = int(start.split(":")[0])
    startmin = int(start.split(":")[1].split()[0])
    AMPM = start.split(":")[1].split()[1]

    durationhr = int(duration.split(":")[0])
    durationmin = int(duration.split(":")[1])

    week_days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]

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
        newAMPM = "PM"

    if addedday > 1:
        stradded = " (" + str(int(addedday)) + " days later)"
    elif addedday == 1:
        stradded = " (next day)"
    else:
        stradded = ""

    if day != None:
        week = int(addedday) / 7
        d = (week - int(week)) * 7
        a = week_days.index(day.lower()) + int(d)
        if a == 7:
            a = 0
        strday = ", " + week_days[a].capitalize()

    return str(reshr) + ":" + str('{:02d}'.format(int(round(resmin, 0)))) + " " + newAMPM + strday + stradded

print(add_time("11:40 AM", "0:25"))
