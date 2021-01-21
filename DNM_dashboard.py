import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

'''
# Darknet Markets
## Crypto Crime in 2020

This project uses live data from Chainalysis Reactor!
#

'''



'''
#
## Darknet Market Revenue v. Total Transfers to Darknet Markets, 2011-2020
'''
csv1 = pd.read_csv('dnm/yr_rev_and_no_transfers_r.csv')
df1 = pd.DataFrame(csv1)
df1_years = df1['year'].tolist()
dnm_rev = df1['Darknet market revenue'].tolist()
num_trans = df1['Number of transfers sent to darknet markets'].tolist()
DNMRev = go.Bar(name='dnm rev', x=df1_years, y=dnm_rev, xaxis='x', yaxis='y1')
NumTransfers = go.Scatter(name='# transfers', x=df1_years, y=num_trans, xaxis='x', yaxis='y2')
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
        anchor = 'x'
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
received_usd_7 = df7['received_usd'].tolist()
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
### weekly in 2020
'''
csv9 = pd.read_csv('dnm/weekly2020_revenue_r_top20_all.csv')
df9 = pd.DataFrame(csv9)
x9 = df9['week_detailed'].tolist()
y9 = df9.columns.tolist()
y9.pop(0)
layout9 = dict(
    xaxis=dict(title='Week',
              tickangle=-50),
    yaxis=dict(title='Received USD'),
    barmode='stack',
    height=800,
    width=900
)
data9 = []
for col in y9:
    data9.append(go.Bar(
        name=col,
        x=x9,
        y=df9[col]
    ))
fig9 = go.Figure(data = data9, layout=layout9)
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
### weekly in 2020
'''
csv10 = pd.read_csv('dnm/weekly2020_revenue_r_top20_global.csv')
df10 = pd.DataFrame(csv10)
x10 = df10['week_detailed'].tolist()
y10 = df10.columns.tolist()
y10.pop(0)
layout10 = dict(
    xaxis=dict(title='Week',
              tickangle=-50),
    yaxis=dict(title='Received USD'),
    barmode='stack',
    height=800,
    width=1000
)
data10 = []
for col in y10:
    data10.append(go.Bar(
        name=col,
        x=x10,
        y=df10[col]
    ))
fig10 = go.Figure(data = data10, layout=layout10)
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
    go.Bar(name='dnm rev', x=df5['name'], y=df5['2020'], marker=dict(color='orange'))
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
    "Choose category", list(col6), ["Exchanges", "Darknet markets"]
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

#csv6 = pd.read_csv('dnm/yr_destination_top6.csv')
#df6 = pd.DataFrame(csv6)
#df6 = df6.transpose()
#new_header = df6.iloc[0]
#df6 = df6[1:]
#df6.columns = new_header
#cats = st.multiselect("Choose category", list(df6.index), ["Exchanges", "Darknet markets"])
#if not cats:
#    st.error("Please select at least one country.")
#else:
#    data = df6.loc[cats]
#    st.write("### Share of all funds sent from darknet markets", data.sort_index())
#    data = data.T.reset_index()
#    data.sort_index()
#    data5 = pd.melt(data, id_vars=["year"]).rename(columns={"index": "year", "value": "shares"})
#    chart = (alt.Chart(data5).mark_area(opacity=0.3).encode(x="year:T",y="shares",color="variable:N",))
#    st.altair_chart(chart, use_container_width=True)


'''
#
## Average lifespan of Darknet Markets in a given year, but are no longer active as of Dec '20
'''
csv7 = pd.read_csv('dnm/yr_avg_lifespan_and_count.csv')
df7 = pd.DataFrame(csv7)
graph7 = px.bar(df7, x='year', y=['Average lifespan among dead markets that started receiving revenue in given year',
                     'Number of dead markets that started receiving revenue in given year'], barmode='group')
graph7.update_layout(
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor="LightSteelBlue",
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
    title="Where Darknet Markets are Sending Funds",
    height = 850,
    width = 900,
    font=dict(size = 12, color = 'black'),
    plot_bgcolor='black',
    paper_bgcolor='white'
)
st.plotly_chart(fig11)
