import sys
import numpy as np

def check_usage(arg):
    if arg == "-h" or arg == "--help":
        print("USAGE\n\t./friendshipMemory file\nDESCRIPTION\n\tfile\tfile that contains the list of Friendship connections\n")
        sys.exit(0)

def getUniqueFriends(friendLinks):
    friends = []
    for i in friendLinks:
        friends.append(i[0])
        friends.append(i[1])

    friends = list(dict.fromkeys(friends))
    friends.sort()
    return (friends)

def parseFile(path):
    try:
        content = open(path, 'r').read().split("\n")
    except:
        sys.exit(84)
    friendLinks = []
    for link in content:
        if link != "":
            friendLinks.append(link.split(" is friends with ", 1))
    return friendLinks

def parse(args):
    if len(args) > 2:
        print("Invalid number of arguments. Try ./302separation -h for usage")
        sys.exit(84)
    check_usage(args[0])
    friendLinks = parseFile(args[0])
    return (getUniqueFriends(friendLinks), friendLinks)