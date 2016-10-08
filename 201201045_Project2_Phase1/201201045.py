import nltk	
import sys

# function to add the contents of file, after proper parsing, to the given dictionary
def add_to_dict(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def remove_reduncy(list1,list2,list3,list4,list5):
	l=[]
	l.extend(list1)
	l.extend(list2)
	l.extend(list3)
	l.extend(list4)
	l.extend(list5)
	toreturn=[]
	for i in l:
		if i not in toreturn:
			toreturn.append(i)
	return toreturn

def addlist(fname,lists):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split('\t')
		a = temp[0]
		b = temp[1:]
		lists.append(a)

def add_to_dict3(dictionary,fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split('\t')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			dictionary[a] = b

def add_to_dict2(dictionary, fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		if a not in dictionary:
			tmp=[]
			tmp.append(int(b[1]))
			if(tmp[0]==0):
				tmp.append(1)
			else:
				tmp.append(0)
			dictionary[a] = tmp
		else:
			tmp=[]
			tmp.append(int(b[1]))
			dictionary[a][0]+=tmp[0];
			if(tmp[0]==0):
				dictionary[a][1]+=1;
def add_to_list(lists,fname):
	f = open(fname, 'r')
	for line in f:
		temp = line[:-1]
		temp = temp.split('\t')
		a=temp[0]
		if(a not in lists):
			lists.append(a)


# This function returns a list of variable, corresponding to players who satisfy the criteria : strike rate > 150.0
def parse_for_sr(bat, num):
	toreturn = []

	# strike rate is in the 7th column
	for i in bat:
		temp = bat[i]
		k = float(temp[6])
		if k > num:
			toreturn.append(i)
	return  toreturn

# It retrieves the variable names corresponding to players, who have greater than 0 sixes
def parse_for_six(bat, num):
	toreturn  = []

	# number of six hit are in 6th column
	for i in bat:
		temp = bat[i]
		k = int(temp[5])
		if k > num:
			toreturn.append(i)
	return toreturn
def parse_for_bat(bat,num):
	toreturn=[]
	for i in bat:
		temp=bat[i]
		k=int(temp[1])
		if(k==0):
			toreturn.append(i)
	return toreturn
def parse_for_mom(mom):
	toreturn =[]
	for i in mom:
		#		temp=mom[1];
#		if temp not in toreturn:
		toreturn.append(i);
	return toreturn;

def parse_for_wonby(wonby):
	toreturn=[]
	for i in wonby:
		temp=wonby[1];
		if temp not in toreturn:
			toreturn.append(temp);
	return toreturn;

def parse_for_strate(bat):
	toreturn=[]
	for i in bat:
		temp=bat[i][6];
		temp=(float)(temp);
		if(temp>200.00 and i not in toreturn):
			toreturn.append(i);
	return toreturn

def parse_for_sixmorefour(bat):
	toreturn=[]
	for i in bat:
		temp=bat[i][5];
		temp=(int)(temp);
		temp1=bat[i][4]
		temp1=(int)(temp1);
		if(temp>temp1 and i not in toreturn):
			toreturn.append(i);
	return toreturn

def parse_for_run(bat,num):
	toreturn=[]
	for i in bat:
		temp=bat[i][1];
		temp=(int)(temp);
		if(temp>=num and i not in toreturn):
			toreturn.append(i);
	return toreturn

def parse_for_wicket(bowl,num):
	toreturn=[]
	for i in bowl:
		temp=bowl[i][3];
		temp=int(temp);
		if(temp>=num and i not in toreturn):
			toreturn.append(i);
	return toreturn

def parse_for_over(bowl,num):
	toreturn=[]
	for i in bowl:
		temp=bowl[i][0];
		temp=float(temp);
		if(temp>=num and i not in toreturn):
			toreturn.append(i);
	return toreturn

def parse_for_nowicket(bowl):
	toreturn=[]
	for i in bowl:
		temp=bowl[i][3];
		temp=int(temp);
		if(temp==0 and i not in toreturn):
			toreturn.append(i);
	return toreturn

def parse_for_economy(bowl,val):
	toreturn=[]
	for i in bowl:
		temp=bowl[i][4];
		temp=float(temp);
		if(temp>val and i not in toreturn):
			toreturn.append(i);
	return toreturn;
def parse_for_hund(bat):
	toreturn=[]
	for i in bat:
		temp=bat[i][1];
		temp=int(temp)
		if(temp>=100 and i not in toreturn):
			toreturn.append(i);
	return toreturn;

def parse_for_run_wo_ducks(bat):
	toreturn=[]
	for i in bat:
		temp=bat[i][0];
		temp=int(temp)
		temp1=bat[i][1];
		temp1=int(temp1);
		if(temp>250 and temp1==0 and i not in toreturn):
			toreturn.append(i);
	return toreturn;

def parse_for_age(people,num):
	toreturn=[]
	for i in people:
		#print people
	#	temp=people[i].split('\t')
		temp=people[i][2]
		#temp=temp[2]
		temp=temp.split(' ');
		temp=temp[0];
		temp=int(temp);
		if(temp<26 and i not in toreturn):
			toreturn.append(i);
	return toreturn;

def parse_for_bat_boundary(bat):
	toreturn=[]
	for i in bat:
		temp=bat[i][4]
		temp1=bat[i][6]
		temp=int(temp)
		temp1=float(temp1)
		if(temp>=1 and temp1<100.0 and i not in toreturn):
			toreturn.append(i);
	return toreturn;
def add_to_list2(rhand,lhand,people):
	for i in people:
		temp=people[i][(len(people[i]))-1]
		temp=temp.split('-');
		temp=temp[0];
		if(temp=='Right' and i not in rhand ):
			rhand.append(i)
		elif(temp=='Left' and i not in lhand):
			lhand.append(i)

def compute(rhand,lhand,bowl,right,left):
	for i in bowl:
		if i in rhand:
			temp=bowl[i][0]
			temp=float(temp)
			right=right+temp
		elif i in lhand:
			temp=bowl[i][0]
			temp=float(temp)
			left=left+temp
	temp=[]
	temp.append(right)
	temp.append(left)
	return temp

def parse_for_bat1(bat):
	toreturn=[]
	for i in bat:
		if i not in toreturn:
			toreturn.append(i)
	return toreturn;

def check_wides(bowl,s):
	temp=0
	for i in bowl:
		if i==s and len(bowl[i])>5:
			#print bowl[i][5]
			temp1=int(bowl[i][5][1])
			temp+=temp1
	return temp;

def check_catches(bowl,s):
	temp=0
	for i in bowl:
		if ((("c & b "+s) in bowl[i][0] )or(("c "+s) in bowl[i][0])):
			#print bowl[i][5]
			temp+=1
	return temp;

def check(wonby,wonby_1):
	temp=wonby.keys()[0]
	if temp not in wonby_1:
		wonby_1[temp]=1
	else:
		wonby_1[temp]+=1

def heuristic_15(bowl,temp):
	for i in bowl:
		if i=="RA Jadeja":
			l=int(bowl[i][3]);	#wicket
			h=int(bowl[i][1]);	#maiden
			t=float(bowl[i][4]);  	#economy
			h=4*l + 3.5*h +(13*1.0)/t
			temp.append(h)
	
def heuristic_16(bat,temp):
	for i in bat:
		if i=="MS Dhoni":
			stkrate=float(bat[i][6]);
			six=int(bat[i][5])
			four=int(bat[i][4])
			heu=5*stkrate + 4*six +3.5*four
			temp.append(heu)

def  heuristic_17(bowl,temp,s):
	for i in bowl:
		if i==s:
			l=int(bowl[i][3]);	#wicket
			h=int(bowl[i][1]);	#maiden
			t=float(bowl[i][4]);  	#economy
			h=4*l + 3.5*h +(13*1.0)/t
			temp.append(h)


def heuristic_18(bat,temp):
	for i in bat:
		stkrate=float(bat[i][6]);
		six=int(bat[i][5])
		four=int(bat[i][4])
		run=int(bat[i][1])
		heu=7*run + 5*stkrate + 4*six + 3.5*four
		temp.append(heu)

def loop1(bat,lists1,lists2,profile_ind,profile_new):
	for i in bat:
		if i in profile_ind:
			stkrate=float(bat[i][6]);
			six=int(bat[i][5])
			four=int(bat[i][4])
			run=int(bat[i][1])
			heu=7*run + 5*stkrate + 4*six + 3.5*four
			lists1.append(heu)
		elif i in profile_new:
			stkrate=float(bat[i][6]);
			six=int(bat[i][5])
			four=int(bat[i][4])
			run=int(bat[i][1])
			heu=7*run + 5*stkrate + 4*six + 3.5*four
			lists2.append(heu)

def loop2(bowl,lists1,lists2,profile_ind,profile_new):
	for i in bowl:
		if i in profile_ind:
			l=int(bowl[i][3]);	#wicket
			h=int(bowl[i][1]);	#maiden
			t=float(bowl[i][4]);  	#economy
			h=4*l + 3.5*h +(13*1.0)/t
			lists1.append(h)
		elif i in profile_new:
			l=int(bowl[i][3]);	#wicket
			h=int(bowl[i][1]);	#maiden
			t=float(bowl[i][4]);  	#economy
			h=4*l + 3.5*h +(13*1.0)/t
			lists2.append(h)

def fast_read(lists,fname):
	f = open(fname, 'r')
	i=0
	for line in f:
		if(i==2):
			break
		dictionary={}
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		dictionary[a] = b
		heuristic_18(dictionary,lists)
		i+=1

def fast_read2(lists,fname):
	f = open(fname, 'r')
	i=0
	for line in f:
		if(i<2):
			i+=1
			continue
		if(i==4):
			break
		dictionary={}
		temp = line[:-1]
		temp = temp.split(',')
		a = temp[0]
		b = temp[1:]
		dictionary[a] = b
		heuristic_18(dictionary,lists)
		i+=1

# the function to make the model and answer the query, given the properly formatted strings
def make_model_and_answer(v, query, dt):
	val = nltk.parse_valuation(v)
	dom = val.domain
	m = nltk.Model(dom, val)
	g = nltk.Assignment(dom, [])
	print "The anwer for the query is : ",
	print m.evaluate(query, g)

	# to show the variable (corresponding to player names) for which "srate(x) -> gtsix(x) you can do

	print "Showing the player Names for which  srate(x) -> gtsix(x) given srate(x) is true"
	
	l = nltk.LogicParser()
	c1 = l.parse(' ((srate(x)) & (srate(x) -> gtsix(x)))')
	varnames =  m.satisfiers(c1, 'x', g)
	#print varnames


	for i in varnames:
		for p,q in dt.iteritems():   # naive method to get key given value, in a dictionary
			if q == i:
				print p



# the function to 
#	1. generate the appropriate Model, after getting the values of the required predicates;
#	2. construct the query 
#	3. to prove/disprove the query.
def generate_and_solve_query1(bats, bowl):
	
	# for this query, we only need to consider the columns in bats dictionary
	c1 = parse_for_sr(bats, 150.0)
	c2 = parse_for_six(bats, 0)
	#print c1
	#print c2
	#Now constructing strings which are needed to create the model:
	#first creating mapping from playername to variable: we create a temporary dictionary
	# For example,
	# MS Dhoni => r1
	# SK Raina => r2
	name_to_var = {}
	count = 0
	for i in bats:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	# Now for creating a Model, we need to write down a string which shows mapping from predicates to varible names
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'srate => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'gtsix => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	#print v
	# now forming the query
	query = 'all x (srate(x) -> gtsix(x))'
	make_model_and_answer(v, query, name_to_var)

def generate_and_solving_query1(mom,wonby,lists):
	c1=parse_for_mom(mom);
	#c2=parse_for_wonby(wonby);
	c2=[]
	profile1='./dataset/player_profile/indian_players_profile.txt'
	profile2='./dataset/player_profile/nz_players_profile.txt'
	people=[]
	add_to_list(people,profile1);
	add_to_list(people,profile2);
	if(wonby.keys()[0]=='India'):
		add_to_list(c2,profile1)
	elif(wonby.keys()[0]=='New Zealand'):
		add_to_list(c2,profile2)
	else:
		return False
	#name_to_var = {}
	#name_to_var['India']=1;
	#name_to_var['New Zealand']=2;
	#name_to_var['tie']=3;
	name_to_var = {}
	count = 0
	for i in people:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	temp_strin2 = 'mom => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	temp_strin3 = 'wonby => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (mom(x) & wonby(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((mom(x)) & (mom(x) & wonby(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
		m.evaluate(query, g);
		return m.evaluate(query, g);


	#now for the predicate "gtsix"
def generate_and_solving_query2(bat,wonby,lists):
	c1=parse_for_bat(bat,0)
	c2=wonby.keys()[0]
	losing=[]
	if(c2=='India'):
		losing.append('New Zealand')
		c2=[]
		c2.append('New Zealand')
	elif c2=='New Zealand':
		losing.append('India')
		c2=[]
		c2.append('India')
	else:
		return False
	if(losing[0]=='New Zealand'):
		prof='./dataset/player_profile/nz_players_profile.txt'
	elif(losing[0]=='India'):
		prof='./dataset/player_profile/indian_players_profile.txt'
	people=[]
	add_to_list(people,prof);
	duck_player=[]
	fl=0
	if c1:
		for i in people:
			for j in c1:
				if i==j:
					if i not in duck_player:
						duck_player.append(i)
						fl=1;
	win=[]
	if(fl==1):
		if(c2[0]=='India'):
			win.append('India')
		elif(c2[0]=='New Zealand'):
			win.append('New Zealand')
	else:
		return False
	name_to_var = {}
	name_to_var['India']='1';
	name_to_var['New Zealand']='2';
	name_to_var['Tie']='3';
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	temp_strin2 = 'lose => {'
	for i in losing:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	temp_strin3 = 'duck => {'
	for i in win:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (lose(x) -> duck(x))'
	if losing and win:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((lose(x)) & (lose(x) -> duck(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
	#	m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query3(bat,lists):
	c1=parse_for_strate(bat)
	c2=parse_for_sixmorefour(bat)
	name_to_var = {}
	count = 0
	for i in bat:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'srate => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'sixmorefour => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (srate(x) -> sixmorefour(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		print m
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((srate(x)) & (srate(x) -> sixmorefour(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
#		print 'ans',m
		return m.evaluate(query, g);
	else:
		return False

def generate_and_solving_query4(bat,wonby,lists):
	c1=parse_for_bat_boundary(bat)
	c2=wonby.keys()[0]
	losing=[]
	if(c2=='India'):
		losing.append('India')
		c2=[]
		c2.append('India')
	elif c2=='New Zealand':
		losing.append('New Zealand')
		c2=[]
		c2.append('New Zealand')
	else:
		return True
	if(losing[0]=='New Zealand'):
		prof='./dataset/player_profile/nz_players_profile.txt'
	elif(losing[0]=='India'):
		prof='./dataset/player_profile/indian_players_profile.txt'
	people=[]
	add_to_list(people,prof);
	duck_player=[]
	fl=0
	if c1:
		for i in people:
			for j in c1:
				if i==j:
					if i not in duck_player:
						duck_player.append(i)
						fl=1;
	win=[]
	if(fl==1):
		if(c2[0]=='India'):
			win.append('India')
		elif(c2[0]=='New Zealand'):
			win.append('New Zealand')
	else:
		return False
	name_to_var = {}
	name_to_var['India']='1';
	name_to_var['New Zealand']='2';
	name_to_var['Tie']='3';
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	temp_strin2 = 'win => {'
	for i in losing:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	temp_strin3 = 'boundary => {'
	for i in win:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (win(x) -> boundary(x))'
	if losing and win:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((win(x)) & (win(x) -> boundary(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
#		for i in varnames:
#			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
#				if q == i:
					#lists.append(p);
					
		lists.extend(duck_player)
	#	m.evaluate(query, g);
		return m.evaluate(query, g);


def generate_and_solving_query5(bat,bowl,lists):
	c1=parse_for_run(bat,50)
	c2=parse_for_wicket(bowl,1)
	profile1='./dataset/player_profile/indian_players_profile.txt'
	profile2='./dataset/player_profile/nz_players_profile.txt'
	people=[]
	add_to_list(people,profile1);
	add_to_list(people,profile2);
	name_to_var = {}
	count = 0
	for i in bat:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in bowl:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'bats => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'bowl => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exists x (bats(x) -> bowl(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((bats(x)) & (bats(x) -> bowl(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
		#m.evaluate(query, g);
		return m.evaluate(query, g);
def generate_and_solving_query6(bowl,lists):
	c1=parse_for_over(bowl,7)
	c2=parse_for_nowicket(bowl)
	profile1='./dataset/player_profile/indian_players_profile.txt'
	profile2='./dataset/player_profile/nz_players_profile.txt'
	people=[]
	add_to_list(people,profile1);
	add_to_list(people,profile2);
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'over => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'wicket => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (over(x) -> wicket(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((over(x)) & (over(x) -> wicket(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query7(bowl,lists):
	c1=parse_for_nowicket(bowl)
	c2=parse_for_economy(bowl,8.00)
	profile1='./dataset/player_profile/indian_players_profile.txt'
	profile2='./dataset/player_profile/nz_players_profile.txt'
	people=[]
	add_to_list(people,profile1);
	add_to_list(people,profile2);
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'nowicket => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'economy => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (nowicket(x) & economy(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((nowicket(x)) & (nowicket(x) & economy(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query8(bat,wonby,lists):
	c2=wonby.keys()[0]
	c1=parse_for_hund(bat)
	losing=[]
	if(c2=='India'):
		losing.append('New Zealand')
		c2=[]
		c2.append('New Zealand')
	elif c2=='New Zealand':
		losing.append('India')
	#	print losing
		c2=[]
		c2.append('India')
	else:
		return False
	if(losing[0]=='New Zealand'):
		prof='./dataset/player_profile/nz_players_profile.txt'
	elif(losing[0]=='India'):
		prof='./dataset/player_profile/indian_players_profile.txt'
	people=[]
	add_to_list(people,prof);
	duck_player=[]
	fl=0
	if c1:
		for i in people:
			for j in c1:
				if i==j:
					if i not in duck_player:
						duck_player.append(i)
						fl=1;
	win=[]
	if(fl==1):
		if(c2[0]=='India'):
			win.append('India')
		elif(c2[0]=='New Zealand'):
			win.append('New Zealand')
	else:
		return False
	name_to_var = {}
	name_to_var['India']='1';
	name_to_var['New Zealand']='2';
	name_to_var['Tie']='3';
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	temp_strin2 = 'hundred => {'
	for i in losing:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	temp_strin3 = 'lost => {'
	for i in win:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exists x (hundred(x) -> lost(x))'
	if losing and win:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((hundred(x)) & (hundred(x) -> lost(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		#for i in varnames:
			#for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
			#	if q == i:
			#		lists.append(p);
		lists.extend(duck_player)
	#	print '8',duck_player,lists
	#	m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query10(bat,lists):
	c1=parse_for_run_wo_ducks(bat)
	people={}
	prof='./dataset/player_profile/nz_players_profile.txt'
	add_to_dict3(people,prof);
	prof='./dataset/player_profile/indian_players_profile.txt'
	add_to_dict3(people,prof);
	c2=parse_for_age(people,26)
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'run => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'age => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (run(x) -> age(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((run(x)) & (run(x) & age(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query9(bowl,lists):
	people={}
	prof='./dataset/player_profile/nz_players_profile.txt'
	add_to_dict3(people,prof);
	prof='./dataset/player_profile/indian_players_profile.txt'
	add_to_dict3(people,prof);
	rhand=[]
	lhand=[]
	add_to_list2(rhand,lhand,people)
	right=0;
	left=0;
	temp=compute(rhand,lhand,bowl,right,left)
	right=temp[0]
	left=temp[1]
	#print right,left
	c1=[]
	c2=[]
	for i in bowl:
		if i in rhand and i not in c1:
			c1.append(i)
	if(right>left):
		c2=c1;
	else:
		for i in bowl:
			if i in lhand and i not in c2:
				c2.append(i)
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'right => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'left => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (right(x) & left(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((right(x)) & (right(x) & left(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);
	
def generate_and_solving_query11(bat1,bat2,lists):
	c1=[]
	c2=[]
	c1=parse_for_bat1(bat1)
	c2=parse_for_bat1(bat2)
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'bat1 => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'bat2 => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'exist x (bat1(x) & bat2(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((bat1(x)) & (bat1(x) & bat2(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query12(ishant_wides,jadeja_wides,lists):
	c1=[]
	c2=[]
	c1.append("I Sharma")
	if(ishant_wides>jadeja_wides):
		c2.append("I Sharma")
	else:
		c2.append("RA Jadeja")
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'sharma => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'jadeja => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (sharma(x) & jadeja(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((sharma(x)) & (sharma(x) & jadeja(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query13(southee_catches,ryder_catches,lists):
	c1=[]
	c2=[]
	c1.append("Southee")
	if(southee_catches>ryder_catches):
		c2.append("Southee")
	else:
		c2.append("Ryder")
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'southee => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'ryder => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (southee(x) & ryder(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((southee(x)) & (southee(x) & ryder(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query14(wonby,lists):
	c1=[]
	c2=[]
	fl=0
	for i in wonby:
		if wonby[i]>1:
			fl=1
			break
	
	c1.append(wonby.keys()[0])
	if(fl==1):
		c2.append(wonby.keys()[0])
	else:
		c2.append("lose")
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'win => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'lose => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (win(x) & lose(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((win(x)) & (win(x) & lose(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query19(wonby,toss,lists):
	c1=[]
	c2=[]
	c1=wonby.keys()[0]
	c2=toss.keys()[0]
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'wonby => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'toss => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (wonby(x) & toss(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((wonby(x)) & (wonby(x) & toss(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query15(temp1,temp2,lists):
	c1=[]
	c2=[]
	if(temp1>temp2):
		c1.append('1st Innings')
		c2.append('1st Innings')
	else:
		c1.append('2nd Innings')
		c2.append('2nd Innings')
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'inning1 => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'inning2 => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (inning1(x) & inning2(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((inning1(x)) & (inning1(x) & inning2(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
	#	lists.append(c1[0])
	#	print 'q15',lists
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query16(temp1,temp2,lists):
	c1=[]
	c2=[]
	if(temp1>temp2):
		c1.append('Hard-Batman')
		c2.append('Hard-Batman')
	else:
		c1.append('Not Hard-Batman')
		c2.append('Not Hard-Batman')
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'HB => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'NHB => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (HB(x) & NHB(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((HB(x)) & (HB(x) & NHB(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
	#	lists.append(c1[0])
	#	print 'q15',lists
#		m.evaluate(query, g);
		return m.evaluate(query, g);

def generate_and_solving_query17(temp1,temp2,lists):
	c1=[]
	c2=[]
	if(temp1>temp2):
		c1.append('I Sharma')
		c2.append('I Sharma')
	else:
		c1.append('RA Jadeja')
		c2.append('RA Jadeja')
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'sharma => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'jadeja => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (sharma(x) & jadeja(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((sharma(x)) & (sharma(x) & jadeja(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
	#	lists.append(c1[0])
	#	print 'q15',lists
#		m.evaluate(query, g);
		if(c2[0]=='I Sharma'):
			return True
		else:
			return False
		return m.evaluate(query, g);

def generate_and_solving_query18(temp1,temp2,lists):
	c1=[]
	c2=[]
	if(temp1>temp2):
		c1.append('Opening Batsmen')
		c2.append('Opening Batsmen')
	else:
		c1.append('Middle Order Batsmen')
		c2.append('Middle Order Batsmen')
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'OB => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'MB => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (OB(x) & MB(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((OB(x)) & (OB(x) & MB(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
	#	lists.append(c1[0])
	#	print 'q15',lists
#		m.evaluate(query, g);
		if(c2[0]=="Middle Order Batsmen"):
			return True
		else:
			return False
		return m.evaluate(query, g);

def generate_and_solving_query20(temp1,temp2,lists):
	c1=[]
	c2=[]
	if(temp1>temp2):
		c1.append('India')
		c2.append('India')
	else:
		c1.append('New Zealand')
		c2.append('New Zealand')
	name_to_var = {}
	count = 0
	for i in c1:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	for i in c2:
		if i not in name_to_var:
			name_to_var[i] = 'r' + str(count)
			count += 1
	temp_strin1 = ''
	for i in name_to_var:
		temp_strin1 += i + ' => ' + name_to_var[i] + '\n'
	# this is for the predicate "srate"
	temp_strin2 = 'in => {'
	for i in c1:
		temp_strin2 += name_to_var[i] +  ','
	temp_strin2 = temp_strin2[:-1]  #removing the extra "," character
	temp_strin2 += '} \n'
	#now for the predicate "gtsix"
	temp_strin3 = 'new => {'
	for i in c2:
		temp_strin3 += name_to_var[i] + ','
	temp_strin3 = temp_strin3[:-1]  #removing the extra "," charater
	temp_strin3 += '}'
	v = temp_strin1 + temp_strin2 + temp_strin3
	query = 'all x (in(x) & new(x))'
	if c1 and c2:
		val = nltk.parse_valuation(v)
		dom = val.domain
		m = nltk.Model(dom, val)
		g = nltk.Assignment(dom, [])
		l = nltk.LogicParser()
		c1 = l.parse(' ((in(x)) & (in(x) & new(x)))')
		varnames =  m.satisfiers(c1, 'x', g)
		for i in varnames:
			for p,q in name_to_var.iteritems():   # naive method to get key given value, in a dictionary
				if q == i:
					lists.append(p);
	#	lists.append(c1[0])
	#	print 'q15',lists
#		m.evaluate(query, g);
		lists=[]
		if(c2[0]=="New Zealand"):
			lists.append("New Zealand")
			return True
		else:
			lists.append("India")
			return False
		return m.evaluate(query, g);

def main():

	bats = {}
	bowl = {}
	#f1 = './dataset/match2/odi2_inn1_bat.txt'
	#f2 = './dataset/match2/odi2_inn2_bat.txt'
	#f3 = './dataset/match2/odi2_inn1_bowl.txt'
	#f4 = './dataset/match2/odi2_inn1_bowl.txt'
	#add_to_dict(bats, f1)
	#add_to_dict(bats, f2)

	#add_to_dict(bowl, f3)
	#add_to_dict(bowl, f4)
	#generate_and_solve_query1(bats, bowl)


	#query1
	mom1='./dataset/match1/mom.txt'
	mom2='./dataset/match2/mom.txt'
	mom3='./dataset/match3/mom.txt'
	mom4='./dataset/match4/mom.txt'
	mom5='./dataset/match5/mom.txt'

	wonby1='./dataset/match1/wonby.txt'
	wonby2='./dataset/match2/wonby.txt'
	wonby3='./dataset/match3/wonby.txt'
	wonby4='./dataset/match4/wonby.txt'
	wonby5='./dataset/match5/wonby.txt'
	mom10={};
	mom20={};
	mom30={};
	mom40={};
	mom50={};
	add_to_dict(mom10,mom1);
	add_to_dict(mom20,mom2);
	add_to_dict(mom30,mom3);
	add_to_dict(mom40,mom4);
	add_to_dict(mom50,mom5);

	wonby10={};
	wonby20={};
	wonby30={};
	wonby40={};
	wonby50={};
	add_to_dict(wonby10,wonby1);
	add_to_dict(wonby20,wonby2);
	add_to_dict(wonby30,wonby3);
	add_to_dict(wonby40,wonby4);
	add_to_dict(wonby50,wonby5);
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	temp=[]
	temp.append(generate_and_solving_query1(mom10,wonby10,lists10));
	temp.append(generate_and_solving_query1(mom20,wonby20,lists20));
	temp.append(generate_and_solving_query1(mom30,wonby30,lists30));
	temp.append(generate_and_solving_query1(mom40,wonby40,lists40));
	temp.append(generate_and_solving_query1(mom50,wonby50,lists50));
	flag=0;
	print 
	print "Query 1"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print list10
		#print list20
		#print list30
		#print list40
		#print list50

	#query2
	odi1_inn1_bat='./dataset/match1/odi1_inn1_bat.txt'
	odi1_inn2_bat='./dataset/match1/odi1_inn2_bat.txt'
	odi2_inn1_bat='./dataset/match2/odi2_inn1_bat.txt'
	odi2_inn2_bat='./dataset/match2/odi2_inn2_bat.txt'
	odi3_inn1_bat='./dataset/match3/odi3_inn1_bat.txt'
	odi3_inn2_bat='./dataset/match3/odi3_inn2_bat.txt'
	odi4_inn1_bat='./dataset/match4/odi4_inn1_bat.txt'
	odi4_inn2_bat='./dataset/match4/odi4_inn2_bat.txt'
	odi5_inn1_bat='./dataset/match5/odi5_inn1_bat.txt'
	odi5_inn2_bat='./dataset/match5/odi5_inn2_bat.txt'
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	temp.append(generate_and_solving_query2(bat10,wonby10,lists10));
	temp.append(generate_and_solving_query2(bat20,wonby20,lists20));
	temp.append(generate_and_solving_query2(bat30,wonby30,lists30));
	temp.append(generate_and_solving_query2(bat40,wonby40,lists40));
	temp.append(generate_and_solving_query2(bat50,wonby50,lists50));
	flag=0;
	print 
	print "Query 2"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print list10
		#print list20
		#print list30
		#print list40
		#print list50

	##query3
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	bat11={}
	bat21={}
	bat31={}
	bat41={}
	bat51={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	lists11=[];
	lists21=[];
	lists31=[];
	lists41=[];
	lists51=[];
	temp.append(generate_and_solving_query3(bat10,lists10));
	temp.append(generate_and_solving_query3(bat20,lists20));
	temp.append(generate_and_solving_query3(bat30,lists30));
	temp.append(generate_and_solving_query3(bat40,lists40));
	temp.append(generate_and_solving_query3(bat50,lists50));
#	temp.append(generate_and_solving_query3(bat11,lists10));
#	temp.append(generate_and_solving_query3(bat21,lists20));
#	temp.append(generate_and_solving_query3(bat31,lists30));
#	temp.append(generate_and_solving_query3(bat41,lists40));
#	temp.append(generate_and_solving_query3(bat51,lists50));
	flag=0;
	print 
	print "Query 3"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print lists10
		#print lists20
		#print lists30
		#print lists40
		#print lists50
#		print list11
#		print list21
#		print list31
#		print list41
#		print list51

	#generate_and_solving_query2(wonby,)
	#query4
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	wonby10={};
	wonby20={};
	wonby30={};
	wonby40={};
	wonby50={};
	add_to_dict(wonby10,wonby1);
	add_to_dict(wonby20,wonby2);
	add_to_dict(wonby30,wonby3);
	add_to_dict(wonby40,wonby4);
	add_to_dict(wonby50,wonby5);
	temp.append(generate_and_solving_query4(bat10,wonby10,lists10));
	temp.append(generate_and_solving_query4(bat20,wonby20,lists20));
	temp.append(generate_and_solving_query4(bat30,wonby30,lists30));
	temp.append(generate_and_solving_query4(bat40,wonby40,lists40));
	temp.append(generate_and_solving_query4(bat50,wonby50,lists50));
	flag=0;
#	print 'new',temp
	print 
	print "Query 4"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print lists10
		#print lists20
		#print lists30
		#print lists40
		#print lists50
	
	#query5
	odi1_inn1_bowl='./dataset/match1/odi1_inn1_bowl.txt'
	odi1_inn2_bowl='./dataset/match1/odi1_inn2_bowl.txt'
	odi2_inn1_bowl='./dataset/match2/odi2_inn1_bowl.txt'
	odi2_inn2_bowl='./dataset/match2/odi2_inn2_bowl.txt'
	odi3_inn1_bowl='./dataset/match3/odi3_inn1_bowl.txt'
	odi3_inn2_bowl='./dataset/match3/odi3_inn2_bowl.txt'
	odi4_inn1_bowl='./dataset/match4/odi4_inn1_bowl.txt'
	odi4_inn2_bowl='./dataset/match4/odi4_inn2_bowl.txt'
	odi5_inn1_bowl='./dataset/match5/odi5_inn1_bowl.txt'
	odi5_inn2_bowl='./dataset/match5/odi5_inn2_bowl.txt'
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	bowl10={}
	bowl20={}
	bowl30={}
	bowl40={}
	bowl50={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl10,odi1_inn2_bowl)
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl20,odi2_inn2_bowl)
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl30,odi3_inn2_bowl)
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl40,odi4_inn2_bowl)
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl50,odi5_inn2_bowl)
	
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	
	temp.append(generate_and_solving_query5(bat10,bowl10,lists10));
	temp.append(generate_and_solving_query5(bat20,bowl20,lists20));
	temp.append(generate_and_solving_query5(bat30,bowl30,lists30));
	temp.append(generate_and_solving_query5(bat40,bowl40,lists40));
	temp.append(generate_and_solving_query5(bat50,bowl50,lists50));
	flag=0;
	print 
	print "Query 5"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print lists10
		#print lists20
		#print lists30
		#print lists40
		#print lists50
	
	#query6
	bowl10={}
	bowl20={}
	bowl30={}
	bowl40={}
	bowl50={}
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl10,odi1_inn2_bowl)
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl20,odi2_inn2_bowl)
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl30,odi3_inn2_bowl)
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl40,odi4_inn2_bowl)
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl50,odi5_inn2_bowl)
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	
	temp.append(generate_and_solving_query6(bowl10,lists10));
	temp.append(generate_and_solving_query6(bowl20,lists20));
	temp.append(generate_and_solving_query6(bowl30,lists30));
	temp.append(generate_and_solving_query6(bowl40,lists40));
	temp.append(generate_and_solving_query6(bowl50,lists50));
	flag=0;
#	print 'new',temp
	print 
	print "Query 6"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print lists10
		#print lists20
		#print lists30
		#print lists40
		#print lists50
	
	#query7
	bowl10={}
	bowl20={}
	bowl30={}
	bowl40={}
	bowl50={}
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl10,odi1_inn2_bowl)
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl20,odi2_inn2_bowl)
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl30,odi3_inn2_bowl)
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl40,odi4_inn2_bowl)
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl50,odi5_inn2_bowl)
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	
	temp.append(generate_and_solving_query7(bowl10,lists10));
	temp.append(generate_and_solving_query7(bowl20,lists20));
	temp.append(generate_and_solving_query7(bowl30,lists30));
	temp.append(generate_and_solving_query7(bowl40,lists40));
	temp.append(generate_and_solving_query7(bowl50,lists50));
	flag=0;
#	print 'new',temp
	print 
	print "Query 7"
	for i in temp:
		if(i==True):
			flag=1;

	if(flag==0):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print lists10
		#print lists20
		#print lists30
		#print lists40
		#print lists50
	
	#query8
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	wonby10={};
	wonby20={};
	wonby30={};
	wonby40={};
	wonby50={};
	add_to_dict(wonby10,wonby1);
	add_to_dict(wonby20,wonby2);
	add_to_dict(wonby30,wonby3);
	add_to_dict(wonby40,wonby4);
	add_to_dict(wonby50,wonby5);
	temp.append(generate_and_solving_query8(bat10,wonby10,lists10));
	temp.append(generate_and_solving_query8(bat20,wonby20,lists20));
	temp.append(generate_and_solving_query8(bat30,wonby30,lists30));
	temp.append(generate_and_solving_query8(bat40,wonby40,lists40));
	temp.append(generate_and_solving_query8(bat50,wonby50,lists50));
	flag=0;
#	print 'new',temp
	print 
	print "Query 8"
	for i in temp:
		if(i==True):
			flag=1;

	if(flag==0):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
		#print lists10
		#print lists20
		#print lists30
		#print lists40
		#print lists50

	#query9
	bowl10={}
	bowl20={}
	bowl30={}
	bowl40={}
	bowl50={}
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl10,odi1_inn2_bowl)
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl20,odi2_inn2_bowl)
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl30,odi3_inn2_bowl)
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl40,odi4_inn2_bowl)
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl50,odi5_inn2_bowl)
	temp=[]
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	
	temp.append(generate_and_solving_query9(bowl10,lists10));
	temp.append(generate_and_solving_query9(bowl20,lists20));
	temp.append(generate_and_solving_query9(bowl30,lists30));
	temp.append(generate_and_solving_query9(bowl40,lists40));
	temp.append(generate_and_solving_query9(bowl50,lists50));
	flag=0;
#	print 'new',temp
	print 
	print "Query 9"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		#flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		#print flist
		print lists10
		print lists20
		print lists30
		print lists40
		print lists50

		

	#query10
	bat10={}
	add_to_dict2(bat10,odi1_inn1_bat);
	add_to_dict2(bat10,odi1_inn2_bat);
	add_to_dict2(bat10,odi2_inn1_bat);
	add_to_dict2(bat10,odi2_inn2_bat);
	add_to_dict2(bat10,odi3_inn1_bat);
	add_to_dict2(bat10,odi3_inn2_bat);
	add_to_dict2(bat10,odi4_inn1_bat);
	add_to_dict2(bat10,odi4_inn2_bat);
	add_to_dict2(bat10,odi5_inn1_bat);
	add_to_dict2(bat10,odi5_inn2_bat);
	temp=[]
	lists10=[];
#	lists20=[];
#	lists30=[];
#	lists40=[];
#	lists50=[];
	temp.append(generate_and_solving_query10(bat10,lists10));
#	temp.append(generate_and_solving_query8(bat20,wonby20,lists20));
#	temp.append(generate_and_solving_query8(bat30,wonby30,lists30));
#	temp.append(generate_and_solving_query8(bat40,wonby40,lists40));
#	temp.append(generate_and_solving_query8(bat50,wonby50,lists50));
	flag=0;
#	print 'new',temp
	print 
	print "Query 10"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		print lists10
#		print lists20
#		print lists30
#		print lists40
#		print lists50

	
	#query11
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	add_to_dict(bat10,odi1_inn1_bowl);
	add_to_dict(bat10,odi1_inn2_bowl)
	add_to_dict(bat20,odi2_inn1_bowl);
	add_to_dict(bat20,odi2_inn2_bowl)
	add_to_dict(bat30,odi3_inn1_bowl);
	add_to_dict(bat30,odi3_inn2_bowl)
	add_to_dict(bat40,odi4_inn1_bowl);
	add_to_dict(bat40,odi4_inn2_bowl)
	add_to_dict(bat50,odi5_inn1_bowl);
	add_to_dict(bat50,odi5_inn2_bowl)
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	generate_and_solving_query11(bat10,bat20,lists10)
	generate_and_solving_query11(lists10,bat30,lists20)
	generate_and_solving_query11(lists20,bat40,lists30)
	generate_and_solving_query11(lists30,bat50,lists40)
	print 
	print "Query 11"
	print "Player who played all the matches in the series"
	print lists40

	#query12
	bowl10={}
	bowl20={}
	bowl30={}
	bowl40={}
	bowl50={}
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl10,odi1_inn2_bowl)
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl20,odi2_inn2_bowl)
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl30,odi3_inn2_bowl)
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl40,odi4_inn2_bowl)
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl50,odi5_inn2_bowl)
	temp=0
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	ishant_wides=0
	ishant_wides+=check_wides(bowl10,"I Sharma")
	ishant_wides+=check_wides(bowl20,"I Sharma")
	ishant_wides+=check_wides(bowl30,"I Sharma")
	ishant_wides+=check_wides(bowl40,"I Sharma")
	ishant_wides+=check_wides(bowl50,"I Sharma")


	jadeja_wides=0
	jadeja_wides+=check_wides(bowl10,"RA Jadeja")
	jadeja_wides+=check_wides(bowl20,"RA Jadeja")
	jadeja_wides+=check_wides(bowl30,"RA Jadeja")
	jadeja_wides+=check_wides(bowl40,"RA Jadeja")
	jadeja_wides+=check_wides(bowl50,"RA Jadeja")
	
	temp=generate_and_solving_query12(ishant_wides,jadeja_wides,lists10)
	print 
	print "Query 12"
	print "Did Ishant sharma bowl more wides than Sir Jadeja :"
	if(temp==True):
		print "True"
	else:
		print "False"

	#query13
	bowl10={}
	bowl20={}
	bowl30={}
	bowl40={}
	bowl50={}
	add_to_dict(bowl10,odi1_inn1_bat);
	add_to_dict(bowl10,odi1_inn2_bat)
	add_to_dict(bowl20,odi2_inn1_bat);
	add_to_dict(bowl20,odi2_inn2_bat)
	add_to_dict(bowl30,odi3_inn1_bat);
	add_to_dict(bowl30,odi3_inn2_bat)
	add_to_dict(bowl40,odi4_inn1_bat);
	add_to_dict(bowl40,odi4_inn2_bat)
	add_to_dict(bowl50,odi5_inn1_bat);
	add_to_dict(bowl50,odi5_inn2_bat)
	temp=0
	lists10=[];
	lists20=[];
	lists30=[];
	lists40=[];
	lists50=[];
	southee_catches=0
	ryder_catches=0;
	southee_catches+=check_catches(bowl10,"Southee")
	southee_catches+=check_catches(bowl20,"Southee")
	southee_catches+=check_catches(bowl30,"Southee")
	southee_catches+=check_catches(bowl40,"Southee")
	southee_catches+=check_catches(bowl50,"Southee")

	ryder_catches+=check_catches(bowl10,"Ryder")
	ryder_catches+=check_catches(bowl10,"Ryder")
	ryder_catches+=check_catches(bowl10,"Ryder")
	ryder_catches+=check_catches(bowl10,"Ryder")
	ryder_catches+=check_catches(bowl10,"Ryder")
	
	temp=generate_and_solving_query13(southee_catches,ryder_catches,lists10)
	print 
	print "Query 13"
	print "Did Southee take more catches than Ryder :"
	if(temp==True):
		print "True"
	else:
		print "False"

	#query14
	wonby10={};
	wonby20={};
	wonby30={};
	wonby40={};
	wonby50={};
	add_to_dict(wonby10,mom1);
	add_to_dict(wonby20,mom2);
	add_to_dict(wonby30,mom3);
	add_to_dict(wonby40,mom4);
	add_to_dict(wonby50,mom5);
	wonby_1={}
	check(wonby10,wonby_1)
	check(wonby20,wonby_1)
	check(wonby30,wonby_1)
	check(wonby40,wonby_1)
	check(wonby50,wonby_1)
	temp=generate_and_solving_query14(wonby_1,lists10)
	print 
	print "Is there a player who has been awarded player of the match twice :"
	print "Query 14"
	if(temp==True):
		print "True"
	else:
		print "False"

	#query15
	bowl10={}
	bowl11={}
	bowl20={}
	bowl21={}
	bowl30={}
	bowl31={}
	bowl40={}
	bowl41={}
	bowl50={}
	bowl51={}
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl11,odi1_inn2_bowl);
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl21,odi2_inn2_bowl);
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl31,odi3_inn2_bowl);
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl41,odi4_inn2_bowl);
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl51,odi5_inn2_bowl);
	temp1=[]
	temp2=[]
	heuristic_15(bowl10,temp1);
	heuristic_15(bowl11,temp2);
	heuristic_15(bowl20,temp1);
	heuristic_15(bowl21,temp2);
	heuristic_15(bowl30,temp1);
	heuristic_15(bowl31,temp2);
	heuristic_15(bowl40,temp1);
	heuristic_15(bowl41,temp2);
	heuristic_15(bowl50,temp1);
	heuristic_15(bowl51,temp2);
	temp1=float((sum(temp1)*1.0)/len(temp1))
	temp2=float((sum(temp2)*1.0)/len(temp2))
	lists10=[]
	temp=[]
	temp.append(generate_and_solving_query15(temp1,temp2,lists10))
	print
	print "Query 15"
	print "Did Sir Jadeja bowl better in innings1 or innings 2 :"
	print lists10

	#query16
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	temp1=[]
	heuristic_16(bat10,temp1);
	heuristic_16(bat20,temp1);
	heuristic_16(bat30,temp1);
	heuristic_16(bat40,temp1);
	heuristic_16(bat50,temp1);
	temp1=float((sum(temp1)*1.0)/len(temp1))
	lists10=[]
	temp=[]
	temp2=490;
	temp.append(generate_and_solving_query16(temp1,temp2,lists10))
	print
	print "Is Dhoni a hard hitting batsman :"
	print "Query 16"
	print temp

	#query17
	bowl10={}
	bowl11={}
	bowl20={}
	bowl21={}
	bowl30={}
	bowl31={}
	bowl40={}
	bowl41={}
	bowl50={}
	bowl51={}
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl11,odi1_inn2_bowl);
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl21,odi2_inn2_bowl);
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl31,odi3_inn2_bowl);
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl41,odi4_inn2_bowl);
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl51,odi5_inn2_bowl);
	temp1=[]
	temp2=[]
	heuristic_17(bowl10,temp1,"I Sharma");
	heuristic_17(bowl11,temp1,"I Sharma");
	heuristic_17(bowl20,temp1,"I Sharma");
	heuristic_17(bowl21,temp1,"I Sharma");
	heuristic_17(bowl30,temp1,"I Sharma");
	heuristic_17(bowl31,temp1,"I Sharma");
	heuristic_17(bowl40,temp1,"I Sharma");
	heuristic_17(bowl41,temp1,"I Sharma");
	heuristic_17(bowl50,temp1,"I Sharma");
	heuristic_17(bowl51,temp1,"I Sharma");

	heuristic_17(bowl10,temp2,"RA Jadeja");
	heuristic_17(bowl11,temp2,"RA Jadeja");
	heuristic_17(bowl20,temp2,"RA Jadeja");
	heuristic_17(bowl21,temp2,"RA Jadeja");
	heuristic_17(bowl30,temp2,"RA Jadeja");
	heuristic_17(bowl31,temp2,"RA Jadeja");
	heuristic_17(bowl40,temp2,"RA Jadeja");
	heuristic_17(bowl41,temp2,"RA Jadeja");
	heuristic_17(bowl50,temp2,"RA Jadeja");
	heuristic_17(bowl51,temp2,"RA Jadeja");
	
#	print temp1
#	print temp2
	temp1=float((sum(temp1)*1.0)/len(temp1))
	temp2=float((sum(temp2)*1.0)/len(temp2))
#	print temp1,temp2
	lists10=[]
	temp=[]
	temp.append(generate_and_solving_query17(temp1,temp2,lists10))
	print 
	print "Query 17"
	print "Is  Ishant  sharma  a  better  bowler  than  Sir  Jadeja :"
	print temp

	#query 18
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	bat11={}
	bat21={}
	bat31={}
	bat41={}
	bat51={}
	temp1=[]

	fast_read(temp1,odi1_inn1_bat);
	fast_read(temp1,odi1_inn2_bat);
	fast_read(temp1,odi2_inn1_bat);
	fast_read(temp1,odi2_inn2_bat);
	fast_read(temp1,odi3_inn1_bat);
	fast_read(temp1,odi3_inn2_bat);
	fast_read(temp1,odi4_inn1_bat);
	fast_read(temp1,odi4_inn2_bat);
	fast_read(temp1,odi5_inn1_bat);
	fast_read(temp1,odi5_inn2_bat);

	temp2=[]
	fast_read2(temp2,odi1_inn1_bat);
	fast_read2(temp2,odi1_inn2_bat);
	fast_read2(temp2,odi2_inn1_bat);
	fast_read2(temp2,odi2_inn2_bat);
	fast_read2(temp2,odi3_inn1_bat);
	fast_read2(temp2,odi3_inn2_bat);
	fast_read2(temp2,odi4_inn1_bat);
	fast_read2(temp2,odi4_inn2_bat);
	fast_read2(temp2,odi5_inn1_bat);
	fast_read2(temp2,odi5_inn2_bat);

	temp1=float((sum(temp1)*1.0)/len(temp1))
	temp2=float((sum(temp2)*1.0)/len(temp2))
	lists10=[]
	temp=[]
	temp.append(generate_and_solving_query18(temp1,temp2,lists10))
	print
	print "Query 18"
	print "Do  the  middle  order  batsmen  perform  better  than  the  opening  batsmen :"
	print temp

		
	#query19
	toss1='./dataset/match1/toss'
	toss2='./dataset/match2/toss'
	toss3='./dataset/match3/toss'
	toss4='./dataset/match4/toss'
	toss5='./dataset/match5/toss'
	wonby10={};
	wonby20={};
	wonby30={};
	wonby40={};
	wonby50={};
	add_to_dict(wonby10,wonby1);
	add_to_dict(wonby20,wonby2);
	add_to_dict(wonby30,wonby3);
	add_to_dict(wonby40,wonby4);
	add_to_dict(wonby50,wonby5);
	toss10={};
	toss20={};
	toss30={};
	toss40={};
	toss50={};
	add_to_dict(toss10,toss1);
	add_to_dict(toss20,toss2);
	add_to_dict(toss30,toss3);
	add_to_dict(toss40,toss4);
	add_to_dict(toss50,toss5);
	list10=[]
	list20=[]
	list30=[]
	list40=[]
	list50=[]
	temp=[]
	temp.append(generate_and_solving_query19(wonby10,toss10,lists10))
	temp.append(generate_and_solving_query19(wonby20,toss20,lists20))
	temp.append(generate_and_solving_query19(wonby30,toss30,lists30))
	temp.append(generate_and_solving_query19(wonby40,toss40,lists40))
	temp.append(generate_and_solving_query19(wonby50,toss50,lists50))

	print 
	print "Query 19"
	print "Do the teams that win matches win tosses too :"
	for i in temp:
		if(i==False):
			flag=1;

	if(flag==1):
		print 'False'
	else:
		print 'True'
		flist=[]
		flist=remove_reduncy(lists10,lists20,lists30,lists40,lists50)
		print flist
	#	print lists10
	#	print lists20
	#	print lists30
	#	print lists40
	#	print lists50
	
	
	#query20  finallly
	bat10={}
	bat20={}
	bat30={}
	bat40={}
	bat50={}
	bowl10={}
	bowl20={}
	bowl30={}
	bowl40={}
	bowl50={}
	add_to_dict(bat10,odi1_inn1_bat);
	add_to_dict(bat10,odi1_inn2_bat);
	add_to_dict(bat20,odi2_inn1_bat);
	add_to_dict(bat20,odi2_inn2_bat);
	add_to_dict(bat30,odi3_inn1_bat);
	add_to_dict(bat30,odi3_inn2_bat);
	add_to_dict(bat40,odi4_inn1_bat);
	add_to_dict(bat40,odi4_inn2_bat);
	add_to_dict(bat50,odi5_inn1_bat);
	add_to_dict(bat50,odi5_inn2_bat);
	
	add_to_dict(bowl10,odi1_inn1_bowl);
	add_to_dict(bowl10,odi1_inn2_bowl)
	add_to_dict(bowl20,odi2_inn1_bowl);
	add_to_dict(bowl20,odi2_inn2_bowl)
	add_to_dict(bowl30,odi3_inn1_bowl);
	add_to_dict(bowl30,odi3_inn2_bowl)
	add_to_dict(bowl40,odi4_inn1_bowl);
	add_to_dict(bowl40,odi4_inn2_bowl)
	add_to_dict(bowl50,odi5_inn1_bowl);
	add_to_dict(bowl50,odi5_inn2_bowl)
	
	wonby10={};
	wonby20={};
	wonby30={};
	wonby40={};
	wonby50={};
	add_to_dict(wonby10,wonby1);
	add_to_dict(wonby20,wonby2);
	add_to_dict(wonby30,wonby3);
	add_to_dict(wonby40,wonby4);
	add_to_dict(wonby50,wonby5);
	
	temp=[]
	profile1='./dataset/player_profile/indian_players_profile.txt'
	profile2='./dataset/player_profile/nz_players_profile.txt'
	profile_ind=[]
	profile_new=[]
	addlist(profile1,profile_ind);
	addlist(profile2,profile_new);
	
	listsN_bat=[];
	listsN_bowl=[];
	listsI_bat=[];
	listsI_bowl=[];
	avg_in_bat=[]
	avg_in_bowl=[]
	avg_new_bat=[]
	avg_new_bowl=[]
	loop1(bat10,listsI_bat,listsN_bat,profile_ind,profile_new)
	if(wonby10.keys()[0]=="India"):
		for i in xrange(len(listsI_bat)):
			listsI_bat[i]*=2;
	if(wonby10.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bat)):
			listsN_bat[i]*=2;
	avg_in_bat.append(float((sum(listsI_bat)*1.0)/len(listsI_bat)))
	avg_new_bat.append(float((sum(listsN_bat)*1.0)/len(listsN_bat)))
	listsN_bat=[];
	listsI_bat=[];

	loop1(bat20,listsI_bat,listsN_bat,profile_ind,profile_new)
	if(wonby20.keys()[0]=="India"):
		for i in xrange(len(listsI_bat)):
			listsI_bat[i]*=2;
	if(wonby20.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bat)):
			listsN_bat[i]*=2;
	avg_in_bat.append(float((sum(listsI_bat)*1.0)/len(listsI_bat)))
	avg_new_bat.append(float((sum(listsN_bat)*1.0)/len(listsN_bat)))
	listsN_bat=[];
	listsI_bat=[];
	
	loop1(bat30,listsI_bat,listsN_bat,profile_ind,profile_new)
	if(wonby30.keys()[0]=="India"):
		for i in xrange(len(listsI_bat)):
			listsI_bat[i]*=2;
	if(wonby30.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bat)):
			listsN_bat[i]*=2;
	avg_in_bat.append(float((sum(listsI_bat)*1.0)/len(listsI_bat)))
	avg_new_bat.append(float((sum(listsN_bat)*1.0)/len(listsN_bat)))
	listsN_bat=[];
	listsI_bat=[];
	
	loop1(bat40,listsI_bat,listsN_bat,profile_ind,profile_new)
	if(wonby40.keys()[0]=="India"):
		for i in xrange(len(listsI_bat)):
			listsI_bat[i]*=2;
	if(wonby40.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bat)):
			listsN_bat[i]*=2;
	avg_in_bat.append(float((sum(listsI_bat)*1.0)/len(listsI_bat)))
	avg_new_bat.append(float((sum(listsN_bat)*1.0)/len(listsN_bat)))
	listsN_bat=[];
	listsI_bat=[];
	
	loop1(bat50,listsI_bat,listsN_bat,profile_ind,profile_new)
	if(wonby50.keys()[0]=="India"):
		for i in xrange(len(listsI_bat)):
			listsI_bat[i]*=2;
	if(wonby50.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bat)):
			listsN_bat[i]*=2;
	avg_in_bat.append(float((sum(listsI_bat)*1.0)/len(listsI_bat)))
	avg_new_bat.append(float((sum(listsN_bat)*1.0)/len(listsN_bat)))
	listsN_bat=[];
	listsI_bat=[];

	loop2(bowl10,listsI_bowl,listsN_bowl,profile_ind,profile_new)
	if(wonby10.keys()[0]=="India"):
		for i in xrange(len(listsI_bowl)):
			listsI_bowl[i]*=2;
	if(wonby10.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bowl)):
			listsN_bowl[i]*=2;
	avg_in_bowl.append(float((sum(listsI_bowl)*1.0)/len(listsI_bowl)))
	avg_new_bowl.append(float((sum(listsN_bowl)*1.0)/len(listsN_bowl)))
	listsN_bowl=[];
	listsI_bowl=[];
	
	loop2(bowl20,listsI_bowl,listsN_bowl,profile_ind,profile_new)
	if(wonby20.keys()[0]=="India"):
		for i in xrange(len(listsI_bowl)):
			listsI_bowl[i]*=2;
	if(wonby20.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bowl)):
			listsN_bowl[i]*=2;
	avg_in_bowl.append(float((sum(listsI_bowl)*1.0)/len(listsI_bowl)))
	avg_new_bowl.append(float((sum(listsN_bowl)*1.0)/len(listsN_bowl)))
	listsN_bowl=[];
	listsI_bowl=[];
	
	loop2(bowl30,listsI_bowl,listsN_bowl,profile_ind,profile_new)
	if(wonby30.keys()[0]=="India"):
		for i in xrange(len(listsI_bowl)):
			listsI_bowl[i]*=2;
	if(wonby30.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bowl)):
			listsN_bowl[i]*=2;
	avg_in_bowl.append(float((sum(listsI_bowl)*1.0)/len(listsI_bowl)))
	avg_new_bowl.append(float((sum(listsN_bowl)*1.0)/len(listsN_bowl)))
	listsN_bowl=[];
	listsI_bowl=[];
	
	loop2(bowl40,listsI_bowl,listsN_bowl,profile_ind,profile_new)
	if(wonby40.keys()[0]=="India"):
		for i in xrange(len(listsI_bowl)):
			listsI_bowl[i]*=2;
	if(wonby40.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bowl)):
			listsN_bowl[i]*=2;
	avg_in_bowl.append(float((sum(listsI_bowl)*1.0)/len(listsI_bowl)))
	avg_new_bowl.append(float((sum(listsN_bowl)*1.0)/len(listsN_bowl)))
	listsN_bowl=[];
	listsI_bowl=[];
	
	loop2(bowl50,listsI_bowl,listsN_bowl,profile_ind,profile_new)
	if(wonby50.keys()[0]=="India"):
		for i in xrange(len(listsI_bowl)):
			listsI_bowl[i]*=2;
	if(wonby50.keys()[0]=="New Zealand"):
		for i in xrange(len(listsN_bowl)):
			listsN_bowl[i]*=2;
	avg_in_bowl.append(float((sum(listsI_bowl)*1.0)/len(listsI_bowl)))
	avg_new_bowl.append(float((sum(listsN_bowl)*1.0)/len(listsN_bowl)))
	listsN_bowl=[];
	listsI_bowl=[];

	avg_in_bat=float((sum(avg_in_bat)*1.0)/len(avg_in_bat))
	avg_new_bat=float((sum(avg_new_bat)*1.0)/len(avg_new_bat))
	avg_in_bowl=float((sum(avg_in_bowl)*1.0)/len(avg_in_bowl))
	avg_new_bowl=float((sum(avg_new_bowl)*1.0)/len(avg_new_bowl))

	temp1=avg_in_bat+100*avg_in_bowl;
	temp2=avg_new_bat+100*avg_new_bowl;
	lists10=[]
	temp=[]
	temp.append(generate_and_solving_query20(temp1,temp2,lists10))
	print
	print "Query 20"
	print "Outcome of Next Match can be :" ,lists10


if __name__ == "__main__":
	main()
