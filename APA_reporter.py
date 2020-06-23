# -*- coding: utf-8 -*-
####this code creates APA-formulas of ANOVA


#copy the SPSS output table ("Test of within-subject effects") in csv
Path_to_your_file = "ANOVA_within.csv" ###copy here the path to the file
Sphericity_assumed = True #if sphericity not assumed, switch to False
df2 = "32" #change to the degree of freedom in the "Error" line


###################################################################


if Sphericity_assumed:
    lookFor = "Sphericity Assumed"
else:
    lookFor = "Greenhouse-Geisser"


data = open(Path_to_your_file)


Lines = []
for line in data:
    words = line.split(",")
    Lines.append(words)



if Sphericity_assumed:
    for line in Lines:
        
        if line[1] == lookFor and not line[0].startswith("Error"):
            effect = line[0]
            F = line[5]
            df1 = line[3]
            Sig = line[6]
            eta2 = line[7]
            print(effect)
            print("F(" + str(df1)+ ", " + df2 + ") = " + str(F) + ", p = " + str(Sig) + ", eta2 = " + str(eta2))
            '''
else:
    for line in Lines:
        if line[1].startswith(",Greenhouse-Geisser"):
            effect = line[0]       
            F = line[5]
            df1 = line[3]
            Sig = line[6]
            eta2 = line[7]
            print(effect)
            print("F(" + str(df1)+ ", " + df2 + ") = " + str(F) + ", p = " + str(Sig) + ", eta2 = " + str(eta2))


'''
    
        
