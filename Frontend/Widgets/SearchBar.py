import flet as ft


def makeSearchBar(controls, help_text, responsive_multiplier):
    bar_search = ft.Container(
        ft.Row(
            [
                ft.SearchBar(
                    controls=controls,
                    bar_hint_text=help_text,
                    height=65 * responsive_multiplier,
                    width=469 * responsive_multiplier,
                    bar_bgcolor="#211521",
                    bar_trailing=[
                        ft.Container(
                            ft.Image(src=f"Icons/Search.png"),
                            margin=ft.margin.only(right=21 * responsive_multiplier),
                            height=36.79 * responsive_multiplier,
                        )
                    ],
                    view_hint_text_style=ft.TextStyle(size=22 * responsive_multiplier),
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        margin=ft.margin.only(bottom=10 * responsive_multiplier),
    )

    return bar_search
