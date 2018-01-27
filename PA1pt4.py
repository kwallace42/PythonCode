# Programmed by Kevin Wallace 
# Bioinformatics Assignment 1 part 4
# This program capitalizes the exons and makes the intron lowecase then prints
# their sequence for the user.

DNASequence = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = DNASequence [0:64]
intron = DNASequence[64:91].lower()
exon2 = DNASequence[91:]

print "The first exon is: %s" % exon1
print "The intron is: %s" % intron
print "The the second exon is: %s" % exon2
