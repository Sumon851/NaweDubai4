	
import streamlit as st 
import pandas as pd
st.set_page_config(page_title='Budget',initial_sidebar_state='collapsed')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


df=pd.read_csv('new.csv')
df['budget']=df['col1']+df['soil_col']+df['landue_col']
budget=df.loc[0,'budget']

st.subheader('Extra task ')
extra_prompt1=st.selectbox("Do you want PM report to be in Swedish?",options=[' ','No','Yes'] )
extra_prompt2=st.selectbox("Do you want external meetings?",options=[' ','No','Yes'] )


TOTAL=[budget]
if extra_prompt1=='Yes':
	#st.write(df['col2'])
	budget1=df.loc[0,'col2']
	print(budget1)
	TOTAL.append(budget1)
else:
	budget1=0
if extra_prompt2=='Yes':
	hours=st.slider('How many?',1,20,1)
	budget2=df.loc[0,'col3']*int(hours)
	TOTAL.append(budget2)
else:
	budget2=0
#st.write(budget,budget1)

print(TOTAL)
if len(TOTAL)>1:
	
	st.write('*:red[Final estimated budget', f'SEK {round(budget+budget1+budget2)} ]*')
else:
	st.write('*:red[Final estimated budget without translated PM and external meetings', f'SEK {round(budget)} ]*')
#placeholder.empty()

	
df=pd.read_csv('new.csv')


tab1, tab2, tab3, tab4 = st.tabs(['Main task','Data Requirement','Duration', 'Deliverables'])
with tab1:
   st.subheader(':blue[Main Task]')
   st.write(df.loc[0,'Main tasks'])

with tab2:
	st.subheader(':blue[Data Requirement]')
	st.write('*:red[Client is required to provide all the necessary data beforehand in order to iniate project activities]*')
	st.write(df.loc[0,'Data requirement'])

with tab3:
	st.subheader(':blue[Duration]')
	st.write(df.loc[0,'duration'])

with tab4:
	st.subheader(':blue[Deliverables]')
	st.write(df.loc[0,'Deliverable'])
