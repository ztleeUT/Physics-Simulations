## ** Author's Note **
My background is in physics and mathematics, and the focus of this project is on accurate modeling, numerical reasoning, and clear visualization of physical systems. I am actively expanding my software engineering skills, so the code in this repository prioritizes clarity, correctness, and transparency of the physics over optimization or advanced programming patterns.

This project reflects both my technical foundation and my ongoing growth as I build more experience with Python, numerical methods, and scientific computing.
##
Projectile Motion with Quadratic Drag Simulation

This project simulates projectile motion with and without quadratic air resistance using Python and Jupyter Notebook.

## Features
- Adjustable initial velocity, angle, mass, drag constant, and initial height
- Realistic quadratic drag model
- Side-by-side comparison of trajectories (drag vs no drag)
- Interactive sliders using ipywidgets
- Clean matplotlib visualizations

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
