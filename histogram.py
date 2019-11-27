import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.offline as po 
import plotly.graph_objs as go
import dash_table
import numpy as np 
import pandas as pd 

x = np.random.randn(500)
hist1 =go.Histogram(x=x,marker={'color':'green'})
layout =go.Layout(title='A sample histogram')
x1 = np.random.randn(500)
data = [go.Histogram(x=x1,
                     histnorm='probability',marker={'color':'yellow'})]
layout1 =go.Layout(title='Normally Distributed histogram')
df1 =pd.DataFrame.from_dict({'Observations':['11-20','20-30','30-40'],'Frequency':[5,9,8]})
data1 =[11,11,15,15,16,20,21,23,27,29,24,23,24,28,31,32,32,33,34,34,35,35]
hist_gram = go.Histogram(x=data1,xbins=dict(start=10,end=40,size=10),marker={'color':'orange'})
hist_layout=go.Layout(title='your histogram')



histogram_layout=html.Div(className='nav-div',children=[
				html.Nav(className='nav',
                children=[
                    
                    html.Ul(
                        className='main-ul',
                       children= [
                            html.Li(html.A('Graphvidz',href='#')),
                            
                            html.Li(html.A('Visualize',href='/learn')),
                            html.Li(html.A('learn',href='#')),
                            html.Li(html.A('About Me',href='#'))
                        ]
                    )
                ]
            ),

			html.Section(className='basic-graph',
			children=[html.H2('Histogram',style={'color':'red'}),
				html.P('''A histogram is a bar graph having no gaps between bars. It is used to represent data in intervals. 
					When a large amount of data is given then we can convert it into intervals after which it can be easily 
					analysed through histogram. 
					The bars show the frequency of data. 
					It helps to understand the variations in data. It shows whether the data is symmetry or skewed.Here are 
					some example of histogram.'''),
				dcc.Graph(id='hist1',figure={'data':[hist1],'layout':layout}),
				html.P('''the graph above shows many beans interlinked with each other.the x axis shows 
					the interval of value,while the y axis shows the total count(number of data point in the interval.)'''),
				dcc.Graph(id='hist2',figure={'data':data,'layout':layout1}),
				html.P('''In this case the total count is converted into probabillity.
					i.e (count in interval)/(total count) in y axis,x axis same'''),
				html.H3('Method to plot histogram'),
				html.H4('Data collection',style={'color':'red'}),
				html.P('''It is very important to collect and arrange the data smartly. for this first of 
					all we have to separate the data into different  groups or items or observations. Now we need to 
					count the no of times a particular entry occurs in that group and this is 
					known as frequency. These can be done in different methods. So two of the ways are given below.'''),
				html.H5('Group frequency counts',style={'color':'green'}),
				html.P('''When there is a large  no of data values then we can create a 
					class interval of specific width.Then,calculate the number of value in that interval and 
					 make frequency table For example-'''),
				html.P('''lets say we have the data =(11,11,15,15,16,20,21,23,27,29,24,23,24,28,31,32,
					32,33,34,34,35,35)'''),
				html.P('frequency table is below:-'),
				dash_table.DataTable(
					id='histo-gram',
					columns=(
			            
			            [{"name":i,"id":i} for i in df1.columns]
			        ),
						data=df1.to_dict("rows"),

						style_table={'width':'800px','align':'center'},
						
			        ),
				html.H3('Constructing Histogram',style={'color':'red'}),
				html.P('''Constructing the histogram from above the data is very 
					simple to that of bar graph.you can take your observations or class interval on x-axis and your frequency on y-axis.
					Finally draw the boxes keeping the height of box as the frequency of respective intervals.Yes histogram is the 
					continous bar graph'''),
				html.H4('Here is your finall bar graph'),
				dcc.Graph(id='hist3',figure={'data':[hist_gram],'layout':hist_layout}),
				html.P('''You can see that the above histogram is drawn with three bins.
					Hover over the bin to see the width and count of the bins'''),

			    html.H4('Plot your histogram'),
			    html.P('Enter a value to generate random numbers.That random number will be used to create histogram. '),
				dcc.Input(id='input_value', type='number',value=50),
				dcc.Graph(id ='output'),

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