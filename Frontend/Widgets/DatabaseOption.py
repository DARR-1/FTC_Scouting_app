import flet as ft

def makeDatabaseOption(title, description, size, responsive_multiplier):
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
