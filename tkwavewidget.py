from tkinter import Canvas
import librosa as lr
from warnings import warn

CLASS_KEYS = {'x_scale' : 1,
'y_scale' : 4,
'duration' : 0,
'play_offset' : 0 }

class WaveWidget(Canvas):
    def __init__(self, master = None, audio_path = None, cnf = {}, wave_cnf = {}):
        super(WaveWidget, self).__init__(master, cnf)
        self.wave_config(wave_cnf)
        if not audio_path is None:
            self.wave_array, self.samplerate = lr.load(audio_path)
            self.audio_loaded = True
        else:
            self.wave_array, self.samplerate = ([None], None)
            self.audio_loaded = False


    def draw_wavform(self):
        self.clear()
        width = int(self.config('width')[4])
        height = int(self.config('height')[4])

        y_center = int( height / 2)
        slice_count = int(len(self.wave_array)/width)
        root_n = self.wave_array[0]
        n = root_n * root_n * 100 * self.y_scale
        self.create_rectangle((0, y_center + n, 0 + self.x_scale, y_center - n))
        i = slice_count
        while i <= width * slice_count:
            root_n = self.wave_array[i]
            n = root_n * 100 * self.y_scale
            x1 = i / slice_count
            x2 = x1 + self.x_scale
            y1 = y_center + n
            y2 = y_center - n
            self.create_rectangle((x1,y1,x2,y2), {'fill':"blue", 'outline':"blue"})
            i += slice_count

    def load(self, audio_path):
        self.wave_array, self.samplerate = lr.load(audio_path)
        self.audio_loaded = True

    def clear(self):
        self.delete("all")

    def wave_config(self, wave_cnf = {}):
        for key,value in wave_cnf.items():
            if key in CLASS_KEYS:
                self.__setattr__(key, value)
            else:
                warn(f"No such option: {key}")
