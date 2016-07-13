#print pirticular word in given text

text = "X-DSPAM-Confidence:0.8475"; 
num = text.find(':')                
# print num
pnum = text[num+1: ]
print pnum
#exnum = float(pnum)                                                                                                   print exnum

#0.8475
