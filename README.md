# Dokumentation

## Funktion der Anwendung

* ist eine Event-Management Software
* es können Veranstaltungen von Kuenstler\*innen erstellt/ihre eigens erstellten bearbeitet werden und diese für die Öffentlichkeit sichtbar gemacht. Und Tickets können für diese Veranstaltungen gebucht werden.
* Besucher*innen können alle Veranstaltungen ohne Login einsehen.
* Besucher*innen können Veranstaltungen buchen und dann im Warenkorb einsehen.

## Anforderungen zur Installation der Anwendung

* ist in Python3 geschrieben
* Framework: Django
* nutzt als Datenbank MySQL
 
## Verknüpfung der Anwendung mit der Datenbank

* 

## Aufbau der Anwendung

* Seitenanzahl
* Welche Seiten gibt es und was kann da gemacht werden
* Besonderheiten der Seiten (ist Login nötig, besonderes bei der Eingabe von Daten beachten, ...)
* Das Formular ist einheitlich gestaltet und wird für alle Formularfunktionen der Anwendung genutzt.
    * Das Formular wird über den csrf Token geschützt.

## Anlegen/Bearbeiten von User-Daten
* User also in diesem Fall Künstler*innen können nur von Admin-Seite im Admin Interface angelegt werden.
    * Das Admin Interface wird von Django generiert und ist unter: /admin zu erreichen.
    * Der Username in dieser Anwendung ist die Email-Adresse.
    * 
