import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

loc = 'D:\calibreci.csv'
df = pd.read_csv(loc)
# # get the title of the figure
title = df['Name'][0:1].to_string(index=False)

# find the max value of the license usage
max_value = df['Used'].max()
# find the min value of the license usage
min_value = df['Used'].min()

df = df[-121:-1]

fig = go.Figure()
fig = px.bar(df, x='Time', y='Used', text='Used', title=title+' Usage through 5 days', color='Used', barmode='group')
# fig.add_bar(df, x='Time', y='Issued')
fig.update_traces(texttemplate='%{text:.1s}', textposition='outside', textfont_size=18)
fig.update_layout(xaxis_tickangle=-45)
fig.show()
