import plotly.graph_objects as go
from datetime import datetime

cumulative = {}
cumulativeDeath = {}
allTotalConfirmed = 0
with open("WHO-COVID-19-global-data.csv") as data:
    tmp = data.readline()
    for line in data:
        line = line.split(",")
        if line[0] not in cumulative:
            cumulative[line[0]] = int(line[4]) if int(line[4]) > 0 else 0
            allTotalConfirmed += int(line[4]) if int(line[4]) > 0 else 0
            cumulativeDeath[line[0]] = int(line[6]) if int(line[6]) > 0 else 0
        else:
            try:
                cumulative[line[0]] += int(line[4]) if int(line[4]) > 0 else 0
                allTotalConfirmed += int(line[4]) if int(line[4]) > 0 else 0
                cumulativeDeath[line[0]] += int(line[6]) if int(line[6]) > 0 else 0
            except:
                continue     
cumulative = sorted(cumulative.items(), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
cumulativeDeath = sorted(cumulativeDeath.items(), key=lambda x: datetime.strptime(x[0], "%Y-%m-%d"))
lastRecordDate = cumulative[-1][0]
date = []
total =[]
totalDeathList = []
for i in range(len(cumulative)):
    date.append(cumulative[i][0])
    total.append(cumulative[i][1])
    totalDeathList.append(cumulativeDeath[i][1])
world_line_new_fig = go.Figure(
    data=[
        go.Scatter(
            x = date,
            y = total,
            mode = "lines",
            line = dict(color = "purple"),
        )
    ],
    layout=go.Layout(
        title="<b>Total Daily New Cases<b>", titlefont=dict(
        size=22, color="#7f7f7f")
    )
)

world_line_new_fig.update_traces(marker_line_colorscale="ylgn", showlegend=True, selector=dict(type="scatter"), name="New")
world_line_new_fig.update_layout(plot_bgcolor="whitesmoke",
                      modebar_bgcolor="black",
                      margin=dict(l=0, r=50, t=100, b=0,pad=0),
)