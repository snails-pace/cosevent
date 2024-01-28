# Dokumentation

## Funktion der Anwendung

Cosevent ist eine Event-Management Software.
* Es können Veranstaltungen von Künstler\*innen erstellt/ihre eigens erstellten bearbeitet und gelöscht werden und diese für die Öffentlichkeit sichtbar gemacht werden. 
* Tickets für die Veranstaltungen können gebucht werden.
* Künstler\*innen können Kategorien anlegen/löschen, die mit den Veranstaltungen verknüpft sind.
* Besucher*innen der Anwendung können alle Veranstaltungen auch ohne Login einsehen.
* Besucher*innen der Anwendung können Veranstaltungen buchen und dann im Warenkorb einsehen.

## Anforderungen zur Installation der Anwendung

* Programmiersprache: Python3
* Framework: Django
* Datenbank: MySQL
* IDE: PyCharm (optional)

## Bereitstellung der Anwendung

```shell
git clone ...
cd cosevent
# create virtual environment of your choice and switch to it (
pip install -r requirements.txt
# create mysql database (see Datenbankverknüpfung)
python3 manage.py makemigrations
python3 manage.py migrate
# for testing start (test your app in your browser at port 8000):
python3 manage.py runserver
```

## Datenbankverknüpfung mit PyCharm
1. Installiere MySQL
2. In PyCharm mit MySQL verbinden: https://www.jetbrains.com/help/pycharm/mysql.html#connect-to-mysql-database
3. Datenbank erstellen: In PyCharm in der Query Konsole mit Create DATABASE <name> und dann nach der unten genannten Struktur implementieren:
4. Django und MySQL verbinden:
```shell
pip install mysqlclient
# connect with root user
mysql -u root -p
```
5. In EventManager eine settings_local.py Datei erstellen, diese wird automatisch von settings.py importiert.
6. In der settings_local.py die Datenbankverbindung eintragen:
```python
DATABASES = {
    'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "EventManager",
        "HOST": "localhost",
        "USER": "root",
        "PASSWORD": "<yourPassword>"
    }
}
```

## Datenbankstruktur
* Die App Cosevent beinhaltet die folgenden Tabellen, die durch die Models nach MySQL migriert wurden:

### cosevent_category
Mit den Spalten:
* id (von Django erstellt)
* name: varchar(255)

### cosevent_event
Mit den Spalten:
* id (von Django erstellt)
* name: varchar(255)
* date: date
* description: longtext
* venue: varchar(255)
* availability: int (positiv)
* price: decimal
* artist_id: bigint, Foreign key from Profile

### cosevent_profile
* id (von Django erstellt)
* nickname: varchar(255)
* birthdate: date
* user_id: bigint, Foreign key from User

### cosevent_user
* id (von Django erstellt)
* email: varchar(254)
* password (von Django erstellt)

### cosevent_order
* id (von Django erstellt)
* customer_name: varchar(255)
* customer_email: email
* total_price: decimal
* date: date

### cosevent_eventorder
* id (von Django erstellt)
* event: bigint, Foreign key from Event
* ticket_count: positive integer
* price: decimal
* order: bigint, Foreign key from Order

## Benutzung der Anwendung

### Nach Events suchen
1. Gehe zu 'Events' und stöbere durch die verschiedenen Veranstaltungen.
2. Um zur Detail-Seite des Events zu gelangen, klicke auf das jeweilige Event.

### Event erstellen
Login benötigt: Gehe auf Login und gebe die Anmelde-Daten ein und klicke auf 'Login'. 
1. Gehe zu 'My Events' und klicke auf den Button 'New' oben rechts. 
2. Fülle die Formulardaten aus. (Unvollständige Angaben werden rot markiert mit Fehlermeldung angezeigt.)
   * Falls ein Video zu der Veranstaltung angezeigt werden soll, muss ein Link zu dem Video an die Administrator:innen per Email gesendet werden.
3. Speichere das Event mit dem 'Save'-Button.
   

### Event löschen
Login benötigt: Gehe auf Login und gebe die Anmelde-Daten ein und klicke auf 'Login'. 
1. Gehe unter 'My Events' oder 'Events' zum jeweiligen Event und klicke darauf. 
2. In der Detailseite des Events klicke auf den Button 'Delete'. 
3. Bestätige das Löschen auf der nun auftauchenden Seite mit dem 'Delete'-Button.

### Event editieren
Login benötigt: Gehe auf Login und gebe die Anmelde-Daten ein und klicke auf 'Login'. 
1. Gehe unter 'My Events' oder 'Events' zum jeweiligen Event und klicke darauf.
2. In der Detailseite des Events klicke auf den Button 'Edit'.
3. Fülle die Formulardaten aus. (Unvollständige Angaben werden rot markiert mit Fehlermeldung angezeigt.)
4. Speichere die Änderungen mit dem 'Save'-Button.

### Kategorie erstellen
Login benötigt: Gehe auf Login und gebe die Anmelde-Daten ein und klicke auf 'Login'. 
1. Gehe zu 'Categories' und klicke auf den Button 'New' oben rechts.
2. Fülle die Formulardaten aus. (Unvollständige Angaben werden rot markiert mit Fehlermeldung angezeigt.)
3. Speichere die Kategorie mit dem 'Save'-Button.

### Kategorie löschen
Login benötigt: Gehe auf Login und gebe die Anmelde-Daten ein und klicke auf 'Login'. 
1. Gehe unter 'Categories' zur jeweiligen Kategorie und klicke auf den zugehörigen 'Delete' Button. 
2. Bestätige das Löschen auf der nun auftauchenden Seite mit dem 'Delete'-Button.

### Ticket für eine Veranstaltung kaufen
1. Gehe unter 'Events' zum jeweiligen Event und klicke darauf, um zur Detail-Ansicht zu gelangen.
2. Klicke auf den 'Add to cart' Button. Es gibt eine Weiterleitung zum Warenkorb.
3. Im Warenkorb kann die Anzahl der Tickets angepasst werden. Die Summe erscheint neben jeder Veranstaltung und der Gesamtpreis ist unter der Zusammenfassung von den Tickets zu sehen.
4. Um den Kauf abzuschließen klicke auf den 'Buy' Button.
5. Gib auf der nächsten Seite die Formulardaten an und bestätige den Kauf mit dem 'Confirm' Button.
6. Die Availability vom Event wird dementsprechend runtergezählt und ein Order und EventOrder Model angelegt.
6. Eine Kaufbestätigungs-Seite mit der Bestell-Nummer erscheint.



## Aufbau der Anwendung

### Seitenübersicht der Anwendung - Ihre Aufgaben und Besonderheiten
* Besonderheiten der Seiten (ist Login nötig, besonderes bei der Eingabe von Daten beachten, ...)
* Alle Seiten enthalten ein Menü im oberen Bereich der Seite, mit welchem zu den folgenden Seiten navigiert werden kann:
  * Event-Liste/Homepage
  * Event-Liste der eigens erstellten Events
  * Liste der Kategorien
  * Warenkorb
  * Kaufen mit Bestägigung
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
* Das 'Category' Feld ist mit den Kategorie-Instanzen verknüpft, die in der Rubrik 'Categories' erstellt werden können.
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
* Hier gibt es noch einmal eine eigene Seite für die Abfrage, ob das Event wirklich gelöscht werden soll.
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
* Der 'Cancel'-Button führt ohne weitere Aktionen auf die Kategorie-Übersicht zurück.

#### Cart
* Hier werden alle Tickets angezeigt, die zum Warenkorb hinzugefügt wurden als Liste (Cards) mit:
  * Name der Veranstaltung
  * Anzahl der Karten
  * Preis der Karten
  * Summe der Karten für die jeweilige Veranstaltung
* Mit '+' und '-' Buttons neben der Anzahl der Karten für die jeweilige Veranstaltung kann die Anzahl verändert werden. 
* Unten wird die Gesamtsumme aller Karten zusammen angezeigt.

### Buy and Confirmation
* Hier werden alle Tickets angezeigt, die zum Warenkorb hinzugefügt wurden als Liste (Cards) mit:
  * Name der Veranstaltung
  * Anzahl der Karten
  * Preis der Karten
  * Summe der Karten für die jeweilige Veranstaltung
* Es wird ein Formular angezeigt mit Name- und Email-Feld.
* Der 'Save'-Button speichert den Auftrag (falls alle Daten validiert wurden) in der Datenbank (im Order- und EventOrder Model. Und führt zur Confirmation-Seite.
  * Die Confirmation Seite zeigt die Bestätigungsmeldung der Bestellung mit Bestell-Nummer an.
* der 'Cancel'-Button führt ohne weitere Aktionen zum Warenkorb zurück.

#### Login/Logout
* wenn ausgeloggt:
  * Es ist im Menü das Navigations-Element 'Login' zu sehen.
  * Es wird das Django-Formular für Login geöffnet. 
  * Der Username ist hier die Email-Adresse.
  * Mit Klick auf den 'Login Button', wird bei korrekten Daten eingeloggt und auf die Homepage verwiesen.
* Wenn eingeloggt:
  * Es ist im Menü das Navigations-Element 'Logout' zu sehen.
  * Mit Klick auf 'Logout' wird zur Logout Nachricht weitergeleitet und einem Link zum wieder einloggen.

### Formulare

* Die Formular HTML Datei ist einheitlich gestaltet und wird für alle Formularfunktionen der Anwendung genutzt und auf der jeweiligen Seite eingebettet.
    * Das Formular wird über den csrf Token geschützt.


## Admin Interface (Anlegen und Bearbeiten von User- und Profildaten und Gruppen)
* Das Admin Interface wird von Django generiert und ist unter: /admin zu erreichen.
* User- und Profildaten können nur auf der Admin Seite angelegt/bearbeitet werden.
### User-Daten anlegen
* User also in diesem Fall Künstler*innen können nur von der Admin-Seite im Admin Interface angelegt werden.
1. Von der Übersichtsseite unter dem App Namen (Cosevent) auf das '+' neben 'Users' klicken
2. Formular ausfüllen (Username ist hier die Email-Adresse)
3. 'Save'-Button klicken
* Die Person wurde in der Datenbank angelegt.

### User-Daten bearbeiten/ Berechtigungen hinzufügen
1. In der linken Menüleiste unter dem App Namen (Cosevent) auf 'Users' klicken
2. Den jeweiligen Usernamen, der bearbeitet werden soll anklicken
3. Daten bearbeiten (hier können die User zu Gruppen hinzugefügt werden)
4. 'Save'-Button klicken
* Die Personendaten wurden in der Datenbank aktualisiert.

### Profil-Daten anlegen
1. In der linken Menüleiste unter dem App Namen (Cosevent) auf das '+' neben 'Profiles' klicken
2. Eine bestehende User-Person auswählen und Daten ausfüllen
3. 'Save'-Button klicken
* Das Profil wurde in der Datenbank angelegt.

### Profil-Daten bearbeiten
1. In der linken Menüleiste unter dem App Namen (Cosevent) auf 'Profiles' klicken 
2. Daten bearbeiten
3. 'Save'-Button klicken
* Die Profil-Daten wurden in der Datenbank aktualisiert.

### Gruppen anlegen
* Hier können Gruppen mit verschiedenen Berechtigungen angelegt werden.
1. In der linken Menüleiste unter 'Authentication and Authorization' auf das '+' neben 'Groups' klicken
2. Namen für die Gruppe eintragen und Berechtigungen auswählen
3. 'Save'-Button klicken
* Die Gruppe mit den Berechtigungen wurde angelegt.

### Video anlegen und einem Event zuweisen
* Videos können nur von Administrator:innen in der Administrator:innen-Ansicht hinzugefügt werden.
1. In der linken Menüleiste auf das '+' neben 'Videos' klicken
2. Formular ausfüllen
3. 'Save'-Button klicken
4. In der linken Menüleiste auf 'Events' klicken
5. Das gewünschte Event ausfindig machen und in der Spalte 'Video' das Video aus der Auswahl auswählen
6. 'Save'-Button klicken
