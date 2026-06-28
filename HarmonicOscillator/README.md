## ** Author's Note **
My background is in physics and mathematics, and the focus of this project is on accurate modeling, numerical reasoning, and clear visualization of physical systems. I am actively expanding my software engineering skills, so the code in this repository prioritizes clarity, correctness, and transparency of the physics over optimization or advanced programming patterns.

This project reflects both my technical foundation and my ongoing growth as I build more experience with Python, numerical methods, and scientific computing.

## Damped Harmonic Oscillator Simulation
A Python simulation and visualization of underdamped, overdamped, and critically damped harmonic oscillators using Euler's method.

This project numerically solves the second-order differential equation,

- x'' + 2*y*x' + w^2x = 0

by converting it into a system of first-order ODEs and integrating forward in time. The simulation also detects when each oscillator reaches equilibrium and compares how long each damping type takes to reach equilibrium.

## Features
- Simulates three damping types:
    - underdamped.
    - overdamped.
    - critically damped.
- Numerical integration using Euler's Method.
- Automatic equilibrium detection.
- Configurable physical parameters.
	- Mass (m).
	- Spring Constant (k).
	- Damping Coefficient (b).

## How to Use

## Installation

## Quick Start

## Physics Model
In the notebook, I derive everything we need starting with Newton's Second Law and Hooke's Law. I delve more deeply in derivations and explain each step I took. Having knowledge of Calculus and Ordinary Differential Equations isn't necessary, but it helpful in understanding each step.
 
## Requirements
- Python 3
- NumPy
- Matplotlib
- ipywidgets

### Want the full derivations? 
> Open **`docs/HarmonicOscillator_Derivations.md`** to learn how to get the characteristic equation that is used in this simulation.

## Author
Zachary Lee
