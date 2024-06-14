import flet as ft

from Utils.FletRouter import Router


def main(page: ft.Page):

    def onResize(e):
        print("resized")
        my_router.onPageResize()
        page.controls[0] = my_router.body
        page.update()

    page.scroll = ft.ScrollMode.HIDDEN
    page.bgcolor = "#141313"
    page.theme_mode = "dark"

    my_router = Router(page, ft)

    page.on_rute_change = my_router.route_change

    page.on_resize = onResize

    page.controls.append(my_router.body)

    print(page.width)
    page.go("/Database")


ft.app(target=main, assets_dir="Assets", view=ft.AppView.FLET_APP)
