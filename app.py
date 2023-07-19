import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server  # Connect the Dash app to the Flask server

app.layout = html.Div(
    [
        html.H1("Binonic Reading"),
        html.Div(
            [
                dcc.Textarea(
                    id="input_text",
                    placeholder="Enter text",
                    style={"width": "400px", "height": "200px"},
                ),
                html.Div(id="boldified", style={"marginLeft": "10px"}),
            ],
            style={"display": "flex", "alignItems": "top"},
        ),
    ]
)

@app.callback(
    Output("boldified", "children"),
    [Input("input_text", "value")]
)
def update_boldified_text(input_text):
    if input_text:
        words = input_text.split()
        boldified_words = []
        for word in words:
            boldified_words.append(
                html.Span([html.B(word[: int(0.3 * len(word))]), word[int(0.3 * len(word)) :], " "])
            )
        return html.Div(boldified_words)

if __name__ == "__main__":
    app.run_server(debug=True)
