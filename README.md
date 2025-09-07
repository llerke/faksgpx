FAKSGPX

Import av GPX-filer til FAKS fra Ut.no feiler på grunn av FAKS sin logikk for å optimalisere GPX-filen. Ut.no sine GPX-filer har identiske tidsstempel på alle punkter. Dette gjør at FAKS ignorer alle unntatt 1 punkt.
Dette Python-sciptet går gjennom alle tidsstempel og legger til ett sekund for hvert tidsstempel.


Last ned filen.
Åpne en terminal eller kommandolinje.
Scriptet forutsetter at Python-filen og GPX-filen du vil modifisere ligger i samme mappe.
Naviger til mappen der du har lagret både scriptet og GPX-filen din.
Kjør scriptet med filnavnet: Nå kjører du scriptet og gir navnet på GPX-filen som et argument etterpå.

Eksempel 1: Enkel fil
python3 faksgpx.py Storhogda.gpx
(Dette vil lage en ny fil som heter Storhogda_fiks.gpx)

Eksempel 2: Filnavn med mellomrom
Hvis filnavnet inneholder mellomrom, må du sette det i anførselstegn:
python3 faksgpx.py "Min tur til fjellet.gpx"
(Dette vil lage Min tur til fjellet_fiks.gpx)
