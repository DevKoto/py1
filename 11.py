def sos(lst):
 rowSoS = 0 #Αριθμός για το πόσα sos στις γραμμές
 columnSoS = 0#Αριθμός για το πόσα sos στις στήλες
 diagonicalSoS = 0#Αριθμός για το πόσα sos στις διαγώνια  
 for i in range(len(lst)):    
   for j in range(len(lst[i])): 
    firstLetter = lst[i][j] #πρώτο γράμμα           
    #Κοιτάμε την στήλη
    if i+1 < len(lst) - 1: secondLetter = lst[i+1][j]  #δεύτερο γράμμα 
    else : secondLetter = ""
    if i+2 < len(lst) - 1 or ( i+2 == len(lst) - 1) : thirdLetter = lst[i+2][j]#τρίτο γράμμα 
    else : thirdLetter = ""
    if firstLetter + secondLetter + thirdLetter == "sos": columnSoS += 1
    #Κοιτάμε την γραμμή 
    if j+1 < len(lst[i]) - 1: secondLetter = lst[i][j+1]
    if j+2 <= len(lst[i]) - 1: thirdLetter = lst[i][j+2]
    else : thirdLetter = ""
    if firstLetter + secondLetter + thirdLetter == "sos": rowSoS += 1 
    #Κοιτάμε διαγώνια  
    if(i + 2 > len(lst) - 1) : continue 
    if j+1 < len(lst[i]) - 1  and i+1 < len(lst) -1: 
        secondLetter = lst[i+1][j+1]       
        if j+2 <= len(lst[i]) - 1  and i+2 <= len(lst) - 1: thirdLetter = lst[i+2][j+2]    
        else : thirdLetter = ""
        if firstLetter + secondLetter + thirdLetter == "sos": diagonicalSoS += 1 
    if  j-1 < len(lst[i])  and i-1 < len(lst) and j-1 >= 0:
        secondLetter = lst[i-1][j-1] 
        if j-2 < len(lst[i])  and i-2 < len(lst): thirdLetter = lst[i-2][j-2]
        else : thirdLetter = ""
        if firstLetter + secondLetter + thirdLetter == "sos": diagonicalSoS += 1 
     
    
  
   
sos((["s", "o", "o", "s", "o", "s"],["s", "o", "o", "s", "o", "s"],["s", "0", "o", "s", "o", "s"]))
"""
   0    1    2    3    4    5
0["s", "o", "o", "s", "o", "s"]
1["s", "o", "o", "s", "o", "s"]
2["s", "0", "o", "s", "o", "s"]

"""