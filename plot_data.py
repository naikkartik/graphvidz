import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as po 
import plotly.graph_objs as go
import dash_table
import numpy as np 
import pandas as pd 
import base64
import io
plot_layout=html.Div(className='nav-div',children=[
				html.Nav(className='nav',
                children=[
                    
                    html.Ul(
                        className='main-ul',
                       children= [
                            html.Li(html.A('Graphvidz',href='#')),
                            
                            html.Li(html.A('Visualize',href='#')),
                            html.Li(html.A('learn',href='/learn')),
                            html.Li(html.A('About Me',href='#'))
                        ]
                    )
                ]
            ),
            html.Div(
                className='instr',children=[
                    html.H2('Upload a csv file to visualize your data'),
                ],style={'color':'grey','textAlign':'center'}
            ),

            ####dcc component to upload the csv file 
            dcc.Upload(
                id='upload_csv',
                children =html.Div([
                    'Drag or Drop the File ',
                    html.A('Select the Files'),

                ]),
                style={
                    'width':'100%',
                    'height':'60px',
                    'lineHeight':'60px',
                    'borderWidth':'1px',
                    'borderStyle':'dashed',
                    'borderRadius':'5px',
                    'textAlign':'center',
                    'margin':'10px'
                }
            ),
            html.Div([
                html.H2('upload file in csv format to generate some of the statistically important plot '),
                html.H2('The app currently unable to clean your data. So cleaned data would result in clean graph'),
                html.H2('If you are unfamiliar with these plot,then there is a learning section to give a basic intro to graph'),
                html.H2('''.
                Due to free trail deployement in heroku the worker timeout is only 30 sec. So the app will not 
                able to plot graph for large file''')
            ],style={'color':'grey','textAlign':'center'}),
            html.Div(id='output-data'),
            html.Div(id='head_data'),
           

]
)



