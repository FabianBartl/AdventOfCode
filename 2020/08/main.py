
import os, sys

"""
Bestandteile:
(1) Akkumulator      - Accumulator
(2) Befehls-Zähler   - Instruction counter (Program index)
(3) Befehls-Register - Instruction register
(4) Programmspeicher - Program memory
(5) Datenspeicher    - Data memory

Datenstrukturen:
(1): INT
(2): INT
(3): TUPLE [STR, INT]
(4): LIST [ TUPLE [STR, INT], ... ]
(5): DICT { INT: INT, ... }
"""

# Objekt Registermaschine
class RM:
	# Konstruktor
	def __init__(self, file_name):
		# INIT Befehl an Position 0 setzen
		self.pmem = [["nop", +0]]
		# Programmspeicher mit Code aus Datei füllen
		with open(os.path.join(file_name), "r") as file:
			line_list = file.readlines()
			list = [ line.replace("\n", "").split(" ") for line in line_list if not (line.replace("\n", "").startswith("#") or line.replace("\n", "") == "")]
			tuple_list = [ [str(tuple[0]), int(tuple[1])] for tuple in list ]
		self.pmem.extend(tuple_list)
		self.pmem.append(["hlt", +0])
		# Akkumulator und Befehls-Zähler
		self.accu = 0
		self.cind = 0
		# Befehls-Register
		"""
		Das Befehls-Register existiert nicht als eigenständiges Attribut, sondern setzt sich als Befehl und zugehöriger Funktion aus CREG und als Parameter aus CPAR zusammen. Beides wird separat aufgerufen und zur Vereinfachnung global verarbeitet, da immer nur ein Befehl 'aktiv' sein kann.
		"""
		# Allgemeiner Befehls-Parameter
		self.cpar = 0
		# Befehls-Dictionary
		self.creg = {
			"acc": self._acc,
			"jmp": self._jmp,
			"nop": self._nop,
			"hlt": self._hlt
		}
	
	"""
	Parameter sind immer vom Typ INT und Befehle sind immer vom Typ STR. Später werden die STR-Befehle durch das CDIC als Funktion aufgerufen.
	"""
	
	# Befehls-Definitionen
	def _acc(self):
		self.accu += self.cpar
		self.cind += 1
	def _jmp(self):
		self.cind += self.cpar
	def _nop(self):
		self.cind += 1
	def _hlt(self):
		return 0

	# Befehl der RM ausführen
	def run_cmd(self, cmd, par):
		# Parameter übergeben
		self.cpar = par
		# Befehl ausführen
		err = self.creg[cmd]()
		return err

"""
Pseudocode:
'Programzeilen und Datenspeicher beginnt bei 1 in Datei
'Programzeilen beginnen bei 0 in Code -> Startbefehl am Anfang anhängen

solange nicht Programende erreicht oder nicht Fehler gefunden
	Befehl und Parameter aus Programmspeicher nehmen (anhand Index aus Befehlszähler)
	Befehl als Funktion aufrufen und Parameter übergeben

Funktion anwenden
	Parameter verwenden
	Akku lesen | Akku schreiben | Datenspeicher lesen | Datenspeicher schreiben
	Befehlszähler verändern (++ | -- | INT)
"""

def main():
	# Argumente
	arg_file = str(sys.argv[1])
	arg_print, arg_wait = False, False
	if "-p" in sys.argv: arg_print = True
	elif "-w" in sys.argv: arg_wait = True
	
	# 'Befehlsverlauf' als Menge aller bereits ausgeführten Befehle
	history = set()

	# Befehle ausführen
	rm = RM(arg_file)
	while True:
		# Befehl und Parameter lesen
		cmd, par = rm.pmem[rm.cind]
		# Befehl als Funktion mit Parameter aufrufen
		err = rm.run_cmd(cmd, par)
		# Errormeldung verarbeiten
		if err == 0: print("Program finished\n")
		# Program beenden, wenn Error != None
		if err != None: break
		
		word = f"{rm.pmem[rm.cind][0][0]}_{rm.pmem[rm.cind][1]}_{rm.cind}"
		
		# WEITER
		if arg_print: print(f"{word} | {rm.accu} : {rm.cind}")
		elif arg_wait: print(f"{word} | {rm.accu} : {rm.cind}", end=""); input()

		# Befehlsmenge ergänzen oder Schleife erkennen und abbrechen
		if word in history: print("Found loop\n"); break
		else: history.add(word)
		
"""
Argumente:
1: .txt Datei
2: -p (Zustand von Akku und Befehls-Zähler anzeigen) XOR
   -w (Zustand von Akku und Befehls-Zähler anzeigen und auf Eingabe warten)
"""

if __name__ == "__main__":
	main()

