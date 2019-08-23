# python-tkinter-waveform-widget
 Widget leveraging tkinter Canvas and librosa

 I found librosa's waveform draw function to be pretty cumbersome so this is my own
 attempt to implement that functionality as a simple tkinter widget.

Usage:
```
import tkwavewidget
import tkinter as tk

main_window = tk.Tk()
##Takes standard tkinter canvas options:
cnf = {
  "height" : 100,
  "width" : 500,
  "bg" : "green"
}

##Wave options control how large the waveform is:
wave_cnf = {
  "x_scale" : 1
  "y_scale" : 5
}

path_to_audio = 'test.mp3'

waveform_widget = tkwavewidget.WaveWidget(main_window, path_to_audio, cnf, wave_cnf)

##Draw waveform:
waveform_widget.draw_wavform()

##The class inherits tkinter.Canvas:
waveform_widget.place()

waveform_widget.config(cnf)

##To set x_scale and y_scale options:
waveform_widget.wave_config(wave_cnf)
```
