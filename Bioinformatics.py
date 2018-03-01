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