# Define a daysBetweenDates procedure that would produce the
# correct output if there was a correct nextDay procedure.
#
# Note that this will NOT produce correct outputs yet, since
# our nextDay procedure assumes all months have 30 days
# (hence a year is 360 days, instead of 365).
# 

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    noleapmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapmonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isleap(year):
        if day < leapmonth[month-1]:
            return year, month, day+1
        if day == leapmonth[month-1]:
            if month == 12:
                return year+1,1,1
            else:
                return year,month+1,1
                

def isleap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True
        
def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""
    assert not dateisbefore(year2, month2, day2, year1, month1, day1)
    day=0   
    while dateisbefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        day += 1
        
    return day

def dateisbefore(year1, month1, day1, year2, month2, day2):
    if year1<year2:
        return True
    elif year1==year2:
        if month1<month2:
            return True
        elif month1==month2:
            return day1<day2
        else:
            return False
    return False

#print daysBetweenDates(2012, 1, 1, 2013, 1, 1)

def test():
    assert daysBetweenDates(2012,9,30,2012,10,30) == 30
    assert nextDay(2012,12,3) == (2012,12,4)

    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),366),
                  ((2012,9,1,2012,9,4),3)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()
    
