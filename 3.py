def Josephus(n, k):
  listofsoldiers = []#Αρχική λίστα των στρατιωτών
  listofremovedsoldiers = []# Λίστα των στρατιωτών που 'πεθαίνουν'
  for x in range(n):
    listofsoldiers.append(x+1)
  k -= 1 # προσπερνάμε τον 'νεκρό'
  idx = k
  while len(listofsoldiers) > 1:
        listofremovedsoldiers.append(listofsoldiers.pop(idx)) #'σκοτώνουμε' τον στρατιώτη στο σημείοidx
        idx = (idx + k) % len(listofsoldiers)
  listofremovedsoldiers.append(listofsoldiers[0])      
  
  
Josephus(7,3)    
