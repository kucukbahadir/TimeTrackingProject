import json

def load_json(lst):
	lst =[]
	# Opening JSON file
	f = open('UserInfo.json')

	# returns JSON object as list
	data = json.load(f)

	# Iterating through the json
	# list
	for i in data:
		lst.append(i)

	# Closing file
	f.close()
	return(lst)
#########################################################################################################

def generate_usr_lst(lst):
	usr_lst =[]
	for i in lst:
		for key in i:
			if key == "user":
				usr_lst.append(i[key][0])
	return(usr_lst)

############################################################################################################

def update_json (lst):
	#with open(r"UserInfo.json", 'w') as fp:
	#	fp.write('\n'.join(lst))
	#	fp.close()


	f = open("UserInfo.json", "w")  
	f.write("[")
	for item in lst:
        # write each item on a new line
		f.write("%s," % item)
	f.write("]")
	f.close()