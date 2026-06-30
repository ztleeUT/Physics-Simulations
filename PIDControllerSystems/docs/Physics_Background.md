# PID Controller — RLC Circuit Simulation
Author: Zachary Lee
<hr>

A PID Controller is a feedback control system that continuously measures the difference between where a system is and where it should be, and applies a corrective force to drive the system toward its goal. PID is an acronym for Proportional,Integral, and Derivative, where each term means the following:

1) Proportional (P): responds to the current error. The further the system is from its target, the harder the controller corrects.

2) Integral (I): responds to accumulated past error. The controller corrects itself based on how long the system has been off course, eliminating steady-state error over time.

3) Derivative (D): responds to the rate of change of error. As the system approaches its target it eases the correction to prevent overshoot. Too much derivative gain causes a sluggish, slow response.

Each term contributes differently to system behavior. Proportional corrections can introduce oscillations, integral action can cause overshoot, and derivative action acts as a damper on the response.

Together, the PID control signal is modeled as:

$$ \boxed{u(t) = K_{p}e(t) + K_{i}\int_{0}^{t}e{(\tau)}d{\tau} + K_{d}\frac{de(t)}{dt}} $$

where $K_p$, $K_i$, and $K_d$ are the proportional, integral, and derivative gains respectively. Each coefficient is non-negative.

## Physical System — RLC Circuit

An RLC circuit consists of a resistor (R), inductor (L), and capacitor (C) connected in series. When a voltage is applied, charge flows through the circuit and the capacitor voltage responds dynamically over time.

The governing equation of motion is derived from Kirchhoff's Voltage Law:

$$ L\ddot{q} + R\dot{q} + \frac{1}{C}q = V(t) $$

where $q$ is the charge on the capacitor, $L$ is inductance (H), $R$ is resistance (Ω), $C$ is capacitance (F), and $V(t)$ is the voltage supplied by the PID controller.

This equation is mathematically identical in structure to a mass-spring-damper system:

$$ m\ddot{x} + b\dot{x} + kx = u(t) $$

where mass $m$ corresponds to inductance $L$, damping $b$ corresponds to resistance $R$, and spring constant $k$ corresponds to $1/C$. This equivalence is a powerful example of how the same mathematical framework describes fundamentally different physical systems — a core principle in systems engineering.

The goal of the PID controller in this simulation is to drive the capacitor voltage toward a target setpoint despite the circuit's natural dynamic response.