import dict_funcs2 as orthograph
import fst_make as fst
import test 
import os

keyboard = input("GREEKLISH-GREEK (1) GREEKLISH-GREEK_ORTH (2) GREEK-GREEK-ORTH (3) ")

while(1):
	if keyboard == "1":
		test.compare_test("test_gr.txt","test_greng.txt",1,"0")
		break
	elif keyboard == "2":
		test.compare_test("test_gr.txt","test_greng.txt",2,input("S1R (1) S2R (2) S1P (3) S2P (4) "))
		break
	elif keyboard == "3":
		test.compare_test("test_co.txt","test_wr.txt",3,input("S1R (1) S2R (2) S1P (3) S2P (4) "))
		break
	else:
		continue
