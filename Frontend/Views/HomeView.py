import flet as ft
from User_controls.MenuBar import menuBar
from Widgets.DatabaseOption import makeDatabaseOption
from Widgets.Subtitle import makeSubtitle


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

        return subtitle

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

    content = ft.Container(
        ft.Column(
            [
                makeSubtitle("Welcome back, team 4010", responsive_multiplier),
                main_functions,
                makeSubtitle("Your Databases", responsive_multiplier),
                databases,
            ],
            scroll=ft.ScrollMode.HIDDEN,
        ),
        width=page.width,
    )

    return content
