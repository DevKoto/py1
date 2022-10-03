#Η λίστα στην οποίσ αποθηκεύμε τους συνδυασμούς
combinations = []
def thresh(lst,t):
	res = []#λίστα αποτελεσμάτων
	if combinations == [] : #διψήφιοι
		for i in lst:
			for j in lst: 
				combinations.append(int(str(i) + str(j))) 
				if(int(str(i) + str(j)) > int(t)):
					res.append(int(str(i) + str(j))) 
	else:#για τους υπόλοιπους
		for i in combinations:
			for j in lst: 
				"""
				Δυστυχώς για συνδυασμούς αό τέσσερα ψηφία και πάνω υπάρχει πρόβλημα στην 
				μνήμη και χτυπάει πρ
				"""
				combinations.append(int(str(i) + str(j))) 
				if(int(str(i) + str(j)) > int(t)):
					res.append(int(str(i) + str(j))) 
	
     
lst = [2, 4, 5]
for i in range(len(lst)):
	thresh(lst ,20)