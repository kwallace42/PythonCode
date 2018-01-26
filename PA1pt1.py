# Programmed by Kevin Wallace 
# Bioinformatics Assignment 1 part 1
# This program caculates the AT content of a DNA sequence to 3 decimal places. 
# The AT content is (number of A's + Number of T's)/The total length

DNASequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
Abase = DNASequence.count("A")
Tbase= DNASequence.count("T")
TotalBases = len(DNASequence)
ATcontent = (Abase + Tbase)/float(TotalBases)#float is used to make the answer
                                             #a decimal 

print "The AT content of your DNA sequence is: %.3f" % ATcontent