import flet as ft
from Widgets.Subtitle import makeSubtitle
import math


def geOptionSubtitle(text, responsive_multiplier, size=24, function=None):
    subtitle = makeSubtitle(text, responsive_multiplier, size)

    option_icon = ft.Container(
        ft.Image(
            src=f"Icons/options.png",
            width=size / 32 * 21 * responsive_multiplier,
            height=size / 32 * 10 * responsive_multiplier,
        ),
        margin=ft.margin.only(top=10 * responsive_multiplier),
    )

    option_subtitle = ft.Container(
        ft.Row(
            [subtitle, option_icon],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=None,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
        on_click=function,
    )

    return option_subtitle
