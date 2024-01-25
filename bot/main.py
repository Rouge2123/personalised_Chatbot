import flet as ft


def main(page: ft.Page):
    page.title = "Personalised Chatbot"
    # page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT

    def handle_theme_mode_change(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.appbar.bgcolor = ft.colors.BLUE
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.appbar.bgcolor = ft.colors.GREEN
        page.update()

    page.window_always_on_top = True
    page.appbar = ft.AppBar(
        title=ft.Text("Personalised Chatbot"),
        actions=[ft.IconButton(ft.icons.WB_SUNNY_OUTLINED, icon_size=30, on_click=handle_theme_mode_change)],
        # bgcolor=ft.colors.BLUE
    )

    page.add(
        ft.Container(
            expand=True,
        ),
        ft.Row(
            controls=[
                ft.TextField(
                    label="Enter text",
                    expand=True,
                ),
                ft.IconButton(ft.icons.SEND, icon_size=30, bgcolor=ft.colors.BLUE),
            ],

        )
    )


ft.app(target=main)
