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
st.header('NAWE DUBAI INTELLIGENCE PLATFORM')
#st.subheader('please select following criteria to estimate budget
def main_col(a):
	df=pd.read_excel('duration.xlsx',sheet_name=a)
	
	df=df.fillna('')
	
	
	prj_area=st.selectbox('How large is your project area?',options=df.area.unique())
	df1=df.loc[df['area']==prj_area]
	df1.reset_index(drop=True)
	df1.to_csv('new.csv',index=False)
main_service=st.selectbox('Please select your main service?', options=['', 'Stormwater'])

if main_service=='Stormwater':
	service=st.selectbox('Please select the sub-service', options=['','Stormwater Investigation for detailed plan area','Flood Investigation in Mike+ (1D stormwater pipe modelling)',
	'Flood Investigation in Mike+(1D-2D overland runoff  and pipe modelling)'] )
	
	if service=='Stormwater Investigation for detailed plan area':
		main_col('duration-1')
		
		if st.button('next :arrow_forward:'):
			switch_page('web_app')
	elif service=='Flood Investigation in Mike+ (1D stormwater pipe modelling)':
		main_col('duration-2')
		if st.button('next :arrow_forward:'):
			switch_page('web_app-st6')
		
	elif service=='Flood Investigation in Mike+(1D-2D overland runoff  and pipe modelling)':
		main_col('duration-3')

		if st.button('next :arrow_forward:'):
			switch_page('web_app-st8')



		
	
