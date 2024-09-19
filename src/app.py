from dash import Dash, html

app = Dash()
server = app.server

app.layout = [html.Div(children='Hello World')]

if __name__ == '__main__':
    app.run(debug=True)
