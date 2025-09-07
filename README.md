FAKSGPX

Import av GPX-filer til FAKS fra Ut.no feiler på grunn av FAKS sin logikk for å optimalisere GPX-filen. Ut.no sine GPX-filer har identiske tidsstempel på alle punkter. Dette gjør at FAKS ignorer alle unntatt 1 punkt.
Dette Python-scipter går gjennom alle tidsstempel og legger til ett sekund for hvert tidsstempel.
