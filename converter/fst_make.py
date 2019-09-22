import sys

def word_to_fst(word):
	fst = open("sample.txt","w")
	prev_output = sys.stdout
	sys.stdout = fst
	counter = 0
	for letter in word:
		print(counter,counter + 1,letter,letter)
		counter += 1
	else:
		print(counter)
		sys.stdout = prev_output
		fst.close()

def fst_to_word(filename):
	fst = open(filename,"r")
	counter = 0
	word = ''
	first_letter = ''
	fst_lines = fst.readlines()
	for line in fst_lines:
		atom = line.split()
		if len(atom) < 4:
			counter += 1
			continue
		if counter == 0:
			if str(atom[3]) == "<epsilon>":
				continue
			first_letter = str(atom[3])
			counter += 1
		else:
			if str(atom[3]) == "<epsilon>":
				continue
			word = str(atom[3]) + word
	else:
		if counter == 0:
			word = ''
		else:
			word = first_letter + word
		fst.close()
		return word


def make_of_I(): 
	output = open("self_to_self.txt","w")

	prev_output = sys.stdout
	sys.stdout = output

	letter = "Α"		
	code = ord("Α")

	for i in range(0,25):
		if(ord(letter) == ord("Α") + 17):
			letter = ord(letter)
			letter += 1
			letter = chr(letter)
			continue
		print(0,0,letter,letter,0)
		letter = ord(letter)
		letter += 1
		letter = chr(letter)
	else:
		print(0)
		output.close()
		sys.stdout = prev_output

def make_of_I2(): 
	output = open("self_to_self.txt","w")

	prev_output = sys.stdout
	sys.stdout = output

	letter = "Α"		
	code = ord("Α")

	for i in range(0,25):
		if(ord(letter) == ord("Α") + 17):
			letter = ord(letter)
			letter += 1
			letter = chr(letter)
			continue
		print(0,0,letter,letter,0)
		letter = ord(letter)
		letter += 1
		letter = chr(letter)

	letter = "A"		
	code = ord("A")

	for i in range(0,26):
		print(0,0,letter,letter,0)
		letter = ord(letter)
		letter += 1
		letter = chr(letter)
	else:
		print(0)
		output.close()
		sys.stdout = prev_output

def make_of_E(swap,delete,insert,subst):
	output = open("make_of_Efirst.txt","w")

	prev_output = sys.stdout
	sys.stdout = output

	letter = "A"
	code = ord("A")

	letter = "Α"		
	code = ord("Α")

	list_of_greek_letters = []
	print(0,1,"<epsilon>","<epsilon>",0)
	for i in range(0,25):
		if(ord(letter) == ord("Α") + 17):
			letter = ord(letter)
			letter += 1
			letter = chr(letter)
			continue
		list_of_greek_letters.append(letter)
		print(0,1,letter,letter,0)
		letter = ord(letter)
		letter += 1
		letter = chr(letter)
	else:
		print(1)
		# add substitution lines
		for head_letter in list_of_greek_letters:
			for sub_letter in list_of_greek_letters:
				if head_letter == sub_letter:
					continue
				print(0,1,head_letter,sub_letter,subst)
		# add deletion lines
		for letter in list_of_greek_letters:
			print(0,1,letter,"<epsilon>",delete)
		# add insertion lines
		for letter in list_of_greek_letters:
			print(0,1,"<epsilon>",letter,insert)
		# add swap lines
		counter = 2
		for head_letter in list_of_greek_letters:
			for sub_letter in list_of_greek_letters:
				if head_letter == sub_letter:
					continue
				print(0,counter,head_letter,sub_letter,swap)
				print(counter,1,sub_letter,head_letter,0)
				counter += 1
		output.close()
		sys.stdout = prev_output

def Epsilon(rules):
	output = open("make_of_Epsilon.txt","w")

	prev_output = sys.stdout
	sys.stdout = output

	print(0,1,"<epsilon>","<epsilon>",0)

	letter = "Α"

	list_of_greek_letters = []
	for i in range(0,25):
		if(ord(letter) == ord("Α") + 17):
			letter = ord(letter)
			letter += 1
			letter = chr(letter)
			continue
		list_of_greek_letters.append(letter)
		letter = ord(letter)
		letter += 1
		letter = chr(letter)

	for letter in list_of_greek_letters:
		print(0,1,letter,letter,0)

	#subts
	for key in rules:
		if(len(key) == 1)&(key != "e"):
			for combination in rules[key]:
				if combination[0] != "e":
					print(0,1,key,combination[0],combination[1])

	#swaps
	counter = 2
	for key in rules:
		if len(key) == 2:
			for combination in rules[key]:
				print(0,counter,key[0],key[1],combination[1])
				print(counter,1,key[1],key[0],0)
				counter += 1

	#deletes

	for key in rules:
		for combination in rules[key]:
			if combination[0] == "e":
				print(0,1,key,"<epsilon>",combination[1])

	#inserts
	for key in rules:
		if key == "e":
			for combination in rules[key]:
				print(0,1,"<epsilon>",combination[0],combination[1])
	else:
		print(1)
		output.close()
		sys.stdout = prev_output











