import flet as ft
from Widgets.OptionSubtitle import geOptionSubtitle
from math import pi

appbar = None


def dataView(page, ft=ft):

    text = "Teleoperated"
    responsive_multiplier = page.width / 1200
    database = "juan"

    content = ft.Container(
        ft.Column(
            [
                ft.Stack(
                    [
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Image(
                                        src=f"Icons/back.png",
                                        height=24 * responsive_multiplier,
                                    ),
                                    geOptionSubtitle(text, responsive_multiplier, 32),
                                    ft.Image(
                                        src=f"Icons/check.png",
                                        height=24 * responsive_multiplier,
                                    ),
                                ],
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                            ),
                            width=page.width,
                        ),
                        ft.Container(
                            ft.Row(
                                [
                                    ft.Image(
                                        src=f"Images/field2023.png",
                                        width=1126.22 * responsive_multiplier,
                                    )
                                ],
                                alignment=ft.MainAxisAlignment.CENTER,
                            ),
                            margin=ft.margin.only(top=46 * responsive_multiplier),
                        ),
                    ],
                ),
                ft.Row(
                    [
                        ft.Container(
                            content=ft.Text(
                                "Winner",
                                color=ft.colors.BLUE,
                                size=48 * responsive_multiplier,
                            ),
                            width=207 * responsive_multiplier,
                            alignment=ft.alignment.center,
                        ),
                        geOptionSubtitle(
                            f"Actual Database : {database}", responsive_multiplier, 20
                        ),
                        ft.Container(
                            content=ft.Text(
                                "Winner",
                                color=ft.colors.RED,
                                size=48 * responsive_multiplier,
                            ),
                            width=207 * responsive_multiplier,
                            alignment=ft.alignment.center,
                        ),
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        height=page.height - 40 * responsive_multiplier,
        # rotate=ft.Rotate(angle=pi / 2, alignment=ft.alignment.center),
    )

    return content
