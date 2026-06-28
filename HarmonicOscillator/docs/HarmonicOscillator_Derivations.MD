## Harmonic Oscillator Simulation
#### Author: Zachary Lee
<hr>

Description: A simulation that models Harmonic Oscillators and shows the effects of it being underdamped, overdamped, and critically damped. For this simulation, I will be using a mass (m) on a spring that is attached to a block/wall.

So, what is a harmonic oscillator? Believe it or not, we interact with them constantly. Someone bouncing on a pogo stick, riding a playground swing, strumming a guitar string, or even the vibration of our vocal cords when we speak, all of these are examples of harmonic oscillators. Even electronic circuits, such as LC circuits, behave like harmonic oscillators because their voltages and currents oscillate in the same way a mass on a spring does.

In short, a harmonic oscillator is a system that experiences oscillations due to a restoring force that is proportional to its displacement from equilibrium. A simpler way to say this is: it moves back and forth because a force always pulls it back toward its starting position.
<hr>

## Deriving the Characteristic Equation
We can derive the equation of motion for a harmonic oscillator using Hooke’s Law:

$$ (1)\quad \boxed{F = -kx} $$

where $F$ is the restoring force, $k$ is the spring constant, and $x$ is the displacement from equilibrium. Hooke's Law tells us the force at a given displacement, but it does not describe how the system evolves over time. To do that, we can combine Newton's Second Law: $\vec{F} = m\vec{a}$ and Hooke's Law: $\vec{F} = -kx$. Doing so gives the equation:

$$ (2)\quad \boxed{m\vec{a} = -kx} $$

If you have experience with calculus, you'll know that acceleration, velocity, and position are connected through their derivatives with respect to time. This relationship can be summarized as: $x(t) \xrightarrow{\frac{d}{dt}} v(t) \xrightarrow{\frac{d}{dt}} a(t)$. In other words, acceleration $a(t)$ is the second time derivative of position $x(t)$, which we write as $\ddot{x}(t)$. Using this knowledge, we can rewrite equation (2) as:

$$ (3)\quad \boxed{m\ddot{x} = -kx} $$

However, this describes an ideal, undamped oscillator. Real systems lose energy due to friction or drag. A simple and common model for this is adding a damping force that is proportional to velocity $F_d = -b\dot{x}$. We have $-b\dot{x}$ be negative because it is opposing the motion. Accounting for that, we can finally get our equation for motion.

$$ (4)\quad \boxed{m\ddot{x} = -kx - b\dot{x}} $$

Now this is where things get interesting. We can rewrite equation (4) as: $ m\ddot{x} + b\dot{x} + kx = 0$, doing so gives the following differential equation.

$$ (5)\quad \boxed{\ddot{x} + \frac{b}{m}\dot{x} + \frac{k}{m}x = 0} $$

This is a second-order homogeneous differential equation describing a damped harmonic oscillator. It becomes much easier to analyze if we define two important quantities.
- The Natural Frequency: $\omega = \sqrt{\frac{k}{m}}$, which is the frequency the system would oscillate at with no damping.
- The Damping Constant: $\gamma = \frac{b}{2m}$, which measures how quickly energy is lost from the system.

With the above definitions, we obtain an equation that describes the motion of a damped harmonic oscillator.

$$ (6)\quad \boxed{\ddot{x} + 2\gamma\dot{x} + \omega^2x = 0} $$

Before moving on, a damped harmonic oscillator can be in either one of three states: underdamped, overdamped, and critically damped.
- Underdamped ($\gamma < \omega$): The system will oscillate, but the amplitude decreases over time as energy is lost. The mass on the spring will overshoot the equilibrium position repeatedly.
- Overdamped ($\gamma > \omega$): The system returns to equilibrium without oscillating. It moves more slowly, when compared to critically damped, toward its equilibrium position and will never overshoot.
- Critically Damped ($\gamma = \omega$): The system returns to equilibrium without oscillating. It will return to its equilibrium position within the quickest time possible.

Going back to where we left off with equation (6), we have a second-order homogeneous differential equation. A standard method for solving such equations is to assume an exponential solution with the form:

$$ (7)\quad \boxed{x(t) = e^{rt}} $$

where $r$ is a constant to be determined. Substituting this guess into equation (6) gives:

$$ (8)\quad \boxed{r^2e^{rt} + 2\gamma{r}e^{rt} + \omega^2e^{rt} = 0} $$

We can factor out $e^{rt}$, leaving us with our characteristic equation:

$$ (9)\quad \boxed{r^{2} + 2\gamma{r} + \omega^2 = 0} $$

Equation (9) determines the behavior of the system. If we solve it for r, we get the solution $r = -\gamma {\pm}\sqrt{\gamma^2-\omega^2}$.  If we take a look at this solution and use the definition of underdamped ($\gamma < \omega$), overdamped ($\gamma > \omega$), and critically damped ($\gamma = \omega$). We obtain different solutions.
- Underdamped ($\gamma < \omega$): where $r = -\gamma \pm i\omega_{d}$ and $\omega_{d} = \sqrt(\omega^2 - \gamma^2)$. The solution to equation (9) becomes $\boxed{x(t) = e^{-\gamma{t}}(A\cos(\omega_{d}{t}) + B\sin(\omega_{d}{t}))}$.

- Overdamped ($\gamma > \omega$): where $r = -\gamma \pm \sqrt{\gamma^2 - \omega^2}$ The solution to equation (9) becomes $\boxed{x(t) = Ce^{r_{1}t} + De^{r_{2}t}}$.

- Critically Damped ($\gamma = \omega$): where $r = -\gamma$. The solution to equation (9) becomes $\boxed{x(t) = (A + Bt)e^{-\gamma{t}}}$.

We now have all of the information we need to model a harmonic oscillator.
