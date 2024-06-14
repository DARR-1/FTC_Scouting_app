import flet as ft


def makeSubtitle(text, responsive_multiplier):
    subtitle = ft.Container(
        ft.Text(
            text,
            color="#C8C6C6",
            size=24 * responsive_multiplier,
        ),
        margin=22 * responsive_multiplier,
        alignment=ft.alignment.top_left,
    )

    return subtitle
