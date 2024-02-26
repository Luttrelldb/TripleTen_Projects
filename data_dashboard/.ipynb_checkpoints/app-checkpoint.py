import streamlit as st
import pandas as pd
import plotly.express as px


st.header('Data Trends in Vehicle Data')

# Read in Dataset
df_vehicles = pd.read_csv("vehicles_us.csv")

#Create First Chart
fig_price_dirst = px.histogram(df_vehicles['price'])
fig_price_dirst.update_layout(
        title="Vehicle Price Dristribution",
        xaxis_title="Vheicle Sale Price (UDS)",
        yaxis_title="Count of Vehicles")

st.write('The Price dirstribution of the vheicles is very right skwed.') 

st.plotly_chart(fig_price_dirst)

#Create Second Chart
st.write('The most interesting trend is with the condition of the vehicles,  it seems that "good" condition is all that is required to get a good sale price for the vehicles.') 

fig_price_vs_condition = px.scatter(x=df_vehicles['condition'],y=df_vehicles['price'])
fig_price_vs_condition.update_layout(
        title="Price Dristribution per Reported Condition",
        xaxis_title="Condition of Vheicles",
        yaxis_title="Vheicle Sale Price (UDS)")

st.plotly_chart(fig_price_vs_condition)

#Create Third Chart