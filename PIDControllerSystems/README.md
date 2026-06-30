# PID Controller for RLC Circuit Simulation

A discrete-time PID controller implementation that regulates the 
capacitor voltage of a series RLC circuit toward a target setpoint. 
This project models the governing circuit dynamics from first 
principles using Kirchhoff's Loop Laws, then designs and tunes a 
feedback controller to drive the system to a desired state — 
demonstrating the same control theory principles used in electrical, 
systems, and test engineering applications.

![PID Tuning Comparison](images/pid_animation.gif)

## Project Motivation

A PID controller is one of the most widely used feedback control 
mechanisms in engineering, applied across electrical systems, 
aerospace guidance, industrial automation, and robotics. This project 
demonstrates the mathematical equivalence between a series RLC circuit 
and a mass-spring-damper mechanical system — both governed by the same 
second-order differential equation structure — and shows how a single 
control framework can be applied across fundamentally different 
physical systems.

## Physics and Control Theory

The RLC circuit's governing equation is derived from Kirchhoff's 
Voltage Law:

$$ L\ddot{q} + R\dot{q} + \frac{1}{C}q = V(t) $$

where $V(t)$ is the voltage signal supplied by the PID controller. 
The controller continuously measures