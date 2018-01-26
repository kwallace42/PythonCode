# Programmed by Kevin Wallace 
# Bioinformatics Assignment 1 part 3
# This program gives you the complimentary DNA strand for a given DNA sequence
# and prints both for the user  


DNASequence = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
#change to lowercase to prevent re replacing what you already changed.
compliment = DNASequence.replace("A","t")
compliment = compliment.replace("T", "a")
compliment = compliment.replace("C","g")
compliment = compliment.replace("G","c")

print "The orignal DNA sequence is %s"  % DNASequence
print "The complimentar DNA sequence is %s "  % compliment.upper()