lexicon_en = open('en_caps_noaccent.dict','r')
lex_rules_en = open('A2.txt','w')

#gia to greeklish lexiko:
lines = lexicon_en.readlines()
total_counter=1
final_states=[]
for current_line in lines:
        for i in range(0,len(current_line)-1):
            if(i==0):
                lex_rules_en.write(str(0) + ' ' + str(total_counter) + ' ' + current_line[i] + ' ' + current_line[i] + '\n')
                total_counter+=1
            else:
                lex_rules_en.write(str(total_counter-1) + ' ' + str(total_counter) + ' ' + current_line[i] + ' ' + current_line[i] + '\n')
                total_counter+=1
        final_states.append(str(total_counter-1))


for final_state in final_states:
   lex_rules_en.write(final_state+'\n')
