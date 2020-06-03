# Write a procedure, speed_fraction, which takes as its inputs the result of
# a traceroute (in ms) and distance (in km) between two points. It should 
# return the speed the data travels as a decimal fraction of the speed of
# light.

speed_of_light = 300000. # km per second

def speed_fraction(traceroute, distance):
    #return ((distance+0.0)/(traceroute/2))*1000.0/speed_of_light

    light_distance = (distance + 0.0) / ((speed_of_light + 0.0) / 1000) #ms
    return light_distance / ((traceroute + 0.0) / 2)

print speed_fraction(50,5000)
#>>> 0.666666666667

print speed_fraction(50,10000)
#>>> 1.33333333333  # Any thoughts about this answer, or these inputs?

print speed_fraction(16,20)