lexicon_gr = open('el_caps_noaccent.dict','r')
lex_rules_gr = open('A1.txt','w')

#gia to elliniko lexiko:
lines = lexicon_gr.readlines()
total_counter=0
final_states=[]
for current_line in lines:
        if ( total_counter == 0 ):
            for i in range(0,len(current_line)-1):
                if(i==0):
                    total_counter+=1
                elif(i==1):
                    lex_rules_gr.write(str(0) + ' ' + str(total_counter) + ' ' + current_line[i] + ' ' + current_line[i] + '\n')
                    total_counter+=1
                else:
                    lex_rules_gr.write(str(total_counter-1) + ' ' + str(total_counter) + ' ' + current_line[i] + ' ' + current_line[i] + '\n')
                    total_counter+=1

            final_states.append(str(total_counter-1))
        else:
            for i in range(0,len(current_line)-1):
                if(i==0):
                    lex_rules_gr.write(str(0) + ' ' + str(total_counter) + ' ' + current_line[i] + ' ' + current_line[i] + '\n')
                    total_counter+=1
                else:
                    lex_rules_gr.write(str(total_counter-1) + ' ' + str(total_counter) + ' ' + current_line[i] + ' ' + current_line[i] + '\n')
                    total_counter+=1
            final_states.append(str(total_counter-1))


for final_state in final_states:
   lex_rules_gr.write(final_state+'\n')


lex_rules_gr.close()
