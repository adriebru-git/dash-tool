from __future__ import annotations

from dash import Dash
from layout import basic_layout


app = Dash()
app.layout = basic_layout()

if __name__ == "__main__":

    app.run(debug=True)
