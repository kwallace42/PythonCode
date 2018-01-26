# Programmed by Kevin Wallace 
# Bioinformatics Assignment 1 part 2
# This program takes a DNA sequence and cuts at the restriction site for EcoR1 
# which is G*AATTC and it cuts at the *

DNASequence ="ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
ecoR1 = "GAATTC" #restrictions site for EcoR1
cutlocation = DNASequence.find(ecoR1) + 1 #add 1 to get the location after the G
                                          #which is where it cuts
                                          
Frag1 = cutlocation #the location where EchoR1 cut is the first fragment
Frag2 = len(DNASequence) - cutlocation 

print "One fragment is %s bases long" % Frag1
print "The other fragement is %s bases long" %  Frag2

