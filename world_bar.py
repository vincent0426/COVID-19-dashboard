import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('output.csv')

world_bar_fig = go.Figure(data=go.Bar(
        y=df["Country"][:30], #y軸欄位
        x=df["Cumulative_cases"], #x軸欄位
        orientation="h", #調整成橫向
        text=df["Cumulative_cases"], #長條圖上標示資料數值
        textposition = "auto", #長條圖上標示資料數值的位子，有auto、inside、outside可以做設定
        #長條圖顏色設定
        marker=dict(
            color="purple", #長條圖填滿部分顏色設定
            line=dict(color="purple")
        ), #長條圖外框顏色設定
))
#圖表外層設定
world_bar_fig.layout=go.Layout(
    xaxis=dict(
        title="Top 30",
        titlefont=dict(size=18),
        tickfont=dict(
            size=16,
            color="rgb(107, 107, 107)"
        ) #設定X軸名稱、字體大小、顏色
    ),
    yaxis=dict(
        titlefont=dict(
            size=16,
            color="rgb(107, 107, 107)" #設定Y軸字體大小、顏色
        ),
        tickfont=dict(
            size=18,
            color="rgb(107, 107, 107)" #設定Y軸標籤字體大小、顏色
        ),
    ),
    margin=go.Margin(l=0,r=50,b=80,t=100,pad=0,) #調整圖表的位子
)
world_bar_fig.update_layout(
    title="<b>Country total Case<b>",
    titlefont=dict(
        size=22,
        color="#7f7f7f",
    ),
    plot_bgcolor="whitesmoke",
    height=1000,
)
world_bar_fig["layout"]["yaxis"]["autorange"] = "reversed"