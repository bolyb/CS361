import os

class therapist:
    name = ""
    therapist_dir = ""
    

    def __init__(self, name):
        self.name = name
        self.therapist_dir = name
        
"""
 This function was used to create the directories needed to test our script.
 The creation and maintaining of files and directories is not in the scope of 
 this user story.
"""

def instantiate(var1, var2, var3):
        os.mkdir(var1.therapist_dir)
        os.chdir(var1.therapist_dir)
        file1 = open("some.comment", "w+")
        file2 = open("some.other.comment", "w+")
        
        file1.write("Here is a comment about this therapist.")
        file2.write("More stuff")
        
        file1.close()
        file2.close()

        os.chdir("..")

        os.mkdir(var2.therapist_dir)
        os.chdir(var2.therapist_dir)
        file1 = open("comment.more", "w+")
        file2 = open("some.comment", "w+")
        
        file2.write("Some like it hot, I don't")
        file1.write("More words, yay!")

        file1.close()
        file2.close()

        os.chdir("..")

        os.mkdir(var3.therapist_dir)



#####################################
## This function is the crux of our user story.
## In this function it takes in a name of a directory
## and spits out the contents of each file.
## The error checking is pretty cut and dry. Since 
## the user input need to be an exact match of the
## directory name, which is the name of the therapist
## we didn't need to do much.
##
## What is needed for this function to run is:
##  A directory that has text files that are readable.
##
## What this function produces:
##  A list of all contents in all files located in a directory.
##


def read_comment(therapist_var):
    if(os.path.isdir(therapist_var)):
        os.chdir(therapist_var)
    
        for each in os.listdir("."):
            file1 = open(each)
            string = file1.read()

            print(string)
            print("\n")
            
        os.chdir("..")

    else:
        print("No therapist by that name")

    
def main(): 
    shelly = therapist("Shelly Baxter")
    baxter = therapist("Baxter Shelly")
    someone = therapist("Someone")
       
    instantiate(shelly, baxter, someone)   #This is used to create the directories to test.
    
    print(os.listdir("."))
    
    string_name = raw_input("Which Theripist feedback would you like to view?: " )
    read_comment(string_name)

main()
