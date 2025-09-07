import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import argparse
import os

def fiks_gpx_tidspunkter(input_fil, output_fil):
	"""
	Leser en GPX-fil, øker tidspunktet for hvert sporpunkt med ett sekund,
	og lagrer resultatet i en ny fil.
	"""
	# Nødvendig for å håndtere navnerommet i GPX-filer korrekt
	ET.register_namespace('', "http://www.topografix.com/GPX/1/1")
	namespace = {'gpx': 'http://www.topografix.com/GPX/1/1'}

	try:
		tree = ET.parse(input_fil)
		root = tree.getroot()

		tidspunkter = root.findall('.//gpx:trkpt/gpx:time', namespace)

		if not tidspunkter:
			print(f"Fant ingen tidspunkter (<time>) i filen '{input_fil}'. Ingen endringer gjort.")
			return

		start_tid_str = tidspunkter[0].text
		gjeldende_tid = datetime.fromisoformat(start_tid_str.replace('Z', '+00:00'))

		for i in range(1, len(tidspunkter)):
			gjeldende_tid += timedelta(seconds=1)
			ny_tid_str = gjeldende_tid.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
			tidspunkter[i].text = ny_tid_str

		tree.write(output_fil, encoding='UTF-8', xml_declaration=True)
		print(f"✅ Filen er vellykket behandlet og lagret som: {output_fil}")

	except FileNotFoundError:
		print(f"❌ FEIL: Fant ikke filen '{input_fil}'. Sjekk at navnet og stien er korrekt.")
	except ET.ParseError:
		print(f"❌ FEIL: Klarte ikke å lese filen '{input_fil}'. Er det en gyldig GPX/XML-fil?")
	except Exception as e:
		print(f"En uventet feil oppstod: {e}")

if __name__ == '__main__':
	# 1. Sett opp argument-parseren for å håndtere input fra kommandolinjen
	parser = argparse.ArgumentParser(
		description="Korrigerer tidspunkter i en GPX-fil ved å legge til ett sekund per punkt.",
		epilog="Eksempel: python3 %(prog)s min_tur.gpx"
	)
	# 2. Definer hvilket argument vi forventer: en posisjonell 'input_fil'
	parser.add_argument('input_fil', help="Stien til den originale GPX-filen som skal behandles.")
	
	# 3. Les argumentene som ble gitt da scriptet ble kjørt
	args = parser.parse_args()
	
	# 4. Lag output-filnavnet automatisk basert på input-filnavnet
	base, ext = os.path.splitext(args.input_fil)
	output_filnavn = f"{base}_fiks{ext}"
	
	# 5. Kall kjernefunksjonen med filnavnene
	fiks_gpx_tidspunkter(args.input_fil, output_filnavn)