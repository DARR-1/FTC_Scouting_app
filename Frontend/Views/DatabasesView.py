import flet as ft
from User_controls.MenuBar import menuBar
from Widgets.DatabaseOption import makeDatabaseOption
from Widgets.Subtitle import makeSubtitle
from Widgets.SearchBar import makeSearchBar


def databaseView(page, page_width, page_height, ft=ft) -> ft.Column:

    responsive_multiplier = page_width / 540

    print(responsive_multiplier)

    def makeFunctionButtons(title, description, size, func):
        button = ft.Container(
            ft.Column(
                [
                    ft.Text(title, size=20 * responsive_multiplier),
                    ft.Container(
                        ft.Text(
                            description,
                            size=size * responsive_multiplier,
                            color="E7E7E7",
                        ),
                        padding=ft.padding.only(left=12 * responsive_multiplier),
                    ),
                ],
                alignment=ft.MainAxisAlignment.START,
            ),
            height=225 * responsive_multiplier,
            width=225 * responsive_multiplier,
            padding=26 * responsive_multiplier,
            bgcolor="#432547",
            border_radius=25 * responsive_multiplier,
            on_click=func,
            ink=True,
            ink_color="#513a54",
        )

        return button

    databases = ft.Column(
        [
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
                responsive_multiplier,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
                responsive_multiplier,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
                responsive_multiplier,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
                responsive_multiplier,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
                responsive_multiplier,
            ),
        ]
    )

    searchbar = makeSearchBar(
        databases.controls, "Insert the database name", responsive_multiplier
    )

    content = ft.Container(
        ft.Column(
            [
                makeSubtitle(
                    "Choose the database you want to use for the predictions:",
                    responsive_multiplier,
                ),
                searchbar,
                databases,
            ],
            scroll=ft.ScrollMode.HIDDEN,
        ),
        width=page.width,
    )

    page.bottom_appbar = ft.BottomAppBar(
        bgcolor=page.bgcolor,
        content=ft.Column(
            [menuBar(page, page_width)], alignment=ft.MainAxisAlignment.CENTER
        ),
        height=109 * responsive_multiplier,
    )

    return content
