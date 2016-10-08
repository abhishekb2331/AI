from nltk.chunk import *
from nltk.chunk.util import *
from nltk.chunk.regexp import *
from nltk import word_tokenize
from nltk import pos_tag
import re

## teaking inputs ##
text=raw_input()
## tokenising ##
tokens = nltk.pos_tag(word_tokenize(text))
chunk = ChunkRule("<.*>+", "Chunk all the text")
chink = ChinkRule("<VBD|IN|\.>", "Leave verbs and prepositions out of this")
split = SplitRule("<DT><NN>", "<DT><NN>","Chunk on sequences of determiner+noun phrases")
chunker = RegexpChunkParser([chunk, chink, split],chunk_node='NP')
chunked = chunker.parse(tokens)
NPs = list(chunked.subtrees(filter=lambda x: x.node=='NP'))
#print tokens
verb= [s for s in tokens if s[1] == 'VBD']
a=[]
for i in NPs:
	a.append([word for word,tag in i.leaves()])
match=''
for i in a[0]:
  match+=i
l=match.split(",")
match_name=re.sub('match','',l[0])
player_name=l[1]
description=''
over=''
quest=''
#print a
for j in a[1]:
 description+=j
if len(a)==4:
  for j in a[2]:
   over+=j
  t=re.findall(r'\d+',over)
  over=''
  for j in t:
    over+=j
  for j in a[3]:
    quest+=j
 # print match_name,player_name
  print description
  #print over,quest
else:
  for j in a[2]:
    quest+=j
  #print match_name,player_name
  #print description
  #print quest
mj=text.split(" ")
#print mj
for i in mj:
  if "?" in i:
    quest=i[:-1]
#print quest
g=[]
flag=0
if "max" in description:
  flag=1
no_over=re.findall(r'\d+',description)
if no_over:
  flag=2
if "first" in match_name:
  ans=[]
  ct=0
  arct1=[]
  bina=[]
  fa=open('mydataset/odi1_commentary_inn1.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct1.append(ct)
		ct=ct+1
  finalans=[]
  counter=0
  finalarct=[]
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,0))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  ct=0
  arct2=[] 
  ans=[]
  fa=open('mydataset/odi1_commentary_inn2.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in  description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct2.append(ct)
		ct=ct+1
  counter=0
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,1))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  actualans=[]
  maxer=0
  arct=[]
  #print quest
  if "over" in quest:
    if flag==1:
      ctr=0
      prev=0
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi1_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi1_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr>=maxer:
          maxer=ctr
          actualans.append(ti)
        prev=ti
      print actualans[-1]
    elif flag==2:
      ctr=0
      prev=-1
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi1_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi1_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr==int(no_over[0])-1:
          maxer=ctr
          actualans.append(ti)
	  print ti
        prev=ti
      if len(actualans)>0:
	pass
      else:
	print "None"

    else:
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi1_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi1_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
	print ti
        actualans.append(ti)
  if "bowl" in quest:
    for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
  if "ball" in quest:
    if over!="":
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi1_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi1_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
	if ti[:2]==over:
          ti=ti[3:]
	  print ti
          actualans.append(ti)
    else:
       for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi1_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi1_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[3:]
	print ti
        actualans.append(ti)
	
  if "whom" in quest:
     for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
#  print finalans,quest
if "second" in match_name:
  ans=[]
  ct=0
  arct1=[]
  bina=[]
  fa=open('mydataset/odi2_commentary_inn1.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct1.append(ct)
		ct=ct+1
  finalans=[]
  counter=0
  finalarct=[]
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,0))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  ct=0
  arct2=[] 
  ans=[]
  fa=open('mydataset/odi2_commentary_inn2.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in  description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct2.append(ct)
		ct=ct+1
  counter=0
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,1))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  actualans=[]
  maxer=0
  arct=[]
  #print quest
  if "over" in quest:
    if flag==1:
      ctr=0
      prev=0
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi2_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi2_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr>=maxer:
          maxer=ctr
          actualans.append(ti)
        prev=ti
      print actualans[-1]
    elif flag==2:
      ctr=0
      prev=-1
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi2_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi2_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr==int(no_over[0])-1:
          maxer=ctr
          actualans.append(ti)
	  print ti
        prev=ti
      if len(actualans)>0:
	pass
      else:
	print "None"


    else:
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi2_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi2_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
	print ti
        actualans.append(ti)
  if "bowl" in quest:
    for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
  if "ball" in quest:
    if over!="":
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi2_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi2_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
	if ti[:2]==over:
          ti=ti[3:]
	  print ti
          actualans.append(ti)
    else:
       for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi2_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi2_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[3:]
	print ti
        actualans.append(ti)
	
  if "whom" in quest:
     for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
if "third" in match_name:
  ans=[]
  ct=0
  arct1=[]
  bina=[]
  fa=open('mydataset/odi3_commentary_inn1.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct1.append(ct)
		ct=ct+1
  finalans=[]
  counter=0
  finalarct=[]
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,0))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  ct=0
  arct2=[] 
  ans=[]
  fa=open('mydataset/odi3_commentary_inn2.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in  description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct2.append(ct)
		ct=ct+1
  counter=0
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,1))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  actualans=[]
  maxer=0
  arct=[]
  #print quest
  if "over" in quest:
    if flag==1:
      ctr=0
      prev=0
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi3_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi3_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr>=maxer:
          maxer=ctr
          actualans.append(ti)
        prev=ti
      print actualans[-1]
    elif flag==2:
      ctr=0
      prev=-1
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi3_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi3_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr==int(no_over[0])-1:
          maxer=ctr
          actualans.append(ti)
	  print ti
        prev=ti
      if len(actualans)>0:
	pass
      else:
	print "None"


    else:
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi3_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi3_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
	print ti
        actualans.append(ti)
  if "bowl" in quest:
    for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
  if "ball" in quest:
    if over!="":
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi3_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi3_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
	if ti[:2]==over:
          ti=ti[3:]
	  print ti
          actualans.append(ti)
    else:
       for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi3_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi3_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[3:]
	print ti
        actualans.append(ti)
	
  if "whom" in quest:
     for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
if "fourth" in match_name:
  ans=[]
  ct=0
  arct1=[]
  bina=[]
  fa=open('mydataset/odi4_commentary_inn1.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct1.append(ct)
		ct=ct+1
  finalans=[]
  counter=0
  finalarct=[]
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,0))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  ct=0
  arct2=[] 
  ans=[]
  fa=open('mydataset/odi4_commentary_inn2.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in  description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct2.append(ct)
		ct=ct+1
  counter=0
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,1))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  actualans=[]
  maxer=0
  arct=[]
  #print quest
  if "over" in quest:
    if flag==1:
      ctr=0
      prev=0
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi4_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi4_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr>=maxer:
          maxer=ctr
          actualans.append(ti)
        prev=ti
      print actualans[-1]
    elif flag==2:
      ctr=0
      prev=-1
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi4_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi4_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr==int(no_over[0])-1:
          maxer=ctr
          actualans.append(ti)
	  print ti
        prev=ti
      if len(actualans)>0:
	pass
      else:
	print "None"



    else:
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi4_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi4_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
	print ti
        actualans.append(ti)
  if "bowl" in quest:
    for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
  if "ball" in quest:
    if over!="":
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi4_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi4_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
	if ti[:2]==over:
          ti=ti[3:]
	  print ti
          actualans.append(ti)
    elif flag==2:
      ctr=0
      prev=-1
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi4_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi4_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr==int(no_over[0])-1:
          maxer=ctr
          actualans.append(ti)
	  print ti
        prev=ti
      if len(actualans)>0:
	pass
      else:
	print "None"



    else:
       for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi4_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi4_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[3:]
	print ti
        actualans.append(ti)
	
  if "whom" in quest:
     for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
if "fifth" in match_name:
  ans=[]
  ct=0
  arct1=[]
  bina=[]
  fa=open('mydataset/odi5_commentary_inn1.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct1.append(ct)
		ct=ct+1
  finalans=[]
  counter=0
  finalarct=[]
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,0))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "one" in description.lower() or "1 run" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2 run" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  ct=0
  arct2=[] 
  ans=[]
  fa=open('mydataset/odi5_commentary_inn2.txt')
  with fa as f:
        for line in f:
		if "six" in description.lower():
		  description="SIX"
		if "out" in description.lower():
		  description="OUT"
		if "one" in description.lower() or "1 run" in description.lower():
		  description="1 run"
		if "two" in description.lower() or "2 run" in description.lower():
		  description="2 run"
		if "four" in description.lower():
		  description="FOUR"
		if "wide" in description.lower():
		  description="wide"
		if "dismiss" in description.lower():
		  description="OUT"
		if "noball" in  description.lower():
		  description="no ball"
                if re.search(description, line):
			if re.search(player_name.lower(),line.lower()):
			  ans.append(line)
			  arct2.append(ct)
		ct=ct+1
  counter=0
  for i in ans:
    sen=i.split(",")
    if verb[0][0]=="hit" or verb[0][0]=="was":
      if player_name.lower() in sen[0].split("to")[1].lower():
	finalans.append(i)
        finalarct.append((counter,1))
    elif verb[0][0]=="bowled":
      if player_name.lower() in sen[0].split("to")[0].lower():
	if "wide" in description.lower():
	  if "wide" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
        if "noball" in description.lower():
	  if "no ball" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,1))
	if "one" in description.lower() or "1" in description.lower():
	  if "1 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
	if "two" in description.lower() or "2" in description.lower():
	  if "2 run" in sen[1]:
	    finalans.append(i)
            finalarct.append((counter,0))
    counter=counter+1
  actualans=[]
  maxer=0
  arct=[]
  #print quest
  if "over" in quest:
    if flag==1:
      ctr=0
      prev=0
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi5_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi5_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr>=maxer:
          maxer=ctr
          actualans.append(ti)
        prev=ti
      print actualans[-1]
    elif flag==2:
      ctr=0
      prev=-1
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi5_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi5_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
        if ti==prev:
	  ctr=ctr+1
        else:
	  ctr=0
        if ctr==int(no_over[0])-1:
          maxer=ctr
          actualans.append(ti)
	  print ti
        prev=ti
      if len(actualans)>0:
	pass
      else:
	print "None"



    else:
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi5_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi5_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[:2]
	print ti
        actualans.append(ti)
  if "bowl" in quest:
    for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
  if "ball" in quest:
    if over!="":
      for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi5_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi5_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
	if ti[:2]==over:
          ti=ti[3:]
	  print ti
          actualans.append(ti)
    else:
       for i in range(len(finalans)):
	if finalarct[i][1]==0:
        	fa=open('mydataset/odi5_commentary_inn1.txt')
		arct=arct1
	elif finalarct[i][1]==1:
        	fa=open('mydataset/odi5_commentary_inn2.txt')
		arct=arct2
  	lines=fa.readlines()
        ti=lines[arct[finalarct[i][0]]-1]
        ti=ti[3:]
	print ti
        actualans.append(ti)
	
  if "whom" in quest:
     for i in finalans:
	players=i.split(",")
	print players[0].split("to")[0]
