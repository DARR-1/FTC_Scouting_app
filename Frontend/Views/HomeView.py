import flet as ft
from User_controls.MenuBar import menuBar


def homeView(page, page_width, page_height, ft=ft) -> ft.Column:

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

    def makeSubtitle(text):
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

    def makeDatabaseOption(title, description, size):
        container = ft.Row(
            [
                ft.Container(
                    ft.Column(
                        [
                            ft.Text(title, size=20 * responsive_multiplier),
                            ft.Text(description, size=size * responsive_multiplier),
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    padding=ft.padding.only(left=20.25 * responsive_multiplier),
                    height=179 * responsive_multiplier,
                    width=465 * responsive_multiplier,
                    bgcolor="#271a27",
                    border_radius=20 * responsive_multiplier,
                    alignment=ft.alignment.center_left,
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

        return container

    def goToPrediciton(e):
        page.go("/predictions")

    def goToAllianceGenerator(e):
        page.go("/alliances")

    main_functions = ft.Container(
        ft.Row(
            [
                makeFunctionButtons(
                    "Predictions",
                    "Make accurate predictions for any match.",
                    20,
                    goToPrediciton,
                ),
                makeFunctionButtons(
                    "Alliance Generator",
                    "Don’t know who to choose for your alliance. Use the alliance generator to get your best alliances.",
                    16,
                    goToAllianceGenerator,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
    )

    databases = ft.Column(
        [
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
            ),
            makeDatabaseOption(
                "Public Database",
                "A public database where everyone can colaborate.",
                16,
            ),
        ]
    )

    content = ft.Container(
        ft.Column(
            [
                makeSubtitle("Welcome back, team 4010"),
                main_functions,
                makeSubtitle("Your Databases"),
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
