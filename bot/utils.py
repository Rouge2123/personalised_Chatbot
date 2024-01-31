import flet as ft
import constants


class UserMessage(ft.Row):
    def __init__(self, message):
        super().__init__(
            alignment=ft.MainAxisAlignment.END,
            # expand=True
            width=600
        )
        self.controls = [
            ft.Container(
                content=ft.Text(message, size=14, overflow=ft.TextOverflow.ELLIPSIS),
                bgcolor=ft.colors.with_opacity(0.7, ft.colors.YELLOW_700),
                padding=ft.padding.all(10),
                border_radius=ft.BorderRadius(10, 10, 10, 0),
                margin=ft.Margin(0, 15, 10, 10)
            )
        ]


class BotMessage(ft.Row):
    def __init__(self, control):
        super().__init__(
            alignment=ft.MainAxisAlignment.START,
        )
        self.controls = [
            ft.Container(
                content=control,
                bgcolor=constants.DARK_THEME_MODE_COLOR,
                padding=ft.Padding(5, 10, 10, 10),
                border_radius=ft.BorderRadius(10, 10, 0, 10),
                margin=ft.Margin(15, 0, 0, 0)
            )
        ]


def welcome_message(bgcolor):
    return ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                bgcolor=bgcolor,
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
