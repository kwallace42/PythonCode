# Kevin Wallace 
#The goal of this program is to calculate the size of DNA fragments when it is 
#cut with 2 restriction enzymes. 
import re

#reads the file into a string variable so it can be used in string fuctions.
DNA = open("dna.txt").read().rstrip("\n")

# abcI = ANT/AAT N = any base
# abcII = GCRW/TG R= A or G W= A or T
all_cuts = [0]

#add cut positions for abcI
for match in re.finditer(r"A[ATGC]TAAT", DNA):
    all_cuts.append(match.start() + 3)
#add cut positions for abcII    
for match in re.finditer(r"GC[AG][AT]TG", DNA):
    all_cuts.append(match.start() + 4)

#adds the final position to the list
all_cuts.append(len(DNA))

#Sorts the list of cuts in ascending order based on position
sortedlist = sorted(all_cuts)
print sortedlist   
#prints the length of each fragment
print "one fragment size is %s in length" % (sortedlist[1] - sortedlist[0])
print "one fragment size is %s in length" % (sortedlist[2] - sortedlist[1])
print "one fragment size is %s in length" % (sortedlist[3] - sortedlist[2])
print "one fragment size is %s in length" % (sortedlist[4] - sortedlist[3])
print "one fragment size is %s in length" % (len(DNA) - sortedlist[4] - 1)