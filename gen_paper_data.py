import os

import numpy as np
import pandas as pd

from simulate_spectra import batch_gen_spectrum_numerical, batch_gen_spectrum_symbolic

## Hydrogen (poly-L-lysine in water)
offsets = np.arange(-6, 6, 0.05, dtype=float)
powers = np.array([1, 3, 5])
B0 = 4.7
gamma = 267.522
tp = 15.0
args = (offsets, powers, B0, gamma, tp)

R1a = 0.33  # Hz
R2a = 0.5  # Hz
dwa = 0  # ppm
R1b = 1.29  # Hz
R2b = 30.3  # Hz
kb = 200  # Hz
fb = 5e-4  # dimensionless.
dwb = 3.5  # ppm

fit_pars = np.array([R1a, R2a, dwa, R1b, R2b, kb, fb, dwb], dtype=float)

Z_num = batch_gen_spectrum_numerical(fit_pars, offsets, powers, B0, gamma, tp)
Z_sym = batch_gen_spectrum_symbolic(fit_pars, offsets, powers, B0, gamma, tp)

df_num = pd.DataFrame(
    np.c_[offsets, Z_num.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_num.to_csv("hydrogen_num.csv", index=False)

df_sym = pd.DataFrame(
    np.c_[offsets, Z_sym.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_sym.to_csv("hydrogen_sym.csv", index=False)

## Nitrogen (DEST)
offsets = np.arange(-175, 175, 1, dtype=float)
powers = np.array([5.8, 11.6, 23.2])
B0 = 14.1
gamma = -27.116
tp = 1.0
args = (offsets, powers, B0, gamma, tp)

R1a = 1  # Hz
R2a = 10  # Hz
dwa = 0  # ppm
R1b = 1.0  # Hz
R2b = 10e3  # Hz
kb = 100  # Hz
fb = 5e-2  # dimensionless.
dwb = 0  # ppm

fit_pars = np.array([R1a, R2a, dwa, R1b, R2b, kb, fb, dwb], dtype=float)

Z_num = batch_gen_spectrum_numerical(fit_pars, offsets, powers, B0, gamma, tp)
Z_sym = batch_gen_spectrum_symbolic(fit_pars, offsets, powers, B0, gamma, tp)

df_num = pd.DataFrame(
    np.c_[offsets, Z_num.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_num.to_csv("nitrogen_num.csv", index=False)

df_sym = pd.DataFrame(
    np.c_[offsets, Z_sym.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_sym.to_csv("nitrogen_sym.csv", index=False)

## Flurorine (GEST)
offsets = np.arange(-25, 10, 0.05, dtype=float)
powers = np.array([1, 1.75, 2.5])
B0 = 11.7
gamma = 251.815
tp = 4.63
args = (offsets, powers, B0, gamma, tp)

R1a = 0.65  # Hz
R2a = 9.71  # Hz
dwa = 0  # ppm
R1b = 38  # Hz
R2b = 180  # Hz
kb = 145  # Hz
fb = 0.01  # dimensionless.
dwb = -18.4  # ppm

fit_pars = np.array([R1a, R2a, dwa, R1b, R2b, kb, fb, dwb], dtype=float)

Z_num = batch_gen_spectrum_numerical(fit_pars, offsets, powers, B0, gamma, tp)
Z_sym = batch_gen_spectrum_symbolic(fit_pars, offsets, powers, B0, gamma, tp)

df_num = pd.DataFrame(
    np.c_[offsets, Z_num.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_num.to_csv("fluorine_num.csv", index=False)

df_sym = pd.DataFrame(
    np.c_[offsets, Z_sym.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_sym.to_csv("fluorine_sym.csv", index=False)

## Lithium (LP30)
offsets = np.arange(-500, 500, 2, dtype=float)
powers = np.array([30.2, 60.4, 90.6])
B0 = 9.4
gamma = 103.962
tp = 2.0
args = (offsets, powers, B0, gamma, tp)

R1a = 8  # Hz
R2a = 380  # Hz
dwa = 0  # ppm
R1b = 10  # Hz
R2b = 27e3  # Hz
kb = 285  # Hz
fb = 0.02  # dimensionless.
dwb = -260  # ppm

fit_pars = np.array([R1a, R2a, dwa, R1b, R2b, kb, fb, dwb], dtype=float)

Z_num = batch_gen_spectrum_numerical(fit_pars, offsets, powers, B0, gamma, tp)
Z_sym = batch_gen_spectrum_symbolic(fit_pars, offsets, powers, B0, gamma, tp)

df_num = pd.DataFrame(
    np.c_[offsets, Z_num.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_num.to_csv("lithium_num.csv", index=False)

df_sym = pd.DataFrame(
    np.c_[offsets, Z_sym.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers]
)
df_sym.to_csv("lithium_sym.csv", index=False)


## Hydrogen (amide proton transfer)
offsets = np.linspace(-6, 6, 75)
powers = np.array([0.5, 2, 5])
B0 = 7.0
gamma = 267.522
tp = 10.0
args = (offsets, powers, B0, gamma, tp)

R1a = 0.33  # Hz
R2a = 0.67  # Hz
dwa = 0  # ppm
R1b = 1.0  # Hz
R2b = 66.67  # Hz
kb = 30  # Hz
fb = 0.007  # dimensionless.
dwb = 3.5  # ppm

fit_pars = np.array([R1a, R2a, dwa, R1b, R2b, kb, fb, dwb], dtype=float)
Z = batch_gen_spectrum_numerical(fit_pars, offsets, powers, B0, gamma, tp)

rng = np.random.default_rng()
sigma = 0.02
data = rng.normal(Z, sigma)

df = pd.DataFrame(np.c_[offsets, data.T], columns=["ppm"] + [f"{power:.3g} μT" for power in powers])
with pd.ExcelWriter(os.path.join(os.getcwd(), "paper_hydrogen_data.xlsx")) as writer:
    df.to_excel(writer, sheet_name="data", index=False, float_format="%.3g")
