#!/usr/bin/env python3

import argparse
import asyncio
import os
import re
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

version = "Bread Vosk-Edit LGOS-EDITION 1.6.1"
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

            rec = vosk.KaldiRecognizer(model, args.samplerate)
            while True:
                data = q.get()
                if rec.AcceptWaveform(data):

                    # Get JSON
                    vc = json.loads(rec.Result())

                    # randomize
                    randomize = random.choice(['sound1', 'sound2', 'sound3', 'sound4', 'sound5', 'sound6', 'sound7', 'sound8', 'sound9', 'sound10'])
                    randomize_joke = random.choice(['witz1', 'witz2', 'witz3', 'witz4', 'witz5', 'witz6', 'witz7', 'witz8', 'witz9', 'witz10', 'witz11', 'witz12', 'witz13', 'witz14', 'witz15', 'witz16', 'witz17', 'witz18', 'witz4', 'witz2', 'witz5', 'witz1', 'witz3', 'witz8', 'witz7', 'witz6', 'witz9', 'witz10', 'witz11', 'witz14', 'witz13', 'witz12', 'witz15', 'witz18', 'witz17', 'witz16'])
                    
                    oracle = random.choice(['/usr/vosk/oracle/Ja.mp3', '/usr/vosk/oracle/Nein.mp3', '/usr/vosk/oracle/Vielleicht.mp3', '/usr/vosk/oracle/Wahrscheinlich.mp3', '/usr/vosk/oracle/Eher nicht.mp3', '/usr/vosk/oracle/Sieht so aus.mp3', '/usr/vosk/oracle/Sehr wahrscheinlich.mp3', '/usr/vosk/oracle/Sehr unwahrscheinlich.mp3', '/usr/vosk/oracle/Morgen.mp3', '/usr/vosk/oracle/Gestern.mp3', '/usr/vosk/oracle/Übermorgen.mp3', '/usr/vosk/oracle/Nie.mp3', '/usr/vosk/oracle/Immer.mp3'])
                    
                    bullshit = random.choice(['bullshit1', 'bullshit2'])


                    # Do something with the detected text:

                    # TEXT
                    if vc['text'] == "tom a":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"]) # press key "a"
                        print('')
                        
                    if vc['text'] == "tom b":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "b"]) # press key "b"
                        print('')
                        
                    if vc['text'] == "tom c":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "c"]) # press key ...
                        print('')
                        
                    if vc['text'] == "tom d":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"]) # press ...
                        print('')
                        
                    if vc['text'] == "tom e":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"]) # ...
                        print('')
                        
                    if vc['text'] == "tom f":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "f"])
                        print('')
                        
                    if vc['text'] == "tom g":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "g"])
                        print('')
                        
                    if vc['text'] == "tom h":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "h"])
                        print('')
                        
                    if vc['text'] == "tom i":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "i"])
                        print('')
                        
                    if vc['text'] == "tom j":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "j"])
                        print('')
                        
                    if vc['text'] == "tom k":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "k"])
                        print('')
                        
                    if vc['text'] == "tom l":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "l"])
                        print('')
                        
                    if vc['text'] == "tom m":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "m"])
                        print('')
                        
                    if vc['text'] == "tom n":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "n"])
                        print('')
                        
                    if vc['text'] == "tom o":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "o"])
                        print('')
                        
                    if vc['text'] == "tom p":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "p"])
                        print('')
                        
                    if vc['text'] == "tom q":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "q"])
                        print('')
                        
                    if vc['text'] == "tom r":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "r"])
                        print('')
                        
                    if vc['text'] == "tom s":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "tom t":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        print('')
                        
                    if vc['text'] == "tom u":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "u"])
                        print('')
                        
                    if vc['text'] == "tom v":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "v"])
                        print('')
                        
                    if vc['text'] == "tom w":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "tom x":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "x"])
                        print('')
                        
                    if vc['text'] == "tom y":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "y"])
                        print('')
                        
                    if vc['text'] == "tom z":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "z"])
                        print('')
                        

                    #BUCHSTABEN TEXT
                    if vc['text'] == "tom buchstabe a":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe b":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "b"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe c":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "c"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe d":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe e":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe f":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "f"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe g":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "g"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe h":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "h"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe i":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "i"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe j":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "j"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe k":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "k"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe l":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "l"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe m":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "m"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe n":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "n"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe o":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "o"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe p":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "p"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe q":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "q"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe r":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "r"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe s":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe t":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe u":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "u"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe v":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "v"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe w":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe x":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "x"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe y":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "y"])
                        print('')
                        
                    if vc['text'] == "tom buchstabe z":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "z"])
                        print('')
                        

                    # TEXT-SYMBOLE
                    if vc['text'] == "tom leer":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "tom leerzeichen":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "tom space":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "tom löschen":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "BackSpace"])
                        print('')
                        
                    if vc['text'] == "tom nächste zeile":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Return"])
                        print('')
                        
                    if vc['text'] == "tom eingabe":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Return"])
                        print('')
                        
                    if vc['text'] == "tom es cape":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Escape"])
                        print('')
                        
                    if vc['text'] == "tom seite hoch":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Page_Up"])
                        print('')
                        
                    if vc['text'] == "tom seite runter":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Page_Down"])
                        print('')
                        
                    if vc['text'] == "tom menü":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Menu"])
                        print('')
                        
                    if vc['text'] == "tom schifft":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "Shift_L"])
                        print('')
                        

                    # SPIELE
                    # ausgelegt für Minecraft, funktioniert noch nicht ganz fehlerfrei!
                    if vc['text'] == "tom vor":
                        # drücke viermal W, mache 2s pause, drücke wieder viermal W
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(2)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "tom vorwärts":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.1)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.1)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.1)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.1)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.1)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.1)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        print('')
                        
                    if vc['text'] == "tom weit vorwärts":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "w"])
                        time.sleep(0.3)
                        print('')
                        
                    if vc['text'] == "tom zurück":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        time.sleep(2)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "tom rückwärts":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        time.sleep(2)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "s"])
                        print('')
                        
                    if vc['text'] == "tom links":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        time.sleep(2)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "a"])
                        print('')
                        
                    if vc['text'] == "tom rechts":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        time.sleep(2)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "d"])
                        print('')
                        
                    if vc['text'] == "tom inventar":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        time.sleep(2)
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "e"])
                        print('')
                        
                    if vc['text'] == "tom chat":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "t"])
                        print('')
                        
                    if vc['text'] == "tom springen":
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        subprocess.Popen(["/usr/vosk/keypress.sh", "space"])
                        print('')
                        
                    if vc['text'] == "tom schlagen":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "tom setzen":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        

                    # PROGRAMME
                    if vc['text'] == "tom schreiben":
                        subprocess.Popen(["libreoffice"])
                        print('')
                        
                    if vc['text'] == "tom libreoffice":
                        subprocess.Popen(["libreoffice"])
                        print('')
                        
                    if vc['text'] == "tom firefox":
                        subprocess.Popen(["firefox"])
                        print('')
                        
                    if vc['text'] == "tom texteditor":
                        subprocess.Popen(["xed"])
                        print('')
                        
                    if vc['text'] == "tom editor":
                        subprocess.Popen(["xed"])
                        print('')
                        
                    if vc['text'] == "tom terminal":
                        subprocess.Popen(["gnome-terminal"])
                        print('')
                        

                    # MAUS-AKTIONEN
                    if vc['text'] == "tom klicken":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "tom doppelklick":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "tom rechtsklicken":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        
                    if vc['text'] == "tom klicke":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "tom blicke":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "tom blick":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "tom rechtsklicke":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        
                    if vc['text'] == "tom klick":
                        subprocess.Popen(["/usr/vosk/click.sh", "1"])
                        print('')
                        
                    if vc['text'] == "tom rechtsklick":
                        subprocess.Popen(["/usr/vosk/click.sh", "3"])
                        print('')
                        

                    # MULTIMEDIA
                    if vc['text'] == "tom youtube":
                        subprocess.Popen(["firefox", "https://www.youtube.com/"])
                    if vc['text'] == "tom screenshot":
                        subprocess.Popen(["flameshot", "gui"])
                        print('')

                    # FENSTER-AKTIONEN
                    if vc['text'] == "tom fenster schließen":
                        subprocess.Popen(["xdotool", "key", "Alt_L+F4"])
                        print('')
                        
                    # OS-AKTIONEN
                    if vc['text'] == "tom sperren":
                        subprocess.Popen(["xflock4"])
                        print('')
                        
                    if vc['text'] == "tom bildschirm sperren":
                        subprocess.Popen(["xflock4"])
                        print('')

                    # ANDERE-AKTIONEN
                    if vc['text'] == "tom starte dich neu":
                        print("ich bin müüüüde...")
                        time.sleep(2)
                        sys.stdout.flush()
                        os.execv(sys.argv[0], sys.argv)
                    if vc['text'] == "tom starter dich neu":
                        print("ich bin müüüüde...")
                        time.sleep(2)
                        sys.stdout.flush()
                        os.execv(sys.argv[0], sys.argv)
                    if vc['text'] == "tom wer bist du":
                        print("")
                        print("Wer bin ich?")
                        print("")
                        print("Ich bin eine art (sehr kleiner) Sprachassistent, der")
                        print("gerne mal lustige Sachen sagt.")
                        print("Meine Spracherkennung (Vosk API) wurde nicht von Felix")
                        print("gemacht, dann wäre ich ja in 20 Jahren noch nicht fertig.")
                        print("Allerdings wurde das, was nach der Erkennung passiert,")
                        print("also was ich mit den erkannten wörtern mache,")
                        print("von Felix in python programmiert.")
                        print("Also sowas wie zum Beispiel die Wiedergabe von Witzen,")
                        print("das Ausführen von Aktionen und einiges mehr.")
                        print("")
                        playsound('/usr/vosk/sound/wer-bist-du.mp3')

                    # FUNNY-THINGS
                    if vc['text'] == "tom was sind die größten weisheiten der menschheit":
                        print("")
                        print("Die größten Weisheiten der Menschheit:")
                        print("")
                        print("1. I'm here and I'm queer")
                        print("2. ZUERST die Cornflakes, dann die Milch")
                        print("3. Felix ist doof")
                        print("4. Siri, Alexa und Co. sind dumm")
                        print("5. Nutella OHNE Butter!")
                        print("6. Ich bin cool")
                        print("")
                        playsound('/usr/vosk/sound/weisheiten.mp3')
                    
                    if vc['text'] == "tom witzige fakten":
                        print("")
                        print("Witzige Fakten:")
                        print("")
                        print("1. 0.1 + 0.2 ergibt in Python 0.30000000000000004")
                        print("")
                        playsound('/usr/vosk/sound/facts.mp3')

                    if vc['text'] == "tom laber müll":
                        if bullshit == "bullshit1":
                            print("")
                            print("Brot wächst auf bäumen, weil Bäume von Wolken fallen, und Gras am Himmel wächst")
                            print("")
                            playsound('/usr/vosk/sound/bullshit1.mp3')

                    if vc['text'] == "tom laber müll":
                        if bullshit == "bullshit2":
                            print("")
                            print("Brot wächst auf bäumen, weil Bäume von Wolken fallen, und Gras am Himmel wächst")
                            print("")
                            playsound('/usr/vosk/sound/bullshit1.mp3')

                    # orakel, tom sucht nach dem anfang "tom orakel", und antwortet zufällig. unabhänig der gestellten frage
                    str = vc['text']
                    #search using regex
                    x = re.search('^tom orakel', str)
                    if(x!=None):
                        if oracle == "/usr/vosk/oracle/Ja.mp3":
                            print("\nJa\n")
                        elif oracle == "/usr/vosk/oracle/Nein.mp3":
                            print("\nNein\n")
                        elif oracle == "/usr/vosk/oracle/Eher nicht.mp3":
                            print("\nEher nicht\n")
                        elif oracle == "/usr/vosk/oracle/Gestern.mp3":
                            print("\nGestern\n")
                        elif oracle == "/usr/vosk/oracle/Immer.mp3":
                            print("\nImmer\n")
                        elif oracle == "/usr/vosk/oracle/Morgen.mp3":
                            print("\nMorgen\n")
                        elif oracle == "/usr/vosk/oracle/Nie.mp3":
                            print("\nNie\n")
                        elif oracle == "/usr/vosk/oracle/Sehr unwahrscheinlich.mp3":
                            print("\nSehr unwahrscheinlich\n")
                        elif oracle == "/usr/vosk/oracle/Sehr wahrscheinlich.mp3":
                            print("\nSehr wahrscheinlich\n")
                        elif oracle == "/usr/vosk/oracle/Sieht so aus.mp3":
                            print("\nSieht so aus\n")
                        elif oracle == "/usr/vosk/oracle/Übermorgen.mp3":
                            print("\nÜbermorgen\n")
                        elif oracle == "/usr/vosk/oracle/Vielleicht.mp3":
                            print("\nVielleicht\n")
                        elif oracle == "/usr/vosk/oracle/Wahrscheinlich.mp3":
                            print("\nWahrscheinlich\n")
                        else:
                            print("\nNot Found!\n")
                    if(x!=None):
	                    playsound(oracle)
                    if(x!=None):
                        sys.stdout.flush()
                        os.execv(sys.argv[0], sys.argv)
                    else:
                        print("{")
                        print('  "partial" : ""')
                        print("}")


                    # WITZE
                    if vc['text'] == "tom erzähle einen witz":
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

                        elif randomize_joke == 'witz11':
                            print("")
                            print("Schatz?")
                            print("")
                            print("Ja?")
                            print("")
                            print("Ich fühle mich so hässlich, so fett und so faltig. Ich brauche ein Kompliment.")
                            print("")
                            print("Du hast eine gute Beobachtungsgabe.")
                            print("")
                            playsound('/usr/vosk/jokes/joke11.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz12':
                            print("")
                            print("Der Gefängnisdirektor: Was wird nur Ihr armer Vater dazu sagen,")
                            print("dass sie schon wieder hier sind?")
                            print("")
                            print("Fragen Sie ihn doch selbst. Er sitzt nur drei Zellen weiter!")
                            print("")
                            playsound('/usr/vosk/jokes/joke12.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz13':
                            print("")
                            print("In der Schule fragt die Lehrerin, was ein Trauerfall ist.")
                            print("")
                            print("Sagt der erste Schüler: Wenn ich meine Geldbörse verliere!")
                            print("")
                            print("Nein sagt die Lehrerin, das nennt man einen Verlust!")
                            print("")
                            print("Sagt der nächste Schüler: Wenn ein Loch in unserm Dach ist, und es hereinregnet!")
                            print("")
                            print("Nein sagt die Lehrerin wieder, das nennt man einen Schaden!")
                            print("")
                            print("Sagt der dritte Schüler: Wenn unser Bundeskanzler sterben würde!")
                            print("")
                            print("Richtig sagt die Lehrerin, das wäre ein Trauerfall, und kein Schaden und kein")
                            print("Verlust!")
                            print("")
                            playsound('/usr/vosk/jokes/joke13.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz14':
                            print("")
                            print("Sagt die Oma zu Fritzchen: Fritzchen, mach den Krimi aus. Du sollst dir nicht immer")
                            print("so brutales Zeug anschauen. Komm, ich erzähl dir das Märchen wo Hänsel und")
                            print("Gretel die Hexe im Ofen verbrennen.")
                            print("")
                            playsound('/usr/vosk/jokes/joke14.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz15':
                            print("")
                            print("Ein Zeitungsjunge läuft schreiend durch die Straßen:")
                            print("")
                            print("Riesenschwindel! Riesenschwindel! 98 Opfer!")
                            print("")
                            print("Ein Herr kauft die Zeitung, überfliegt sie und rennt dem Burschen nach: Kein Wort")
                            print("wahr von deinem Riesenschwindel!")
                            print("")
                            print("Der Junge schreit:")
                            print("")
                            print("Riesenschwindel! Riesenschwindel! 99 Opfer!")
                            print("")
                            playsound('/usr/vosk/jokes/joke15.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz16':
                            print("")
                            print("Gebet zum Neuen Jahr: Lieber Gott! Bitte mach meine Taille schlanker und mein")
                            print("Bankkonto fetter.")
                            print("")
                            print("Und bitte, bitte, verwechsle es nicht wieder wie letztes Jahr!")
                            print("")
                            playsound('/usr/vosk/jokes/joke16.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz17':
                            print("")
                            print("Fritzchen ist krank und bekommt vom Doktor eine Medizin.")
                            print("")
                            print("Er fragt: Herr Doktor, hat diese Medizin auch Nebenwirkungen?")
                            print("")
                            print("Ja, du kannst schon morgen wieder in die Schule gehen!")
                            print("")
                            playsound('/usr/vosk/jokes/joke17.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)

                        elif randomize_joke == 'witz18':
                            print("")
                            print("Sitzen zwei Männer im Zug. Der eine isst Apfelkerne.")
                            print("")
                            print("Da fragt der andere: Warum essen sie denn Apfelkerne?")
                            print("")
                            print("Das macht intelligent.")
                            print("")
                            print("Darf ich auch welche haben?")
                            print("")
                            print("Ja, für fünf Euro.")
                            print("")
                            print("Er bezahlt fünf Euro, bekommt die Kerne und isst sie. Dann murmelt er kauend:")
                            print("Eigentlich hätte ich mir für fünf Euro ja eine ganze Tüte Äpfel kaufen können!")
                            print("")
                            print("Entgegnet der andere: Sehen sie, es wirkt schon!")
                            print("")
                            playsound('/usr/vosk/jokes/joke18.mp3')
                            sys.stdout.flush()
                            os.execv(sys.argv[0], sys.argv)
                    
                else:
                    print(rec.PartialResult())

except KeyboardInterrupt:
    #print('\nDone')
    parser.exit(0)
except Exception as e:
    parser.exit(type(e).__name__ + ': ' + str(e))
