import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as po 
import plotly.graph_objs as go
import dash_table
import numpy as np 
import pandas as pd 
x =[1,2,3,4,5,6]
y=[5,10,13,43,9,16]
x1 = np.random.randn(100)
y1 =np.random.randn(100)+5
graph1 =go.Scatter(x=x,y=y,mode='lines',marker={'color':'red'})
layout1 =go.Layout(title='Line Plot 1')
graph2 =go.Scatter(x=x1,y=y1,mode='lines',marker={'color':'blue'})
layout2 =go.Layout(title='Line Plot2')

N = 100
x = np.linspace(0, 1, N)
y = np.random.randn(N)
line = go.Scatter(
    x = x,
    y = y,
    marker={'color':'green'}
)
line_layout =go.Layout(title='A sample Line Graph')
df =pd.DataFrame.from_dict({'x':[10,12,30,20,24,53],'y':[56,65,48,85,73,92]})

line2 =go.Scatter(x=df['x'],y=df['y'],mode ='lines+markers',marker={'color':'green','size':15})
layout_line =go.Layout(title='Your Sample Graph.',xaxis=dict(title='x'),yaxis=dict(title='y'))
params = [
    'X','Y']
x1 =[1,3,4,5,6,7,8,9,11]
y1 =[12,13,23,16,25,32,56,92,87]
df1 = pd.DataFrame.from_dict({'x':x1,'y':y1})

layoutline1 = html.Div(className ='nav_div',children=[

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
		html.H1('Line Plot',style={'color':'red'}),
		html.P('''A line chart or line plot or line graph is a 
			type of chart which displays information as a series of data points 
			called 'markers' connected by straight line segments. It is a basic type of chart common in many fields.
			In line graph data points are plotted and connected by a line in a "dot-to-dot" fashion.
			The line graph is a powerful visual tool for marketing, finance, and other areas.Here are some of the coolest line plot''',
			style={'padding-right':'5%','padding-left':'5%'}),
		dcc.Graph(id='graph1',figure={'data':[graph1],'layout':layout1}),
		html.P('The above graph shows five points plotted and connected with straight line'),
		dcc.Graph(id='graph2',figure={'data':[graph2],'layout':layout2}),
		html.P('Oh My God!!.Is it a lineplot?.The number data points increased with a high level of randomness.'),
		dcc.Graph(id='graph3',figure={'data':[line],'layout':line_layout}),
		html.H3('How to Create Your Own line plot?',style={'color':'red'}),
		html.P('Lets learn it using a example'),
		html.H4('Dataset for Graph',style={'color':'red'}),
		html.P('For creating a line plot we need the dataset.And here is our dataset.'),
		html.Div([dash_table.DataTable(
			        id='scatter-plot',
			        columns=(
			            
			           [{"name":i,"id":i} for i in df.columns]
			        ),
			        data=df.to_dict("rows"),
			        
			    )],style={'padding-left':'15%','padding-right':'15%'}),
		html.H4('Range of Data',style={'color':'red'}),
		html.P('Second step is to find the range of the data(both x and y).We have a range of 10-53 for x and 48-92 for y'),
		html.H4('Deciding the Scale',style={'color':'red'}),
		html.P('''
			Now you have to decide the scale.i encourage you to start with the horizontal scale. If you are using graph paper, 
			then, assume 1 unit on the graph paper equal 1 unit of the values you are graphing. Determine whether 
			the greatest value will fit on 
			the graph. If it doesn't, 
			then change the scale and try again.Repeat the same process for y-axis is too'''),
		html.H4('Labelling the Graph',style={'color':'red'}),
		html.P('''To label the graph count the number of division,calculate the range and divide the range by number of division.
			Finnally assign the result to each division'''),
		html.H4('Plotting the point',style={'color':'red'}),
		html.P('Now connect all the point with straight line sequence wise.'),
		html.P('Here is your sample line plot.'),
		dcc.Graph(id ='graph4',figure={'data':[line2],'layout':layout_line}),
		html.H3('Enter your data and plot your line graph',style={'color':'red'}),
		html.P('Put your Data in the table and see live plot of line'),
		html.Div([dash_table.DataTable(
			        id='line-plot',
			        columns=(
			            
			            [{"name":i,"id":i} for i in df1.columns]
			        ),
			        	data=df1.to_dict("rows"),
			        editable=True
			    )],style={'padding-left':'10%','padding-right':'10%'}),
			    dcc.Graph(id='lineplot1'),

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