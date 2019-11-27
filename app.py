import dash
import dash_core_components as dcc
import dash_html_components as html
import  plotly.offline as po
import plotly.graph_objs as go
from bar import bar_layout
from dash.dependencies import Input,Output,State
import numpy as np 
import pandas as pd 
import random
from scatter import scatter_layout
from line import layoutline1
from histogram import histogram_layout
from piechart import piechart_layout
from plot_data import plot_layout
import base64
import datetime
import io
import dash_table
import plotly.express as px
app = dash.Dash(__name__)
server = app.server
app.title = 'Graphs for beginner'
app.config['suppress_callback_exceptions']=True

text ="""Data is very important in this era.It is the only way of information for mankind.But all the data available are
 in raw form,raw form means unorganized form.As we know the quickest way of understanding these data is graphs.So,this 
  web app consist of basic knowledge of these plots.Here you can learn about the plot,use your sample data to plot your graph
  for your activity """

bar_graph =""" Bar graph  is a display of information using bars of uniform width, their heights
being proportional to the respective values.Bar Graph is a informative way to disply categorical data.To learn more about the it
 visit the link below."""



x =['dhoni','virat','rohit','dhawan','jadeja','sachin','sehwag','rahul']
y=[12,13,45,10,50,30,8]
bar1 =go.Bar(x=x,
			y=y,
			text=x+['`s total century ={}'.format(y)],
			marker=dict(color='green'))
layout = go.Layout(title='bar graph',xaxis=dict(title='player name'),yaxis=dict(title='statistics'))
app.layout =html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

#scatter plot example 
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)

scatter =go.Scatter(x=x,y=y,mode='markers',marker={'color':'red','size':10})
layout_scatter =go.Layout(title='Scatter Plot example',xaxis=dict(title='x'),yaxis=dict(title='y'))

#line plot 
N = 100
x = np.linspace(0, 1, N)
y = np.random.randn(N)
line = go.Scatter(
    x = x,
    y = y,
    marker={'color':'red'}
)
line_layout =go.Layout(title='A sample Line Graph')
#histogram
data_hist =[20,12,34,23,45,56,33,45,66,45,33,45,66,45,77,88,20,50,65,80,36,
			52,65,78,85,52,56,32,78,30,87,65,56,46,34,56]
hist_graph =go.Histogram(x=data_hist,marker={'color':'green'})
hist_layout =go.Layout(title='Sample Histogram',xaxis=dict(title='X'))
values =[4500,2500,1053,500]
labels =['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
pie_chart =go.Pie(labels=labels,values=values)
index_layout = html.Div(className='nav_div',
        children=[
            
            html.Nav(className='nav',
            
                children=[
                    html.Div(className='toggle',children=[html.P('Menu')]),
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
        
        ###intro about the website 
        html.Section(
            className='about-page',
            children=[
                html.P(children='''Graph is a way of expressing your data in terms of different figure.
            	Graph plays significant role in understanding your data in short time.'''),
                html.P(className='data',children=text)
            ]
        ),
        html.Section(
            className='basic-graph',
            children =[
                html.H2(children='Bar Graph'),
                html.P(children =bar_graph),
                dcc.Graph(id ='bar-graph',figure={'data':[bar1],'layout':layout}),
                html.P(html.A('Learn More about Bar Plot',href ='/bar')),
                html.H2('Scatter Plot-Scatter the point'),
            html.P('''A scatter plot is a set of points plotted on a horizontal and vertical axes. 
                Scatter plots are important in statistics because 
                they can show the extent of correlation, if any, between the values of 
                observed quantities or phenomena (called variables).Scatter Plot in Plotly is
                 beatiful to see.Below is an exmaple'''),
            dcc.Graph(id ='scatter1',figure={'data':[scatter],'layout':layout_scatter}),
            html.P(html.A('know more about scatter plot! Click here',href ='/scatter')),
            html.H2('Line Graph or Line Chart'),
            html.P('''A line chart or line graph is a type of visualizaitn which displays information as 
            	a series of data points called 'markers' connected by straight line segments.
                It is one of the beautiful graph to plot and generate information.
            	'''),
            dcc.Graph(id='line_plot',figure={'data':[line],'layout':line_layout}),
            html.P(html.A('Learn More about line plot! Click here',href ='/line')),
            html.H2('Histogram-A Continous bar graph'),
            html.P('''A histogram is a display of statistical information that uses rectangles to show 
            	the frequency of data items in successive numerical intervals of equal size. In the most 
            	common form of histogram, the independent variable is plotted along the horizontal axis and the dependent 
            	variable is plotted along the vertical axis. The data appears as colored or shaded rectangles of variable area.
            	A sample example is shown below'''),
            dcc.Graph(id ='histogram',figure={'data':[hist_graph],'layout':hist_layout}),
            html.P(html.A('know more about Histogram!',href='/histogram')),
            html.H2('Pie Chart'),
            html.P('''Pie chart is a circular representation of your data.This graph shows relationship between a whole and its parts.
            	The whole circle is divided into different sectors.The size of each sector is proportional to the 
            	activity of information it represents. Below is an example of pie chart.'''),
            dcc.Graph(figure={'data':[pie_chart],'layout':go.Layout(title='Sample Pie Chart')}),
            html.P('''The above Pie chart shows composition of the atmosphere.You can clearly see that the sector
            	representing different circle is proportional to the air amounts.To know more about pie chart and learn about it
            	 visit the below link.'''),
            html.P(html.A('Know more about pie chart',href ='/pie_chart')),




            ]
        ),

        html.Section(
            className='footer',
            children=[
                html.P('kartik naik'),
                html.P('email-krtknaik595@gmail.com'),
                html.P('ph: +91-8018665502')
            ]
        )

            
            
            
            


])

@app.callback(Output('page-content','children'),
	[Input('url','pathname')])
def move_path(path_name):
    if path_name=='/bar':
        return bar_layout
    elif path_name=='/line':
        return layoutline1
    elif path_name=='/scatter':
        return scatter_layout
    elif path_name=='/histogram':
        return histogram_layout
    elif path_name=='/learn':
        return index_layout
    elif path_name=='/pie_chart':
        return piechart_layout
    else:
        return plot_layout
@app.callback(Output('bar_graph2','figure'),
                    [Input('input-1-keypress','value'),
                    Input('input-2-keypress','value'),
                    Input('input-3-keypress','value')])
def bar_graph_by_user(min,max,num):
    i =0
    x=[]
    y=[]
    for i in range(num):
        x.append(random.randint(min,max))
        y.append(str(random.randint(min,max)))
    graph =go.Bar(x=x,y=y,marker=dict(color='green'))
    layout_app1 =go.Layout(title='play with the graph')
    return {'data':[graph],'layout':layout_app1}


#bar graph by user 
@app.callback(
    Output('table-editing-simple-output', 'figure'),
    [Input('table-editing-simple', 'data'),
     Input('table-editing-simple', 'columns')])
def display_output1(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    graph3 = go.Bar(x=df['X'],y=df['Y'])
    layout3 =go.Layout(title='Bar Graph of Your Plot')

    return {'data':[graph3],'layout':layout3}

@app.callback(
    Output('table-editing-simple-output1', 'figure'),
    [Input('table-editing-simple1', 'data'),
     Input('table-editing-simple1', 'columns')])
def display_output2(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    trace1 = go.Bar(x=df['Name'],y=df['X'],name='type1')
    trace2 = go.Bar(x=df['Name'],y=df['Y'],name='type2')
    layout3 =go.Layout(title='Bar Graph of Your Plot')

    return {'data':[trace1,trace2],'layout':layout3}

@app.callback(
    Output('table-editing-simple-output2', 'figure'),
    [Input('table-editing-simple2', 'data'),
     Input('table-editing-simple2', 'columns')])
def display_output3(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    trace1 = go.Bar(x=df['Name'],y=df['X'],name='type1')
    trace2 = go.Bar(x=df['Name'],y=df['Y'],name='type2')
    layout3 =go.Layout(title='Bar Graph of Your Plot',barmode='stack')

    return {'data':[trace1,trace2],'layout':layout3}


#function for scatter plot
@app.callback(
    Output('scatterplot1', 'figure'),
    [Input('scatter-plot', 'data'),
     Input('scatter-plot', 'columns')])
def display_output4(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    scatter1 =go.Scatter(x=df['X'],y=df['Y'],mode='markers',marker ={'color':'red','size':'15'})
    layout_scatter=go.Layout(title='Draw your Scatter Plot')

    return {'data':[scatter1],'layout':layout_scatter}

@app.callback(
    Output('scatterplot2', 'figure'),
    [Input('scatter-plot2', 'data'),
     Input('scatter-plot2', 'columns')])
def display_output5(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    scatter2 =go.Scatter(x=df['X'],y=df['Y'],mode='markers+lines',marker ={'color':'red','size':'15'})
    layout_scatter2=go.Layout(title='Draw your Scatter Plot')

    return {'data':[scatter2],'layout':layout_scatter2}
@app.callback(Output('scatterplot3','figure'),
	[Input('scatter3-point','value'),Input('size_of_point','value'),Input('color','value')])
def display_output6(value,size,color):
	x = np.random.randn(value)
	y=np.random.randn(value)
	scatter3 = go.Scatter(x=x,y=y,mode='markers',marker={'color':color,'size':size})
	layout =go.Layout(title='Scatter Plot with large points')

	return {'data':[scatter3],'layout':layout}

@app.callback(
    Output('lineplot1', 'figure'),
    [Input('line-plot', 'data'),
     Input('line-plot', 'columns')])
def display_output5(rows, columns):
    df = pd.DataFrame(rows, columns=[c['name'] for c in columns])
    scatter2 =go.Scatter(x=df['x'],y=df['y'],mode='markers+lines',marker ={'color':'red','size':'15'})
    layout_scatter2=go.Layout(title='your line plot')

    return {'data':[scatter2],'layout':layout_scatter2}

@app.callback(
	Output('output','figure'),
	[Input('input_value','value')])
def display_output7(value):
	x = np.random.randn(value)
	
	graph = [go.Histogram(x=x,marker={'color':'maroon'})]
	layout = go.Layout(title ='Histogram created by using your random number',xaxis=dict(title='x'))
	return {'data':graph,'layout':layout}

@app.callback(
		Output('pie-output1','figure'),
		[Input('pie-input1','value'),
		 Input('pie-input2','value'),
		 Input('pie-input3','value')
		]
		)
def pie_graph1(value1,value2,value3):
	labels =['category1','category2','category3']
	values =[value1,value2,value3]
	graph1 =go.Pie(labels=labels,values=values)
	layout1 =go.Layout(title ='Pie chart 1')
	return {'data':[graph1],'layout':layout1}
@app.callback(
		Output('output2','figure'),
		[
			Input('id1','value'),
			Input('id2','value'),
			Input('id3','value'),
			Input('id4','value'),
			Input('id5','value')
		]
	)
def output_pie(value1,value2,value3,value4,value5):
	values =[value1,value2,value3,value4,value5]
	labels =['category1','category2','category3','category4','category5']
	graph1 =go.Pie(labels =labels,values=values)
	layout1 =go.Layout(title ='Pie chart 2')
	return {'data':[graph1],'layout':layout1}

@app.callback(Output('output-data', 'children'),
              [Input('upload_csv', 'contents')],
              [State('upload_csv', 'filename'),
               State('upload_csv', 'last_modified')])

def file_view(contents,filename,date):
    content_type ,content_string =contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        if 'csv' in filename:
            df = pd.read_csv(
                io.StringIO(decoded.decode('utf-8'))
            )
            head =df.head()
            column = df.columns
            numeric_data = []
            categorical_column =[]
            for i in column:
                if len(df[i].value_counts())<=10:
                    categorical_column.append(i)
                else:
                    numeric_data.append(i)
            #######bar graph #########
            categorical_graph_bar =[]
            for i in range(len(categorical_column)):
                bar_cat = go.Bar(
                    y=df[categorical_column[i]].value_counts(),
                    x= df[categorical_column[i]].value_counts().to_dense().keys(),
                    
                    text="d",
                    marker=dict(
                        line={'width':0.5},
                        color=['red','green','orange','maroon']
                    )
                )
                layoutt = {'title':categorical_column[i]}
                categorical_graph_bar.append(
                    dcc.Graph(
                        id = 'figure-{}'.format(i),
                        figure={
                            'data':[bar_cat],'layout':layoutt
                        }
                    )
                )
            ####piechart #########3
            categorical_graph_pie =[]
            for i in range(len(categorical_column)):
                pie_cat = go.Pie(
                    values=df[categorical_column[i]].value_counts(),
                    labels= df[categorical_column[i]].value_counts().to_dense().keys(),
                    
                )
                layoutt_pie = {'title':categorical_column[i]}
                categorical_graph_pie.append(
                    dcc.Graph(
                        id = 'figure_pie-{}'.format(i),
                        figure={
                            'data':[pie_cat],'layout':layoutt_pie
                        }
                    )
                )  
            ##########continous data representation #############
            ###1 histogram  with dist plot 
            numeric_plot_hist = []
            for i in range(len(numeric_data)):
                hist_plot =go.Histogram(x= df[numeric_data[i]],marker={'color':'purple'})
                hist_layout_g = {'title':numeric_data[i]}
                numeric_plot_hist.append(
                    dcc.Graph(
                        id='numeric-{}'.format(i),
                        figure ={
                            'data':[hist_plot],'layout':hist_layout_g
                        }
                    )
                )
            ###box plot  
            numeric_plot_box = []
            for i in range(len(numeric_data)):
                box_plot_ = go.Box(y = df[numeric_data[i]],boxpoints='outliers',
                marker={
                    'color':'violet'
                })
                layout_box = {'title':numeric_data[i]}
                numeric_plot_box.append(
                    dcc.Graph(
                        id='numeric_box-{}'.format(i),
                        figure ={
                            'data':[box_plot_],
                            'layout':layout_box
                        }
                    )
                )
            #point plot 
            scatter_numeric_plot =[]
            for i in range(len(numeric_data)-1):
                for j in range(i+1,len(numeric_data)):
                    scatter_plot = go.Scatter(x=df[numeric_data[i]],y=df[numeric_data[j]],
                    mode = 'markers',
                    marker = dict(
                    size = 10,
                    color = 'red',
                    
                    ))
                    layout_scatter = {'title':numeric_data[i]+' and '+numeric_data[j]}

                    scatter_numeric_plot.append(
                        dcc.Graph(
                            id='scatt-{}'.format(str(i)+str(j)),
                            figure ={
                                'data':[scatter_plot],'layout':layout_scatter
                            }
                        )
                    )
            
            ##box plot and categorical variable 
            box_categorical_mix =[]
            for i in range(len(numeric_data)):
                for j in range(len(categorical_column)):
                    box_plot_car = go.Box(x=df[categorical_column[j]],y=df[numeric_data[i]]
                    ,marker={
                        'color':'red'
                    })
                    layout_ ={'title':numeric_data[i]+' and '+categorical_column[j]}
                    box_categorical_mix.append(
                        dcc.Graph(
                            id='box_cat-{}'.format(str(i)+str(j)),
                            figure={
                                'data':[box_plot_car],'layout':layout_
                            }
                        )
                    )


                
            



                

    except:
        return html.Div([
                'There was an error while loading the file'
            ])
    return html.Div([
        html.H5('head of the data'),
        dash_table.DataTable(
            data=head.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in head.columns]
        ),

        html.Hr(),  # horizontal line 
        ###show basic statistics of the data 
        html.H3('Univariate plot of your data'),
        html.H3('categorical data'),
        html.Div(categorical_graph_bar),
        html.Div(categorical_graph_pie),
        html.H3('Numeric plot'),
        html.Div(numeric_plot_hist),
        html.Div(numeric_plot_box),
        
        
        ###univariate plot of the data 
        ###multi variate plot of the data 
        html.Div(scatter_numeric_plot),
        html.Div(box_categorical_mix)

        
        
    ])



        



	
if __name__=="__main__":
    app.run_server(debug =True)
