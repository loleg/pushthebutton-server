# pushthebutton-server
An #opentourism 2017 project
Please see [here for the node hardware and sofware part](https://github.com/morgulbrut/opendata_lora_circuitpython)

# Push the Button to Get Started
**Der einfachste Zufriedenheitstracker für Tourismusregionen -- mit grossem Potenzial**

## Zusammenfassung
Der Mülleimer quillt über? Bei der Feuerstelle fehlt das Holz? Bislang machten viele Gäste die Faust im Sack. Neu hauen sie höchstens mit der Faust auf den Knopf. Schon ist die Gemeinde über den Missstand informiert und kann ihn beheben. Die unmittelbare Kundenbefragung ist aber nur ein Vorteil, den das Internet der Dinge einer Tourismusregion bietet. Dank eines flächendeckenden und energiesparenden Netzwerkes lassen sich mit bescheidenen finanziellen Mitteln auch neuartige Dienstleistungen realisieren. 

## Hintergrund
Die Anforderungen an die Tourismusdestinationen sind gestiegen. Grossen Wert legen die Gäste insbesondere auf eine gut funktionierende Infrastruktur. Und sie erwarten, dass Informationen zu den Angeboten und zur aktuellen Situation im Gebiet problemlos zugänglich sind. Dank neuer Technologie wie dem Funkstandard LoRaWAN sowie Mikrokontrollern und Sensoren lassen sich solche Dienstleistungen heute mit vergleichsweise tiefen Investitionskosten aufbauen. Eine Investition, die sich auszahlen könnte. 

## Ideen
- Push the Button: Bislang werden Umfragen zur Kundenzufriedenheit stets nachträglich gemacht. Weshalb befragt man die Gäste nicht dann, wenn sie etwas erleben -- auf dem Berggipfel, bei der Brätlistelle, beim Besuch des Bärenparks. Die Fragen können beliebig angepasst werden. 
- Values for free: Wie warm ist der Badeweiher? Wie stark weht der Wind auf dem Gipfel? Die Gäste können die aktuellen Messdaten der im gesamten Tourismusgebiet installierten Sensoren jederzeit im Web abrufen.  
- Book it to my Room: Die Gäste können an beliebigen Orten Dienstleistungen in Anspruch nehmen oder Produkte kaufen -- und die Kosten direkt auf die Hotelrechnung buchen lassen. Dazu halten sie lediglich ihre RFID-Karte aufs entsprechende Bezahlterminal. 
- Surprise, Surprise! Sie möchten die Liebste ganz besonders verwöhnen? Dann bestellen Sie eine Flasche Sekt auf den Berggipfel. Nichts ist einfacher als das: Der Batch wird an die Bestellsäule gehalten -- wenig später bringt eine Drohne die Überraschung. 


## Feldtest
Das Ziel ist, am Ende des Hackatlons einen Button mit auf die Mapatlon Führung mitzunehmen und an diversen Orten den Knopf zu drücken. Mittels GPS Daten von einem Smartphone und dem Zeitpunkt sowie einer Numerierung kann danach eruiert werden, ob das Signal angekommen ist. 
Nach Möglichkeit werden Passanten nach ihrer Meinung über die Grundidee befragt.

Angebote wie diese bieten diverse Vorteile: 
- Die Gäste profitieren von zusätzlichen Dienstleistungen. Die Zufriedenheit steigt, wenn sich Gäste ernst genommen fühlen. 
- Die Wartung der Infrastruktur wird vereinfacht. So kann etwa der Wegmeister sofort reagieren, wenn Gäste bei einer Brätlistelle das Brennholz vermissen oder wenn irgendwo Probleme mit der Infrastruktur bestehen. Wo gemäss den Angaben der Gäste Probleme bestehen, ist jederzeit auf einer Karte ersichtlich. Zudem können Notifikationen verschickt werden.
- Die Tourismusverantwortlichen erhalten zusätzliche Informationen zum Nutzerverhalten. So lässt sich etwa erheben, welche Wanderwege besonders intensiv genutzt werden -- und welche nicht. Eine Optimierung kann somit gerechtfertigt werden.
- Der Aufbau einer solchen Infrastruktur dürfte auf grosses Medieninteresse sowie vielen Posts auf den sozialen Netzwerken führen. Der dadurch erzielte Werbeeffekt dürfte die Investitionen bei Weitem wett machen. Angebote wie "Surprise, Surprise!" eignen sich zudem vortrefflich für Werbekampagnen. 
-  Der positive Effekt auf die Medien als "First Mover" als eine vernetzte Destination wird auch andere Ferienregionen zum nachahmen bewegen.

## Technische Umsetzung
### Infrastruktur
Die Datenübertragung erfolgt über die Funktechnik [LoRaWAN](https://de.wikipedia.org/wiki/Long_Range_Wide_Area_Network). Damit können Daten bei sehr geringem Energieverbrauch über grosse Distanzen übermittelt werden. Damit können Zufriedensheitstracker an beliebigen Stellen platziert werden -- unabhängig von Infrasturktur wie konventioneller Mobilnetzabdeckung und Stomverfügbarkeit. Der Empfang und die Verarbeitung der Daten erfolgt durch das nicht kommerzielle [The Things Network](https://www.thethingsnetwork.org). Damit fallen für die unmittelbare Übertragung keine Extrakosten an. Bei technischen Problemen kann in der "The Things Network"-Gemeinschaft nachgefragt oder bei der [Open Network Infrastructure Association](https://opennetworkinfrastructure.org/) nachgefragt werden. Ist kommerzieller Support nötig oder soll der Gateway nicht selber betrieben werden, können die Übertragungsleistungen bei der [Swisscom](http://lpn.swisscom.ch/d/) eingekauft werden. Nachfolgend wird eine Installation mit dem "The Things Network" beschrieben. 

### Gateway
Die Gemeinde installiert einen Gateway für das "The Things Network". Dieser empfängt die Daten, die von den einzelnen Nodes gesendet werden, und verarbeitet sie. Die einmaligen Anschaffungskosten für den [Gateway](https://shop.thethingsnetwork.com/index.php/product/the-things-gateway/) betragen derzeit rund 350 Franken. Zur Abdeckung der gesamten Region inklusive der näheren Teile des Skigebiets sind vermutlich zwei Gateways nötig. Der Gateway wird via Ethernet ans Internet angeschlossen. Benötigt wird zudem Strom (konventionell oder übers Ethernet-Kabel).  

#### Erste Ideen für mögliche Standorte
Wo die Gateways installiert werden können, müsste im Detail abgeklärt werden. Ideal sind Standorte, zu denen von möglichst vielen Punkten eine Sichtverbindung besteht. Diskutiert werden könnte etwa über die auf [dieser Karte markierten Standorte](http://umap.osm.ch/de/map/lorawan-vorschlage-arosa_909#15/46.7844/9.6638). 

[![alt text](http://wortaholic.ch/div/hackarosa/lorawanstandorte.png "Bitte klicken für interaktive Karte")](http://umap.osm.ch/de/map/lorawan-vorschlage-arosa_909#15/46.7844/9.6638)

### Nodes
Die Sendegeräte bestehen aus einer Mikro-Platine sowie einem Sendemodul und einer Antenne. Gespiesen werden die Geräte durch einen kleinen Akku. An diese können je nach Bedarf Sensoren angeschlossen werden. Je nach Konfiguration und angeschlossenen Sensoren können die Geräte mehrere Monate bis zu wenigen Jahren mit einer Akkuladung betrieben werden. Wobei auch eine verkürzte Akkuladung kein Problem darstellt, da die Standorte der Sensoren ohnehin regelmässig von Mitarbeiter der Destination kontrolliert wird.

#### Sensoren
Je nach Einsatzsznario kommen unterschiedliche Sensoren zum Einsatz. 
- Knopf, Schalter
- Lichtsensor
- Temperatur- und Feuchtigkeitssensor
- Mikrofon

## Inspirationsquellen
- [Züri wie neu](https://www.zueriwieneu.ch/) (Melden von Schäden an der Infrastruktur, basiert auf [FixMyStreet](http://fixmystreet.org/))
- [Mark-a-Spot](http://mark-a-spot.org/) [Open311 integriert](http://wiki.open311.org/Mark-a-Spot/)
- [The Hiveeyes Project](https://hiveeyes.org/) (für die Offenheit)
- [Amazon Dash](https://www.amazon.com/Dash-Buttons/) (for the pervasiveness)
- [Drohnen bringen Champagner](https://www.youtube.com/watch?v=ytqeBpYXtiw)
- [Feedback-Button von Lobaro](http://feedback-button.de/) (ein Zufriedenheitstracker aus Deutschland)
- [Feedback-Button von Proxidyne](https://proxidyne.com/products/lorawan-sensors/sensor-buttons/) (ein Zufriedenheitstracker aus Chicago)
