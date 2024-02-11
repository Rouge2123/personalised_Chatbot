import random
import flet as ft
import music
import utils
import constants


def main(page: ft.Page):
    page.title = "Musik Chatbot"
    page.theme_mode = page.platform_brightness
    song_state = "stopped"
    song_control_id = None
    page.on_error = lambda e: print(f"Error: {page.data}")
    page.padding = ft.padding.only(top=5)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_always_on_top = True
    page.window_min_width, page.window_min_height = 536.0, 442.0
    page.splash = ft.ProgressBar(color=ft.colors.RED_400, visible=False)
    last_play_pause_button = None

    # music.create_cache()

    def handle_theme_mode_change(e):
        """
        Function to handle the theme mode change.

        Explanation:
        This code defines a function to handle the change of theme mode.
        If the current theme mode is dark, it switches to light mode and updates the appbar color and icon.
        If the current theme mode is light, it switches to dark mode and updates the appbar color and icon.
        Finally, it updates the page to render the changes visually.
        """
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
            page.appbar.bgcolor = constants.LIGHT_THEME_MODE_COLOR
            page.appbar.actions[1].icon = ft.icons.WB_SUNNY_OUTLINED
            chat_history.controls[0].controls[0].bgcolor = constants.LIGHT_THEME_MODE_COLOR
            send_button.bgcolor = constants.LIGHT_THEME_MODE_COLOR
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.appbar.bgcolor = constants.DARK_THEME_MODE_COLOR
            page.appbar.actions[1].icon = ft.icons.WB_SUNNY
            chat_history.controls[0].controls[0].bgcolor = constants.DARK_THEME_MODE_COLOR
            send_button.bgcolor = constants.DARK_THEME_MODE_COLOR
        page.update()

    def handle_input_submit(e):
        user_input = chat_input_field.value

        if user_input:  # check if input is not empty
            page.splash.visible = True
            page.update()

            chat_history.controls.append(utils.UserMessage(user_input))  # add input to chat history
            chat_input_field.value = ""
            page.update()
            list_songs(user_input)  # update chat history by listing the songs corresponding to the search input
            chat_history.scroll_to(offset=-1, duration=500)

            page.splash.visible = False
            page.update()

    def play_pause_song(e):
        nonlocal song_state, song_control_id, last_play_pause_button
        if song_control_id == id(e.control):
            if e.control.content.name == ft.icons.PLAY_CIRCLE_ROUNDED:
                e.control.content.name = ft.icons.PAUSE_CIRCLE_ROUNDED
                if song_state == "paused":
                    song.resume()
                elif song_state in ["stopped", "completed", "disposed"]:
                    song.play()
            elif e.control.content.name == ft.icons.PAUSE_CIRCLE_ROUNDED:
                e.control.content.name = ft.icons.PLAY_CIRCLE_ROUNDED
                song.pause()

        else:
            e.control.content = ft.ProgressRing(value=None, stroke_width=2, width=20, height=20)
            e.control.disabled = True
            page.update()

            old_song = song.src
            new_song_name = e.control.data["id"]
            new_song_id = e.control.data["download_id"]
            song_control_id = id(e.control)

            print(f"Requesting: {new_song_name}")

            # Download via videoId, set the new song src
            music.download_music(new_song_id, new_song_name)
            song.release()
            song.src = music.get_audio(new_song_name)
            song.play()

            icon = ft.Icon(ft.icons.PAUSE_CIRCLE_ROUNDED)
            e.control.content = icon
            if last_play_pause_button is None:
                last_play_pause_button = icon
            else:
                last_play_pause_button.name = ft.icons.PLAY_CIRCLE_ROUNDED
                last_play_pause_button = icon
            e.control.disabled = False
            utils.delete_file(old_song)

        page.update()

    def handle_state_change(e):
        nonlocal song_state
        song_state = e.data
        print(f"AudioStatus: {song_state} {song.src}")

    def list_songs(search_term):
        all_songs = music.search_song(search_term)

        songs_column = ft.Column(
            spacing=7,
            controls=[
                ft.Container(
                    padding=ft.Padding(10, 0, 0, 0),
                    content=ft.Text(f"Results for: ", size=14, overflow=ft.TextOverflow.ELLIPSIS, spans=[ft.TextSpan(text=search_term, style=ft.TextStyle(weight=ft.FontWeight.BOLD))]),
                )
            ],
        )

        for s in all_songs['songs'][:3]:
            item = ft.Container(
                content=ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            content=ft.Icon(ft.icons.PLAY_CIRCLE_ROUNDED),
                            on_click=play_pause_song,
                            data={
                                'name': s['name'],
                                'artists': s['artists'],
                                'download_id': s['videoId'],
                                'duration': s['duration'],
                                'id': str(random.randint(1, 10000000))
                            }
                        ),
                        ft.Column(
                            spacing=0,
                            controls=[
                                ft.Text(
                                    s['name'],
                                    size=14,
                                    weight=ft.FontWeight.W_500,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),
                                ft.Text(
                                    f"{s['duration']} - {s['artists']}",
                                    size=12,
                                    overflow=ft.TextOverflow.ELLIPSIS
                                ),
                            ]
                        )
                    ]
                )
            )
            songs_column.controls.append(item)

        chat_history.controls.append(utils.BotMessage(songs_column))
        page.update()

    # Audio
    song = ft.Audio(
        src=music.get_audio(),
        autoplay=True if page.platform not in ["macos", "ios"] else False,
        volume=1,
        balance=0,
        on_state_changed=handle_state_change,
    )

    page.overlay.append(song)
    page.update()
    song.release()

    bgcolor = ft.colors.with_opacity(0.5,
                                     ft.colors.YELLOW_700) if page.theme_mode == ft.ThemeMode.LIGHT else ft.colors.with_opacity(
        0.5, ft.colors.BLUE_700)

    page.appbar = ft.AppBar(
        title=ft.Text("Musik Chatbot"),
        actions=[
            ft.IconButton(
                icon=ft.icons.INFO_OUTLINE,
                icon_size=25,
                tooltip="Info",
                on_click=lambda e: e.page.show_dialog(utils.info_dialog),
            ),
            ft.IconButton(
                icon=ft.icons.WB_SUNNY if page.theme_mode == ft.ThemeMode.DARK else ft.icons.WB_SUNNY_OUTLINED,
                icon_size=30,
                on_click=handle_theme_mode_change,
                tooltip="Switch Theme",
            )
        ],
        bgcolor=bgcolor,
    )

    page.add(
        ft.Container(
            chat_history := ft.ListView(
                controls=[
                    utils.welcome_message(
                        constants.DARK_THEME_MODE_COLOR if page.theme_mode == ft.ThemeMode.DARK else constants.LIGHT_THEME_MODE_COLOR)
                ],
            ),
            expand=True,
            width=600
        ),
        ft.Container(
            padding=ft.Padding(10, 4, 10, 16),
            content=ft.Row(
                controls=[
                    chat_input_field := ft.TextField(
                        label="Search a Song or an Artist",
                        expand=True,
                        on_submit=handle_input_submit,
                        autofocus=True,
                        border_color=ft.colors.BLUE_700,
                        border_radius=ft.border_radius.all(15),

                    ),
                    send_button := ft.FloatingActionButton(
                        icon=ft.icons.SEND,
                        on_click=handle_input_submit,
                        bgcolor=bgcolor
                    ),
                ],
            )
        )
    )


ft.app(
    target=main,
    assets_dir="cache",
    # view=ft.AppView.WEB_BROWSER,
    # port=8551
)
