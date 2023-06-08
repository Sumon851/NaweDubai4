import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
st.set_page_config(page_title='landuse information',initial_sidebar_state='collapsed')
no_sidebar_style = """
    <style>
        div[data-testid="stSidebarNav"] {display: none;}
    </style>
"""
st.markdown(no_sidebar_style, unsafe_allow_html=True)


st.subheader('please provide following landuse information')
landuse=['','agriculture','office','industry','school', 'residential', 'commercial','block']
option=[' ','0-10','11-30','31-50','51-100','101-200','201-350','351-500','501-700','701-1000','>1000'
]
option_block=[' ','0-2','3-5','6-10','11-20','21-35','36-50','51-65','66-80','81-100','>100']

factor=['0','0.2','0.5','1','1.5','2.1','2.8','3.6','4.5','6','10']

number_fruits=[]
top=[]
max_value=None
landuse=st.selectbox('What is the landuse in the area? Please choose from the follwing options. If landuse is mixed, select- *:blue[block]* ', options=landuse)

if landuse=='block':
	block=st.selectbox('Number of block', options=option_block)
	index=option_block.index(block)
	f=float(factor[index])
else:
	use=st.selectbox(f'Area of {landuse} (st)', options=option)
	index=option.index(use)
	f=float(factor[index])

df=pd.read_csv('new.csv')
df['landue_col']=f*df['base']
df.to_csv('new.csv')
if st.button('NEXT :arrow_forward:'):
	switch_page('final')
