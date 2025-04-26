from __future__ import annotations

from dash import html
import dash_mantine_components as dmc

def basic_layout():
    """
    Define the basic layout of the website

    Args: None

    Returns: html Div
    """

    layout = dmc.AppShell(
        [
            dmc.AppShellHeader,
            dmc.AppShellNavbar,
            dmc.AppShellMain
        ]
    )

    return layout
