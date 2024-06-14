import flet as ft


def menuBar(page, page_width, ft=ft) -> ft.Container:

    height_multiplier = 36.5 * (page_width / 540)
    responsive_multiplier = page_width / 540

    menu_row = ft.Row(
        [
            ft.Image(src=f"Icons/Home.png", height=height_multiplier),
            ft.Image(src=f"Icons/Database.png", height=height_multiplier),
            ft.Image(src=f"Icons/Plus.png", height=height_multiplier),
            ft.Image(src=f"Icons/Prediction.png", height=height_multiplier),
            ft.Image(src=f"Icons/Alliances.png", height=height_multiplier),
        ],
        spacing=page_width / 5,
        alignment=ft.MainAxisAlignment.SPACE_AROUND,
        vertical_alignment=ft.CrossAxisAlignment.END,
    )

    return menu_row
