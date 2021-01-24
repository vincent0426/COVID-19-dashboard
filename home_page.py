import dash_html_components as html
import dash_core_components as dcc
from data import *
from world_map import world_map_fig
from world_bar import world_bar_fig
from world_line_new import world_line_new_fig
from world_line_death import world_line_death_fig
home_page = html.Div([
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginRight":".8%"},
            children=[html.P(style={"textAlign":"center",
                                    "fontWeight":"bold",
                                    "color":"purple",
                                    "padding":"1rem",
                                    "fontSize": 20},
                             children="World Total Confirmed Cases"),
                      html.H2(style={"textAlign":"center",
                                     "fontWeight":"bold",
                                     "color":"purple"},
                             children="{:,}".format(world_total_confirmed))],
    ),
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginRight":".8%"},
            children=[html.P(style={"textAlign":"center",
                                    "fontWeight":"bold",
                                    "color":"purple",
                                    "padding":"1rem",
                                    "fontSize": 20},
                             children="World New Cases"),
                      html.H2(style={"textAlign":"center",
                                     "fontWeight":"bold",
                                     "color":"purple"},
                             children="{:,}".format(NewCases))]
    ),
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginRight":".8%"},
            children=[html.P(style={"textAlign":"center",
                                    "fontWeight":"bold",
                                    "color":"purple",
                                    "padding":"1rem",
                                    "fontSize": 20},
                             children="World New Death Cases"),
                      html.H2(style={"textAlign":"center",
                                     "fontWeight":"bold",
                                     "color":"purple"},
                             children="{:,}".format(new_death_cases))]
    ),
    html.Div(
        style={"width":"24.4%", "backgroundColor":"whitesmoke", "display":"inline-block","marginTop":".5%"},
            children=[html.P(style={"textAlign":"center",
                                    "fontWeight":"bold",
                                    "color":"purple",
                                    "padding":"1rem",
                                    "fontSize": 20},
                             children="Total Death / Total Confirmed"),
                      html.H2(style={"textAlign":"center",
                                     "fontWeight":"bold",
                                     "color":"purple",},
                             children="{:.2f}%".format((world_total_death / world_total_confirmed)*100))]
    ),
    html.Div([
        html.Div([
            dcc.Graph(
                id="map",
                figure=world_map_fig,
                style={"margin-left": 0}
            ),

        html.Div(children="Last Updated: {}".format(lastRecordDate),
                 style={"margin-left": 63, "float": "left"}),

        html.Div([
            dcc.Link('Go to each country', href='/page-1', style={"margin-left": 425, "width": 265}),
        ])
        ],
        style={"width": "60%", "float": "left", "display": "inline-block"}),
    ]),

    html.Div([
        html.Div([
            #html.H1(children="Hello Dash"),

            #html.Div(children="""
                #Dash: A web application framework for Python.
            #"""),

            dcc.Graph(
                id="graph2",
                figure=world_bar_fig
            )
        ],
        style={"width": "40%","height": "50%", "float": "right","display":"inline-block"}),
    ]),
    # New Div for all elements in the new "row" of the page
    html.Div([
        html.Div([
            dcc.Graph(
                id="graph3",
                figure=world_line_new_fig
            )
        ],
        style={"width": "30%","float": "left","display":"inline-block"}),    
    ]),
    
    html.Div([
        html.Div([
            dcc.Graph(
                id="graph4",
                figure=world_line_death_fig
            )
        ],
        style={"width": "30%", "display": "inline-block"}),    
    ]),

])