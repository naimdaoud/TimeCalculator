
def add_time(start, duration):

    starthr = int(start.split(":")[0])
    startmin = int(start.split(":")[1].split()[0])
    AMPM = start.split(":")[1].split()[1]

    durationhr = int(duration.split(":")[0])
    durationmin = int(duration.split(":")[1])
    
    if durationhr > 24:
        addday = int(durationhr / 24)
        addhr = (float(durationhr / 24) - addday) * 24
        if startmin + durationmin > 60:
            resmin = startmin + durationmin - 60
            addhr = addhr + 1
        else:
            resmin = startmin + durationmin
        if starthr + addhr > 12:
            reshr = starthr + addhr - 12
            addday = addday + 1
        if addhr >= 12:
            if AMPM == "AM":
                newAMPM = "PM"
            if AMPM == "PM":
                newAMPM = "AM"

#    if startmin + durationmin > 60:
#        resmin = startmin + durationmin - 60
#        addhr = 1
#    else:
#        resmin = startmin + durationmin

#    while starthr + durationhr > 12:
#        res = starthr + durationhr - 12
#        addday = 1

    return str(reshr) + ":" + str(resmin) + " " + newAMPM + " (" + str(addday) + " days later)"

print(add_time("6:30 PM", "205:12"))
