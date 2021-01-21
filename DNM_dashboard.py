import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

'''
# Darknet Markets: Crypto Crime in 2020
### Powered by **Chainalysis Reactor**
#

'''



'''
#
## Darknet Market Revenue v. Total Transfers to Darknet Markets, 2011-2020
'''
st.write(f'''**_Hover_** your mouse over the chart to explore the data''')
csv1 = pd.read_csv('dnm/yr_rev_and_no_transfers_r.csv')
df1 = pd.DataFrame(csv1)
df1_years = df1['year'].tolist()
dnm_rev = df1['Darknet market revenue'].tolist()
num_trans = df1['Number of transfers sent to darknet markets'].tolist()
DNMRev = go.Bar(name='dnm rev', x=df1['year'], y=df1['Darknet market revenue'], xaxis='x', yaxis='y1')
NumTransfers = go.Scatter(name='# transfers', x=df1['year'], y=num_trans, xaxis='x', yaxis='y2')
layouts = dict(
    margin=dict(l=40, r=40, t=40, b=40),
    paper_bgcolor='rgb(255,249,240)',
    geo = dict(
        showframe = True,
        showcoastlines = True,
    ),
    yaxis=dict(
        title = 'DNM Revenue',
        overlaying='y2',
        anchor = 'x',
        zeroline = True
    ),
    yaxis2=dict(
        title = '# of Transfers',
        side = 'right',
        anchor = 'x',
    ),

)
fig1 = go.Figure(data=[DNMRev, NumTransfers], layout=layouts)
st.plotly_chart(fig1)

'''
#
## Darknet Market Received Monthly Since 2019
'''
csv7 = pd.read_csv('dnm/dnm_monthly_since_2019.csv')
df7 = pd.DataFrame(csv7)
layout7 = dict(
    paper_bgcolor='rgb(255,249,240)',
    xaxis=dict(
        tickangle=-50
    )
)
fig7 = go.Figure(data=[
    go.Bar(name='dnm received usd', x=df7['month_year'], y=df7['received_usd'], marker=dict(color='pink'))
], layout=layout7)
st.plotly_chart(fig7)



'''
#
## Monthly darknet market revenue, 2015 - 2020
'''
csv2 = pd.read_csv('dnm/mo_revenue_r_w_wo_Hydra.csv')
df2 = pd.DataFrame(csv2)
df2_years = df2['month_year'].tolist()
tot_rev = df2['Total revenue'].tolist()
tot_rev_exhydra = df2['Total revenue excl. Hydra'].tolist()
layout2 = dict(
    margin=dict(l=40, r=40, t=40, b=40),
    paper_bgcolor='rgb(255,249,240)',
    geo = dict(
        showframe = True
    ),
    xaxis=dict(
        tickangle=-70
    ),
    yaxis=dict(
        overlaying='y2',
        anchor = 'x'
    ),
    yaxis2=dict(
        side = 'right',
        anchor = 'x',

    ),
    legend = dict(
        xanchor='center',
        yanchor='top',
        y=-0.2,
        x=0.5
    )
)
fig2 = go.Figure(data=[
    go.Scatter(name='Total Revenue', x=df2_years, y=tot_rev, xaxis='x'),
    go.Scatter(name='Total Revenue excluding Hydra', x=df2_years, y=tot_rev_exhydra, xaxis='x')
], layout=layout2)
st.plotly_chart(fig2)



'''
#
## All darknet markets by share of total market size over time, 2015 - 2020
'''
csv3 = pd.read_csv('dnm/yr_revenue_r_top20_all.csv')
df3 = pd.DataFrame(csv3)
df3
#stacked or filled area plot
x = df3['year'].tolist()
columns = df3.columns.tolist()
columns.pop(0)
data = []
for column in columns:
    y = df3[column].tolist()
    data.append(go.Scatter(
        name = column,
        x=x,
        y=y,
        mode='lines',
        line=dict(width=0.5),
        stackgroup = 'one'
    ))
layout3 = dict(
    paper_bgcolor='rgb(255,249,240)',
    width=900,
    height=600
)
fig3 = go.Figure(data=data, layout=layout3)
st.plotly_chart(fig3)
'''
### Weekly Darknet Market Revenue in 2020
'''
st.write(f'''Feel free to **_click_** on the **Darknet Markets** in the key on the right to make changes to the chart!''')
csv9 = pd.read_csv('dnm/weekly2020_revenue_r_all.csv')
df9 = pd.DataFrame(csv9)
#stacked or filled area plot
x9 = df9['week_detailed'].tolist()
columns9 = df9.columns.tolist()
columns9.pop(0)
data9 = []
for column in columns9:
    y9 = df9[column].tolist()
    data9.append(go.Scatter(
        name = column,
        x=x9,
        y=y9,
        mode='lines',
        line=dict(width=0.5),
        stackgroup = 'one'
    ))
layout9 = dict(
    paper_bgcolor='rgb(255,249,240)',
    xaxis = dict(
        title='Weekly',
        tickangle=-50
    ),
    width=1000,
    height=800
)
fig9 = go.Figure(data=data9, layout=layout9)
st.plotly_chart(fig9)



'''
#
## Global darknet markets by share of total market size over time, 2015 - 2020
'''
csv4 = pd.read_csv('dnm/yr_revenue_r_top20_global.csv')
df4 = pd.DataFrame(csv4)
df4
#stacked or filled area plot
x4 = df4['year'].tolist()
columns4 = df4.columns.tolist()
columns4.pop(0)
data4 = []
for column in columns4:
    y4 = df4[column].tolist()
    data4.append(go.Scatter(
        name = column,
        x=x4,
        y=y4,
        mode='lines',
        line=dict(width=0.5),
        stackgroup = 'one'
    ))
layout4 = dict(
    paper_bgcolor='rgb(255,249,240)',
    width=900,
    height=600
)
fig4 = go.Figure(data=data4, layout=layout4)
st.plotly_chart(fig4)
'''
### Weekly Revenue of the Top 20 Darknet Markets in 2020
'''
st.write(f'''Feel free to **_click_** on the **Darknet Markets** in the key on the right to make changes to the chart!''')
csv10 = pd.read_csv('dnm/weekly2020_revenue_r_top20.csv')
df10 = pd.DataFrame(csv10)
#stacked or filled area plot
x10 = df10['week_detailed'].tolist()
columns10 = df10.columns.tolist()
columns10.pop(0)
data10 = []
for column in columns10:
    y10 = df10[column].tolist()
    data10.append(go.Scatter(
        name = column,
        x=x10,
        y=y10,
        mode='lines',
        line=dict(width=0.5),
        stackgroup = 'one'
    ))
layout10 = dict(
    paper_bgcolor='rgb(255,249,240)',
    xaxis = dict(
        title='Weekly',
        tickangle=-50
    ),
    width=1000,
    height=800
)
fig10 = go.Figure(data=data10, layout=layout10)
st.plotly_chart(fig10)


'''
#
## Top 20 global darknet markets by revenue, 2020
'''
csv5 = pd.read_csv('dnm/2020_revenue_r_top20_global.csv')
df5 = pd.DataFrame(csv5)
cols5 = df5.columns.tolist()
layout5 = dict(
    paper_bgcolor='rgb(255,249,240)',
    xaxis=dict(
        tickangle=-50
    )
)
fig5 = go.Figure(data=[
    go.Bar(name='dnm rev', x=df5['name'], y=df5['Revenue'], marker=dict(color='orange'))
], layout=layout5)
st.plotly_chart(fig5)


'''
#
## Destination of Funds Leaving Darknet Markets
'''

csv6 = pd.read_csv('dnm/yr_destination_top6.csv')
df6 = pd.DataFrame(csv6)
years6 = df6['year'].tolist()
col6 = df6.columns.tolist()
col6.pop(0)
cats = st.multiselect(
    "Choose Category to Add to Chart", list(col6), ["Darknet markets", "P2P exchanges", "Unnamed services"]
)
st.write("### Share of all funds sent from darknet markets")
scatters6 = []
for cat in cats:
    y6 = df6[cat].tolist()
    scatters6.append(go.Scatter(
        name = cat,
        x=years6,
        y=y6,
        mode='lines',
        line=dict(width=0.9),
        stackgroup = 'one'
    ))
layout6 = dict(
    paper_bgcolor='rgb(255,249,240)',
    width=900,
    height=600
)
fig6 = go.Figure(data=scatters6, layout=layout6)
st.plotly_chart(fig6)
st.text("")

'''
#
## Average lifespan of Darknet Markets in a given year, but are no longer active as of Dec '20
'''
st.write('''The graph below shows the **_average lifespan_** among dead markets that started receiving revenue in given year and **_number of dead markets_** that started receiving revenue in given year.''')
csv7 = pd.read_csv('dnm/yr_avg_lifespan_and_count.csv')
df7 = pd.DataFrame(csv7)
graph7 = px.bar(df7, x='year', y=['Year Average Lifespan, in Months',
                     'Number of Markets'], barmode='group')
graph7.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
    xaxis = dict(
        title='Year'
    ),
    yaxis=dict(
        title=''
    ),
    legend = dict(
        xanchor='center',
        yanchor='top',
        y=-0.2,
        x=0.5
    )
)
st.plotly_chart(graph7)
st.text("")

'''
#
## DNM Received Funds by Market Type, Weekly in 2020
'''
csv8 = pd.read_csv('dnm/weekly_origin_2020.csv')
df8 = pd.DataFrame(csv8)
x8 = df8['week'].tolist()
y8 = df8.columns.tolist()
y8.pop(0)
layout8 = dict(
    xaxis=dict(title='Week',
              tickangle=-50),
    yaxis=dict(title='Received USD'),
    barmode='stack',
    height=800,
    width=900
)
data8 = []
for col in y8:
    data8.append(go.Bar(
        name=col,
        x=x8,
        y=df8[col]
    ))
fig8 = go.Figure(data = data8, layout=layout8)
st.plotly_chart(fig8)

'''
#
## Darknet Market-to-Market Sending Exposure
'''
st.write('''The flow diagram below illustrates where the **_Darknet Markets_** are sending funds. If you **hover** your mouse over the diagram, you can see the source and target darknet markets between which the proportional flow of $USD was exchanged.''')
csv11 = pd.read_csv('dnm/dnm_sankey.csv')
df11 = pd.DataFrame(csv11)
df11 = df11.drop(df11.columns[0], axis=1)
#put columns into list, add a space to each string in counterparty name list
names11 = df11['name'].tolist()
counterparty_names11 = df11['counterparty_name'].tolist()
cnames11 = [n + " " for n in counterparty_names11]
amountusd11 = df11['amount_usd'].tolist()
unique_names11 = np.unique(names11).tolist()
unique_cnames11 = np.unique(cnames11).tolist()
#combine unique names and counterparty names into one list for hash map creation
unique_key11 = unique_names11 + unique_cnames11
#create a hash map with key value pair --> (name, unique key)
def convertDict(lst):
    hashmap = dict()
    for i in range(len(lst)):
        hashmap[lst[i]] = i
    return hashmap
map11 = convertDict(unique_key11)
#create source and target lists for sankey diagram using the hashmap
source_df11 = []
target_df11 = []
for name in names11:
    source_df11.append(map11[name])
for cname in cnames11:
    target_df11.append(map11[cname])

fig11 = go.Figure(data=[go.Sankey(
    valueformat = "$.0f",
    node = dict(
      pad = 35,
      thickness = 25,
      line = dict(color = "black", width = 0.2),
      label =  unique_key11,
    ),
    link = dict(
      source =  source_df11,
      target =  target_df11,
      value =  amountusd11
  ))])

fig11.update_layout(
    hovermode = 'closest',
    height = 850,
    width = 900,
    font=dict(size = 12, color = 'black'),
    plot_bgcolor='black',
    paper_bgcolor='white'
)
st.plotly_chart(fig11)
