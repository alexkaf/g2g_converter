import sys

rules = open("rules_costs.txt","r")
mod_rules = open("G.txt","w")

prev_output = sys.stdout
sys.stdout = mod_rules

rules_lines = rules.readlines()
counter = 2
for line in rules_lines:
	line_split = line.split()

	if len(line_split[0]) == 1:
		if len(line_split[1]) == 1:
			#print(line_split[2],line_split[3])
			print(0,0,line_split[0],line_split[1],line_split[2])
		else:
			#print(line_split[2],line_split[3])
			print(0,counter,line_split[0],line_split[1][0],line_split[2])
			print(counter,0,"<epsilon>",line_split[1][1],0)
			counter += 1
	else:
		if len(line_split[1]) == 1:
			print(0,counter,line_split[0][0],line_split[1],line_split[2])
			print(counter,0,line_split[0][1],'<epsilon>',0)
			counter += 1
else:
	print(0)
	sys.stdout = prev_output
