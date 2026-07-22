import numpy as np
import struct
import wave

Fs = 44100 # sample rate in Hz [CD-quality]
T = 3      # duration of the signal in second
f = 528    # frequncy of the signal/pitch in Hz
A = 0.5    # amplitude :: volume level

t = np.linspace(0, T, int(Fs * T))

wave_data = A * np.sin(2 * np.pi * f * t) 

# convert floating point numbers to 16-bit signed integers (-32768 to 32767)
audio_data = (wave_data * 32767).astype(np.int16)  


filename = 'sound_wave_528Hz.wav'

with wave.open(filename, "wb") as wav_file:
    wav_file.setparams((1, 2, Fs, len(audio_data), "NONE", "not compressed"))

    for sample in audio_data:
        wav_file.writeframes(struct.pack('h', sample))

print(f"File generated {filename}" "!!!")