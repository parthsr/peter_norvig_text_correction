import nltk
from nltk.tokenize import RegexpTokenizer
from correct import correct

new_file = open("new_data.txt","w")
with open("mail_data2.txt","r") as f:
	for line in f:
		tokenizer = RegexpTokenizer('[A-Za-z.,?!]{1,}')		
		a = tokenizer.tokenize(line)
		b = nltk.pos_tag(a)
		for word,tag in b:
			if tag=="NNP":
				new_file.write(word+" ")
			if tag!="NNP":
				word=correct(word.lower())
				new_file.write(word+" ")
		new_file.write("\n")
new_file.close()

