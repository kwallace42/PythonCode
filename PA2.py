# imports Bioinformatics module so we can access its funtions 
import Bioinformatics

# Testing the function pctOfProtein in the bioinformatics module
print Bioinformatics.pctOfProtein("msrslllrfllfllllpplp", ["L"]) 
print Bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ["M"]) 
print Bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) 
print Bioinformatics.pctOfProtein("MSRSLLLRFLLFLLLLPPLP", ['F', 's', 'L'])
