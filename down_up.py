class therapist:
	name = ""
	rank = ""
	
	__init__(self, set_name):
		name = set_name
		rank = 0


#Discription:
#the votetally function is the crux of the task, the rest is used to showcase what the functionality is supposed to do.
#This function takes in a user vote and a therapist to be voted on and manipulates the therapists rank.
#Parameters:
#The user vote should either be a 1 or -1 to increase or decrease the therapists rank.
#The therapist class requires that there is a rank variable to associate the user vote to.
def votetally(user_vote, a_therapist):
	a_therapist.rank = a_therapist.rank + user_vote


def main:
	therapists = []
	therapists.append(therapist("Bobby the psychic"))
	user_vote = 1
	votetally(user_vote, therapist[0])
