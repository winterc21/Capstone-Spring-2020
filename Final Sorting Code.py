import numpy as np
import pandas as pd
import random 

df=pd.read_excel("Baseball INIT data.xlsx")
data=df.to_numpy()

def outcome(team,date):
	r=0
	op_r=0
	total=0
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date==x["DATE"]:
			if x["W"]==1:
				return("Win")
			if x["L"]==1:
				return("Loss")



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
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team == x["TEAM"]:
			if x["W"]==1:
				w+=1
			if x["L"]==1:
				l+=1
			total+=1
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
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
		if x["GAME-ID"] in games and team == x["TEAM"]:
			ab+=x["AB"]
			bh+=x["BH"]
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
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
			op_ab+=x["AB"]
		if x["GAME-ID"] in games and team == x["TEAM"]:
			ph+=x["PH"]
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
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and pitcher != x["STARTING PITCHER"]:
			total+=1
			op_ab+=x["AB"]
		if x["GAME-ID"] in games and pitcher == x["STARTING PITCHER"]:
			ph+=x["PH"]
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
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and pitcher != x["STARTING PITCHER"]:
			total+=1
		if x["GAME-ID"] in games and pitcher == x["STARTING PITCHER"]:
			e+=x["E"]
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
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team != x["TEAM"]:
			total+=1
		if x["GAME-ID"] in games and team == x["TEAM"]:
			e+=x["E"]
	return e

def player_a(pitcher,date):
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
			return pitcher

def team_a(team,date):
	if type(date) != pd.Timestamp:
		date=pd.Timestamp(date)
	games=set()
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if team==x["TEAM"] and date>=x["DATE"]:
			games.add(x["GAME-ID"])
	for row  in data:
		x={header:value for header,value in zip(df.columns,row)}
		if x["GAME-ID"] in games and team == x["TEAM"]:
			return team

N=len(df)
r = np.random.permutation(list(range(800,4857)))
for i in r:
	
	row = df.loc[i]
	
	row['GAME-ID']
	
	pair = df[df['GAME-ID']==row['GAME-ID']]
	
	players = list(pair['STARTING PITCHER'])
	teams = list(pair['TEAM'])
	times = list(pair['DATE'])
	
	(a,b)=(team_winloss(teams[0],times[0]))
	(c,d)=(indiv_winloss(players[0],times[0]))
	
	print("{},{},{},{},{},{},{},{},{},{}({},{}),({},{}),{}" .format((team_a(teams[0],times[0])),(player_a(players[0],times[0])),(team_obpa(teams[0],times[0])),(indiv_obpa(players[0],times[0])),(team_obp(teams[0],times[0])),(team_avg(teams[0],times[0])),(team_avga(teams[0],times[0])),(indiv_avga(players[0],times[0])),(indiv_error(players[0],times[0])),(team_error(teams[0],times[0])),a,b,c,d,(outcome(teams[0],times[0]))))
