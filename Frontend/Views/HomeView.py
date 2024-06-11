import flet as ft
from User_controls.MenuBar import menuBar

def homeView(page, ft=ft) -> ft.Column:
    content = ft.Column([menuBar(page)])

    return content
