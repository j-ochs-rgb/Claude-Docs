Duale Hochschule Baden-Württemberg
Heilbronn
Datenbanken 2
Vorlesungsunterlagen
Duale Hochschule Baden-Württemberg Heilbronn
Prof. Dr. Giacomo Welsch

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 2

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 3

Ziel der Veranstaltung
In dieser Veranstaltung lernen Sie, wie moderne Datenanwendungen entwickelt werden.
Sie werden:
mit strukturierten und semi-strukturierten Daten arbeiten
•
relationale und NoSQL-Datenbanken einsetzen
•
Daten mit Python verarbeiten
•
eine eigene Datenanwendung entwickeln
•
Am Ende der Veranstaltung erstellen Sie eine eigene Streamlit-Anwendung, die sowohl an eine MySQL-Datenbank als auch eine MongoDB
angebunden ist.
Datenbanken 2 Vorlesungsfolien 4

Termine
Räume: C.022 & C.023
Mi 01.04.2026 13:15-16:30 Uhr
•
Do 02.04.2026 09:00-12:15 Uhr
•
Mi 08.04.2026 13:15-16:30 Uhr
•
Mi 15.04.2026 13:15-16:30 Uhr (remote)
•
Mi 22.04.2026 13:15-14:45 Uhr (remote)
•
Mi 29.04.2026 13:15-16:30 Uhr (Präsentationen)
•
Zoom-Raum: Wir nutzen den von WI24A2:
•
https://eu02web.zoom-x.de/j/9271083935
•
Passwort: wi24a2
•
Datenbanken 2 Vorlesungsfolien 5

Projekt und Prüfungsleistung
Im Laufe der Veranstaltung entwickeln Sie eine eigene Anwendung.
Rahmenbedingungen:
Nutzung eines öffentlichen Datensatzes (z.B. Kaggle)
•
Speicherung der Daten in zwei Datenbanken
•
Entwicklung einer interaktiven Anwendung mit Streamlit
•
Am Ende präsentieren Sie Ihre Anwendung kurz im Kurs
•
Prüfungsleistung: Assignment
Die Prüfungsleistung besteht aus einem Projektbericht (5–10 Seiten).
Der Bericht beschreibt:
den verwendeten Datensatz
•
das entwickelte Datenmodell
•
die technische Umsetzung
•
die entwickelte Anwendung
•
Datenbanken 2 Vorlesungsfolien 6

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 7

Typische Architektur analytischer Datenanwendungen
Viele moderne Datenanwendungen dienen der Analyse und Exploration von Daten.
•
Sie bestehen häufig aus mehreren Komponenten:
•
|     |                |     | Daten-           |             | Analyse-    |     |
| --- | -------------- | --- | ---------------- | ----------- | ----------- | --- |
|     | Datenquelle(n) |     |                  | Datenbank   |             |     |
|     |                |     | aufbereitung     |             | anwendung   |     |
|     |  Open Data    |     |  ETL-Tools      |  MySQL     |  BI-Tools  |     |
|     |  ERP          |     |  Python-Skripte |  MongoDB   |  Streamlit |     |
|     |  CRM          |     |  usw.           |  Snowflake |  usw.      |     |
|     |  APIs         |     |                  |  usw.      |             |     |
 usw.
| Datenbanken 2 |     | Vorlesungsfolien |     |     |     | 8   |
| ------------- | --- | ---------------- | --- | --- | --- | --- |

Klassisches Beispiel: ETL und Business Intelligence
Analyse-
anwendung
Datenbank
Daten-
aufbereitung
Datenquelle(n)
https://insightsoftware.com/de/blog/remodel-your-oracle-cloud-data-with-a-data-lakehouse/
Datenbanken 2 Vorlesungsfolien 9

Offene Frage in die Runde
Warum nutzen so viele Unternehmen eine separate/zentrale Datenbank („Data Warehouse“) zur Analyse?
| Datenbanken 2 | Vorlesungsfolien | 10  |
| ------------- | ---------------- | --- |

Motivation für eine zentrale Datenbasis zur Analyse
Entlastung der operativen Systeme (Performance-Grund)
Operative Systeme (z.B. ERP, CRM) sind für schnelle Transaktionen optimiert (z.B. Bestellungen erfassen, Kunden verwalten).

Aufwendige Analysen mit komplexen SQL-Abfragen hätten die Performance dieser Systeme stark beeinträchtigt.

Eine zentrale Datenbasis ermöglicht es, Analysen auf einer separaten Plattform durchzuführen, ohne die operativen Systeme zu

verlangsamen.
Datenintegration aus verschiedenen Quellen
Unternehmen haben oft mehrere operative Systeme (z.B. getrennte Systeme für Vertrieb, Buchhaltung, Lagerverwaltung).

Daten lagen fragmentiert und oft in unterschiedlichen Formaten vor.

Eine zentrale Datenbasis wurde eingeführt, um alle relevanten Daten an einem Ort zusammenzuführen und eine einheitliche Sicht auf

das Unternehmen zu ermöglichen.
Bessere Datenqualität und Historisierung
Operative Systeme speichern oft nur aktuelle Daten, aber für Analysen benötigt man historische Daten (z.B. Umsatztrends über mehrere

Jahre).
Eine zentrale Datenbasis ermöglicht Datenhistorie, Datenbereinigung und eine einheitliche Datenstruktur für konsistente Berichte.

Datenbanken 2 Vorlesungsfolien 11

Data Warehouse
Ein Data Warehouse ist eine zentrale Datenbank, die Daten aus verschiedenen Quellen integriert, um sie für Berichte und Analysen
bereitzustellen.
Gründe für ihre Entstehung:
Datenintegration: Unternehmen benötigten eine zentrale Plattform, um Daten aus verschiedenen Quellen zusammenzuführen und eine

einheitliche Sicht auf ihre Informationen zu erhalten.
Optimierung der Analyse: Operative Systeme waren nicht für umfangreiche Analysen ausgelegt, daher wurden Data Warehouses entwickelt,

um komplexe Abfragen effizient zu verarbeiten.
Historische Datenanalyse: Es bestand Bedarf, historische Daten zu speichern und für langfristige Analysen bereitzustellen.

Eigenschaften:
Strukturierte Daten: Speichert strukturierte und bereinigte Daten, die für Abfragen optimiert sind.

Datenkonsistenz: Stellt durch Transformationsprozesse eine einheitliche Datenqualität sicher.

Unterstützung von Business Intelligence: Dient als Grundlage für Berichte, Dashboards und Entscheidungsfindung.

Beispiele: Amazon Redshift, Google BigQuery, Snowflake.
Datenbanken 2 Vorlesungsfolien 12

Stufen von Business-Analytics-Anwendungen
Business
Intelligence
Delen& Zolbanin(2018)
| Datenbanken 2 | Vorlesungsfolien | 13  |
| ------------- | ---------------- | --- |

Business Intelligence (BI)
Schlüsselfragen:
 Was ist passiert?
 Warum ist es passiert?
Voraussetzungen:
 Reichhaltige und verlässliche
Datengrundlage
|  Genaue | Festlegung | Problembeschreibung |     |     |
| -------- | ---------- | ------------------- | --- | --- |
 Genaue Lösungsbeschreibung
Use Cases:
 Visualisierung von Verkaufszahlen
|  Historische | Veränderungen |     | der  |     |
| ------------- | ------------- | --- | ---- | --- |
Kosten/Preise
|  Effizienzmessungen |          | im              | Kundensupport    |     |
| -------------------- | -------- | --------------- | ---------------- | --- |
|  … (               | Tabellen | und Dashboards) |                  |     |
| Datenbanken 2        |          |                 | Vorlesungsfolien | 14  |

Transaktionale Systeme vs. analytische Datenanwendungen
Transaktionale Systeme Analytische Datenanwendungen
Fokus: operative Prozesse Fokus: Analyse und Exploration
Viele kleine Transaktionen Komplexe Abfragen und Auswertungen
Häufig Kombination aus strukturierten, semi-strukturierten und
Stark strukturierte Daten
unstrukturierten Daten
Häufig alternative Datenschemata, Verwendung des
Klassische relationale Datenbanken
relationalen Schemas aber möglich
Beispiele: Online-Shop, Banking-System Beispiele: Datenanalyse, Dashboards, Data Apps
Datenbanken 2 Vorlesungsfolien 15

Datenquellen und Datenaustausch
Daten können aus sehr unterschiedlichen Quellen stammen, z.B.:
Unternehmenssysteme (z.B. ERP, CRM, Shopsysteme)
•
Web- und Cloud-Anwendungen
•
öffentliche Datensätze (z.B. Open Data, Kaggle)
•
Sensor- oder IoT-Daten
•
Log- oder Eventdaten
•
Für den Austausch und die Weiterverarbeitung werden häufig standardisierte Datenformate verwendet. Zu diesen zählen:
CSV

JSON

XML

YAML

Parquet

Datenbanken 2 Vorlesungsfolien 16

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 17

Offene Frage in die Runde
Was sind Datenformate?
| Datenbanken 2 | Vorlesungsfolien | 18  |
| ------------- | ---------------- | --- |

Strukturierte Daten
Daten liegen in einer klar definierten, festen Struktur vor.
Merkmale:
festes Schema
•
gleiche Struktur für alle Datensätze
•
klar definierte Datentypen
•
typischerweise tabellarische Organisation
•
Beispiel (relationale Tabelle):
|               | Name  | Alter            | Ort     |     |
| ------------- | ----- | ---------------- | ------- | --- |
|               | Anna  | 23               | Berlin  |     |
|               | Jonas | 31               | Hamburg |     |
| Datenbanken 2 |       | Vorlesungsfolien |         | 19  |

Semi-strukturierte Daten
Daten besitzen eine erkennbare Struktur, aber kein strikt vorgegebenes Schema.
Merkmale:
flexible oder optionale Felder
•
verschachtelte Strukturen möglich
•
Datensätze können unterschiedliche Attribute besitzen
•
Beispiel (JSON):
{
"name": "Anna",
"age": 23,
"hobbies": ["Klettern", "Lesen"]
}
Datenbanken 2 Vorlesungsfolien 20

Vergleich von CSV, XML und JSON
|     | Eigenschaft | CSV          | XML               | JSON              |     |
| --- | ----------- | ------------ | ----------------- | ----------------- | --- |
|     | Strukturtyp | strukturiert | semi-strukturiert | semi-strukturiert |     |
hierarchische Elemente
Grundstruktur tabellarisch (Zeilen und Spalten) Objekte und Arrays
(Tags)
meist fest (gleiche Spalten pro  flexibel, optional mit Schema
|     | Schema |     |     | flexibel, optional mit Schema |     |
| --- | ------ | --- | --- | ----------------------------- | --- |
Zeile) (DTD/XSD)
|     | Verschachtelung möglich | nein   | ja                  | ja               |     |
| --- | ----------------------- | ------ | ------------------- | ---------------- | --- |
|     | Erweiterbarkeit         | gering | hoch                | hoch             |     |
|     |                         |        | Systemintegration,  | Web-APIs, NoSQL- |     |
Typische Nutzung Datenexporte, Tabellen
|               |     |                  | Dokumentformate | Datenbanken |     |
| ------------- | --- | ---------------- | --------------- | ----------- | --- |
| Datenbanken 2 |     | Vorlesungsfolien |                 |             | 21  |

CSV – Comma-Separated Values
Was ist CSV?
CSV ist ein einfaches, textbasiertes Format, das verwendet wird, um tabellarische Daten in einer Datei darzustellen.
Dabei gilt:
Jede Zeile in der Datei entspricht einem Datensatz.

Innerhalb jeder Zeile sind die Felder durch ein Trennzeichen getrennt (meist ein Komma, Semikolon oder Tabulator).

Die Datei besteht nur aus Text, es gibt keine Formatierung, Datentypen oder eingebettete Metadaten.

Beispiel:
Name,Alter,Ort
Anna,23,Berlin
Jonas,31,Hamburg
…
Das Format ist sehr leichtgewichtig, maschinenlesbar und menschenlesbar – und dadurch besonders weit verbreitet.
Datenbanken 2 Vorlesungsfolien 22

Ursprung des CSV-Formats
Das CSV-Format hat seinen Ursprung in den frühen Tagen der Tabellenkalkulation, insbesondere bei Lotus 1-2-3 und später Microsoft

Excel.
Ziel war es, ein kompatibles Austauschformat zu schaffen, mit dem Daten zwischen unterschiedlichen Programmen ohne komplexe

Konvertierungen übertragen werden konnten.
Da viele Programme einfache Textdateien einlesen und schreiben können, war CSV ideal für den Export/Import zwischen Systemen, die nicht

dieselbe Software nutzen.
RFC 4180 beschreibt seit 2005 eine (lose) Standardisierung des Formats – allerdings gibt es keine strenge Norm. In der Praxis existieren viele

CSV-Varianten, z. B. mit:
unterschiedlichen Trennzeichen (z.B. , oder ; oder |)

optionalen Anführungszeichen um Felder

Zeilenumbrüche in Feldern (nur mit bestimmten Escape-Konventionen)

Datenbanken 2 Vorlesungsfolien 23

Warum ist CSV bis heute relevant?
Einfachheit: Keine zusätzliche Software oder Parser notwendig – CSV lässt sich mit jedem Texteditor öffnen.

Breite Unterstützung: Fast jedes Datenanalyse-Tool, jede Programmiersprache und jedes Datenbanksystem kann CSV-Dateien lesen und

schreiben.
Plattformunabhängig: CSV-Dateien funktionieren unabhängig von Betriebssystem oder Umgebung.

Datenbanken 2 Vorlesungsfolien 24

Schematische Struktur von CSV-Dateien
CSV-Dateien folgen einem sehr einfachen Aufbau, der sich an Tabellen orientiert:
Spalte1,Spalte2,Spalte3
Wert1,Wert2,Wert3
Wert4,Wert5,Wert6
Merkmale:
Die erste Zeile enthält häufig die Spaltennamen (Header-Zeile), ist aber optional.

Jede weitere Zeile stellt einen Datensatz dar.

Die Felder sind durch ein Trennzeichen (Separator) getrennt – meist ein Komma, aber auch Semikolon oder Tabulator sind gebräuchlich.

Alle Inhalte sind Text – es gibt keine eingebauten Datentypen.

Datenbanken 2 Vorlesungsfolien 25

Beispiele für unterschiedliche Trennzeichen
Beispiel 1: Standard (Komma-separiert, „klassisches“ CSV)
Name,Alter,Ort
Anna,23,Berlin
Jonas,31,Hamburg
Beispiel 2: Semikolon-separiert (z. B. in Deutschland/Excel mit deutschem Sprachpaket)
Name;Alter;Ort
Anna;23;Berlin
Jonas;31;Hamburg
Beispiel 3: Tabulator-separiert (TSV – Tab-Separated Values)
Name\tAlter\tOrt
Anna\t23\tBerlin
Jonas\t31\tHamburg
Datenbanken 2 Vorlesungsfolien 26

Besonderheiten & Stolperfallen bei der Verwendung von CSV
Felder mit Trennzeichen, Zeilenumbrüchen oder Anführungszeichen müssen oft in doppelte Anführungszeichen gesetzt werden:

"Max, der Zweite",27,"Köln\nAltstadt"

Lea Schulz,35,"Frankfurt, Main"

"Dr. Tim Berger",45,Hannover

Kein einheitlicher Standard → Tools müssen oft auf Trennzeichen konfiguriert werden (z.B. Excel, Python csv-Modul)

Datenbanken 2 Vorlesungsfolien 27

XML – Extensible Markup Language
Was ist XML?
XML ist eine textbasierte Auszeichnungssprache, die entwickelt wurde, um strukturierte Daten hierarchisch darzustellen.
Der Fokus liegt dabei auf:
Lesbarkeit für Menschen und Maschinen

Portabilität über verschiedene Systeme

Darstellung komplexer Strukturen

Ein XML-Dokument besteht aus sogenannten Elementen (Tags), die Daten umschließen und strukturieren – ähnlich wie HTML, aber inhaltlich neutral und
beliebig erweiterbar.
Beispiel:
<person>
<name>Anna</name>
<age>23</age>
<city>Berlin</city>
</person>
Datenbanken 2 Vorlesungsfolien 28

Ursprung von XML
XML wurde in den 1990er Jahren vom W3C (World Wide Web Consortium) als vereinfachte Weiterentwicklung von SGML (Standard

Generalized Markup Language) entwickelt.
Ziel: Eine universelle Sprache zur Beschreibung strukturierter Daten, die plattformübergreifend und leicht zu verarbeiten ist.

Die erste Version erschien 1998 – seither weit verbreitet im Kontext von:

Datenaustausch zwischen Anwendungen (z.B. Webservices, SOAP)

Konfigurationsdateien

Datenbanken & Dokumentenspeicher (z.B. XML-Datenbanken)

Office-Dokumenten (z. B. .docx/.xlsx basieren intern auf XML)

https://wiki.selfhtml.org/wiki/SGML
Datenbanken 2 Vorlesungsfolien 29

Warum ist XML bis heute relevant?
Strukturiert & hierarchisch
 Elemente können verschachtelt werden → ideal für komplexe Daten
Beispiel: Personen mit Adressen, Bücher mit Autoren etc.

Selbstbeschreibend
Jedes Feld hat einen eindeutigen Namen

Menschen & Maschinen erkennen sofort, was ein Wert bedeutet

Validierbar
Mit XSD oder DTD können Struktur & Datentypen geprüft werden

Nützlich in sicherheitskritischen oder regulierten Umgebungen

Plattform- & systemunabhängig
 Reiner Text → funktioniert auf jedem System
Viele Standardformate basieren intern auf XML (.docx, .svg, .xlsx)

Bewährt im Datenaustausch
Bis heute verbreitet bei Webservices (z.B. SOAP oder REST)

Besonders relevant in der Systemintegration (z.B. Behörden, Unternehmen)

Datenbanken 2 Vorlesungsfolien 30

Schematische Struktur von XML
Ein XML-Dokument besteht aus:
Deklaration (optional):

Gibt an, dass es sich um XML handelt und in welcher Kodierung:
<?xml version="1.0" encoding="UTF-8"?>
Wurzelelement (Root-Element):

Umfasst das gesamte Dokument – es darf nur eines geben.
<person> ... </person>
Elemente (Tags):

Stellen die eigentlichen Daten dar:
<name>Anna</name>
Attribute (optional):

Können zusätzliche Informationen in einem Element unterbringen:
<person geschlecht="weiblich">...</person>
Datenbanken 2 Vorlesungsfolien 31

Beispiele XML
Einfaches Beispiel (Elementbasiert) mit Deklaration:

<?xml version="1.0" encoding="UTF-8"?>
<person>
<name>Anna</name>
<alter>23</alter>
<ort>Berlin</ort>
</person>
Beispiel mit Attributen und Deklaration:

<?xml version="1.0" encoding="UTF-8"?>
<person geschlecht="weiblich" id="42">
<name>Anna</name>
<ort>Berlin</ort>
</person>
Datenbanken 2 Vorlesungsfolien 32

Beispiel: Liste von Personen in XML
| Datenbanken 2 | Vorlesungsfolien | 33  |
| ------------- | ---------------- | --- |

Validierung von XML-Dokumenten: DTD und XSD
Die Begriffe XSD und DTD beziehen sich auf die Möglichkeit, ein XML-Dokument formell zu beschreiben und zu validieren. Das ist besonders
nützlich in professionellen Kontexten, wo Datenstrukturen klar definiert, überprüfbar und automatisiert verarbeitet werden müssen.
|     | Begriff | Bedeutung | Ziel |     |
| --- | ------- | --------- | ---- | --- |
Legt fest, wie ein XML-Dokument aufgebaut sein darf – ältere, einfachere
|     | DTD | Document Type Definition |     |     |
| --- | --- | ------------------------ | --- | --- |
Variante
Mächtigerer, XML-basiertes Schemaformat mit Typdefinitionen und mehr
|     | XSD | XML Schema Definition |     |     |
| --- | --- | --------------------- | --- | --- |
Kontrolle
| Datenbanken 2 |     | Vorlesungsfolien |     | 34  |
| ------------- | --- | ---------------- | --- | --- |

DTD – Document Type Definition
Merkmale:
Definiert erlaubte Elemente, Attribute und Struktur

Wird entweder intern im XML-Dokument oder extern als separate Datei eingebunden

Kein XML-Format selbst (eigene Syntax)

Einfaches Beispiel (interne DTD):
#PCDATA steht für „parsed character data“ (also Text)

Diese DTD erzwingt, dass <person> genau die drei Elemente in genau dieser Reihenfolge enthält

Datenbanken 2 Vorlesungsfolien 35

XSD – XML Schema Definition
Merkmale:
Wird in XML geschrieben
•
Unterstützt Datentypen (z.B. xs:integer, xs:date)
•
Erlaubt feinere Kontrolle (Pflichtfelder, Reihenfolge, Längen, Wertebereiche, Typprüfungen)
•
Beispiel: XML mit externem XSD
Datenbanken 2 Vorlesungsfolien 36

Tutorials zu XML
XML: https://www.w3schools.com/xml/default.asp XML DTD: https://www.w3schools.com/xml/xml_dtd_intro.asp
• 
XML HOME DTD Introduction
• 
XML Introduction DTD Building Blocks
• 
XML How to use DTD Elements
• 
XML Tree DTD Attributes
• 
XML Syntax DTD Elements vs Attr
• 
XML Elements
•
XML Attributes XSD: https://www.w3schools.com/xml/schema_intro.asp
 
XML DTD XSD Introduction
 
XML Schema XSD How To
 
XSD <schema>

XSD Elements

XSD Attributes

Datenbanken 2 Vorlesungsfolien 37

JSON – JavaScript Object Notation
Was ist JSON?
JSON ist ein leichtgewichtiges, textbasiertes Format zur Darstellung strukturierter Daten. Es basiert auf der Syntax von JavaScript, ist aber

programmiersprachenunabhängig einsetzbar.
JSON stellt Daten mithilfe von Schlüssel-Wert-Paaren, Arrays und Objekten dar. Es ist besonders kompakt, lesbar und hervorragend

geeignet für die Übertragung von Daten zwischen Systemen – z. B. zwischen einem Webbrowser und einem Server.
Beispiel:
{
"name": "Anna",
"alter": 23,
"ort": "Berlin"
}
Schlüssel stehen in Anführungszeichen

Werte können Zahlen, Strings, Booleans, Arrays, Objekte oder null sein

Die Struktur ist hierarchisch und kann beliebig tief verschachtelt werden

Datenbanken 2 Vorlesungsfolien 38

Ursprung von JSON
JSON wurde Anfang der 2000er Jahre von Douglas Crockford als Antwort auf die umständliche XML-Nutzung im Web entwickelt

Ziel: ein einfaches, leicht verarbeitbares Format für Webanwendungen

JSON ist mittlerweile in nahezu jeder Programmiersprache unterstützt (z.B. json in Python, JSON.parse() in JavaScript)

Datenbanken 2 Vorlesungsfolien 39

Warum ist JSON so verbreitet?
Kompakt & lesbar → ideal für Menschen und Maschinen

Verschachtelbar → geeignet für komplexe Objekte und Listen

Standard für Web-APIs (z.B. REST, GraphQL)

Einfach zu parsen → native Unterstützung in fast jeder Sprache

Unabhängig vom System → reines Textformat

Datenbanken 2 Vorlesungsfolien 40

Schematische Struktur von JSON
Ein JSON-Dokument besteht aus Objekten, Arrays, Schlüssel-Wert-Paaren und Datentypen. Es basiert auf der Syntax von JavaScript.
Grundelemente in JSON:
|     | Element | Beschreibung | Beispiel |     |
| --- | ------- | ------------ | -------- | --- |
Objekt Sammlung von Schlüssel-Wert-Paaren (geschweifte Klammern) { "name": "Anna" }
|     |     | Liste von Werten (eckige Klammern) | [23, 45, 31] |     |
| --- | --- | ---------------------------------- | ------------ | --- |
Array
|     | Schlüssel | Immer ein String in Anführungszeichen | "alter" |     |
| --- | --------- | ------------------------------------- | ------- | --- |
Wert String, Zahl, Boolean, Objekt, Array oder null "Berlin", 42, false, null
| Datenbanken 2 |     | Vorlesungsfolien |     | 41  |
| ------------- | --- | ---------------- | --- | --- |

Beispiele JSON
Beispiel 1: Einfaches JSON-Objekt: Beispiel 3: Verschachteltes Objekt
 
{ {
"name": "Anna", "name": "Alex",
"alter": 23, "adresse": {
"ort": "Berlin" "strasse": "Hauptstraße 5",
} "stadt": "München"
}
Beispiel 2: Objekt mit Array: }

{
"name": "Jonas", Beispiel 4: Array von Objekten (Liste von Personen)

"hobbys": ["Lesen", "Klettern", "Gitarre"] [
} { "name": "Anna", "alter": 23 },
{ "name": "Jonas", "alter": 31 },
{ "name": "Alex", "alter": 27 }
]
Datenbanken 2 Vorlesungsfolien 42

Besonderheiten und Stolperfallen in JSON
Schlüssel typischerweise immer in doppelten Anführungszeichen (Ausnahmen: JSON5 und MongoDB-Shell; letzteres kümmert sich

automatisch um Anführungszeichen)
{ "name": "Anna" }  RICHTIG
{ name: "Anna" }  NICHT ERLAUBT
Letztes Element darf kein Komma haben

{
"name": "Anna",
"alter": 23  KEIN KOMMA HIER
}
Keine Kommentare erlaubt

Nur bestimmte Datentypen erlaubt: String, Number, Boolean, null, Object und Array

Zahlen: kein führendes 0, kein NaN oder Infinity

 Bei Unsicherheit Validierung nutzen: (z.B.) https://jsonlint.com/
Datenbanken 2 Vorlesungsfolien 43

Beispiel: Liste von Personen in JSON
| Datenbanken 2 | Vorlesungsfolien | 44  |
| ------------- | ---------------- | --- |

Vergleich Liste von Personen in CSV, XML und JSON
| Datenbanken 2 | Vorlesungsfolien | 45  |
| ------------- | ---------------- | --- |

Tutorial zu JSON
JSON: https://www.w3schools.com/js/js_json.asp
•
JSON Intro

JSON vs XML

JSON Data Types

JSON Objects

JSON Arrays

Datenbanken 2 Vorlesungsfolien 46

Kurze Einordnung: YAML
YAML – Yet Another Markup Language Beispiel
YAML ist ein textbasiertes Format zur Darstellung strukturierter database:
•
Daten. Es wird häufig für Konfigurationsdateien verwendet. host: localhost
Im Gegensatz zu XML oder JSON ist YAML stark auf Lesbarkeit für port: 27017
•
Menschen ausgelegt. name: analytics
Typische Einsatzgebiete Merkmale
Konfigurationsdateien (z.B. Docker, Kubernetes) hierarchische Struktur über Einrückung
• •
CI/CD-Pipelines (z.B. GitHub Actions, GitLab CI) sehr kompakt und gut lesbar
• •
Machine-Learning-Workflows häufige Alternative zu JSON für Konfiguration
• •
Datenkonfiguration in Softwareprojekten
•
 YAML gehört zu den semi-strukturierten Datenformaten.
Datenbanken 2 Vorlesungsfolien 47

Kurze Einordnung: Parquet
Parquet – spaltenorientiertes Datenformat Merkmale
spaltenorientierte Speicherung  besonders effizient für
•
Einordnung analytische Abfragen
Apache Parquet ist ein spaltenorientiertes Datenformat, das hohe Kompression durch ähnliche Werte innerhalb einer
• •
für analytische Datenverarbeitung und große Datenmengen Spalte
entwickelt wurde. Schema und Datentypen werden gespeichert
•
Es wird häufig in Data Lakes, Data Warehouses und Big- optimiert für große analytische Datensätze
• •
Data-Systemen eingesetzt.
 Parquet speichert strukturierte Daten und wird vor allem für
Prinzip der spaltenorientierten Speicherung analytische Workloads verwendet.
Name: Anna | Jonas | Lea
Alter: 23 | 31 | 27
Stadt: Berlin | Hamburg | München
Datenbanken 2 Vorlesungsfolien 48

Ausblick: TOON
TOON – Token Optimized Object Notation Beispiel:
name: Anna
Einordnung
age: 23
TOON ist ein experimentelles Datenformat, das speziell für die
• city: Berlin
Verarbeitung durch Large Language Models (LLMs) entwickelt
wurde.
Merkmale
Ziel ist es, strukturierte Informationen mit möglichst wenigen
•
reduziert Token-Anzahl für LLM-Prompts
•
Tokens darzustellen.
einfacher, flacher Aufbau
•
derzeit kein etablierter Standard
Motivation •
LLMs verarbeiten Text als Tokens.
•
 TOON gehört – ähnlich wie JSON oder YAML – zu den semi-
Formate wie JSON enthalten viele zusätzliche Zeichen (z. B.
•
Klammern und Anführungszeichen), die ebenfalls Tokens strukturierten Datenformaten.
erzeugen.
TOON versucht daher, syntaktischen Overhead zu
•
reduzieren.
Datenbanken 2 Vorlesungsfolien 49

Einige Medium-Artikel zu Datenformaten
Beginner-Friendly Guide: https://medium.com/@asifazad114/why-file-formats-matter-a-beginner-friendly-guide-to-json-xml-csv-yaml-
•
parquet-and-markdown-007b4dc7df83
Understanding Data Formats: https://rathi-ankit.medium.com/understanding-data-formats-0851fe34c041
•
TOON vs. JSON vs CSV: https://medium.com/data-science-in-your-pocket/toon-vs-json-vs-csv-9cbfbb9a93f8
•
Bye bye JSON for LLMs: https://medium.com/data-science-in-your-pocket/toon-bye-bye-json-for-llms-91e4fe521b14
•
Datenbanken 2 Vorlesungsfolien 50

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 51

Offene Frage in die Runde
Was sind NoSQL-Datenbanken?
| Datenbanken 2 | Vorlesungsfolien | 52  |
| ------------- | ---------------- | --- |

NoSQL-Datenbanken
NoSQL steht für „Not only SQL“ – es handelt sich also nicht um anti-SQL, sondern um eine Alternative oder Ergänzung zu klassischen
relationalen Datenbanken.
Der Begriff bezeichnet Datenbanksysteme, die:
nicht relational aufgebaut sind (also keine Tabellen mit festen Schemata verwenden)

oft flexiblere Datenmodelle verwenden (z. B. Dokumente, Schlüssel-Wert-Paare, Graphen, Spalten)

besonders gut mit großen Datenmengen, verteilten Systemen und skalierbaren Anwendungen umgehen können

NoSQL-Systeme sind besonders nützlich, wenn:
die Daten nicht streng strukturiert sind (z. B. JSON, Logs, Nutzerprofile)

sich die Struktur häufig ändert (agile Entwicklung, Prototyping)

extrem viele Daten gespeichert oder schnell verarbeitet werden müssen (z. B. bei Webanwendungen, IoT, Social Media)

horizontale Skalierung erforderlich ist (z. B. in Cloud-Systemen oder Microservices)

Datenbanken 2 Vorlesungsfolien 53

Abgrenzung zu relationalen Datenbanken
Merkmal Relationale DB (z.B. PostgreSQL) NoSQL (z.B. MongoDB)
Struktur Tabellen mit festem Schema Flexibel (z.B. Dokumente)
|     | Datenmodell |     | Relational | z. B. dokumentenbasiert       |     |
| --- | ----------- | --- | ---------- | ----------------------------- | --- |
|     |             |     | SQL        | Eigene APIs oder JSON-Queries |     |
Abfragen
|               | Joins         |                  | Voll unterstützt | Eingeschränkt oder gar nicht     |     |
| ------------- | ------------- | ---------------- | ---------------- | -------------------------------- | --- |
|               | Transaktionen |                  | Stark            | Eingeschränkt oder anders gelöst |     |
|               | Skalierung    |                  | Vertikal         | Horizontal                       |     |
| Datenbanken 2 |               | Vorlesungsfolien |                  |                                  | 54  |

Vergleich SQL und NoSQL
https://pandorafms.com/blog/nosql-vs-sql-key-differences/
| Datenbanken 2 | Vorlesungsfolien | 55  |
| ------------- | ---------------- | --- |

Typen von NoSQL-Datenbanken
Es gibt verschiedene Kategorien, je nach Einsatzzweck:
Dokumentenorientiert → z.B. MongoDB, CouchDB
1.
Key-Value-Stores → z.B. Redis, Amazon DynamoDB
2.
Spaltenorientiert → z.B. Apache Cassandra, HBase
3.
Graphdatenbanken → z.B. Neo4j, ArangoDB
4.
Datenbanken 2 Vorlesungsfolien 56

Dokumentenorientiert
Speichern Daten als Dokumente (meist JSON/BSON oder XML-ähnliche Strukturen).
•
Flexible Schemas → Felder können sich zwischen Dokumenten unterscheiden.
•
Ideal für hierarchische und semi-strukturierte Daten.
•
Daten können verschachtelt werden (z.B. Arrays, Objekte).
•
Abfragen oft über Schlüssel und Attribute innerhalb der Dokumente.
•
Datenbanken 2 Vorlesungsfolien 57

Key-Value-Stores
Einfachstes Modell: Schlüssel (Key) → Wert (Value).
•
Sehr hohe Performance bei einfachen Lese-/Schreiboperationen.
•
Werte können beliebige Datentypen sein (Strings, JSON, BLOBs).
•
Gut für Caches, Session-Management, schnelle Lookups.
•
Abfragen sind in der Regel nur über den Schlüssel möglich.
•
Datenbanken 2 Vorlesungsfolien 58

Spaltenorientiert
Daten in Tabellen mit Zeilen und Spalten, aber Fokus liegt auf Spaltenfamilien statt ganzen Zeilen.
•
Eignet sich für sehr große, verteilte Datenmengen.
•
Optimiert für hohe Schreib- und Lese-Performance bei großen Datenmengen.
•
Abfragen oft über bestimmte Spalten oder Spaltenbereiche.
•
Beliebt für Big-Data-Analytics, Zeitreihendaten, Logging.
•
https://de.wikipedia.org/wiki/Spaltenorientierte_Datenbank
Datenbanken 2 Vorlesungsfolien 59

Graphdatenbanken
Daten als Knoten (Entities) und Kanten (Beziehungen) gespeichert.
•
Beziehungen sind erstklassige Objekte (nicht nur Fremdschlüssel).
•
Sehr effizient für komplexe Beziehungsabfragen (z.B. „Kürzester Pfad“).
•
Nutzen eigene Abfragesprachen (z.B. Cypher in Neo4j).
•
Ideal für soziale Netzwerke, Empfehlungs-Engines, Betrugserkennung.
•
https://de.wikipedia.org/wiki/Graphdatenbank
Datenbanken 2 Vorlesungsfolien 60

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 61

Einführung in MongoDB
Was ist MongoDB?
MongoDB ist eine dokumentenorientierte NoSQL-Datenbank

Daten werden als JSON-ähnliche Dokumente (genauer: Binary JSON, bzw. BSON) gespeichert

Entwickelt für hohe Flexibilität, horizontale Skalierbarkeit und schnelle Entwicklung

Besonders beliebt im Web- und App-Bereich

|     | Begriff    | Entspricht in SQL | Beschreibung                         |     |
| --- | ---------- | ----------------- | ------------------------------------ | --- |
|     | Datenbank  | Datenbank         | Sammler für mehrere Collections      |     |
|     | Collection | Tabelle           | Enthält viele Dokumente gleicher Art |     |
|     | Dokument   | Zeile (Record)    | JSON-Objekt mit freier Struktur      |     |
|     |            | Spalte            | Schlüssel in einem Dokument          |     |
Feld (Key)
Dokument:
| Datenbanken 2 |     | Vorlesungsfolien |     | 62  |
| ------------- | --- | ---------------- | --- | --- |

Einsatzszenarien
Typische Einsatzszenarien
Webanwendungen (z.B. Nutzerprofile, Foren, Kommentare)

Content-Plattformen und CMS

Prototypen und Startups mit sich ändernden Anforderungen

IoT & Event-Logging

Systeme mit vielen, schnell wachsenden Daten

Datenbanken 2 Vorlesungsfolien 63

MongoDB im Kontext von Data Science
Warum ist MongoDB für Data Science interessant?
Flexible Datenstruktur

Ideal für heterogene, halbstrukturierte oder sich ständig ändernde Daten (z. B. Logdaten, Sensordaten, Nutzerverhalten)

Kein aufwendiges Aufbereiten in ein starres relationales Schema nötig

Nahtlose Integration mit modernen Programmiersprachen

Gute Anbindung an Python (z.B. via pymongo) → direkte Nutzung in Jupyter Notebooks

JSON-artiges Datenmodell passt gut zu typischen Datenstrukturen in Pandas, NumPy etc.

Schnelles Prototyping & Datenzugriff

Ideal für explorative Datenanalyse

Einfache Abfragen mit find(), Aggregations-Framework, Indexunterstützung

Skalierbarkeit bei großen Datenmengen

MongoDB eignet sich für die Vorphase der Analyse, wenn Daten noch gesammelt, gecleant oder angereichert werden müssen

Datenbanken 2 Vorlesungsfolien 64

Grundlegende MongoDB-Befehle
1. Datenbank & Collection auswählen/erstellen
use meineDatenbank // Wechselt zur DB (wird angelegt, falls nicht vorhanden)
db.createCollection("buecher")
2. Einfügen eines Dokuments
db.buecher.insertOne({
titel: "MongoDB verstehen",
autor: "Max Schröder",
jahr: 2022
})
3. Mehrere Dokumente einfügen
db.buecher.insertMany([
{ titel: "Datenanalyse", autor: "Anna", jahr: 2021 },
{ titel: "KI kompakt", autor: "Jana", jahr: 2023 }
])
Datenbanken 2 Vorlesungsfolien 65

Grundlegende MongoDB-Befehle (cont‘d)
4. Alle Dokumente anzeigen
db.buecher.find()
5. Dokumente filtern
db.buecher.find({ autor: "Anna" }) // einfache Abfrage
db.buecher.find({ jahr: { $gt: 2021 } }) // Jahr > 2021
6. Ein Dokument aktualisieren
db.buecher.updateOne(
{ titel: "Datenanalyse" },
{ $set: { jahr: 2022 } }
)
7. Ein Dokument löschen
db.buecher.deleteOne({ titel: "KI kompakt" })
Datenbanken 2 Vorlesungsfolien 66

Vergleichsoperatoren in MongoDB
|     | Operator |     | Bedeutung   | Beispiel                 |     |
| --- | -------- | --- | ----------- | ------------------------ | --- |
|     | $gt      |     | größer als  | { preis: { $gt: 10 } }   |     |
|     |          |     | kleiner als | { seiten: { $lt: 300 } } |     |
$lt
|               | $gte |                  | größer oder gleich  | { jahr: { $gte: 2020 } }        |     |
| ------------- | ---- | ---------------- | ------------------- | ------------------------------- | --- |
|               | $lte |                  | kleiner oder gleich | { alter: { $lte: 18 } }         |     |
|               | $eq  |                  | gleich              | { sprache: { $eq: "Deutsch" } } |     |
|               | $ne  |                  | ungleich            | { autor: { $ne: "Anna" } }      |     |
| Datenbanken 2 |      | Vorlesungsfolien |                     |                                 | 67  |

Updateoperatoren in MongoDB
| Operator | Beschreibung | Beispiel |     |
| -------- | ------------ | -------- | --- |
Wert eines Felds setzen oder aktualisieren { $set: { jahr: 2023 } }
$set
| $unset | Feld entfernen | { $unset: { seitenzahl: "" } } |     |
| ------ | -------------- | ------------------------------ | --- |
$inc Numerischen Wert erhöhen oder verringern { $inc: { seitenzahl: 50 } }
| $rename | Feld umbenennen                | { $rename: { autor: "verfasser" } } |     |
| ------- | ------------------------------ | ----------------------------------- | --- |
|         | Wert zu einem Array hinzufügen | { $push: { tags: "NoSQL" } }        |     |
$push
$pull Wert aus einem Array entfernen { $pull: { tags: "Lehrbuch" } }
$addToSet Wert zu Array hinzufügen, nur wenn nicht vorhanden { $addToSet: { tags: "Datenbank" } }
Beispiele:
| Datenbanken 2 | Vorlesungsfolien |     | 68  |
| ------------- | ---------------- | --- | --- |

w3schools Tutorial zu MongoDB
https://www.w3schools.com/mongodb/index.php
| Datenbanken 2 | Vorlesungsfolien | 69  |
| ------------- | ---------------- | --- |

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 70

Python in dieser Veranstaltung
Für die Entwicklung der Datenanwendungen verwenden wir Python. Python ist eine weit verbreitete Programmiersprache für Datenanalyse, Data
Science, Machine Learning, Datenverarbeitung u.v.m.  Viele Bibliotheken für Datenbanken und Datenanalyse sind direkt für Python verfügbar.
Hinweis für die Veranstaltung
In dieser Veranstaltung verwenden wir Python hauptsächlich für:
Einlesen und Verarbeiten von Daten
•
Zugriff auf Datenbanken
•
Visualisierung mit Streamlit
•
Vorkenntnisse
Grundlegende Programmierkenntnisse (z.B. aus Java) sind ausreichend.
•
Die wichtigsten Python-Konzepte werden kurz wiederholt.
•
Datenbanken 2 Vorlesungsfolien 71

Wichtige Unterschiede zwischen Java und Python
|     | Aspekt |     | Java                 | Python                       |     |
| --- | ------ | --- | -------------------- | ---------------------------- | --- |
|     | Syntax |     | stärker formalisiert | kompakte und einfache Syntax |     |
|     |        |     | statisch typisiert   | dynamisch typisiert          |     |
Typisierung
Programmstruktur Klassen und Methoden erforderlich auch einfache Skripte möglich
Blockstruktur geschweifte Klammern {} Einrückung (Indentation)
Variablen Typ muss angegeben werden Typ wird automatisch bestimmt
| Datenbanken 2 |     | Vorlesungsfolien |     |     | 72  |
| ------------- | --- | ---------------- | --- | --- | --- |

Beispiele: Java vs. Python
Variablendeklaration
Java
int age = 23;
String name = "Anna";
Python
age = 23
name = "Anna"
Datenbanken 2 Vorlesungsfolien 73

Beispiele: Java vs. Python (cont‘d)
Bedingung (if / else)
Java
if (age >= 18) {
System.out.println("Adult");
} else {
System.out.println("Minor");
}
Python
if age >= 18:
print("Adult")
else:
print("Minor")
Datenbanken 2 Vorlesungsfolien 74

Beispiele: Java vs. Python (cont‘d)
Schleife (for)
Java
for (int i = 0; i < 3; i++) {
System.out.println(i);
}
Python
for i in range(3):
print(i)
Datenbanken 2 Vorlesungsfolien 75

Beispiele: Java vs. Python (cont‘d)
Array vs. Liste
Java
int[] numbers = {1, 2, 3};
System.out.println(numbers[0]);
Python
numbers = [1, 2, 3]
print(numbers[0])
Datenbanken 2 Vorlesungsfolien 76

Beispiele: Java vs. Python (cont‘d)
HashMap vs. Dictionary
Java (HashMap) Python (Dictionary)
import java.util.HashMap; ages = {
"Anna": 23,
HashMap<String, Integer> ages = new "Jonas": 31
HashMap<>(); }
ages.put("Anna", 23); print(ages["Anna"])
ages.put("Jonas", 31);
System.out.println(ages.get("Anna"));
Datenbanken 2 Vorlesungsfolien 77

Wichtige Python-Bibliotheken für die Datenverarbeitung
Bibliothek Zweck
pandas Verarbeitung und Analyse von Daten
mysql-connector Zugriff auf MySQL-Datenbanken
pymongo Zugriff auf MongoDB
Datenbanken 2 Vorlesungsfolien 78

Datenverarbeitung mit Pandas
Einordnung
Pandas ist eine weit verbreitete Python-Bibliothek zur Verarbeitung und Analyse von Daten.
•
Sie wird häufig verwendet für
•
das Einlesen von Datensätzen
•
die Verarbeitung tabellarischer Daten
•
einfache Datenanalysen
•
Zentrale Datenstruktur
Die wichtigste Datenstruktur in Pandas ist der DataFrame.
•
Ein DataFrame ist eine tabellarische Datenstruktur, ähnlich wie eine Tabelle in einer Datenbank oder eine Excel-Tabelle.
•
Datenbanken 2 Vorlesungsfolien 79

Pandas Dataframe
https://www.w3schools.com/python/pandas/pandas_dataframes.asp
| Datenbanken 2 | Vorlesungsfolien | 80  |
| ------------- | ---------------- | --- |

Einlesen externer Daten mit Pandas
Einordnung Beispiel:
Pandas bietet Funktionen zum Einlesen von Daten aus import pandas as pd
verschiedenen Quellen.
df = pd.read_csv("data.csv")
Zu diesen zählen insb.:
CSV-Dateien print(df.head())
•
JSON-Dateien
•
Excel-Dateien Erklärung
•
Parquet-Dateien read_csv() lädt eine CSV-Datei
• •
das Ergebnis ist ein DataFrame
•
Die eingelesenen Daten werden als DataFrame gespeichert. head() zeigt die ersten Zeilen des Datensatzes
•
Datenbanken 2 Vorlesungsfolien 81

Arbeiten mit DataFrames: Typische Funktionen
Datensatz anzeigen: df.head()

Anzahl der Zeilen und Spalten: df.shape

Spalten auswählen: df["age"]

Zeilen filtern: df[df["age"] > 30]

Einfache Statistik berechnen: df.describe()

 Weitere Funktionen und Beispiele u.a. unter https://pandas.pydata.org/docs/user_guide/10min.html
Datenbanken 2 Vorlesungsfolien 82

Zugriff auf MySQL mit Python
Einordnung
Python kann über spezielle Bibliotheken mit relationalen Datenbanken kommunizieren.
•
Diese Bibliotheken stellen eine Schnittstelle zwischen Python und dem Datenbanksystem bereit.
•
Typischer Ablauf:
Verbindung zur Datenbank herstellen
•
SQL-Abfrage ausführen
•
Ergebnisse auslesen und weiterverarbeiten
•
Bibliothek
Für MySQL verwenden wir in dieser Veranstaltung mysql-connector-python. Diese Bibliothek ermöglicht es, SQL-Abfragen direkt aus Python
heraus auszuführen.
Datenbanken 2 Vorlesungsfolien 83

Zugriff auf MySQL mit Python – Beispiel
Bibliothek installieren (mit pip): pip install mysql-connector-python
Beispiel: Verbindung herstellen und Daten abfragen
Verbindung zur Datenbank aufbauen
SQL-Abfrage ausführen
Ergebnisse weiterverarbeiten
Verbindung schließen
Datenbanken 2 Vorlesungsfolien 84

SQL-Daten in DataFrame laden
Einordnung
SQL-Abfragen können direkt in Pandas DataFrames geladen werden. Dadurch lassen sich Daten aus Datenbanken leicht weiter analysieren.
| Datenbanken 2 | Vorlesungsfolien | 85  |
| ------------- | ---------------- | --- |

Zugriff auf MongoDB mit Python
Bibliothek installieren (mit pip): pip install pymongo Ergänzung: MongoDB-Dokumente werden in Python als Dictionaries
dargestellt, z.B.:
Beispiel:
{
"name": "Anna",
"age": 23,
"city": "Berlin"
}
Datenbanken 2 Vorlesungsfolien 86

MongoDB-Daten in DataFrame laden
Einordnung
Dokumente aus MongoDB können in Python abgefragt und anschließend in einen Pandas DataFrame überführt werden.
| Datenbanken 2 | Vorlesungsfolien | 87  |
| ------------- | ---------------- | --- |

Datenbankoperationen mit Python
Einordnung
Mit Python-Bibliotheken wie mysql.connector und pymongo können Datenbanken vollständig aus Programmen heraus gesteuert werden.
Typische Operationen sind:
Operation Bedeutung
Create neue Daten einfügen
Read Daten abfragen
Update vorhandene Daten ändern
Delete Daten löschen
Beispiele (Read)
MySQL: cursor.execute("SELECT * FROM users")
•
MongoDB: collection.find()
•
Datenbanken 2 Vorlesungsfolien 88

W3schools Tutorials
Python Grundlagen: https://www.w3schools.com/python/default.asp
•
Pandas: https://www.w3schools.com/python/pandas/default.asp
•
Python MySQL: https://www.w3schools.com/python/python_mysql_getstarted.asp
•
Python MongoDB: https://www.w3schools.com/python/python_mongodb_getstarted.asp
•
Datenbanken 2 Vorlesungsfolien 89

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 90

Streamlit
“Streamlit is a free and open-source framework to rapidly build and share beautiful machine learning and data science web apps.
It is a Python-based library specifically designed for machine learning engineers. Data scientists or machine learning engineers are not web
developers and they're not interested in spending weeks learning to use these frameworks to build web apps. Instead, they want a tool that is
easier to learn and to use, as long as it can display data and collect needed parameters for modeling.
Streamlit allows you to create a stunning-looking application with only a few lines of code” (datacamp).
Datenbanken 2 Vorlesungsfolien 91

Einführung Streamlit
Was ist Streamlit?
Streamlit ist ein Open-Source-Python-Framework, das es ermöglicht, interaktive Webanwendungen für Datenanalysen und maschinelles Lernen
mit minimalem Codeaufwand zu erstellen.
Entwicklung und Veröffentlichung
Entwickelt im Jahr 2018 von Adrien Treuille, Amanda Kelly und Thiago Teixeira, wurde die erste Version von Streamlit im Oktober 2019
veröffentlicht und gewann schnell an Beliebtheit, insb. unter Data-Scientists und Data-Engineers.
Einsatzmöglichkeiten:
Interaktive Dashboards: Erstellung von Dashboards zur Visualisierung von Daten in Echtzeit (d.h. Einsatz als BI-Tool möglich).

Machine-Learning-Modelle: Bereitstellung und Visualisierung von ML-Modellen für Endnutzer.

Datenexploration: Schnelle und einfache Datenexploration mit interaktiven Widgets.

Prototyping: Rasche Entwicklung und Testung von Datenanwendungen und -ideen.

Datenbanken 2 Vorlesungsfolien 92

Beispiel Streamlit
https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/ und
https://github.com/dataprofessor/population-dashboard/blob/master/streamlit_app.py
| Datenbanken 2 | Vorlesungsfolien | 93  |
| ------------- | ---------------- | --- |

Einige wichtige Streamlit-Komponenten
Layout und Anzeige Interaktive Widgets
st.title() st.button()
• •
st.header() st.slider()
• •
st.write() st.selectbox()
• •
st.dataframe() st.text_input()
• •
st.table() st.checkbox()
• •
st.image()
•
Layout
Visualisierung st.sidebar
•
st.line_chart() st.columns
• •
st.bar_chart()
•
st.map()
•
Datenbanken 2 Vorlesungsfolien 94

Architektur einer analytischen Datenanwendungen in dieser Veranstaltung
|     |                |     | Daten-       |           | Analyse-    |     |
| --- | -------------- | --- | ------------ | --------- | ----------- | --- |
|     | Datenquelle(n) |     |              | Datenbank |             |     |
|     |                |     | aufbereitung |           | anwendung   |     |
|     |  Kaggle       |     |  Pandas     |  MySQL   |  Streamlit |     |
 MongoDB
| Datenbanken 2 |     | Vorlesungsfolien |     |     |     | 95  |
| ------------- | --- | ---------------- | --- | --- | --- | --- |

Streamlit: Getting started
Installieren Sie Streamlit und machen sich Sie sich mit den Funktionen der Library vertraut.

Hier einige hilfreiche Links:

Streamlit-Documentation – Get started (sehr hilfreich!): https://docs.streamlit.io/get-started

Dashboard-Tutorial: https://blog.streamlit.io/crafting-a-dashboard-app-in-python-using-streamlit/

Zugehöriger Code: https://github.com/dataprofessor/population-dashboard/blob/master/streamlit_app.py

Zugehöriges Frontend: https://population-dashboard.streamlit.app/?ref=blog.streamlit.io

Ganz einfache Streamlit-App: https://medium.com/@chaitanyasirivuri/building-your-first-streamlit-app-a-step-by-step-tutorial-

e058d5dfe5f4
Streamlit-Tutorial von datacamp: https://www.datacamp.com/tutorial/streamlit

Etwas Inspiration: https://github.com/jrieke/best-of-streamlit

Falls Sie Probleme mit der lokalen Installation haben sollten, nutzen Sie Google Colab, siehe z.B. hier: https://discuss.streamlit.io/t/how-to-

launch-streamlit-app-from-google-colab-notebook/42399
Lassen Sie sich gerne so viel wie nötig von einer KI Ihrer Wahl helfen.

Datenbanken 2 Vorlesungsfolien 96

Agenda
Organisatorisches

Einführung: Moderne Datenanwendungen

Datenformate und semi-strukturierte Daten

NoSQL-Datenbanken

Dokumentenorientierte Datenspeicherung mit MongoDB

Datenverarbeitung und Datenbankanbindung mit Python

Entwicklung von Datenanwendungen mit Streamlit

Projektarbeit: Entwicklung einer eigenen Datenanwendung

Präsentation und Diskussion der Projekte

Datenbanken 2 Vorlesungsfolien 97

MySQL-Datenbank über phpMyAdmin nutzen (neue User!)
Link: https://wi-web.heilbronn.dhbw.de/phpmyadmin/ oder http://10.150.16.50/phpmyadmin/
•
Initialpasswort für alle User: WI2026!InitPwd
•
User: WI24A2_3_DB_User + [ihre Nummer]  d.h. z.B. WI24A2_3_DB_User5, WI24A2_3_DB_User22, usw.
•
Achtung: Datenbanken immer mit User-Präfix anlegen, d.h. z.B. WI24A2_3_DB_User2_DB1
•
Datenbanken 2 Vorlesungsfolien 98

Datenbankzugriff MongoDB wird nachgereicht
Per Moodle
•
| Datenbanken 2 | Vorlesungsfolien | 99  |
| ------------- | ---------------- | --- |

Projektarbeit: Entwicklung einer Datenanwendung
Aufgabe
Entwickeln Sie eine interaktive Datenanwendung mit Streamlit, die einen öffentlich verfügbaren Datensatz analysiert und visualisiert.
Mögliche Datenquellen:
Kaggle
•
Open Data Portale
•
öffentliche APIs
•
andere frei verfügbare Datensätze
•
Ziel der Anwendung
Die Anwendung soll es ermöglichen,
Daten interaktiv zu erkunden
•
Visualisierungen zu erzeugen
•
interessante Zusammenhänge im Datensatz sichtbar zu machen.
•
Datenbanken 2 Vorlesungsfolien 100

Mindestanforderungen an die Datenanwendung
Die entwickelte Anwendung sollte folgende Elemente enthalten:
Datenquelle: Einlesen eines externen Datensatzes (z.B. Kaggle, Open Data, API)

Datenverarbeitung: Verarbeitung oder Transformation der Daten mit Pandas
•
Datenbanken: Die Daten sollen in zwei unterschiedlichen Datenbanksystemen gespeichert werden:
•
MySQL (relationale Datenbank)
•
MongoDB (NoSQL-Datenbank)
•
Die Anwendung soll Daten aus diesen Datenbanken lesen und verwenden.
•
Interaktive Anwendung: Entwicklung einer Streamlit-App mit mindestens einem interaktiven Widget (z.B. Filter oder Auswahl)
•
Visualisierung: mindestens eine grafische Darstellung der Daten
•
Datenbanken 2 Vorlesungsfolien 101

Präsentation der Ergebnisse
Am Ende der Veranstaltung präsentieren Sie Ihre Anwendung kurz.
Inhalt der Präsentation
Vorstellung des Datensatzes
•
Ziel der Anwendung
•
kurze Demonstration der App
•
wichtigste Erkenntnisse aus der Datenanalyse
•
Dauer: ca. 5 Minuten pro Person
Datenbanken 2 Vorlesungsfolien 102

Prüfungsleistung: Schriftliches Assignment
Zusätzlich zur Anwendung erstellen Sie einen Projektbericht (5–10 Seiten).
Der Bericht sollte folgende Punkte enthalten:
Beschreibung des Datensatzes
•
Ziel der Anwendung
•
Aufbau und Funktionsweise der Anwendung
•
verwendete Technologien (Python, Pandas, Streamlit)
•
zentrale Ergebnisse oder Erkenntnisse
•
Abgabedeadline: TBD
Datenbanken 2 Vorlesungsfolien 103

| Datenbanken 2 | Vorlesungsfolien | 104 |
| ------------- | ---------------- | --- |