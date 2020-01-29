import numpy as np
import pandas as pd

df=pd.read_excel("Baseball INIT data.xlsx")
data=df.to_numpy()

def getPitcherDate(gameid):
	pass

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
			print(x)
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
	print(op_ab,ph,pbb,hb,total)
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
	print(op_ab,ph,pbb,hb,total)
	return (ph+pbb+hb)/op_ab		
			
def indiv_count (pitcher,date,value,op)

def team_count (team,date,value,op)
	
	
# ~ print(indiv_obpa("Charlie Morton","7/18/19"))
print(team_obpa("Tampa Bay Rays","7/18/19"))

# ~ print(df[["BBB","BH"]])
# ~ preint(np.array(df[["BR","BH","BBB","AVG","W","PH","PR"]]))
