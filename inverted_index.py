import sys
import os 
import string

d = {}     #  global dictionary declared 

def _stemmer(word) :
	suffixes = {
			1: ["ो","े","ू","ु","ी","ि","ा"],
			2: ["कर","ाओ","िए","ाई","ाए","ने","नी","ना","ते","ीं","ती","ता","ाँ","ां","ों","ें"],
			3: ["ाकर","ाइए","ाईं","ाया","ेगी","ेगा","ोगी","ोगे","ाने","ाना","ाते","ाती","ाता","तीं","ाओं","ाएं","ुओं","ुएं","ुआं"],
			4: ["ाएगी","ाएगा","ाओगी","ाओगे","एंगी","ेंगी","एंगे","ेंगे","ूंगी","ूंगा","ातीं","नाओं","नाएं","ताओं","ताएं","ियाँ","ियों","ियां"],
			5: ["ाएंगी","ाएंगे","ाऊंगी","ाऊंगा","ाइयाँ","ाइयों","ाइयां"],
		}
	if len(word) > 6 :
		for s in suffixes[5] :
			if word.endswith(s) :
				return(word[:-5])
	if len(word) > 5 :
		for s in suffixes[4] :
			if word.endswith(s) :
				return(word[:-4])
	if len(word) > 4 :
		for s in suffixes[3] :
			if word.endswith(s) :
				return(word[:-3])
	if len(word) > 3 :
		for s in suffixes[2] :
			if word.endswith(s) :
				return(word[:-2])
	if len(word) > 2 :
		for s in suffixes[1] :
			if word.endswith(s) :
				return(word[:-1])
	return word
def _punctuation(word) :	# to remove words like <story>
	if "<" in word  and ">" in word :
		temp = word[word.index("<"):word.index(">")]
		word = word.replace(temp,"")
	if "<" in word  :
		temp = word[word.index("<"):]
		word = word.replace(temp,"")
	new_word = word.strip(string.punctuation + "।" + " ")
	return new_word



def inverted_index(filename,stop_words,index) :
	file = open(os.path.join('hindi',filename),"r").read().split()
	for word in file :
		word = _punctuation(word)
		word = _stemmer(word)
		# print(word)	
		if word in stop_words :
			pass
		else :
			if word not in d :    # all the words are stored in dictionary with the name of its document 
				d.update({word:[filename]} )			
			else :
				d[word].append(filename)

def main():
	# reading stop words file 
	stop_words = open('stop_words.txt','r').read().split()
	
	print("stop words are added ")
	print("reading all the files in the folder . . . ") 	

	count = 1  
	files = os.listdir('hindi/.')
	n_files = len(files)
	for filename in files:
		inverted_index(filename,stop_words,count)
		count = count + 1
		print("Percentage Complete: {0}".format(count/float(n_files)*100), end='\r')


if __name__ == '__main__':
	main()
  # if you want to print whole dictionary
	# for i in d : 
	# 	print("%s -----> "%i),        
	# 	print(d[i])
	 n = input("enter choice to exit press 2");
	 while n != 2 :
      print("sixe of lexicon ...   =  ") ,
      print(len(d))
      filename = input("enter file name")
      word = input("entr the word you want to check ")
      print("size of the posting list of the entered word ="),
      print(len(d[word]))
      print(d[word])
      print(filename in d[word])

