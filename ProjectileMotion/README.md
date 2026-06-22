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

## How to Use Program

When the code loads, simply select a preset or adjust the sliders and press the "run" button. Doing so will generate the following plots:

- Impact Distance
- Impact Speed
- Impact Energy

It will also generate the distance, speed, and energy values when the projectile impacts the ground.

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
- $\frac{dx}{dt} = v_x$ &nbsp;&nbsp;&nbsp;
- $\frac{dy}{dt} = v_y$ &nbsp;&nbsp;&nbsp;
- $\frac{dv_x}{dt} = 0$ &nbsp;&nbsp;&nbsp;
- $\frac{dv_y}{dt} = -g$

### **Quadratic Drag Model**
Drag force:   
- $F_d = -c v^2$

Resulting accelerations:  
- ${a_x} = -\frac{c}{m} * v * v_x$
- ${a_y} = -g - \frac{c}{m} * v * v_y$ 
  
### **Ground Impact Detection**
An event function stops integration when:

- $y(t) = 0$

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
