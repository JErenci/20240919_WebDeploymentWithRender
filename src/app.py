from dash import Dash, html

app = Dash()
server = app.server

app.layout = [html.Div(children='Hello World 19 Sept 2024 9h in Sant JoanDespí')]

if __name__ == '__main__':
    app.run(debug=True)
