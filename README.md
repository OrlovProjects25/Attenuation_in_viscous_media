Theme: Modelling attenuation in viscous media

Created by: Aleksandr Orlov

The project focuses on changing the original audio recording accounting for the medium through which and the distance which the sound of the recording has to travel before reaching the receiver.
The sound is disassembled into harmonic functions using FFT, and each of them is then changed according to the dissipative wave equation. Then, it is reassembled into a new recording - therefore, becoming what will be caught by the receiver.

The theory can be viewed in "Theory"

The original audio-file is "White_noise.wav"
The changed one - "Changed_White_Noise.wav"

The code that performs all the transformations is in "main_body.py". The medium used is high-viscosity Polydimethylsiloxane (PDMS / Silicone Fluid) with a nominal viscosity of 1,000,000 cSt
Spectro0.py creates a spectrogram (Spectrogram_original.png) of the original audio-file.
Spectro1.py creates a spectrogram (Spectrogram_changed.png) of the changed audio-file.
Sound_velocity.py makes a plot (Plot_SVelocity(frequency).png) of how sound velocity changes with frequency.

Spectrogram_original.png, Spectrogram_changed.png, Plot_SVelocity(frequency).png can be viewed in "Graphs"
