
from subprocess import call

SHOULD_STAGE = input("Do you want to stage the changes by patch?[y/n]\n")
if SHOULD_STAGE == "y" :
    call(["git","add","-p"])
    print("--------------------------------------------------------\n")
    call(["git","status"])
    print("--------------------------------------------------------\n")
    COMMIT_MSG = input("Enter the commit message...\n")
    print("Committing your changes...\n")
    call(["git","commit","-m%s"%(COMMIT_MSG)])
    print("--------------------------------------------------------\n")
    print("Pushing the changes...\n")
    call(["git","push"])
elif SHOULD_STAGE == "n" :
    print("Process terminated...")
else :
    print("Please select the correct response")
