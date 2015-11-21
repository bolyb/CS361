#Program for CS 361 Homework six implementation
#Written by Nathaniel Whitlock and Courtney Bonn

#This module is designed to take the input zip and radius and return a
#map of the surrounding therapy resources

from PIL import Image
import webbrowser

print "\nWelcome to Therapy Finder!\n\nThis program is designed to take in a local area code and radius input."
print "This data will be used to output a link to google maps that details local therapy options.\n"

# zip code menu
print "\nValid zipcodes include:"
print "~Corvallis : 97330"
print "~Albany : 97321"
print "~Salem : 97301\n"

# collect and verify zip input
zipCode = 0
ctr = 0
while(zipCode!="97330" and zipCode!="97301" and zipCode!="97321"):
    zipCode = raw_input("Please put in your zip code:")
    ctr += 1
    if(ctr > 1):
        print "That is not a valid zip code..."

# conditional logic to display links
if zipCode == "97330":
    webbrowser.open("https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=counselling+services+corvallis&rflfq=1&rlha=0&tbm=lcl&tbs=lf:1,lf_ui:2&oll=44.51666818279491,-123.12954024999999&ospn=1.5941690530948023,2.801513671875&oz=16&fll=44.56282832761475,-123.25929396872564&fspn=0.02488917808202018,0.043773651123046875&fz=15&qop=1&rlfi=hd:;si:")

elif zipCode == "97321":
    webbrowser.open("https://www.google.com/maps/place/Counseling+Center/@44.6294374,-123.107438,14.5z/data=!4m2!3m1!1s0x54c06b53c25aabf9:0xfd49e7f73d2e7022")

elif zipCode == "97301":
    webbrowser.open("https://www.google.com/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q=counselling+services+salem+oregon&rflfq=1&rlha=0&tbm=lcl&tbs=lf:1,lf_ui:2&oll=44.92960032018957,-123.01355584999999&ospn=0.0989270284024073,0.1750946044921875&oz=13&fll=44.93786390002031,-123.01381334206542&fspn=0.049456397261593565,0.08754730224609375&fz=14&qop=1&rlfi=hd:;si:")

# request radius range
radiusRange = {"1": 5, "2": 10, "3": 15, "4": 20}
print "\nValid input ranges include:"
print "~Option (1) : 5 miles"
print "~Option (2) : 10 miles"
print "~Option (3) : 15 miles"
print "~Option (4) : 20 miles\n"

# collect and verify radius input
radius = 0
ctr = 0
while(radius != "1" and radius != "2" and radius != "3" and radius != "4" ):
    radius = raw_input("Please select option ie.(1,2,3,4):")
    ctr += 1
    if(ctr > 1):
        print "\nValid input selections are 1,2,3, or 4\n"

#store radius input
value = radiusRange[radius]

print "\nValid radius requested is %d" %(value)

##
#possibly implement range restrictions??? to much work?
##
