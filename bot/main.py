import flet as ft
import music
import utils
import constants


def main(page: ft.Page):
    page.title = "Personalised Chatbot"
    page.theme_mode = page.platform_brightness
    song_state = "stopped"
    song_control_id = None
    page.on_error = lambda e: print(e.data)
    page.padding = ft.padding.only(top=5)
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window_always_on_top = True
    page.window_min_width, page.window_min_height = 536.0, 442.0

    music.create_cache()

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
            page.appbar.actions[0].icon = ft.icons.WB_SUNNY_OUTLINED
            chat_history.controls[0].controls[0].bgcolor = constants.LIGHT_THEME_MODE_COLOR
        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.appbar.bgcolor = constants.DARK_THEME_MODE_COLOR
            page.appbar.actions[0].icon = ft.icons.WB_SUNNY
            chat_history.controls[0].controls[0].bgcolor = constants.DARK_THEME_MODE_COLOR
        page.update()

    def handle_input_submit(e):
        user_input = chat_input_field.value

        if chat_input_field.value:  # check if input is not empty
            chat_history.controls.append(utils.UserMessage(user_input))  # add input to chat history
            chat_input_field.value = ""
            page.update()
            list_songs(user_input)  # update chat history by listing the songs corresponding to the search input
            chat_history.scroll_to(offset=-1, duration=500)

    def play_pause_song(e):
        nonlocal song_state, song_control_id
        if song_control_id == id(e.control):
            if e.control.icon == ft.icons.PLAY_CIRCLE_ROUNDED:
                e.control.icon = ft.icons.PAUSE_CIRCLE_ROUNDED
                if song_state == "paused":
                    song.resume()
                elif song_state in ["stopped", "completed", "disposed"]:
                    song.play()
            elif e.control.icon == ft.icons.PAUSE_CIRCLE_ROUNDED:
                e.control.icon = ft.icons.PLAY_CIRCLE_ROUNDED
                song.pause()

        else:
            song_control_id = id(e.control)
            # Release resources and clear cache
            song.release()
            music.resetcache()

            # Download via videoId, set the new song src
            music.dmusic(e.control.data[2])
            song.src = music.get_audio()

            song.play()
            e.control.icon = ft.icons.PAUSE_CIRCLE_ROUNDED

        page.update()

    def check_status(e):
        nonlocal song_state
        print(f"AudioStatus: {e.data}")
        song_state = e.data

    def track_progress(e):
        print(
            f"Position: {(int(e.data) / song.get_duration()) if song.get_duration() and song.get_duration() != 0 else 0}")

    def list_songs(search_term):
        all_songs = music.search_song(search_term)

        songs_column = ft.Column(
            spacing=7,
            controls=[
                ft.Container(
                    padding=ft.Padding(10, 0, 0, 0),
                    content=ft.Text(f"Results for: {search_term}", size=14, overflow=ft.TextOverflow.ELLIPSIS),
                )
            ],
        )

        for s in all_songs['songs'][:3]:
            item = ft.Container(
                content=ft.Row(
                    spacing=0,
                    controls=[
                        ft.IconButton(
                            icon=ft.icons.PLAY_CIRCLE_ROUNDED,
                            icon_size=30,
                            on_click=play_pause_song,
                            data=[s['name'], s['artists'], s['videoId'], s['duration']],
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
        src="https://luan.xyz/files/audio/ambient_c_motion.mp3",
        autoplay=False,
        volume=1,
        balance=0,
        on_state_changed=check_status,
        on_position_changed=track_progress
    )

    page.overlay.append(song)

    page.appbar = ft.AppBar(
        title=ft.Text("Personalised Chatbot"),
        actions=[
            ft.IconButton(
                icon=ft.icons.WB_SUNNY if page.theme_mode == ft.ThemeMode.DARK else ft.icons.WB_SUNNY_OUTLINED,
                icon_size=30,
                on_click=handle_theme_mode_change
            )
        ],
        bgcolor=ft.colors.with_opacity(0.5, ft.colors.YELLOW_700)
        if page.theme_mode == ft.ThemeMode.LIGHT
        else ft.colors.with_opacity(0.5, ft.colors.BLUE_700),
    )

    chat_history = ft.ListView(
        controls=[utils.welcome_message(
            constants.DARK_THEME_MODE_COLOR if page.theme_mode == ft.ThemeMode.DARK else constants.LIGHT_THEME_MODE_COLOR)],
    )

    chat_input_field = ft.TextField(
        label="Search a Song or an Artist",
        expand=True,
        on_submit=handle_input_submit,
    )

    page.add(
        ft.Container(
            expand=True,
            content=chat_history,
            width=600,

        ),
        ft.Row(
            controls=[
                chat_input_field,
                ft.IconButton(ft.icons.SEND, icon_size=30, on_click=handle_input_submit),
            ],

        )
    )
    # chat_history.controls.append(utils.UserMessage("Tiakola"))
    # list_songs("Tiakola")


ft.app(target=main, assets_dir="cache")
