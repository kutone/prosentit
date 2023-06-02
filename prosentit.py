import streamlit as st
import streamlit as st
import pandas as pd
import numpy as np
import datetime
import plotly.express as px
from datetime import date

today_timestamp = date.today()
start_date = st.sidebar.date_input("Puurtaminen alkoi",datetime.date(2011, 6, 1), max_value=today_timestamp)
length = st.sidebar.number_input("Kauanko painetaan",value=40, min_value= 1, max_value=60)
start_date_str = start_date.strftime('%Y-%m-%d')
end_date = start_date + pd.DateOffset(years=length)
end_date_str = end_date.strftime('%Y-%m-%d')

st.markdown("<h1 style='text-align: center;'>Tänään jäljellä</h1>", unsafe_allow_html=True)
df = pd.DataFrame({'date': pd.date_range(start=start_date, end=end_date)})
df['Päiviä takana'] = df.index + 1
df['Päiviä jäljellä'] = (end_date - df['date']).dt.days
df['Prosentit'] = (df['Päiviä takana'] / len(df)) * 100
df = df.set_index("date")
today = date.today().strftime('%Y-%m-%d')
df.loc[today]

fig = px.line(df, y="Prosentit")
fig.add_vline(x=today, line_width=5, 
              line_dash="dash", line_color='yellow', opacity=0.5)

fig.add_vrect(x0=start_date_str, x1=today, 
              fillcolor="yellow", opacity=0.25, line_width=0)
st.plotly_chart(fig)
