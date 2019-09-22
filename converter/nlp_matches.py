import mods
import sys



rules = {'C':[],'Q':[]}

greek_file = open("train_gr.txt","r")
greeklish_file = open("train_greng.txt","r")
rules_file = open("rules_partial_poss.txt","w")
output = open("rules_counts.txt","w")

line_greek = greek_file.readline()
line_greeklish = greeklish_file.readline()

global_counter = 0
flag = 0
while((line_greeklish != '')|(line_greek != '')):
	split_greek_line = line_greek.split()
	split_greeklish_line = line_greeklish.split()
	word_counter = 0
	for word_greek in split_greek_line:
		word_greeklish = split_greeklish_line[word_counter]
		if(len(word_greek)/2 == len(word_greeklish)):
			mods.one2onemod(word_greek,word_greeklish,rules)
			global_counter = global_counter + 1
		word_counter = word_counter + 1
	line_greeklish = greeklish_file.readline()
	line_greek = greek_file.readline()

greek_file.close()
greeklish_file.close()

mods.printer1(output,rules)			#tipwnei tis antistoixies me to plithos emfanisis!
mods.calculate_possibilities(rules) #ipologizei tis sxetikes pithanotites!
mods.printer1(rules_file,rules)		#tipwnei tis antistoixies me tis sxetikes pithanotites
rules_file.close()


#2-1 kai 1-2 eythi
greek_file = open("train_gr.txt","r")
greeklish_file = open("train_greng.txt","r")


line_greek = greek_file.readline()
line_greeklish = greeklish_file.readline()

while ((line_greeklish != '')|(line_greek != '')):
	split_greeklish_line = line_greeklish.split()
	split_greek_line = line_greek.split()
	gr_counter = 0
	for en_word in split_greeklish_line:
		gr_word = split_greek_line[gr_counter]
		if(len(en_word) == len(gr_word)):
			gr_counter += 1
			continue
		if (len(en_word) > len(gr_word)/2):
			mods.two2one(gr_word,en_word,rules,False)
		elif (len(en_word) < len(gr_word)/2):
			mods.one2two(gr_word,en_word,rules,False)
		gr_counter += 1
	line_greeklish = greeklish_file.readline()
	line_greek = greek_file .readline()

greek_file.close()
greeklish_file.close()

lexicon = {}

mods.concat(output,rules)		#enwsi dictionaries kai olwn twn antistoixiwn me ta plithi emfanisis sto output(rules_counts)
output.close()
output = open('rules_counts.txt','r+')	#xrisi gia dimiourgia tou dictionary
output1 = open('rules_poss.txt','w')
output2 = open('rules_costs.txt','w')
mods.create_dic(output,lexicon)
mods.calc_possibilities(lexicon)		#ipologizei oliki pithanotita gia kathe antistoixia!
mods.printer1(output1,lexicon)			#tipwnei tin oliki pithanotita gia kathe antistoixia
mods.printer_costs(output2,lexicon)		#tipwnei to kostos gia kathe antistoixia
output.close()
output1.close()
output2.close()
