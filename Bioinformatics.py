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
        
        
#the goal of this function is to take in a DNA sequence and translate it into
#an amino acid string an return this value. 
def translate_dna(sequence):
    #Amino acid translation chart. Used to convert DNA to amino acids.
    gencode = {
 'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
 'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
 'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
 'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
 'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
 'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
 'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
 'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}
 
    #Set a changeable final codon position based on the sequence length 
    Last_start_pos = len(sequence) - 2 
    protein = ""
    #range function gives us only codon in the range of the DNA sequence
    for codon_start in range(0,Last_start_pos,3):
        #seperates the sequence into codons
        codon = sequence[codon_start:codon_start+3]
        #gets the amino acid from the dictionary based on the codon
        amino_acid = gencode.get(codon.upper())
        #builds the protein string
        protein = protein + amino_acid
    return(protein) 