#Kevin Wallace
#Bioinformatics 
#The foal of this function is to calculate the pecentage of a protein that is made 
#up of specific amino acids.
def pctOfProtein(sequence, AminoAcids):
    
    # Sets the protein sequence to be upper case to make it case insensitive 
    sequence = sequence.upper() 
    # Counter for when multiple Amino Acids are passed as parameters 
    #Global variable to the function so it isn't replaced after each loop run 
    aa_Total = 0
    
    #For in loop to count the number of times each amino acid appears in the Sequence 
    for aa in AminoAcids:
        #Makes each aa passed uppercase to make it case insensitive 
        aa = aa.upper()
        count = sequence.count(aa)
        aa_Total = aa_Total + count
    #Calculate the total precent of the sequence that is the amino acids     
    pct = float(aa_Total)/ len(sequence) *100
    return(pct)

#Takes in a DNA sequence and returns the AT content of that sequence.
def AT_Content(DNASequence):
    Abase = DNASequence.upper().count("A")
    Tbase= DNASequence.upper().count("T")
    TotalBases = len(DNASequence)
    ATcontent = (Abase + Tbase)/float(TotalBases)#float is used to make the answer
                                             #a decimal
    return (ATcontent)

#Takes a floating point value for ATcontent and checks to see if has > 65% AT  
def HighAT(ATcontent):
    if ATcontent > .65:
        return(True)
    else:
        return (False)
#Takes a floating point value for ATcontent and checks to see if has between 
#45% and 65% AT inclusively 
def MedAT(ATcontent):
    if ATcontent >= .45 and ATcontent <= .65: 
        return (True)
    else:
        return (False)
#Takes a floating point value for ATcontent and checks to see if has < 45% AT         
def LowAT(ATcontent):
    if ATcontent < .45:
        return (True)
    else:
        return (False)