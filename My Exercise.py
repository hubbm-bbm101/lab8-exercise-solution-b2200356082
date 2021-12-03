import sys
names = sys.argv[2].split(",")
with open("{}".format(sys.argv[1]), "r") as inputFile:
    uni = dict()
    for i in inputFile:
        records[i.split(":")[0]] = i.split(":")[1]
    for j in names:
        try:
            print("Name:{}, University:{}".format(j, uni[j]))
        except KeyError:
            print("No record of {} was found.".format(j))