


import pyaudio
import wave
import threading
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class WavePlayer(threading.Thread):
    """
    A simple class based on PyAudio to play a sine wave.
    It's a threading class. You can play audio while your application
    continues to do stuff.
    """

    def __init__(self):
        threading.Thread.__init__(self)
        self.p = pyaudio.PyAudio()

        self.fs = 44100          # sampling rate, Hz, must be integer

    def run(self):
        """
        Just another name for self.start()
        """
        # define stream chunk
        chunk = 1024

        # open a wav format music
        f = wave.open(os.path.join(BASE_DIR, "audio/beginning_theme.wav"), "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

        # stop audio stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()

    def sound_effect(self, path):
        """
        Use for sound effects throughout the game
        """
        # define stream chunk
        chunk = 1024

        # open a wav format music
        f = wave.open(os.path.join(BASE_DIR, path), "rb")
        # instantiate PyAudio
        p = pyaudio.PyAudio()
        # open stream
        stream = p.open(format=p.get_format_from_width(f.getsampwidth()),
                        channels=f.getnchannels(),
                        rate=f.getframerate(),
                        output=True)
        # read data
        data = f.readframes(chunk)

        # play stream
        while data:
            stream.write(data)
            data = f.readframes(chunk)

        # stop audio stream
        stream.stop_stream()
        stream.close()

        # close PyAudio
        p.terminate()


s = WavePlayer()                                            # initialize intro music
s.sound_effect('access_library_computer.wav')


