import flet as ft
import music
import utils


def main(page: ft.Page):
    page.title = "Personalised Chatbot"
    page.theme_mode = page.platform_brightness
    song_state = "stopped"
    song_control_id = None

    page.window_always_on_top = True

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
            page.appbar.bgcolor = ft.colors.with_opacity(1, ft.colors.YELLOW_700)
            page.appbar.actions[0].icon = ft.icons.WB_SUNNY_OUTLINED

        else:
            page.theme_mode = ft.ThemeMode.DARK
            page.appbar.bgcolor = ft.colors.with_opacity(0.5, ft.colors.BLUE_700)
            page.appbar.actions[0].icon = ft.icons.WB_SUNNY
        page.update()

    def handle_input_submit(e):
        user_input = chat_input_field.value
        if chat_input_field.value:  # check if input is not empty
            chat_history.controls.append(ft.Text(f"Searching for: {user_input}", size=18))  # add input to chat history
            page.update()
            list_songs(user_input)  # update chat history by listing the songs corresponding to the search input
            chat_history.scroll_to(offset=-1, duration=2000)  # scroll to the bottom

    def play_pause_song(e):
        nonlocal song_state, song_control_id
        print(f"EventControlID: {id(e.control)}")
        if song_control_id == id(e.control):
            print("same control")
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
            print("new control")
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
        print(f"Position: {(int(e.data) / song.get_duration()) if song.get_duration() and song.get_duration() != 0 else 0}")


    def list_songs(search_term):
        all_songs = music.search_song(search_term)

        songs_column = ft.Column(spacing=7)

        for s in all_songs['songs'][:3]:
            item = ft.Container(
                content=ft.Row(
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
                                ft.Text(s['name'], size=13),
                                ft.Text(
                                    f"{s['duration']} - {s['isExplicit']}{s['artists']}",
                                    size=11
                                ),
                            ]
                        )
                    ]
                )
            )
            songs_column.controls.append(item)

        chat_history.controls.append(songs_column)
        page.update()

    # Audio
    song = ft.Audio(
        src=music.get_audio(),
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
        controls=[utils.welcome_message],
    )

    chat_input_field = ft.TextField(
        label="Welche Musik möchtest du jetzt abspielen?",
        expand=True,
        on_submit=handle_input_submit,
    )

    page.add(
        ft.Container(
            expand=True,
            content=chat_history
        ),
        ft.Row(
            controls=[
                chat_input_field,
                ft.IconButton(ft.icons.SEND, icon_size=30, on_click=handle_input_submit),
            ],

        )
    )


ft.app(target=main, assets_dir="cache")
