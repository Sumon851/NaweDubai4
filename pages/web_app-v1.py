import pandas as pd
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title='Budget',initial_sidebar_state='collapsed')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)

st.header('NAWE DUBAI')
st.subheader('please provide following information')


df=pd.read_excel('demo-st5.xlsx')
df=df.fillna(' ')
coln_list=[]
q_list=[]
x=[]
for coln,c in enumerate(df.columns):
    if not c.startswith('f'):
        print(coln,c)
       
        coln_list.append(coln)
        q_list.append(c)

df=df.drop(index=0)
x=[]
#st.sidebar.header("Please Filter Here:")

#st.sidebar.header("Please Filter Here:")
def filter_criteria(q_list):
    for q in q_list:
        bar=(st.selectbox(" {}".format(q), options=df[str(q)].unique()))

        x.append(bar)

filter_criteria(q_list)## factor lists
#print(x)
area=x[1]##selecting area base value

total_f=[]
#x=['<1','1-3','1-5']
df1=pd.DataFrame()
#def selectionq(x):
try:
	for i in range(len(q_list)):
	#print('q_list', q_list)
	#print(df[q_list[i]])
		df1=df.loc[df[q_list[i]]==x[i]]
		
		total_f.append(df1.iloc[:,coln_list[i]+1].values[0])
		df1=pd.DataFrame()
	print(total_f)
	df_b=pd.read_excel('budget.xlsx',sheet_name='ST-1')
	df_b.index=df_b.Rate
	df_b=df_b.drop(columns='Rate')
	
	
	df_b['External Meeting (SEK/hr)']=df_b['External Meeting (SEK/hr)'].fillna(6000)
	
	
	constant=df_b.loc[str(x[1])].values[:]
	
except:
	pass
df_new=pd.read_csv('new.csv')
try:
	budget=sum(total_f)*(constant[0])
	
	df_new=df_new.assign(col1=[budget],col2=constant[1],col3=constant[2])
	
	df_new.to_csv('new.csv',index=False)

except:
	st.write(':red[please select all the boxes above]')
	pass
#print(constant,budget)
st.title("Preliminary Budget")
#
#

#

CLICK_PROMPT=st.selectbox("Do you want to proceed to next page to view budget?",options=[' ','No','Yes'] )

	
if CLICK_PROMPT=='Yes':
	switch_page('final')





