# Grading Criteria Programmieren T3INF1004

In jedem Unterbereich werden die Punkte (gerne auch Links ins GIT) erklärt, wie das LO erreicht worden ist.
Alle Kriterien betreffen nur die Projektarbeit. Beweismaterial kommt aus dem Gruppenprojekt.

## FACHKOMPETENZ (40 Punkte)

# Die Studierenden kennen die Grundelemente der prozeduralen Programmierung. (10)

- Algorithmenbeschreibung: Im vorliegenden Code werden Algorithmen verwendet, um iCal-Daten zu analysieren und Vorlesungsinformationen für einen bestimmten Tag abzurufen.

- Datentypen: Der Code verwendet verschiedene Datentypen wie `datetime`, `date`, `str` und Listen für die Speicherung von Vorlesungsinformationen.

- E/A-Operationen und Dateiverarbeitung: Der Code verwendet E/A-Operationen für HTTP-Anfragen (`requests.get`) und Dateiverarbeitung für den Umgang mit iCal-Daten.

- Operatoren: Es werden verschiedene Operatoren wie Zuweisungsoperatoren, Vergleichsoperatoren und arithmetische Operatoren verwendet.

- Kontrollstrukturen: Der Code enthält Schleifen (z.B. `for`-Schleifen) und bedingte Anweisungen (z.B. `if-else`), um durch Kalenderdaten zu iterieren und Bedingungen zu überprüfen.

- Funktionen: Es gibt Funktionen wie `lecture_data`, `regular_data`, `buttons`, etc., die verschiedene Aufgaben erfüllen, z.B. Abrufen von Vorlesungsinformationen, Erstellen von Buttons usw.

- Stringverarbeitung: Die Verarbeitung von Zeichenketten erfolgt in den Funktionen, um Daten in einem lesbaren Format anzuzeigen.

- Strukturierte Datentypen: Strukturierte Datentypen werden in Form von Dictionaries verwendet, um Vorlesungsinformationen zu speichern und zu organisieren.

# Sie können die Syntax und Semantik von Python (10)

- Korrekte Python-Syntax: Der Code verwendet die richtige Syntax für die Definition von Funktionen, Verzweigungen, Schleifen, Klassen, Methoden und Funktionen aus externen Bibliotheken.

Beispiel:

````python
class embed_buttons(discord.ui.View): ```
- Semantik von Python-Elementen: Der Code zeigt ein Verständnis für die Semantik von Python, da er Funktionen definiert und sie mit den richtigen Parametern aufruft. Zum Beispiel werden die Funktionen `lecture_data`, `regular_data`, `buttons`, etc. mit den erwarteten Parametern aufgerufen.

Beispiel:
```python
embed.add_field(name="__"+lecture_lists[i][0]+"__:",value="- Beginn: "+"*"+lecture_lists[i][1]+"*"+ "   ┃   Ende: *"+lecture_lists[i][2]+"*"+ "\n"+"- Raum: *"+lecture_lists[i][3]+"*", inline=False)
````

- Verwendung von Python-spezifischen Konstrukten: Der Code nutzt spezifische Python-Konstrukte wie Listen, Dictionaries, Funktionen aus externen Bibliotheken (z.B. discord) und spezielle Python-Bibliotheken wie `datetime` und `requests`.

  Beispiel:

  ```python
  from datetime import date, datetime, timedelta
  import discord
  import requests
  ```

- Beherrschung von Python-Objekten und Modulen: Die Studierenden zeigen eine Kenntnis von Python-Objekten und Modulen, da sie Discord-Bibliotheken, Datums- und Zeitobjekte sowie HTTP-Anfragemodule verwenden.

  Beispiel:

  ```python
  select2 = discord.ui.Select(
              placeholder="Choose a month!",
              min_values=1,
              max_values=1,
              options=select_options2
              )
  ```

Basierend auf diesen Beispielen scheinen die Studierenden die Syntax und Semantik von Python zu verstehen, da sie erfolgreich komplexe Funktionen und Steuerelemente implementieren und dabei spezifische Python-Elemente korrekt verwenden.

# Sie können ein größeres Programm selbständig entwerfen, programmieren und auf Funktionsfähigkeit testen (Das Projekt im Team) (10)

- Modularität und Funktionen: Der Code ist in verschiedene Funktionen unterteilt, die jeweils bestimmte Aufgaben erfüllen. Dies fördert die Modularität und Wiederverwendbarkeit des Codes.

  Beispiel:

  ```python
  def lecture_data(date_entry):
  ```

- Externe Bibliotheken und API-Integration: Der Code verwendet externe Bibliotheken wie `discord` und `requests` sowie Integrationen von APIs (iCal). Dies zeigt die Fähigkeit, externe Ressourcen in das Programm zu integrieren.

  Beispiel:

  ```python
  import discord
  from icalendar import Calendar
  import requests
  ```

- Objektorientierte Programmierung: Der Code verwendet objektorientierte Konzepte, insbesondere durch die Definition von Klassen und die Erstellung von Objekten. Zum Beispiel wird die `embed_buttons`-Klasse für die Discord-Interaktionen verwendet.

  Beispiel:

  ```python
  class embed_buttons(discord.ui.View):
  ```

- Datei- und Netzwerkoperationen: Der Code führt Dateioperationen (Lesen von iCal-Daten) und Netzwerkoperationen (HTTP-Anfragen) durch. Dies zeigt Verständnis für die Interaktion mit verschiedenen Datenquellen.

  Beispiel:

  ```python
  response = requests.get(cal_url)
  ```

- Testbarkeit: Der Code enthält Funktionen wie `lecture_data`, die spezifische Funktionalitäten ausführen und getrennt getestet werden können. Dies erleichtert die Überprüfung der Funktionsfähigkeit.

  Beispiel:

  ```python
  await interaction.message.edit(embed=lecture_data(datetime.strptime(date,"%Y-%m-%d %H:%M:%S").date()), view=embed_buttons())
  ```

# Sie kennen verschiedene Datenstrukturen und können diese exemplarisch anwenden. (10)

- Listen: Der Code verwendet Listen, um Daten zu speichern und zu organisieren. Zum Beispiel werden in `lecture_lists` und `lecture_lists2` Listen von Vorlesungsinformationen erstellt.

  Beispiel:

  ```python
  lecture_lists = []
  ```

- Dictionaries: Dictionaries werden verwendet, um strukturierte Daten zu speichern. In `target_date_events` und `target_date_events2` werden Informationen zu Vorlesungen in einem Dictionary-Format gespeichert.

  Beispiel:

  ```python
  target_date_events = []
  ```

- Strings: Strings werden ausgiebig verwendet, insbesondere für die Formatierung von Daten in Embeds und für die Anzeige von Informationen.

  Beispiel:

  ```python
  event['start_time'].strftime("%H:%M" + ' Uhr')
  ```

- Selektionsdatentypen (Select Menus): Die Verwendung von Discord-Select-Menüs zeigt die Anwendung eines datenstrukturierten Ansatzes für die Benutzerinteraktion.

  Beispiel:

  ```python
  class WeekSelectionView(discord.ui.View):
  ```

- Benutzerdefinierte Datenstrukturen (Klassen): Der Code definiert benutzerdefinierte Klassen wie `embed_buttons` und `WeekSelectionView`, um bestimmte Funktionalitäten zu kapseln und zu organisieren.

  Beispiel:

  ```python
  class embed_buttons(discord.ui.View):
  ```

## PERSONALE UND SOZIALE KOMPETENZ (20 Punkte)

# Die Studierenden können ihre Software erläutern und begründen. (5)

<!-- Jeder in der Gruppe: You have helped someone else and taught something to a fellow student (get a support message from one person) -->

Ja, die Gruppe hat mit ihrer Präsentation die Software gut erläutert.

# Sie können sich selbstständig in Entwicklungsumgebungen und Technologien einarbeiten und diese zur Programmierung und Fehlerbehebung einsetzen. (10)

<!-- Which technology did you learn outside of the teacher given input -->

Anhand des Codes sehen wir, dass die Gruppe Discord, xlwings und asyncio verwendet hat.
