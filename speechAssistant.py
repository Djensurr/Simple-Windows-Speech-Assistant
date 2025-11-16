import pvporcupine
import pyaudio
import struct
import speech_recognition as sr
import subprocess
import psutil
import sys
import winsound
import webbrowser

WAKE_WORD_FILE = # Path to your Picovoice Wake word file (.ppn)
ACCESS_KEY = # Your Picovoice key



# Speech Recognition
recognizer = sr.Recognizer()

def is_running(process):
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == process:
            return True
        return False
    
def play_beep():
    frequency = 300 # Hz
    duration = 200 # ms
    winsound.Beep(frequency, duration)

def listen_command():
    with sr.Microphone() as source:
        print("Listening for command...")
        play_beep()
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except:
        return ""

# Command Examples
def run_command(command):
    if "chrome" in command or "browser" in command:
        subprocess.Popen(# Your browser path)

    elif "spotify" in command:
        subprocess.Popen(# Your spotify path)

    elif "counter strike" in command or "counter-strike" in command or "cs2" in command or "cs" in command:
        subprocess.Popen(# Your counter strike path)

    elif "google maps" in command:
        webbrowser.open("https://www.google.com/maps")
    
    elif "brightspace" in command or "bride space" in command or "right space" in command:
        webbrowser.open("https://brightspace.ru.nl/d2l/home")

    elif "email" in command:
        webbrowser.open("https://outlook.live.com/mail/0/")

    elif "discord" in command:
        subprocess.Popen(# Your discord path)
    
    elif "steam" in command:
        subprocess.Popen(# Your steam path)
    
    elif "vsc" in command:
        subprocess.Popen(# Your VSC path)
    
    elif "quit" in command or "exit" in command:
        play_beep()
        sys.exit()

    else:
        ""

def main():
    porcupine = pvporcupine.create(
        access_key=ACCESS_KEY,
        keyword_paths=[WAKE_WORD_FILE]
    )

    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )


    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            command = listen_command()
            run_command(command)

if __name__ == "__main__":
    main()
