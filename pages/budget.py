def budget_calc(area):
	import pandas as pd 
	df=pd.read_excel('budget.xlsx')
	df.index=df.Rate
	df=df.drop(columns='Rate')
	
	
	df['External Meeting (SEK/hr)']=df['External Meeting (SEK/hr)'].fillna(6000)
	
	
	a=df.loc[area].values[:]
	