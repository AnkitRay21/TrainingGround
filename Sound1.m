Fs = 44100;       % Sampling frequency in Hz
duration = 3;     % Duration of the audio in seconds
t = 0:1/Fs:duration-1/Fs; % Time vector

frequency = 528;  % Frequency of the audio signal in Hz
amplitude = 0.8;  % Amplitude of the signal :: volume

% Generate the audio signal (sine wave)
audio_signal = amplitude * sin(2 * pi * frequency * t);

% Play the audio signal
sound(audio_signal, Fs);

% Save as a WAV file
audiowrite('audio_output.wav', audio_signal, Fs);

% Save as an MP3 file
audiowrite('audio_output.mp3', audio_signal, Fs);