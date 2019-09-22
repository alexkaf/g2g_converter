import sys
import math

def reverse_greeklish(text):
    if len(text) <= 1:
        return text

    return reverse_greeklish(text[1:]) + text[0]


def reverse_greek(text):
    if len(text) <= 1:
        return text

    return reverse_greek(text[2:])+(text[0]+text[1])


def one2onemod(greek_word,greeklish_word,dictionary):
	counter = 0
	for greeklish_letter in greeklish_word:
		greek_letter = greek_word[counter] + greek_word[counter + 1]
		if(dictionary.get(greeklish_letter) == None):
			dictionary[greeklish_letter] = [[greek_letter,1]]
		else:
			for combination in dictionary[greeklish_letter]:
				if greek_letter == combination[0]:
					combination[1] = combination[1] + 1
					break
			else:
				dictionary[greeklish_letter].append([greek_letter,1])
		counter = counter + 2

def printer1(filename,dictionary):
	prev = sys.stdout
	sys.stdout = filename
	for greeklish_letter in dictionary:
		for combination in dictionary[greeklish_letter]:
			print greeklish_letter,combination[0],(combination[1])
	sys.stdout = prev


#den tin xrisimopoihsame!!
def printer(filename,dictionary):
	prev = sys.stdout
	sys.stdout = filename
	for greeklish_letter in dictionary:
		for combination in dictionary[greeklish_letter]:
			print greeklish_letter,combination[0],("%.4f" % combination[1])
	sys.stdout = prev


def printer_costs(filename,dictionary):
	prev = sys.stdout
	sys.stdout = filename
	for greeklish_letter in dictionary:
		for combination in dictionary[greeklish_letter]:
			print greeklish_letter,combination[0],(- math.log10(combination[1]))
	sys.stdout = prev

def calculate_possibilities(dictionary):
	for greeklish_letter in dictionary:
		sum_of_appearences = 0
		for combination in dictionary[greeklish_letter]:
			sum_of_appearences = sum_of_appearences + combination[1]
		for combination in dictionary[greeklish_letter]:
			combination[1] = 100*float(combination[1])/sum_of_appearences

def one2two(greek_word,greeklish_word,dictionary,inverse):
	flag1 = flag2 = False
	gr_offset = 0
	flag_break = True
	for offset in range(0,len(greeklish_word)):
		gr_letter = greek_word[2*(offset + gr_offset)] + greek_word[2*(offset + gr_offset) + 1]
		en_letter = greeklish_word[offset]
		for combination in dictionary[en_letter]:
			if((combination[0] == gr_letter)&(combination[1] < 4.48)):
				flag1 = True
				break
			elif((combination[0] == gr_letter)&(combination[1] > 4.48)):
				flag1 = False
				break
		else:
			flag1 = True
		if flag1:
			if (((offset + 1) == len(greeklish_word))&((2*(offset + gr_offset + 1)) == len(greek_word))):
				break
			elif (((offset + 1) == len(greeklish_word))&((2*(offset + gr_offset + 1)) < len(greek_word))):
				gr_pair = greek_word[2*(offset + gr_offset)] + greek_word[2*(offset + gr_offset) + 1] + greek_word[2*(offset + gr_offset) + 2]  + greek_word[2*(offset + gr_offset) + 3]
				if(inverse==True):
					gr_pair=reverse_greek(gr_pair)
				if en_letter in dictionary:
					for combination in dictionary[en_letter]:
						if(combination[0] == gr_pair):
							combination[1] += 1
							break
					else:
						dictionary[en_letter].append([gr_pair,1])
						break
				else:
					dictionary[en_letter] = [[gr_pair,1]]
					break
				break
			next_en_letter = greeklish_word[offset + 1]
			next_gr_letter = greek_word[2*(offset + gr_offset) + 2] + greek_word[2*(offset + gr_offset) + 3]
			for combination in dictionary[next_en_letter]:
				if((combination[0] == next_gr_letter)&(combination[1] < 4.48)):
					flag2 = True
					break
				elif((combination[0] == next_gr_letter)&(combination[1] > 4.48)):
					flag2 = False
					break
			else:
				flag2 = True
		if flag1&flag2:
			gr_pair = gr_letter + next_gr_letter
			if en_letter in dictionary:
				for combination in dictionary[en_letter]:
					if (combination[0] == gr_pair):
						combination[1] += 1
						break
				else:
					dictionary[en_letter].append([gr_pair,1])
			else:
				dictionary[en_letter] = [[gr_pair,1]]
			gr_offset += 1

def two2one(greek_word,greeklish_word,dictionary,inverse):
	counter_gr = 0
	counter_en = 0
	flag1 = flag2 = flag_cont = False
	for en_letter in greeklish_word:
		if flag_cont:
			flag_cont = False
			continue
		greek_letter = greek_word[counter_gr] + greek_word[counter_gr + 1]
		for combination in dictionary[en_letter]:
			if((combination[0] == greek_letter)&(combination[1] < 4.48)):
				flag1 = True
				break
			elif ((combination[0] == greek_letter)&(combination[1] > 4.48)):
				flag1 = False
				break
		else:
			flag1 = True
		if flag1:
			next_greek_letter = greek_word[counter_gr + 2] + greek_word[counter_gr + 3]
			next_en_letter = greeklish_word[counter_en + 1]
			for combination in dictionary[next_en_letter]:
				if((combination[0] == next_greek_letter)&(combination[1] < 4.48)):
					flag2 = True
					break
				elif ((combination[0] == greek_letter)&(combination[1] > 4.48)):
					flag2 = False
					break
			else:
				flag2 = True
		if flag1&flag2:
			flag_cont = True
			greeklish_pair = en_letter + next_en_letter
			if inverse:
				greeklish_pair=reverse_greeklish(greeklish_pair)
			if greeklish_pair in dictionary:
				for combination in dictionary[greeklish_pair]:
					if (combination[0] == greek_letter):
						combination[1] += 1
						break
				else:
					dictionary[greeklish_pair].append([greek_letter,1])
			else:
				dictionary[greeklish_pair] = [[greek_letter,1]]
		counter_gr += 2
		counter_en += 1
		flag1 = flag2 = False

def concat(filename,dictionary):
	temp = sys.stdout
	sys.stdout = filename
	for key in dictionary:
		if len(key) == 2:
			for combination in dictionary[key]:
				print key,combination[0],combination[1]
		elif len(key) == 1:
			for combination in dictionary[key]:
				if len(combination[0]) == 4:
					print key,combination[0],combination[1]
	sys.stdout = temp

def create_dic(filename,dictionary):
	line = filename.readline()
	while line != '':
		split = line.split()
		if split[0] not in dictionary:
			dictionary[split[0]] = [[split[1],int(split[2])]]
		else:
			dictionary[split[0]].append([split[1],int(split[2])])
		line = filename.readline()

def calc_possibilities(dictionary):
	sum_of_N = 0
	for key in dictionary:
		for combination in dictionary[key]:
			sum_of_N += combination[1]
	for key in dictionary:
		for combination in dictionary[key]:
			combination[1] = float(combination[1])/sum_of_N
