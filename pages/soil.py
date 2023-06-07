import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title='Soil information',initial_sidebar_state='collapsed')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


st.subheader('please provide following soil information')
soil=['Filling material (no contamination)','Sand','Gravel','Rock','Silt','Clay','Peat','Filling material (contaminated)']
factor=['0.02','0.03','0.05','0.075','0.1','0.15','0.2','0.5']
number_fruits=[]
top=[]
max_value=None
for index,types in enumerate(soil):
	
	number=st.number_input(f'{types} %',max_value=max_value)
	top.append(number*float(factor[index]))
	number_fruits.append(number)

	if sum(number_fruits)==100:
		break
soil_sum=sum(top)/100
df=pd.read_csv('new.csv')
df['col1']=df['col1']+soil_sum*df['base']
df.to_csv('new.csv')
if st.button('NEXT :arrow_forward:'):
	switch_page('landuse')
