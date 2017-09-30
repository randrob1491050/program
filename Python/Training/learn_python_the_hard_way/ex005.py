#!python

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_height_cm = my_height * 5
my_weight_kg = my_weight * 2
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

#Print: Zed A. Shaw
print "Let's talk about %s." % my_name
#Print: 35
print "My age is %s." % my_age
#Print: 74
print "He's %d inches tall." % my_height
#Print: 180
print "He's %d pounds heavy." % my_weight
#Print: 74*5.0
print "He's %s cm tall." % my_height_cm
#Print: 180*2.0
print "He's %s kg heavy." % my_weight_kg
print "Actually that's not too heavy."
#Print: Blue and Brown
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
#Print: White
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
#Print: 35,74,180,35+74+180
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

print "Just show: %r, %r, %r,%r" % (my_name, my_age, my_eyes, my_height)

float_numbers = round(1.7777777)
print "there numbers is %s." % float_numbers
