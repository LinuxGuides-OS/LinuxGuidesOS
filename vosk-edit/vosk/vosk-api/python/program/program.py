#!/usr/bin/env python3

import argparse
import os
import queue
import sounddevice as sd
import vosk
import sys
import json
import subprocess
import csv
import time
import random
import importlib
from playsound import playsound


version = ("1.5.2 (LGOS)")
q = queue.Queue()

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))

parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    '-f', '--filename', type=str, metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-m', '--model', type=str, metavar='MODEL_PATH',
    help='Path to the model')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
args = parser.parse_args(remaining)

try:
    if args.model is None:
        args.model = "model"
    if not os.path.exists(args.model):
        print ("Please download a model for your language from https://alphacephei.com/vosk/models")
        print ("and unpack as 'model' in the current folder.")
        print (" ")
        parser.exit(0)
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        # soundfile expects an int, sounddevice provides a float:
        args.samplerate = int(device_info['default_samplerate'])

    model = vosk.Model(args.model)

    if args.filename:
        dump_fn = open(args.filename, "wb")
    else:
        dump_fn = None

    with sd.RawInputStream(samplerate=args.samplerate, blocksize = 8000, device=args.device, dtype='int16', channels=1, callback=callback):

            rec = vosk.KaldiRecognizer(model, args.samplerate)

            # display informations
            print("")
            print("###########################################################################")
            print("Bread Vosk-Edit LGOS-EDITION")
            print("")
            print("Dieses Tool ist dazu da, um Ihnen die Nutzung Ihres Computers mittels")
            print("Spracheingabe zu erleichtern. Weitere Infos und Befehle finden Sie unter")
            print("https://felixbread.github.io/projekte/vosk-edit/commands")
            print("")
            print("Versuchen Sie bitte, so deutlich wie möglich zu Sprechen!")
            print("")
            print("Bread Vosk-Edit Version: " + version)
            print("###########################################################################")
            print("")
            time.sleep(4)

            while True:
                data = q.get()
                if rec.AcceptWaveform(data):

                    # Get JSON
                    vc = json.loads(rec.Result())

                    # randomize
                    randomize = random.choice(['sound1', 'sound2', 'sound3', 'sound4', 'sound5', 'sound6', 'sound7', 'sound8', 'sound9', 'sound10'])
                    randomize_joke = random.choice(['witz1', 'witz2', 'witz3', 'witz4', 'witz5', 'witz6', 'witz7', 'witz8', 'witz9', 'witz10'])

                    # Do something with the detected text:

                    # TEXT
                    if vc['text'] == "brot a":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        print('')
                        
                    if vc['text'] == "brot b":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "b"])
                        print('')
                        
                    if vc['text'] == "brot c":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "c"])
                        print('')
                        
                    if vc['text'] == "brot d":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        print('')
                        
                    if vc['text'] == "brot e":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        print('')
                        
                    if vc['text'] == "brot f":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "f"])
                        print('')
                        
                    if vc['text'] == "brot g":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "g"])
                        print('')
                        
                    if vc['text'] == "brot h":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "h"])
                        print('')
                        
                    if vc['text'] == "brot i":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "i"])
                        print('')
                        
                    if vc['text'] == "brot j":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "j"])
                        print('')
                        
                    if vc['text'] == "brot k":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "k"])
                        print('')
                        
                    if vc['text'] == "brot l":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "l"])
                        print('')
                        
                    if vc['text'] == "brot m":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "m"])
                        print('')
                        
                    if vc['text'] == "brot n":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "n"])
                        print('')
                        
                    if vc['text'] == "brot o":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "o"])
                        print('')
                        
                    if vc['text'] == "brot p":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "p"])
                        print('')
                        
                    if vc['text'] == "brot q":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "q"])
                        print('')
                        
                    if vc['text'] == "brot r":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "r"])
                        print('')
                        
                    if vc['text'] == "brot s":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "brot t":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        print('')
                        
                    if vc['text'] == "brot u":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "u"])
                        print('')
                        
                    if vc['text'] == "brot v":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "v"])
                        print('')
                        
                    if vc['text'] == "brot w":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "brot x":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "x"])
                        print('')
                        
                    if vc['text'] == "brot y":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "y"])
                        print('')
                        
                    if vc['text'] == "brot z":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "z"])
                        print('')
                        

                    #BUCHSTABEN TEXT
                    if vc['text'] == "brot buchstabe a":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe b":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "b"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe c":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "c"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe d":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe e":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe f":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "f"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe g":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "g"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe h":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "h"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe i":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "i"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe j":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "j"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe k":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "k"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe l":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "l"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe m":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "m"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe n":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "n"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe o":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "o"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe p":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "p"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe q":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "q"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe r":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "r"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe s":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe t":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe u":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "u"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe v":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "v"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe w":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe x":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "x"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe y":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "y"])
                        print('')
                        
                    if vc['text'] == "brot buchstabe z":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "z"])
                        print('')
                        

                    # TEXT-SYMBOLE
                    if vc['text'] == "brot leer":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "brot leerzeichen":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "brot space":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "brot löschen":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "BackSpace"])
                        print('')
                        
                    if vc['text'] == "brot nächste zeile":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Return"])
                        print('')
                        
                    if vc['text'] == "brot eingabe":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Return"])
                        print('')
                        
                    if vc['text'] == "brot es cape":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Escape"])
                        print('')

                    if vc['text'] == "brot escape":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Escape"])
                        print('')
                        
                    if vc['text'] == "brot seite hoch":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Page_Up"])
                        print('')
                        
                    if vc['text'] == "brot seite runter":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Page_Down"])
                        print('')
                        
                    if vc['text'] == "brot menü":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Menu"])
                        print('')
                        
                    if vc['text'] == "brot schifft":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Shift_L"])
                        print('')

                    if vc['text'] == "brot shift":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Shift_L"])
                        print('')
                        

                    # SPIELE
                    if vc['text'] == "brot vor":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "brot vorwärts":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "brot zurück":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "brot rückwärts":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "brot links":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        print('')
                        
                    if vc['text'] == "brot rechts":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        print('')
                        
                    if vc['text'] == "brot inventar":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        print('')
                        
                    if vc['text'] == "brot chat":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        print('')
                        
                    if vc['text'] == "brot springen":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "brot fliegen":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "brot schlagen":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "brot setzen":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        

                    # PROGRAMME
                    if vc['text'] == "brot libreoffice":
                        subprocess.Popen(["libreoffice"])
                        print('')
                        
                    if vc['text'] == "brot firefox":
                        subprocess.Popen(["firefox"])
                        print('')
                        
                    if vc['text'] == "brot terminal":
                        subprocess.Popen(["gnome-terminal"])
                        print('')
                        

                    # MAUS-AKTIONEN
                    if vc['text'] == "brot klicken":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "brot doppelklick":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "brot rechtsklicken":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        
                    if vc['text'] == "brot klicke":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "brot blicke":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "brot blick":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "brot rechtsklicke":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        
                    if vc['text'] == "brot klick":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "brot rechtsklick":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        
                    # OS-AKTIONEN
                    if vc['text'] == "brot fenster schließen":
                        subprocess.Popen(["xdotool", "key", "Alt_L+F4"])
                        print('')

                    if vc['text'] == "brot screenshot":
                        subprocess.Popen(["flameshot", "gui"])
                        print('')
                        
                        x = vc['text'].split()
                        print(x)
                    if vc['text'] == "brot sperren":
                        subprocess.Popen(["xflock4"])
                        print('')
                        
                        x = vc['text'].split()
                        print(x)
                    if vc['text'] == "brot bildschirm sperren":
                        subprocess.Popen(["xflock4"])
                        print('')
                        
                        x = vc['text'].split()
                        print(x)

                    # BROT-AKTIONEN
                    if vc['text'] == "brot starte dich neu":
                        print("ich bin müüüüde...")
                        time.sleep(2)
                        sys.stdout.flush()
                        os.execv(sys.argv[0], sys.argv)
                    if vc['text'] == "brot version":
                        print("")
                        print("#############################################")
                        print("Bread Vosk-Edit Version: " + version)
                        print("#############################################")
                        print("")
                        time.sleep(5)

                    # WITZE
                    if vc['text'] == "brot erzähle einen witz":
                        if randomize_joke == "witz2":
                            print("")
                            print("Ich schlafe abends sehr schlecht ein.")
                            print("")
                            print("Kenne ich. Ich zähle dann immer bis drei.")
                            print("")
                            print("Ach, und das hilft?")
                            print("")
                            print("Na ja, manchmal zähle ich auch bis halb vier ...")
                            print("")
                            playsound('/usr/vosk/jokes/joke2.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == "witz1":
                            print("")
                            print("Zwei Jäger sitzen auf einem Hochsitz und feiern ihr 20-jähriges Berufsjubiläum. ")
                            print("Beide haben ausreichend Alkohol dabei und sind nach zwei Stunden strotzbesoffen. ")
                            print("Auf einmal fliegt ein Drachenflieger über den Hochsitz.")
                            print("")
                            print("Der erste Jäger krakehlt: Sssschau dir deeen Riesenaaadler an. Waaahnsinn. Knall")
                            print("ihn ab! Daraufhin reißt der andere sein Jagdgewehr in die Luft und ballert drei Mal")
                            print("auf den vermeintlichen Raubvogel. Etwas ernüchtert schaut er den anderen Jäger")
                            print("an und lallt: Und? Hhhab isch ihn gedroffen?")
                            print("")
                            print("Daraufhin der andere: Nnnö. Aber ssseine Beute hat er fallen lassen!")
                            print("")
                            playsound('/usr/vosk/jokes/joke1.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz3':
                            print("")
                            print("Das Telefon im Büro klingelt. Ein Angestellter hebt ab und fragt: Welcher Idiot wagt ")
                            print("es, mich in der Mittagspause anzurufen?")
                            print("")
                            print("Da brüllt der Anrufer: Wissen Sie eigentlich, mit wem Sie sprechen? Ich bin der")
                            print("Generaldirektor!")
                            print("")
                            print("Der Angestellte erwidert: Wissen Sie eigentlich, mit wem Sie sprechen?")
                            print("")
                            print("Der Generaldirektor antwortet verdutzt: Nein.")
                            print("")
                            print("Worauf der Angestellte sagt: Na, dann habe ich ja nochmal Glück gehabt! und legt")
                            print("auf.")
                            print("")
                            playsound('/usr/vosk/jokes/joke3.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz4':
                            print("")
                            print("Adolf Hitler geht zum Wahrsager.")
                            print("")
                            print("Wahrsager: Führer, du wirst an einem jüdischen Feiertag sterben.")
                            print("")
                            print("Hitler: An welchem denn?")
                            print("")
                            print("Wahrsager: Ja der Tag, an dem du stirbst, wird ein jüdischer Feiertag sein!")
                            print("")
                            playsound('/usr/vosk/jokes/joke4.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz5':
                            print("")
                            print("Ein Pfarrer will sich ein Pferd kaufen.")
                            print("Beim Pferdehändler: Ich kann ihnen dieses Pferd wärmstens empfehlen. Bei 'Gott")
                            print("sei Dank' rennt es los und bei 'Amen' bleibt es stehen.")
                            print("")
                            print("Gut, das nehme ich.")
                            print("")
                            print("Der Pfarrer reitet los. Nach einiger Zeit merkt er, dass sein Pferd geradezu auf eine")
                            print("Klippe zurennt. Vor Schreck kann er sich nicht mehr an das Wort erinnern, mit dem")
                            print("er das Pferd anhalten kann.")
                            print("")
                            print("Also betet er: ... Amen!")
                            print("")
                            print("Das Pferd bleibt wie angewurzelt vor der Klippe stehen.")
                            print("")
                            print("Daraufhin seufzt der Pfarrer: Gott sei Dank!...")
                            print("")
                            playsound('/usr/vosk/jokes/joke5.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz6':
                            print("")
                            print("Schröder, Fischer und Merkel fliegen über Deutschland.")
                            print("")
                            print("Sagt Schröder: Wenn ich einen 100 Euro Schein runter werfe, dann freut sich ein")
                            print("Deutscher!")
                            print("")
                            print("Sagt Fischer: Wenn ich zehn 10 Euro Scheine runter werfe, dann freuen sich zehn")
                            print("Deutsche!")
                            print("")
                            print("Sagt Merkel: Wenn ich hundert 1 Euro Stücke runter werfe, dann freuen sich ")
                            print("hundert Deutsche!")
                            print("")
                            print("Dann sagt der Pilot: Wenn ihr nicht bald euer Maul haltet, dann werfe ich euch ")
                            print("runter und es freut sich ganz Deutschland!")
                            print("")
                            playsound('/usr/vosk/jokes/joke6.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz7':
                            print("")
                            print("Häschen beim Bäcker: Gib mir ein Brot, du Arsch.")
                            print("")
                            print("Der Bäcker gibt ihm das Brot und sagt: Nanana, das geht aber freundlicher!")
                            print("")
                            print("Am nächsten Tag kommt Häschen wieder: Ein Brot, du Arsch.")
                            print("")
                            print("Bäcker: Hey! Wenn du mich noch einmal Arsch nennst, nagle ich dich mit den")
                            print("Ohren an die Decke!")
                            print("")
                            print("Tags darauf kommt das Häschen wieder: Haddu Nägel?")
                            print("")
                            print("Bäcker: Nein!!!")
                            print("")
                            print("Häschen: Dann gib mir ein Brot, du Arsch!")
                            print("")
                            playsound('/usr/vosk/jokes/joke7.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz8':
                            print("")
                            print("Keiner, Niemand und Doof wohnen in einem Haus. Eines Tages geht Doof unten")
                            print("vorm Haus spazieren, als Keiner Doof von oben auf den kopf spuckt und dieser")
                            print("umgehend zur Polizei rennt.")
                            print("")
                            print("Dort angekommen berichtet er dem Polizisten: Keiner hat mir auf den Kopf")
                            print("gespuckt und Niemand hat's gesehen!")
                            print("")
                            print("Darauf der Polizist: Sind sie doof?")
                            print("")
                            print("Ja, höchst persönlich!")
                            print("")
                            playsound('/usr/vosk/jokes/joke8.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz9':
                            print("")
                            print("Warum nimmt Heinz eine Leiter mit in den Baumarkt?")
                            print ("")
                            print("Weil die Preise steigen. ")
                            print("")
                            playsound('/usr/vosk/jokes/joke9.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz10':
                            print("")
                            print("Auf dem Parkplatz entdeckt Luise eine große Beule an ihrer Autotür.")
                            print("Verzweifelt fragt sie sich, was sie dagegen tun kann. Da kommt ein junger Mann")
                            print("vorbei und rät ihr, in den Auspuff zu blasen, um das Auto aufzupumpen und damit")
                            print("die Beule auszudellen. Luise versteht den Scherz nicht und fängt an in den ")
                            print("Auspuff zu blasen.")
                            print("")
                            print("Währenddessen kommt eine andere Dame und fragt: Was machst du da?")
                            print("")
                            print("Ich versuche die Beule an meiner Tür wieder aufzupumpen.")
                            print("")
                            print("Die Dame lacht sich tot: Armches Dummchen, das wird nie klappen!")
                            print("")
                            print("Fragt Luise: Wieso nicht?")
                            print("")
                            print("Weil die Fenster offen sind!")
                            print("")
                            playsound('/usr/vosk/jokes/joke10.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)
                    
                else:
                    print(rec.PartialResult())

except KeyboardInterrupt:
    #print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
