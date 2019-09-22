import math

def calculate_pos(swaps,deletes,subts,inserts):

	total = swaps + deletes + subts + inserts

	cost_ins = -math.log(inserts*1.0/total,10)
	cost_swap = -math.log(swaps*1.0/total,10)
	cost_sub = -math.log(subts*1.0/total,10)
	cost_del = -math.log(deletes*1.0/total,10)
	return cost_del,cost_sub,cost_swap,cost_ins


def calculate(rules):
	#calculate swaps
	total_swaps = 0

	for key in rules:
		if len(key) == 2:
			for combination in rules[key]:
				total_swaps += combination[1]
	else:
		for key in rules:
			if len(key) == 2:
				for combination in rules[key]:
					combination[1] = -math.log(combination[1]*1.0/total_swaps,10)
	#calculate deletes
	total_dels = 0
	for key in rules:
		for combination in rules[key]:
			if combination[0] == "e":
				total_dels += combination[1]
	else:
		for key in rules:
			for combination in rules[key]:
				if combination[0] == "e":
					combination[1] = -math.log(combination[1]*1.0/total_dels,10)
	#calculate inserts
	total_ins = 0
	for key in rules:
		if key == "e":
			for combination in rules[key]:
				total_ins += combination[1]
	else:
		for key in rules:
			if key == "e":
				for combination in rules[key]:
					combination[1] = -math.log(combination[1]*1.0/total_ins,10)


	#calcuate subts 
	total_subts = 0
	for key in rules:
		if (len(key) == 1)&(key != "e"):
			for combination in rules[key]:
				if combination[0] != "e":
					total_subts += combination[1]
	else:
		for key in rules:
			if (len(key) == 1)&(key != "e"):
				for combination in rules[key]:
					if combination[0] != "e":
						combination[1] = -math.log(combination[1]*1.0/total_subts,10)

	total_sum = total_subts + total_ins + total_dels + total_swaps

	for key in rules:
			if len(key) == 2:
				for combination in rules[key]:
					combination[1] = -math.log(combination[1]*1.0/total_sum,10)
	for key in rules:
			for combination in rules[key]:
				if combination[0] == "e":
					combination[1] = -math.log(combination[1]*1.0/total_sum,10)
	for key in rules:
			if key == "e":
				for combination in rules[key]:
					combination[1] = -math.log(combination[1]*1.0/total_sum,10)
	for key in rules:
			if (len(key) == 1)&(key != "e"):
				for combination in rules[key]:
					if combination[0] != "e":
						combination[1] = -math.log(combination[1]*1.0/total_sum,10)
	return rules

def errors_find(right_file,wrong_file,prm):

	rules = {}
	rules = fill_rules(rules)
	file_right = open(right_file,"r")
	file_wrong = open(wrong_file,"r")

	right_lines = file_right.readlines()
	wrong_lines = file_wrong.readlines()

	swaps = 0
	delete = 0
	inserts = 0
	subts = 0

	for right_line,wrong_line in zip(right_lines,wrong_lines):
		right_split = right_line.split()
		wrong_split = wrong_line.split()

		for right_word,wrong_word in zip(right_split,wrong_split):

			faults = 0
			counter = 0
			flag = False
			if len(right_word) == len(wrong_word):
				swap_flag = False
				buff = []
				for right_letter,wrong_letter in zip(right_word,wrong_word):
					if flag:
						flag = False
						continue
					if right_letter == wrong_letter:
						counter += 1
						continue
					elif(right_letter != wrong_letter):
						if faults == 1:
							faults += 1
							break
						if counter + 1 == len(right_word):
							if right_letter == wrong_letter:
								break
							else:
								buff = [wrong_letter,right_letter]
								swap_flag = False
								faults += 1
								continue
						if(right_letter == wrong_word[counter + 1])&(wrong_letter == right_word[counter + 1]):
							swap_flag = True
							buff = [wrong_letter + wrong_word[counter + 1],right_letter + right_word[counter + 1]]
							faults += 1
							flag = True
							counter += 2
							continue
						else:
							buff = [wrong_letter,right_letter]
							swap_flag = False
							faults += 1
							counter += 1
							continue
				if faults != 2:
					if swap_flag:
						#print("SWAP",right_word,wrong_word)
						put(buff,rules)
						swaps += 1
					else:
						if faults == 0:
							continue
						put(buff,rules)
						#print("SUB",right_word,wrong_word)
						subts += 1
			else:
				if len(right_word) > len(wrong_word):
					delete += not_eq(right_word,wrong_word,rules,"less")
				else:
					inserts += not_eq(wrong_word,right_word,rules,"more")
	if prm == 1:
		return (calculate_pos(swaps,delete,subts,inserts))
	else:
		return calculate(rules)



def not_eq(right_word,wrong_word,rules,set):
	counter_right = 0
	counter_wrong = 0
	temp_dels = 0
	buff = []
	while(counter_wrong != len(wrong_word)):
		if counter_right == len(right_word):
			break
		if(right_word[counter_right] == wrong_word[counter_wrong]):
			counter_wrong += 1
			counter_right += 1
		elif(right_word[counter_right + 1] == wrong_word[counter_wrong]):
			if set == "less":
				buff = ["e",right_word[counter_right]]
			else:
				buff = [right_word[counter_right],"e"]
			counter_right += 1
			temp_dels += 1
		else:
			counter_right += 1
			counter_wrong += 1
	else:
		if(counter_right != len(right_word)):
			while(counter_right != len(right_word)):
				if(right_word[counter_right] == wrong_word[counter_wrong - 1]):
					counter_right += 1
					continue
				else:
					if set == "less":
						buff = ["e",right_word[counter_right]]
					else:
						buff = [right_word[counter_right],"e"]
					temp_dels += 1
					counter_right += 1
	if(temp_dels == 1):
		if buff != []:
			put(buff,rules)
		return 1
	else:
		return 0

def fill_rules(rules):
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

	#swaps
	for head_letter in list_of_greek_letters:
		for sub_letter in list_of_greek_letters:
			if sub_letter == head_letter:
				continue
			pair = head_letter + sub_letter
			inv_pair = sub_letter + head_letter
			rules[pair] = [[inv_pair,1]]

	#subts
	for head_letter in list_of_greek_letters:
		counter = 0
		for sub_letter in list_of_greek_letters:
			if head_letter == sub_letter:
				continue
			if counter == 0:
				rules[head_letter] = [[sub_letter,1]]
				counter += 1
			else:
				rules[head_letter].append([sub_letter,1])

	#inserts
	for letter in list_of_greek_letters:
		if "e" not in rules:
			rules["e"] = [[letter,1]]
		else:
			rules["e"].append([letter,1])

	for letter in list_of_greek_letters:
		rules[letter].append(["e",1])
	return rules


def put(buffer,rules):
	for combination in rules[buffer[0]]:
		if combination[0] == buffer[1]:
			combination[1] += 1




