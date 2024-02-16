# Grading Criteria Programmieren T3INF1004

In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10 Punkte)

- Algorithmen Beschreibung (2 Punkte): Code enthält spezifische Algorithmen, wie beispielsweise die Suche nach Songs (`list_songs`) und die Verwaltung von Musikdateien (`download_music`). Diese Algorithmen sind effektiv beschrieben und umgesetzt.

- Datentypen (2 Punkte): verschiedene Datentypen wie Strings, Listen und Dictionaries im Code verwendet. Ein Beispiel ist die Verwendung von Listen in der Funktion `list_songs`, um Songs zu strukturieren.

- E/A-Operationen und Dateiverarbeitung (2 Punkte): In der Funktion `download_music` werden E/A-Operationen durchgeführt, um Musikdateien herunterzuladen und zu speichern. Auch die Funktionen in `utils.py` zeigen Dateiverarbeitung.

- Operatoren (1 Punkt): verschiedene Operatoren wurden im Code verwendet, wie zum Beispiel den Mitgliedschaftsoperator (`in`) in der Bedingung `if user_input:` in der Funktion `handle_input_submit`.

- Kontrollstrukturen (1 Punkt): Code enthält verschiedene Kontrollstrukturen wie `if`, `else` und `for` in der Funktion `list_songs`. Diese zeigen, wie wir den Programmfluss kontrollieren.

- Funktionen (1 Punkt): Code demonstriert die Verwendung von Funktionen, sowohl vordefinierte (z.B., `os.makedirs`, `os.path.join`) als auch selbst definierte Funktionen (z.B., `main`, `list_songs`, `download_music`).

- Stringverarbeitung (1 Punkt): Die Verarbeitung von Strings ist im Code zu sehen, insbesondere in der Funktion `list_songs`, wo wir Strings für Songinformationen verwenden.

- Strukturierte Datentypen (1 Punkt): strukturierte Datentypen wie Listen und Dictionaries wurden verwendet, um Daten zu organisieren und zu speichern, z.B., in der Funktion `list_songs`.

# Sie können die Syntax und Semantik von Python (10)

- Verwendung von Lambda-Funktionen (2 Punkte): Lambda-Funktionen wurden verwendet, beispielsweise in den Funktionen `page.on_error`, `page.window_always_on_top`, `page.padding`, `page.horizontal_alignment`, usw. Dies zeigt ein Verständnis für die syntaktischen Konstruktionen von Lambda-Funktionen in Python.

- Korrekte Verwendung von Funktionen und Methoden (3 Punkte): verschiedene Funktionen und Methoden von externen Bibliotheken wie `flet`, `music`, `os`, `PyTube`, und `YTMusic` wurden verwendet. Dies zeigt ein Verständnis für die semantischen Aspekte dieser Funktionen und Methoden.

- Einsatz von List Comprehension (2 Punkte): In der Funktion `list_songs` wurde eine `for`-Schleife in Form von List Comprehension für die Verarbeitung von Songs verwendet. Dies zeigt ein Verständnis für die syntaktische Konstruktion von List Comprehensions in Python.

- Korrekter Einsatz von Kontrollstrukturen (3 Punkte): bedingte Anweisungen (`if`, `else`) und Schleifen (in der Funktion `list_songs`) wurden verwendet, was unser Verständnis für die semantischen Aspekte dieser Kontrollstrukturen zeigt.

Ein besonderer Teil unseres Programms ist der Umgang mit dem Thema Mode (die Hintergrundfarbe - dunkel/hell). Dies war uns sehr wichtig.

```python
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
```

Ebenso wie das Herunterladen der angeforderte Musik von Youtube, die Hauptfunktion in unserem Programm:

```python
def download_music(video_id, file_name: str):
    video_url = 'http://youtube.com/watch?v=' + str(video_id)
    yt = YouTube(video_url)

    # search and get the first stream - with audio only
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    # Download and save music
    stream.download(
        output_path="cache/",
        filename=f"{file_name}.mp4"
    )
```

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

![Contributors from GIT insights](git_contributers.png)
Der Großteil wurde zusammen in Präsenz programmiert und besprochen.

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10 Punkte)

- Verwendung von Listen (3 Punkte): In der Funktion `list_songs` verwenden wir eine Liste (`all_songs['songs']`) zur Strukturierung von Songs. Die Liste enthält Dictionaries, die Informationen über jeden Song enthalten. Diese zeigen, dass wir Listen effektiv für die Strukturierung von Daten einsetzen können.

- Verwendung von Dictionaries (3 Punkte): In der Funktion `search_song` erstellen wir ein Dictionary (`songs_dict`), um die Suchergebnisse zu speichern. Die Schlüssel-Wert-Paare enthalten Informationen über Titel, Künstler, Video-ID, Dauer und ob es sich um eine explizite Version handelt. Diese zeigen, dass wir Dictionaries als Datenstruktur nutzen können.

- Manipulation von Datenstrukturen (2 Punkte): In der Funktion `list_songs` erstellen wir dynamisch Listen und Container, die dann der `chat_history` hinzugefügt werden. Das zeigt, dass wir Datenstrukturen verwenden können um diese zu manipulieren und für die Benutzeroberfläche darzustellen.

- Effektive Datensuche (2 Punkte): Die Funktion `search_song` durchsucht die Suchergebnisse und erstellt ein Dictionary mit relevanten Informationen. Das zeigt, dass wir in der Lage sind, Datenstrukturen zu iterieren und relevante Informationen zu extrahieren.

## METHODENKOMPETENZ (10 Punkte)

# Die Studierenden können eine Entwicklungsumgebung verwenden um Programme zu erstellen (10)

- Git
  https://github.com/Rouge2123/personalised_Chatbot/tree/main

- VSC
  2/3 haben VSC für das Projekt benutzt

- Copilot
  ![Copilot beweis](Copilot.png)

- other
  1/3 hat PyCharm als IDE benutzt

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)

-> Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person)

Henri: Habe bei der Flet-Installation geholfen

# Sie können existierenden Code analysieren und beurteilen. (5)

<!-- Pro Gruppe:You have critiqued another group project. Link to your critique here (another wiki page on your git) and link the project in the critique, use these evaluation criteria to critique the other project. Make sure they get a top grade after making the suggested changes -->

Ja - Link: https://github.com/laraanastasia/Phylia

- [Grading Criteria from other group](grading_pylia.md)

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

<!-- Which technology did you learn outside of the teacher given input -->

Externe Python-Bibliotheken wie Flet (die auf Flutter basiert) und YTMusic.

-> Did you or your group get help from someone in the classroom (get a support message here from the person who helped you)
No

## ÜBERGREIFENDE HANDLUNGSKOMPETENZ (30 Punkte)

# Die Studierenden können eigenständig Problemstellungen der Praxis analysieren und zu deren Lösung Programme entwerfen (30)

<!-- Which parts of your project are you proud of and why (describe, analyse, link) -->

```python
ft.IconButton(
                icon=ft.icons.WB_SUNNY if page.theme_mode == ft.ThemeMode.DARK else ft.icons.WB_SUNNY_OUTLINED,
                icon_size=30,
                on_click=handle_theme_mode_change,
                tooltip="Switch Theme",
            )
```

Mit dem Button haben wir versucht, den Theme-Mode (siehe Screenshot in vorheriger Frage) in Dark-Mode und Light-Mode zu switchen und gleichzeitig das passende Icon dazu. Das war uns als Gruppe wichtig und es hat auch funktioniert.

Passend dazu wollten wir unsere Hintergrundfarben entsprechend dem Theme-Mode anpassen, um unser Layout schlicht zu halten.

```python
bgcolor = ft.colors.with_opacity(0.5, ft.colors.YELLOW_700) if page.theme_mode == ft.ThemeMode.LIGHT else ft.colors.with_opacity(0.5, ft.colors.BLUE_700)
```

Auch unsere “Welcome-Message” haben wir dementsprechend angepasst.

```python
 utils.welcome_message(constants.DARK_THEME_MODE_COLOR if page.theme_mode == ft.ThemeMode.DARK else constants.LIGHT_THEME_MODE_COLOR)
```

<!-- Where were the problems with your implementation, timeline, functionality, team management (describe, analyse, reflect from past to future, link if relevant) -->

1/3 der Gruppe hatte Probleme mit der Installation von Flet, wofür etwas Zeit verloren gegangen ist.
