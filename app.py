import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables ######
myheading = "What's your favorite Donut from YES! Donut's, your local donut store ?"
mytitle = "Top 3 Flavors"
mylabels = ['Blueberry donut cake', 'Chocolate nut donut', 'Glazed donut']
myvalues = [20,50,30]
color1 = '800080'
color2 = '964B00'
color3 = 'CDAB87'
tabtitle = 'YES Donuts'
sourceurl = 'https://brandpalettes.com/dunkin-donuts-color-codes/'
githublink = 'https://github.com/Malathy-Muthu/103-dunkin-donuts'

########### Set up the chart
mydata = go.Pie(
    hole=0.5,
    sort=False,
    values=myvalues,
    labels=mylabels,
    marker={'colors': [color1, color2, color3],
            'line': {'color': 'white', 'width': 5}}
)
mylayout = go.Layout(
    title = mytitle
)
fig = go.Figure(data=[mydata], layout=mylayout)

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()
