#edw den xreiazomaste diaforetiko afou ta latinika metatrepontai ston euato tous!
#epomenws arkei to idi iparxon dict_eng.syms ws input kai output sthn fstcompile!


fI = open("I.txt","w")
fdict= open("dict_eng.syms","r")

cost=2
lines=fdict.readlines()
i=0
for current_line in lines:
    if(i==0):
        i+=1
        continue #kanw skip to <epsilon>
    words=current_line.split()
    fI.write( str(0) + " " + str(0) + " " + words[0] + " " + words[0] + " " + str(cost) + "\n")

#orismos miden ws katastasis apodoxis
fI.write(str(0))
fI.close()
fdict.close()
