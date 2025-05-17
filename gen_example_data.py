import os

import numpy as np
import pandas as pd

from simulate_spectra import batch_gen_spectrum_numerical as gen_spectrum


offsets = np.linspace(-6, 6, 75) # ppm
powers = np.array([0.5, 2, 5]) # micro T
B0 = 7.0 # T
gamma = 267.522 # MHz/T * 2pi
tp = 10.0 # s

R1a = 0.33  # Hz
R2a = 0.67  # Hz
dwa = 0  # ppm
R1b = 1.0  # Hz
R2b = 66.67  # Hz
kb = 30  # Hz
fb = 0.007  # dimensionless.
dwb = 3.5  # ppm

fit_pars = np.array([R1a, R2a, dwa, R1b, R2b, kb, fb, dwb], dtype=float)
Z = gen_spectrum(fit_pars, offsets, powers, B0, gamma, tp)

rng = np.random.default_rng()
sigma = 0.02
data = rng.normal(Z, sigma)

df = pd.DataFrame(np.c_[offsets, data.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers])
with pd.ExcelWriter(os.path.join(os.getcwd(), "APT_phantom.xlsx")) as writer:
    df.to_excel(writer, sheet_name="data", index=False, float_format="%.3g")
