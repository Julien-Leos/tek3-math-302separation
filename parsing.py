import sys
import numpy as np

def is_number(number):
    try:
        int(number)
        return True
    except ValueError:
        return False

def check_usage(arg):
    if arg == "-h" or arg == "--help":
        print("USAGE\n\t./302separation file [n | p1 p2]\nDESCRIPTION\n\tfile\tfile that contains the list of Facebook connections\n\tn\tmaximum length of the paths\n\tpi\tname of someone in the file")
        sys.exit(0)

def check_if_friend_exist(friendToCheck, listOfFriend):
    for friend in listOfFriend:
        if friendToCheck == friend:
            return True
    return False

def getUniqueFriends(links):
    tmp = []
    for i in links:
        tmp.append(i[0])
        tmp.append(i[1])

    friends = list(dict.fromkeys(tmp))
    friends.sort()
    return (friends)

def parseFile(path):
    try:
        content = open(path, 'r').read().split("\n")
    except:
        sys.exit(84)
    links = []
    for link in content:
        if link != "":
            links.append(link.split(" is friends with ", 1))
    return links

def parse(args):
    if len(args) == 1:
        check_usage(args[0])
    if len(args) < 2 or len(args) > 3:
        print("Invalid number of arguments. Try ./302separation -h for usage")
        sys.exit(84)
    if len(args) == 2:
        if is_number(args[1]) == True:
            if int(args[1]) < 1:
                print("Invalid argument: n must be strictly positive. Try ./302separation -h for usage")
                sys.exit(84)
            return [parseFile(args[0]), args[1]]
        else:
            print("Invalid argument: n must be an integer. Try ./302separation -h for usage")
            sys.exit(84)
    else:
        links = parseFile(args[0])
        uniqueFriends = getUniqueFriends(links)
        # if check_if_friend_exist(args[1], uniqueFriends) == False or check_if_friend_exist(args[2], uniqueFriends) == False:
            # print("Invalid argument: p1 and p2 must exist in the file passed as parameter. Try ./302separation -h for usage")
            # sys.exit(84)
        return [links, args[1], args[2]]