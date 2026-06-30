# PID Controller for RLC Circuit Simulation
Author: Zachary Lee
<hr>

This simulation will model a PID Controller controlling the output of a RLC Circuit. A PID Controller is a feedback control system that continuously measures the difference between where a system is and where it should be, and applies a corrective force to drive the system toward its goal. PID is an acronym for Proportional, Integral, and Derivative, where each term means the following:

1) Proportional (P): responds to the current error. The further the system is from its target, the harder the controller corrects.

2) Integral (I): responds to accumulated past error. The controller corrects itself based on how long the system has been off course, eliminating steady-state error over time.

3) Derivative (D): responds to the rate of change of error. As the system approaches its target it eases the correction to prevent overshoot. Too much derivative gain causes a sluggish, slow response.

Each term contributes differently to system behavior. Proportional corrections can introduce oscillations, integral corrections can cause overshoot, and derivative corrections act as a damper on the response.

Together, the PID control signal is modeled as:

$$ \boxed{u(t) = K_{p}e(t) + K_{i}\int_{0}^{t}e{(\tau)}d{\tau} + K_{d}\frac{de(t)}{dt}} $$

where $K_p$, $K_i$, and $K_d$ are the proportional, integral, and derivative gain coefficients respectively, $e(t)$ is the error signal defined as the difference between the target setpoint $r(t)$ and the measured output $y(t)$:

$$ e(t) = r(t) - y(t) $$

and $e(\tau)$ is the error as a function of the integration variable 
$\tau$, representing the history of past errors from time $0$ to the 
current time $t$. Each gain coefficient is non-negative.

## RLC Circuit

An RLC circuit consists of a resistor (R), inductor (L), and capacitor (C) connected in series. When a voltage is applied, charge flows through the circuit and the capacitor voltage responds dynamically over time.

The governing equation to model flowing charge is derived from Kirchhoff's Loop Laws (which will be covered in the next section):

$$ L\ddot{q} + R\dot{q} + \frac{1}{C}q = V(t) $$

where $q$ is the charge on the capacitor, $L$ is inductance (H), $R$ is resistance (Ω), $C$ is capacitance (F), and $V(t)$ is the voltage supplied by the PID controller.

This equation is mathematically identical in structure to a mass-spring-damper system (see my Harmonic Oscillator project for full derivation):

$$ m\ddot{x} + b\dot{x} + kx = u(t) $$

where mass $m$ corresponds to inductance $L$, damping $b$ corresponds to resistance $R$, and spring constant $k$ corresponds to $1/C$. This equivalence is a powerful example of how the same mathematical framework describes fundamentally different physical systems, which is valuable across engineering disciplines including electrical engineering, test engineering, and systems engineering.

## Kirchhoff's Loop Laws

Kirchhoff's Loop Laws describe the behavior of voltage and current 
in electrical circuits and form the foundation of circuit analysis.

### Kirchhoff's Current Law (KCL)
The sum of all currents entering a node must equal the sum of all 
currents leaving that node:

$$ \sum I_{in} = \sum I_{out} $$

In other words, charge is conserved at every junction in a circuit. 
No charge accumulates at a node.

### Kirchhoff's Voltage Law (KVL)
The sum of all voltage drops around any closed loop in a circuit must equal zero:

$$ \sum V = 0 $$

Equivalently, the sum of voltage rises must equal the sum of voltage drops around any closed loop. This is a statement of conservation of energy.

### Applying KVL to a Series RLC Circuit

For a series RLC circuit with an applied voltage V(t), KVL gives:

$$ V(t) - V_R - V_L - V_C = 0 $$

Which rearranges to:

$$ V(t) = V_R + V_L + V_C $$

We can use Ohm's law: $V = IR$,  where $V$ = voltage, $I$ = current, $R$ = resistance, to get the component voltage relationships:

- Resistor: $V_R = IR$
- Inductor: $V_L = L\frac{dI}{dt}$
- Capacitor: $V_C = \frac{q}{C}$

$$ V(t) = IR + L\frac{dI}{dt} + \frac{q}{C} $$

Since current is the time derivative of charge, $I = \dot{q}$:

$$ V(t) = R\dot{q} + L\ddot{q} + \frac{q}{C} $$

Rearranging into standard second-order ODE form:

$$ L\ddot{q} + R\dot{q} + \frac{1}{C}q = V(t) $$

With the governing ODE established, the PID control signal $V(t)$ can now be defined numerically.

## Numerical Implementation of PID

In continuous time the PID control law is:

$$ u(t) = K_{p}e(t) + K_{i}\int_{0}^{t}e(\tau)d\tau + 
K_{d}\frac{de(t)}{dt} $$

In a numerical simulation time is discretized into small steps of size $\Delta t$. Each term is approximated as follows:

### Proportional Term
The proportional term requires no approximation, it is evaluated directly at each timestep:

$$ u_P = K_p \cdot e(t) $$

### Integral Term
The continuous integral is approximated using a running sum (Riemann sum) accumulated over each timestep:

$$ u_I = K_i \cdot \sum_{j=0}^{t} e(j) \cdot \Delta t $$

In code this is implemented as a running accumulator that adds the current error multiplied by the timestep at each iteration:

### Derivative Term
The continuous derivative is approximated using a backward finite difference, the change in error divided by the timestep:

$$ u_D = K_d \cdot \frac{e(t) - e(t - \Delta t)}{\Delta t} $$

In code this is implemented by storing the previous error and computing the difference at each iteration:

### Total Control Signal
At each timestep the three terms are summed to produce the total control signal applied to the circuit:

$$ u(t) = u_P + u_I + u_D $$

### Accuracy Considerations
The accuracy of these approximations improves as $\Delta t$ decreases. A smaller timestep produces a closer approximation to the true continuous behavior but increases computational cost. For this simulation a timestep of $\Delta t = 0.001$ seconds provides sufficient accuracy for the system parameters used.
