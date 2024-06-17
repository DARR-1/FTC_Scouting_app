import flet as ft


def makeSubtitle(text, responsive_multiplier, size=24):
    subtitle = ft.Container(
        ft.Text(
            text,
            color="#C8C6C6",
            size=size * responsive_multiplier,
        ),
        alignment=ft.alignment.top_left,
    )

    return subtitle
