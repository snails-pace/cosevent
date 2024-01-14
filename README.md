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
### Seiten der Anwendung, ihre Aufgaben und Besonderheiten
* Besonderheiten der Seiten (ist Login nötig, besonderes bei der Eingabe von Daten beachten, ...)
* Alle Seiten enthalten ein Menü im oberen Bereich der Seite, mit welchem zu den folgenden Seiten navigiert werden kann:
  * Event-Liste/Homepage
  * Event-Liste der eigens erstellten Events
  * Liste der Kategorien
  * Warenkorb
  * Login/Logout
#### Homepage (Events)
ohne Login erreichbar
* Die Homepage beinhaltet die frei zugängliche Liste aller eingetragener Veranstaltungen mit dem Namen, Ort und Datum.
* Durch klick auf die Veranstaltungs-Cards wird die Detailseite der jeweiligen Veranstaltung geöffnet.

#### My Events
Login benötigt
* Hier ist wie bei 'Events' eine Auflistung der Veranstaltungen. In diesem Fall aber nur derer, die selbst erstellt wurden.
* Oben rechts ist ein Button 'New' mit dem zur Seite 'Create Event' gelangt werden kann bei der eine neue Veranstaltung erstellt werden kann.

#### Event Details
* Mit Klick auf eine Veranstaltung in der Liste in 'Events' oder 'My Events' wird auf die Detail-Seite des jeweiligen Events weitergeleitet.
* Hier befinden sich Detail-Informationen zu der Veranstaltung.
* Ohne Login:
  * kann als Aktion das Hinzufügen eines Tickets für die Veranstaltung zum Warenkorb ausgeführt werden. Es wird in diesem Fall automatisch zum Warenkorb weitergeleitet.
* Mit Login:
  * können die gleichen Aktionen wie ohne Login durchgeführt werden.
  * sind bei eigens erstellten Veranstaltungen auch die Buttons 'Edit' und 'Delete' zu sehen. Hierüber ist eine Weiterleitung im ersten Fall an die 'Edit Event' Seite und im zweiten Fall an die 'Delete Seite'. 

  
#### Create Event
Login benötigt

UpdateEventForm eingebettet
* Hier können mittels eines Formulars neue Events erstellt werden. 
* Das 'Category' Feld ist mit den Kategorie-Instancen verknüpft, die in der Rubrik 'Categories' erstellt werden können.
* Bis auf das 'Description' Feld und das 'Availability' Feld, welches einen Default-Wert 0 hat, sind alle Angaben Pflichtfelder.
* Die derzeit eingeloggte Person wird automatisch in das 'Artist' Feld der Instanz des Event Models eingefügt, jedoch in der Sichtbarkeit versteckt, damit nicht andere Künstler*innen als die eingeloggte Person eingetragen werden können.
* Der Veranstaltungsort wird im Formular (UpdateEventForm) überprüft, ob dieser schon eine Veranstaltung an diesem Tag hat und falls dies der Fall ist, ein Fehler ausgegeben.
* Der 'Save'-Button speichert das Event in der Datenbank und führt mit einer Erfolgsnachricht auf die 'My Events' Seite zurück.
* Der 'Cancel'-Button führt ohne weitere Aktionen auf die 'My Events' Seite zurück.

#### Edit Event
Login benötigt

UpdateEventForm eingebettet
* Hier ist das gleiche Formular wie bei Create Event zu sehen, jedoch mit den schon vorausgefüllten Daten des bestehenden Events. Diese können dann in dem Formular geändert und gespeichert werden.
* Mit dem Speichern wird das Event in der Datenbank geändert und auf die Event-Liste zurückgeführt.
* Mit dem 'Cancel' Button wird auf die Event-Liste zurückgeführt ohne das Event zu verändern.
* Der 'Save'-Button führt zur Eintragung des Events in der Datenbank und es gibt eine Weiterleitung auf die 'My Events' Seite mit einer Erfolgsnachricht, auf welcher das neue Event nun zu sehen ist.
* Der 'Cancel'-Button führt einen zur 'My Events' Seite zurück
* Der Veranstaltungsort wird im Formular (UpdateEventForm) überprüft, ob dieser schon eine Veranstaltung an diesem Tag hat und falls dies der Fall ist, ein Fehler ausgegeben.

#### Delete Event
Login benötigt
* Es können nur eigens erstellte Events gelöscht werden.
* Diese Seite ist über den 'Delete'-Button der Detail Ansicht der Events erreichbar.
* Hier gibt es nocheinmal eine eigene Seite für die Abfrage, ob das Event wirklich gelöscht werden soll.
* Der 'Confirm'-Button löscht das Event aus der Datenbank und leitet auf die 'My Events' Seite weiter mit einer Banner-Benachrichtigung, dass das Event gelöscht wurde.
* Der 'Cancel Button' führt auf die Detail-Seite des Events zurück ohne weitere Aktionen.

#### Categories
Login benötigt
* Die Kategorien werden als Liste (Cards untereinander) mit dem Namen und einem 'Delete'-Button dargestellt.
* Alle eingeloggten User können Kategorien über den 'New'-Button erstellen und über den 'Delete'-Button löschen.
* Es können nur Kategorien gelöscht werden, die nicht mit Veranstaltungen verbunden sind, da diese im Event-Model als 'PROTECTED' Relation verbunden ist.
  * Beim Löschvorgang wird auf die 'Delete Category' Seite weitergeleitet.
* Der 'New'-Button führt zur 'Create Category' Seite.

#### Create Category
Login benötigt

UpdateCategoryForm eingebettet
* Es kann der Name der Kategorie eingegeben werden
  * Dieser wird überprüft und Capitalized.
* Der 'Save'-Button speichert die Kategorie in der Datenbank und führt auf die Kategorie Übersicht zurück mit einer Erfolgsnachricht.
* Der 'Cancel'-Button führt ohne weitere Aktionen auf die Kategorieübersicht zurück.

#### Cart
* 

#### Login/Logout

### Formulare

* Das Formular ist einheitlich gestaltet und wird für alle Formularfunktionen der Anwendung genutzt.
    * Das Formular wird über den csrf Token geschützt.

## Anlegen/Bearbeiten von User-Daten
* User also in diesem Fall Künstler*innen können nur von Admin-Seite im Admin Interface angelegt werden.
    * Das Admin Interface wird von Django generiert und ist unter: /admin zu erreichen.
    * Der Username in dieser Anwendung ist die Email-Adresse.
    * 
