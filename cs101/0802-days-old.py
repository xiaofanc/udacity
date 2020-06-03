# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days. 
# Account for leap days. 
#
# Assume that the birthday and current date are correct dates (and no 
# time travel). 
#

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    ##
    # Your code here.
    ans = 0
    for year in range(year1, year2):
        if isleap(year):
            ans += 366
        else:
            ans += 365
    # ans = sum({True: 366, False:365}[isleap(year)] for year in range(year1, year2))
    noleapmonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leapmonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    y1 = leapmonth if isleap(year1) else noleapmonth
    y2 = leapmonth if isleap(year2) else noleapmonth
    d1 = sum(y1[:month1-1]) + day1 
    d2 = sum(y2[:month2-1]) + day2  
    ans = ans-d1+d2
    return ans
    
def isleap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

    
# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58), 
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

print daysBetweenDates(2012,1,1,2012,2,28)
