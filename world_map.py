import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('output.csv')

df["text"] = "Country: " + df["Country"]  # 設定要輸出的文字
world_map_fig = go.Figure(data=go.Choropleth(
    locations = df["Code"],  # 標國家位置用三碼表示
    text = df["text"],
    z = df["Cumulative_cases"],  # 分佈數據
    zauto=True,
    colorscale = "purpor",
    autocolorscale=False,
    reversescale=False,
    marker_line_color="darkgray",
    marker_line_width=0.5,
))

world_map_fig.update_layout(
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type="equirectangular",
        bgcolor= "whitesmoke",
    ),
    #設定標題名稱、字體大小、顏色
    title="<b>Confirmed Map<b>",
    titlefont=dict(
        size=22,
        color="#7f7f7f",
    ),
    # 插入CNN連結
    annotations = [dict(
        x=0.5,
        y=0.1,
        xref="paper",
        yref="paper",
        text="<a href='https://edition.cnn.com/search?q=covid'>CNN News(click)</a>",
        font = dict(size = 24)
    )],
    height=500,
    width=1000,
    margin=dict(l=0, r=50, t=100, b=0,pad=0),
)