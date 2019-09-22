import os
import fst_make as fst

def compare_test(correct,wrong,set,prm):
	file_correct = open(correct,"r")
	file_wrong = open(wrong,"r")
	correct_lines = file_correct.readlines()
	wrong_lines = file_wrong.readlines()
	counter = 0
	counter_wr = 0
	counter_trans = 0
	counter_empty = 0
	counter_co = 0
	if set == 1:
		os.system("fstarcsort T.fst Ts.fst")
		for correct_line_full,wrong_line_full in zip(correct_lines,wrong_lines):
			correct_line = correct_line_full.split()
			wrong_line = wrong_line_full.split()
			for wrong_word,correct_word in zip(wrong_line,correct_line):
				fst.word_to_fst(wrong_word)
				os.system("./greeklish_to_greek")
				word = fst.fst_to_word("text.txt")
				counter += 1
				print("Greeklish word:",wrong_word,"Changed word:",word)
				if(word == correct_word):
					counter_co += 1
				else:
					if word == '':
						counter_empty += 1
					if (isEnglish(correct_word))&(not isEnglish(word)):
						counter_trans += 1
					counter_wr += 1
		os.system("rm Ts.fst")
	elif set == 2:
		for correct_line_full,wrong_line_full in zip(correct_lines,wrong_lines):
			correct_line = correct_line_full.split()
			wrong_line = wrong_line_full.split()
			for wrong_word,correct_word in zip(wrong_line,correct_line):
				fst.word_to_fst(wrong_word)
				os.system("./greeklish_to_pos")
				if prm == "1":
					os.system('./spell_checker1')
				elif prm == "2":
					os.system('./spell_checker2')
				elif prm == "3":
					os.system('./spell_checker3')
				else:
					os.system('./spell_checker4')
				word = fst.fst_to_word("text.txt")
				print("Greeklish word:",wrong_word,"Changed word:",word)
				counter += 1
				if(word == correct_word):
					counter_co += 1
				else:
					if word == '':
						counter_empty += 1
					if (isEnglish(correct_word))&(not isEnglish(word)):
						counter_trans += 1
					counter_wr += 1
	else:
		for correct_line_full,wrong_line_full in zip(correct_lines,wrong_lines):
			correct_line = correct_line_full.split()
			wrong_line = wrong_line_full.split()
			for wrong_word,correct_word in zip(wrong_line,correct_line):
				fst.word_to_fst(wrong_word)
				if prm == "1":
					os.system('./spell_checker11')
				elif prm == "2":
					os.system('./spell_checker22')
				elif prm == "3":
					os.system('./spell_checker33')
				else:
					os.system('./spell_checker44')
				word = fst.fst_to_word("text.txt")
				print("Old greek word:",wrong_word,"Changed word:",word)
				counter += 1
				if(word == correct_word):
					counter_co += 1
				else:
					if word == '':
						counter_empty += 1
					if (isEnglish(correct_word))&(not isEnglish(word)):
						counter_trans += 1
					counter_wr += 1


	os.system("rm text.txt sample.txt WS1.fst w.fst ")
	print("Correct words:",counter_co,counter_co*1.0/counter,"%")
	print("Wrong words:",counter_wr,counter_wr*1.0/counter,"%")
	print("English to Greek:",counter_trans,counter_trans*1.0/counter,"%")
	print("No match:",counter_empty,counter_empty*1.0/counter,"%")
	print("All words:",counter)
	print("Accuracy:",((counter_co)/counter)*100,"%")
	os.system("say End ")

#-*- coding: utf-8 -*-
def isEnglish(s):
    try:
        s.encode(encoding='utf-8').decode('ascii')
    except UnicodeDecodeError:
        return False
    else:
        return True

