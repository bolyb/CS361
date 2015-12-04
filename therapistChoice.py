#########################################################################
# Program covers the user story for agile design focusing on this need:
# As a patient, I want to be able to choose from multiple therapists so
# that I can choose the one that best fits my needs.
#########################################################################

## Program designed and implemented by Nathaniel Whitlock and Brian Boly

# dictionary of therapists
therapists = { "Susie Q" : "Narcolepsy",
               "Randy P" : "Drug and Alcohol",
               "Bill H" : "Sexual Abuse" }

# menu interface for the user
print "\n\n#############################################################"
print "##Welcome to the therapist browser!"
print "##Here you can browse therapists that will be fit you needs"
print "##Available therapists include:"
print "#############################################################\n"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"

# print available therapists
print "\n+Susie Q : " + therapists["Susie Q"]
print "+Randy P : " + therapists["Randy P"]
print "+Bill H : " + therapists["Bill H"]
print "\n"

# prompt user for input and verify input at run-time
choice ="none"
while(choice != "Susie Q" and choice != "Randy P" and choice != "Bill H"):
    choice = raw_input("Enter your selection by name: ")

# print out users selection
print "\nUser has selected therapist %s." %(choice)
print "Therapist %s specializes in " %(choice) + therapists[choice]

# prompt the user to see if they would like to connect to their new therapist
input_user = raw_input("\nWould you like to connect to your therapist?")

# verify the user input for therapist connection
if input_user == "Yes" or input_user == "Y" or input_user == "yes" or input_user == "y":
    print "Connecting to therapist...."
else:
    print "Thank you for visiting therapist browser"
