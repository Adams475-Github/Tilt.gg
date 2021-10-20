# Returns true if date is within 5 hours of each other
def is_recent(time1, time2):
    m1 = int(time1[6:7])
    d1 = int(time1[9:10])
    h1 = int(time1[11:13])

    m2 = int(time2[6:7])
    d2 = int(time2[9:10])
    h2 = int(time2[11:13])

    if abs(h1 - h2) < 5:
        if (m1 - m2) == 0:
            if (d1 - d2) == 0:
                return True
    return False
