import flet as ft

from Utils.FletRouter import Router


def main(page: ft.Page):

    page.theme_mode = "light"

    my_router = Router(page, ft)

    page.on_rute_change = my_router.route_change

    page.add(my_router.body)

    page.go("/")


ft.app(target=main, assets_dir="Assets")
