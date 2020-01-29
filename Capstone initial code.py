import numpy as np
import pandas as pd

df=pd.read_excel("Baseball INIT data.xlsx")
data=df.to_numpy()

def getPitcherDate(gameid):
	pass

# ~ def indiv_count (pitcher,date,value,op):

# ~ def team_count (team,date,value,op):

def indiv_winloss(pitcher,date):
	w=0
	l=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if pitcher==x["STARTING PITCHER"] and date>=x["DATE"]:
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and pitcher == x["STARTING PITCHER"]:
			if x["W"]==1:
				w+=1
			if x["L"]==1:
				l+=1
			total+=1
	# ~ print(l,w,total)
	return(w,l)

def team_winloss(team,date):
	w=0
	l=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date>=x["DATE"]:
			games.add(x["GAME-ID"])
	# ~ print(games)
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team == x["TEAM"]:
			if x["W"]==1:
				w+=1
			if x["L"]==1:
				l+=1
			total+=1
	# ~ print(op_win,win,total)
	return(w,l)

def indiv_obpa(pitcher,date):
	op_ab=0
	ph=0
	pbb=0
	hb=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if pitcher==x["STARTING PITCHER"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and pitcher != x["STARTING PITCHER"]:
			total+=1
			op_ab+=x["AB"]
		if x["GAME-ID"] in games and pitcher == x["STARTING PITCHER"]:
			ph+=x["PH"]
			pbb+=x["PBB"]
			hb+=x["HB"]
	# ~ print(op_ab,ph,pbb,hb,total)
	return (ph+pbb+hb)/op_ab



def team_obpa(team,date):
	op_ab=0
	ph=0
	pbb=0
	hb=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
			op_ab+=x["AB"]
		if x["GAME-ID"] in games and team == x["TEAM"]:
			ph+=x["PH"]
			pbb+=x["PBB"]
			hb+=x["HB"]
	# ~ print(op_ab,ph,pbb,hb,total)
	return (ph+pbb+hb)/op_ab
	


def team_obp(team,date):
	ab=0
	bh=0
	bbb=0
	op_hb=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
			op_hb+=x["HB"]
		if x["GAME-ID"] in games and team == x["TEAM"]:
			ab+=x["AB"]
			bh+=x["BH"]
			bbb+=x["BBB"]
	# ~ print(ab,bh,bbb,op_hb,total)
	return (bh+bbb+op_hb)/ab		


def team_avg(team,date):
	ab=0
	bh=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
		if x["GAME-ID"] in games and team == x["TEAM"]:
			ab+=x["AB"]
			bh+=x["BH"]
	# ~ print(ab,bh,total)
	return bh/ab
	
	
def team_avga(team,date):
	op_ab=0
	ph=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
			op_ab+=x["AB"]
		if x["GAME-ID"] in games and team == x["TEAM"]:
			ph+=x["PH"]
	# ~ print(op_ab,ph,total)
	return ph/op_ab


def indiv_avga(pitcher,date):
	op_ab=0
	ph=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if pitcher==x["STARTING PITCHER"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and pitcher != x["STARTING PITCHER"]:
			total+=1
			op_ab+=x["AB"]
		if x["GAME-ID"] in games and pitcher == x["STARTING PITCHER"]:
			ph+=x["PH"]
	# ~ print(op_ab,ph,total)
	return ph/op_ab


def indiv_error(pitcher,date):
	e=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if pitcher==x["STARTING PITCHER"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and pitcher != x["STARTING PITCHER"]:
			total+=1
		if x["GAME-ID"] in games and pitcher == x["STARTING PITCHER"]:
			e+=x["E"]
	# ~ print(e,total)
	return e


def team_error(team,date):
	e=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date>=x["DATE"]:
			# ~ print(x)
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
		if x["GAME-ID"] in games and team == x["TEAM"]:
			e+=x["E"]
	# ~ print(e,total)
	return e



	
	
# ~ print(indiv_obpa("Charlie Morton","10/1/19"))
# ~ print(team_obpa("Tampa Bay Rays","10/1/19"))
# ~ print(team_obp("Tampa Bay Rays","10/1/19"))
# ~ print(team_avg("Tampa Bay Rays","10/1/19"))
# ~ print(team_avga("Tampa Bay Rays","10/1/19"))
# ~ print(indiv_avga("Charlie Morton","10/1/19"))
# ~ print(indiv_error("Charlie Morton","10/1/19"))
# ~ print(team_error("Tampa Bay Rays","10/1/19"))
print(team_winloss("Tampa Bay Rays","10/1/19"))
print(indiv_winloss("Charlie Morton","10/1/19"))


# ~ print(df[["BBB","BH"]])
# ~ print(np.array(df[["BR","BH","BBB","AVG","W","PH","PR"]]))
