# Z-spectra-fitting-app
Python application for the fitting of Z-spectra.

## Table of Contents
* [Intended Audience](#intended-audience)
* [Features](#features)
* [Setup](#setup)
* [Usage](#usage)
* [Contributing and contact info](#contributing-and-contact-info)


## Intended Audience
This package is inteded for robust fitting of multi-$`B_1`$ Z-spectra to Bloch-McConnell equations.
Inherent model assumptions:
* Continuous wave irradiation (bloch saturation pulse)
* (Pseudo-) first order exchange schemes
* Signal measurement may not be at steady state.
Currently the package supports only two-site models.
Expansion for multi-pool models and *in-vivo* semi-solid pools is possible and may be implemented upon request.

## Features
* Choice of a method for solving Bloch-McConnell equations
    * Numerical solution, using matrix exponentiation
    * Analytical solution by [Zaiss and Bachert](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/nbm.2887), using an off-resonance spin-lock approximation
    * A revised spin-lock approximation to solving Bloch-McConnell equations that supports
        * Arbitrary identity of exchanging nuclei, given gyromagnetic ratio
        * Arbitrary fractions of equilibrium magnetizations of the exchanging pools (from symmetrical to highly assymetrical).
        * Arbitrary longitudinal relaxation rates, including rates common to paramagnetic compounds.
* Choice of a fitting procedure
    * Nonlinear least squares --- [Levenberg–Marquardt algorithm](https://en.wikipedia.org/wiki/Levenberg%E2%80%93Marquardt_algorithm)
    * Bayesian Markov chain Monte Carlo (MCMC) --- the No-U-Turn-Sampler ([NUTS](https://arxiv.org/abs/1111.4246))
    * Bayesian variational inference --- Stochastic Variational Inference ([SVI](https://arxiv.org/abs/1206.7051)), using a full-rank multivariate normal as the approximating distribution.

## Setup
This package builds on top of [QT6](https://doc.qt.io/qtforpython-6/), [Numpyro](https://num.pyro.ai/en/latest/index.html) and [lmfit](https://lmfit.github.io/lmfit-py/).

### Requirements
* Python 3.10 and above
* arviz
* jax
* lmfit
* matplotlib
* numpy
* numpyro
* pandas
* PyQt6
* pyqtgraph
* pyqtwaitingspinner
* toml

### Installation
1. Clone the repository to your desired directory using
```
git clone https://github.com/YuvalBernard/Z-spectra-fitting-app.git
```
2. Create a Python virtual environemnt in the local repository directory
```
python -m venv <directory>
```
3. Within the same directory, install the required packages using
```
pip install -r requirements.txt
```

You are ready to go!
## Usage
Data for fitting is expected in a .xlsx format.
See `APT_phantom.xlsx` for example.

To run the application, ensure that the virtual environment is activated, and type ``python main.py``.
This should open the GUI.
1. Select the data file and click next.
2. Fill in the experimental constants: static field strength, gyromagnetic ratio, saturation duration and saturation amplitude (as a comma separated list if fitting multi-$`B_1`$ Z-spectra.

You may also fill in the power levels automatically by clicking the designated button.
3. Configure variables for fitting: to set a parameter as a constant, change its state from `Vary` to `Static`.
Otherwise, for each fitting variable set the minimal and maximal values and an initial guess.
All of the fields above may be updated procedurally by loading a predefined configuration file in `toml` format. See the example file in the repository for details.
4. Choose a solver:
    * Symbolic (default) for the solution presented in the paper
    * Analytical for the solution by [Zaiss and Bachert](https://analyticalsciencejournals.onlinelibrary.wiley.com/doi/10.1002/nbm.2887)
    * Numerical for the solution via matrix exponentiation, without approximations.
5. Choose a fitting method:
    * Bayesian, Markov chain Monte Carlo (MCMC) --- via the NUTS algorithm
    * Bayesian, SVI -- Stochastica Variational Inference
    * NLS --- Nonlinear least squares --- Levenberg–Marquardt algorithm (default) or others of choice, described on the [lmfit](https://lmfit.github.io/lmfit-py/fitting.html) page
6. Each fitting method has a default configuration. You may change the parameters to your liking. Refer to [Numpyro documentation](https://num.pyro.ai/en/stable/) for additional information.
7. Once the fitting procedure is finished, you may save the results in a directory of choice. Depending on the fitting method, you may find:
    * Bayesian, MCMC
        * Plot of the best-fit Z-spectra
        * Excel file containing the original dataset, as well as the best-fit spectra via the posterior mean, median and mode
        * A text file containing summary statistics
        * A pair plot, describing relationships among fitting parameters
        * Effective-sample-size plot for each fitting parameter. This is a measure of the quality of the posterior samples obtained via NUTS. Refer to [Arviz](https://python.arviz.org/en/stable/api/generated/arviz.ess.html) for more information
    * Bayesian, SVI
        * Plot of the best-fit Z-spectra
        * Excel file containing the original dataset, as well as the best-fit spectra via the posterior mean, median and mode
        * A text file containing summary statistics
        * A pair plot, describing relationships among fitting parameters
        * A trace plot of the objective function for minimization at each iteration, also called the ELBO --- evidence lower bound
    * Nonlinear least squares
        * Plot of the best-fit Z-spectra
        * Excel file containing the original dataset and the best-fit simulation
        * A text file containing summary statistics
    See the `APT_phantom` folder for examples.
We strongly encourage using the Bayesian MCMC fitting method using the Symbolic solver.

## Contributing and contact info
This package is proprety of the [Leskes group](https://www.weizmann.ac.il/MCMS/Leskes/home) at the Weizmann Institude of Science.
However, you may freely make changes to the software and redistribute it. Please cite our paper while doing so!

We are open to suggestions for improving the software! Please contact [yuval.bernard@weizmann.ac.il].
You may also open a bug report or a feature request via Github.
