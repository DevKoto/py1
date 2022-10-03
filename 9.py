def pair(lst,t):        
    
    res = []#λίστα αποτελεσμάτων
    for ele in lst:
        if ele[0] + ele[1] == t: 
            res.append(ele)
pair([(4, 5), (6, 7), (3, 6), (1, 2), (1, 8)],9)
pair([(4, 5), (6, 7), (3, 7), (8, 2), (1, 4)],10)
