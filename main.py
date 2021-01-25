import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from datetime import datetime

from download import *
from data import *
from home_page import *

df["text"] = "Country: " + df["Country"]  # 設定要輸出的文字

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url',
                 refresh=False
    ),
    html.Div(id='page-content')
])
app.config.suppress_callback_exceptions = True  


page_1_layout = html.Div([
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginRight":".8%"},
            children=[html.P(
                        style={"textAlign":"center",
                               "fontWeight":"bold",
                               "color":"purple",
                               "padding":"1rem",
                               "fontSize": 20},
                        children="Total Confirmed Cases"),
                      html.H2(
                        id="totalCases",
                        style={"textAlign":"center",
                               "fontWeight":"bold",
                               "color":"purple"},
                      )],
    ),
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginRight":".8%"},
            children=[html.P(
                        style={"textAlign":"center",
                               "fontWeight":"bold",
                               "color":"purple",
                               "padding":"1rem",
                               "fontSize": 20},
                        children="New Confirmed Cases"),
                      html.H2(
                        id="newCases",
                        style={"textAlign":"center",
                               "fontWeight":"bold",
                               "color":"purple"},
                      )]
    ),
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginRight":".8%"},
            children=[html.P(
                        style={"textAlign":"center",
                               "fontWeight":"bold",
                               "color":"purple",
                               "padding":"1rem",
                               "fontSize": 20},
                        children="New Death Cases"),
                      html.H2(
                        id="DeathCases",
                        style={"textAlign":"center",
                               "fontWeight":"bold",
                               "color":"purple"}
                      )]
    ),
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginTop":".5%"},
            children=[html.P(
                        style={"textAlign":"center",
                               "fontWeight":"bold",
                               "color":"purple",
                               "padding":"1rem",
                               "fontSize": 20},
                        children="Total Death / Total Confirmed"),
                      html.H2(
                          id="percent",
                          style={"textAlign":"center",
                                 "fontWeight":"bold",
                                 "color":"purple"}                                
                      )]
    ),
    dcc.Link('Go back to home', href='/',style={"float":"right", "marginRight":50},),
    dcc.Dropdown(
        id='second_page_dropdown',
        options=[{'label': i, 'value': i} for i in countryDrop],
        value='United States of America',
        style={"width": 250, "marginTop":".5%"},
    ),
    html.Div(
        dcc.Graph(id='second_page_map',
        style={"width": "50%", "float" : "left"},
        )
    ),    
    html.Div(
        dcc.Graph(id='second_page_pie',
        style={"width": "50%", "float" : "right"},
        )
    ),
    html.Div(
        dcc.Graph(id='second_page_new_line',
        style={"width": "50%", "float" : "left"},
        )
    ),
    html.Div(
        dcc.Graph(id="second_page_death_line",
        style={"width": "50%", "float" : "right"},
        )
    ),
])

@app.callback(dash.dependencies.Output('totalCases', component_property='children'),
              dash.dependencies.Output('newCases', component_property='children'),
              dash.dependencies.Output('DeathCases', component_property='children'),
              dash.dependencies.Output('percent', component_property='children'),
              [dash.dependencies.Input('second_page_dropdown', component_property='value')])
def title(value):
    with open("output.csv") as each:
        for line in each:
            line = line.split(",")
            if(line[0] == value):
                newCases = int(line[6])
                newDeath = int(line[7])
                totalDeath = float(line[3])
                totalCases = int(line[2])
                break
    return "{:,}".format(totalCases), "{:,}".format(newCases), "{:,}".format(newDeath), "{:.2f}%".format((totalDeath / totalCases)*100)


@app.callback(dash.dependencies.Output('second_page_map', component_property='figure'),
              dash.dependencies.Output('second_page_pie', component_property='figure'),
              dash.dependencies.Output('second_page_new_line', component_property='figure'),
              dash.dependencies.Output('second_page_death_line', component_property='figure'),
              [dash.dependencies.Input('second_page_dropdown', component_property='value')])
def page_1_dropdown(value):
    with open("Country lon and lat.csv") as ln:
        for line in ln:
            line = line.split(",")
            if(line[3].strip() in value):
                latitude = float(line[1])
                longitude = float(line[2])
                break
    eachfig = go.Figure(data=go.Choropleth(
        locations = df["Code"],  # 標國家位置用三碼表示
        text = df["text"],
        z = df["Cumulative_cases"],  # 分佈數據
        zauto=True,
        colorscale = "purpor",
        autocolorscale=False,
        reversescale=False,
        marker_line_color="darkgray",
        marker_line_width=0.5,
        #colorbar_title = "Confirmed Cases",
    ))

    eachfig.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,
            projection_type="equirectangular",
        ),
    )
    eachfig.update_layout(geo=dict(bgcolor= "whitesmoke"),
                          margin=dict(l=0, r=50, t=100, b=0,pad=0)
    )
    eachfig.update_layout(
        title="<b>Confirmed Map<b>", titlefont=dict(
        size=22, color="#7f7f7f"), #設定標題名稱、字體大小、顏色
        height=500,
        width=1000,
    )
    eachfig.update_geos(center=dict(lon=longitude, lat=latitude),
                        lataxis_range=[latitude-40,latitude+40],
                        lonaxis_range=[longitude-40, longitude+40],
    )
    cumulative = {}
    cumulativeDeath = {}
    with open("WHO-COVID-19-global-data.csv") as data:
        for line in data:
            line = line.split(",")
            if(line[2] == value):
                if(line[0] not in cumulative):
                    cumulative[line[0]] = int(line[4]) if int(line[4]) > 0 else 0
                    cumulativeDeath[line[0]] = int(line[6]) if int(line[6]) > 0 else 0
                else:
                    cumulative[line[0]] += int(line[4]) if int(line[4]) > 0 else 0
                    cumulativeDeath[line[0]] += int(line[6]) if int(line[6]) > 0 else 0        
    cumulative = sorted(cumulative.items(), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
    cumulativeDeath = sorted(cumulativeDeath.items(), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
    date = []
    total =[]
    totalDeathList = []
    totalCases = 0
    for i in range(len(cumulative)):
        date.append(cumulative[i][0])
        total.append(cumulative[i][1])
        totalCases += int(cumulative[i][1]) if int(cumulative[i][1]) > 0 else 0
        totalDeathList.append(cumulativeDeath[i][1])
    labels = ['Country Confirmed','World Confirmed']
    values = [totalCases / world_total_confirmed, 1 - totalCases / world_total_confirmed]
    colors=["rgb(253,218,236)","#9467BD"]
    piefig = go.Figure(data=[go.Pie(labels=labels, values=values,
                                 hole=.50)])
    piefig.update_traces(marker=dict(colors=colors))
    piefig.update_layout(title='<b>Percent of confirmed cases<b>', titlefont=dict(size=22, color='#7f7f7f'), #設定標題名稱、字體大小、顏色
                       height=500
                      ),
    linefig = go.Figure(
        data=[
            go.Scatter(
                x=date,
                y=total,
                mode="lines",
                line = dict(color = "purple"),
                fillcolor="blue",
            )
        ],
        layout=go.Layout(
            title="<b>Daily New Cases<b>", titlefont=dict(
            size=22, color="#7f7f7f")
        )
    )

    linefig.update_traces(marker_line_colorscale="ylgn", showlegend=True, selector=dict(type="scatter"), name="New")
    linefig.update_layout(plot_bgcolor="whitesmoke")
    linefig.update_layout(modebar_bgcolor="black", margin=dict(l=20, r=50, t=100, b=50,pad=0))
    lineDeathfig = go.Figure(
        data=[
            go.Scatter(
                x=date,
                y=totalDeathList,
                mode="lines",
                line = dict(color = "purple"),
                fillcolor="blue",
            )
        ],
        layout=go.Layout(
            title="<b>Daily Death Cases<b>",
            titlefont=dict(size=22, color="#7f7f7f"
            )
        )
    )
    lineDeathfig.update_traces(marker_line_colorscale="ylgn", showlegend=True, selector=dict(type="scatter"), name="Death")
    lineDeathfig.update_layout(plot_bgcolor="whitesmoke")
    lineDeathfig.update_layout(modebar_bgcolor="black",margin=dict(l=20, r=50, t=100, b=50,pad=0))
    return eachfig, piefig, linefig, lineDeathfig
    

# Update the index
@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1_layout
    else:
        return home_page

if __name__ == "__main__":
    app.run_server(debug=True)
