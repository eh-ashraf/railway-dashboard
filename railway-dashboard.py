#import libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#loading data
df = pd.read_csv('New Reilway.csv')
# Sidebar
st.sidebar.header("Railway Analyze Dashboard")
st.sidebar.image("railwayimage.jpg")


st.sidebar.subheader('filter your data')
cat_filter = st.sidebar.selectbox('categorical Filtering',[None,'Purchase Type','Payment Method','Railcard','Reason for Delay'])
num_filter = st.sidebar.selectbox('Numerical Filtering',[None,])
col_filter = st.sidebar.selectbox('Column Filtering',[None,'Purchase Type','Payment Method','Railcard','Reason for Delay'])
row_filter = st.sidebar.selectbox('Row Filtering',[None])


st.sidebar.write('')
st.sidebar.markdown('made with :two_hearts: by [Ehab Ashraf]')
# body
st.subheader('- Revenue by Ticket Type:')
#row a
a1, a2, a3 = st.columns(3)

a1.metric(' - Advance:',"£309,274")
a2.metric('- Anytime: ','£209,309')
a3.metric('- Off-Peak:','£223,338')
#body
st.subheader('- Revenue by Travel Class:')
#row b
a1 , a2 = st.columns(2)

a1.metric('- First Class:','£149,399')
a2.metric('- Standard:', '£592,522')

#row c
st.subheader("Departure Station vs. Price")
fig = px.scatter(data_frame=df, x= 'Departure Station' , y= 'Price', color=cat_filter,size=num_filter,facet_col=col_filter,facet_row=row_filter)
st.plotly_chart(fig, use_container_width=True)

#charts
c1, c2, c3 = st.columns((4,3,3))

with c1:
    st.text('Payment method vs. Price')
    fig = px.bar(data_frame=df , x = 'Payment Method' , y = 'Price',color=cat_filter )
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.text('Purchase Type vs. Price')
    fig = px.pie(data_frame=df , names = 'Purchase Type' , values = 'Price',hole=0.4 )
    st.plotly_chart(fig, use_container_width=True)


with c3:
    st.text('Ticket Type vs. Price')
    fig = px.pie(data_frame=df , names = 'Ticket Type' , values = 'Price',color=cat_filter,hole=0.4 )
    st.plotly_chart(fig, use_container_width=True)

