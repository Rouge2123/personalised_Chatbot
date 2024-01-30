import flet as ft


class UserMessage(ft.Container):
    def __init__(self, message):
        super().__init__(
            content=ft.Text(message),
            bgcolor=ft.colors.BLUE,

        )
        self.message = message


welcome_message = ft.Row(
    alignment=ft.MainAxisAlignment.CENTER,
    controls=[
        ft.Container(
            bgcolor=ft.colors.with_opacity(1, ft.colors.YELLOW_700) if ft.ThemeMode.LIGHT==False & ft.ThemeMode.DARK==True else ft.colors.with_opacity(0.5, ft.colors.BLUE_500),
            border_radius=10,
            padding=15,
            width=470,
            height=110,
            content=ft.Text(
                "Hi, I am your personal assistant. :)\n"
                "At the moment I can only search and play songs.\n"
                "Want to try me? Use the Textfield below!",
                size=18,
                text_align=ft.TextAlign.CENTER
            ),
        )
    ]
)
