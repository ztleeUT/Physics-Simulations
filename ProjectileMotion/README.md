# Projectile Motion Simulator


An interactive physics simulation that models projectile motion **with and without aerodynamic drag**.  
This tool visualizes trajectories, speed, and energy in real time using adjustable parameters and presets for common objects.

---

## Overview

This simulation numerically solves the equations of motion for a projectile launched at an angle, comparing:

- **Ideal motion (no drag)**
- **Realistic motion (quadratic drag)**

The interface allows you to adjust:

- Mass  
- Drag coefficient  
- Launch angle  
- Initial height  
- Initial velocity  

You can also select from several real‑world presets (baseball, soccer ball, shotput, etc.).

---

## Try It Online

Launch the fully interactive version in your browser:
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ArchonL33/Physics-Simulations/HEAD?labpath=ProjectileMotion%2Fprojectile_sim.ipynb) 
No installation required.

---

## Preview

### User Interface
![UI](images/ui.png)

### Trajectory Comparison (Drag vs No Drag)
![Trajectory](images/trajectory.png)

### Speed vs Time
![Speed](images/speed.png)

### Energy vs Time
![Energy](images/energy.png)


---

## Physics Model

The simulation solves a system of four coupled ODEs representing:

- Horizontal position \( x \)  
- Vertical position \( y \)  
- Horizontal velocity \( v_x \)  
- Vertical velocity \( v_y \)

### **No‑Drag Model**



$\dot{x} = v_x,\quad$ 
$\dot{y} = v_y,\quad$ 
$\dot{v_x} = 0,\quad$ 
$\dot{v_y} = -g$




### **Quadratic Drag Model**
Drag force:


F_d = -c v^2



Resulting accelerations:



\dot{v_x} = -\frac{c}{m} v v_x,\quad 
\dot{v_y} = -g - \frac{c}{m} v v_y




### **Ground Impact Detection**
An event function stops integration when:



y(t) = 0




This allows accurate calculation of:

- Impact distance  
- Impact speed  
- Impact kinetic energy  

---

## Features

- Real‑time interactive plots  
- Drag vs no‑drag comparison  
- Speed and energy visualization  
- Adjustable physical parameters  
- Presets for real objects  
- Clean UI with sliders and output panel  
- Numerical integration using `scipy.integrate.solve_ivp`

---
