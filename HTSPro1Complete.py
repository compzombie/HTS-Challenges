import os
from tkinter import *

def sortString(strIn):
	out = ""
	toChar = []
	
	for c in strIn:
		toChar.append(c)
		
	toChar.sort()
	
	out = ''.join(toChar)
	
	return out

def StrToList(search, strIn):
    
	strList = []
	oldLen = 0
	while len(strIn) > 0:
		#print(len(strIn))
		#print(strIn)
		oldLen = len(strIn)
		
		index = strIn.find(search)
		strList.append(strIn[:index])
		strIn = strIn[index+1:]
		
		
		#if length stops changing, append remaining chars as one string and stop
		if oldLen == len(strIn):
			strList.append(strIn)
			strIn = ""
        
        
        
	return strList

def wordToSum(word):

    sum = 0
    
    for c in word:
        sum += ord(c)
    
    return sum
    
def createHash(data):
    
    table = {}
    
    for d in data:
        
        sum = wordToSum(d)
		
		
        if not sum in table.keys():
            table[sum] = []
            
        table[sum].append(d)
        
    return table
    
def findWords(table, scrambled):

	data = StrToList('\n', scrambled)
	out = ""

	#for k in table.keys():
	#	print(table[k])
	last = data[-1]
	for d in data:
		sum = wordToSum(d)
		
		#search table for words matching sum
		for val in table[sum]:
			if sortString(val) == sortString(d):
			
				if d is last:
					out += val
					break
				else:
					out += val + ","
					break
		
		
		#check all chars of each word matching sum
    
	return out
    
    
def descramble():
	scrambled = usrin.get()
	usrin.delete(0, len(usrin.get()))
	descrambled = findWords(table, scrambled)
	
	usrin.insert(0, descrambled)
	
	return 0
    

#get word list

#listFile = open(r"C:\Users\Megan\Documents\Python Scripts\HTS\Pro1\wordlist.txt", "r")
listFile = open(r"wordlist.txt", "r")
wordList = listFile.read()

#convert wordlist to array of strings
data = StrToList('\n', wordList)
data.sort()
table = createHash(data)



master = Tk()

inLabel = Label(master, text="Paste Here: ")
inLabel.pack()

usrin = Entry(master)
usrin.pack()

confirm = Button(master, text="Confirm", command = descramble)
confirm.pack()

master.mainloop()





