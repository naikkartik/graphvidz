import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as po 
import plotly.graph_objs as go
import dash_table
import numpy as np 
import pandas as pd 
labels =['Sleep','Home Work','School','Play','Others']
values =[8,4,6,3,3]
pie1 = go.Pie(labels =labels,values=values)
pie1_layout =go.Layout(title ='Pie Chart for Activity of the person')

piechart_layout = html.Div(className ='nav_bar',children=[
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
	
		html.Section(className='basic-graph',children=[
	html.H1('Pie chart',style={'color':'red'}),
	html.P('''Pie chart is a way of representing the data interms of circle.Generally it used to represent the composition of dataset.
		 Pie chart shows the relationship between a whole and its part.The whole 
		 circle is divided into different sector. Where the whole is the total dataset and each sectors
		  represents the composition of the dataset. You can better understand the relation of circle and data by below example'''),

	html.H4('Relation of circle and data',style ={'color':'red'}),
	html.P('Lets assume a person is using his 24 hours of each day as follows:-'),
	html.P('i.Sleep = 8 hours'),
	html.P('ii.Home Work = 4 hours'),
	html.P('iii. School = 6 hours'),
	html.P('iv. Play = 3 hours'),
	html.P('v. Others = 3 hours'),
	html.P('To represent these data in terms of a circle we have to assume that 360 degree(whole circle) represent the total 24 hours'),
	html.P('Each action is a sector of the circle.And the degree of the respective circle is found as follow:-'),
	html.P('degree = (hour for the action/total hour))*360'),
	html.P('So degree of each sector for respective activity are:-'),
	html.P('Sleep =(8/24)*360 =120 degree'),
	html.P('Home Work =(4/24)*360 = 60 degree'),
	html.P('School = (6/24)*360 =90 degree'),
	html.P('Play = (3/24)*360 = 45 degree'),
	html.P('Others = (3/24)*360 = 45 degree'),
	html.P('''Now the final step is to draw the sector inside the circle for 
		these activities.The final circle with different label for each activity is called as pie chart'''),
	html.P('the pie chart would look like this'),
	dcc.Graph(id ='pie1',figure ={'data':[pie1],'layout':pie1_layout}),
	html.H4('The Basic steps to make your pie chart',style ={'color':'red'}),
	html.P('i.Take the dataset and find the composition of it'),
	html.P('ii.Convert the data of each category to degree.'),
	html.P('iii.make all sector with coressponding degree and label these sector.'),
	html.H3('Few example of pie chart',style ={'color':'red'}),
	html.H5('Pie chart1',style ={'color':'red'}),
	html.P('alter the value in the box below to see the automatic plot of the pie chart'),
	html.Div([
		dcc.Input(type ='number',id ='pie-input1',value =100),
		dcc.Input(type='number',id ='pie-input2',value=200),
		dcc.Input(type='number',id='pie-input3',value=300)
		],style={'padding':'5px'}),
	dcc.Graph(id='pie-output1'),

	html.H5('Pie chart 2',style ={'color':'red'}),
	html.P('alter the value in the box below to see the automatic plot of the pie chart'),
	
	html.Div([
		dcc.Input(type ='number',id ='id1',value =100),
		dcc.Input(type ='number',id ='id2',value =200),
		dcc.Input(type ='number',id = 'id3',value =300),
		dcc.Input(type ='number',id ='id4',value=400),
		dcc.Input(type ='number',id='id5',value=500),

		]),
	dcc.Graph(id ='output2'),

	html.P(html.A('Return To Home',href ='/')),




	]),
			html.Section(
            className='footer',
            children=[
                html.P('kartik naik'),
                html.P('email-krtknaik595@gmail.com'),
                html.P('ph: +91-8018665502')
            ]
        )




	])