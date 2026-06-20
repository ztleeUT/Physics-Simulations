## ** Author's Note **
My background is in physics and mathematics, and the focus of this project is on accurate modeling, numerical reasoning, and clear visualization of physical systems. I am actively expanding my software engineering skills, so the code in this repository prioritizes clarity, correctness, and transparency of the physics over optimization or advanced programming patterns.

This project reflects both my technical foundation and my ongoing growth as I build more experience with Python, numerical methods, and scientific computing.

## Projectile Motion with Quadratic Drag.
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArchonL33/Physics-Simulations/blob/main/ProjectileMotion/HEAD?urlpath=%2Fdoc%2Ftree%2FProjectileMotion.ipynb)
A numerical simulation and visualization project using Python. This project models projectile motion under two conditions:
- With quadratic air resistance (realistic physics)
- Without air resistance (idealized parabola)

The simulation uses numerical integration to compute the trajectory and plots both paths on the same graph for direct comparison. Adjustable parameters allow exploration of how launch conditions and drag strength affect the motion.

## Features
- Realistic quadratic drag model.
- Side‑by‑side comparison of drag vs. no‑drag trajectories.
- Adjustable parameters:
    - Initial velocity.
    - Launch angle.
    - Mass.
    - Drag constant.
    - Initial height.
- Clean matplotlib visualizations.
- Optional interactive sliders using ipywidgets.
- Clear, readable physics‑focused code.

## Files
- `ProjectileMotion.ipynb` — main notebook with simulation and plots.

## Physics Model

I derived the equations for projectile motion (kinematics) and other useful formulas to aid in this project.
Such examples used are:

The drag force is modeled as:

F_drag = -c * v^2 * v_hat

where  
- c = ½ ρ C_d A  
- v is speed  
- v_hat is the unit velocity vector

## Requirements
- Python 3
- NumPy
- Matplotlib
- ipywidgets

## Author
Zachary Lee
