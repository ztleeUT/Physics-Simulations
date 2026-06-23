## 2D Projectile Motion With Drag.
### Author: Zachary Lee
<hr>


Description: The purpose of this project is to build upon my programming skills using my background in physics and math. I will consider this project to be successful when two things are accomplished:
1) Derive all the math needed to explain the motion of projectiles within this project.
2) Use the derived math to accurately model projectile motion when various forms of drag is applied.
<hr>

### Derivation of Kinematics Equations
<hr>

What exactly is kinematics? Kinematics is a branch of physics that studies the motion of objects without considering the forces that cause the motion. It is a field that emphasizes the relationships between the positions, velocity, and acceleration of moving objects. Equations that describe the motion of a projectile (kinematics) can be derived from the definitions of average acceleration and average velocity.

$$(a)\quad \boxed{\text{Average Acceleration = } \bar{a} = \frac{\Delta v}{\Delta t} = \frac{v_2 - v_1}{t_2 - t_1}}$$
$$(b)\quad \boxed{\text{Average Velocity = } \bar{v} = \frac{\Delta x}{\Delta t} = \frac{x_2 - x_1}{t_2 - t_1} = \frac{v_0 + v}{2}}$$

<div style="display:flex; justify-content:center; gap:10px;">
    
<span style="display:inline-block;">Where: $v_1$ = starting velocity,</span>
<span style="display:inline-block;"> $v_2$ = final velocity,</span>
<span style="display:inline-block;"> $x_1$ = starting position,</span>
<span style="display:inline-block;"> $x_2$ = final position,</span>
<span style="display:inline-block;"> $t_1$ = initial time,</span>
<span style="display:inline-block;">and  $t_2$ = end time.</span>

</div>

In the above, $velocity$ and $time$ are used to describe $acceleration$, while $position$ and $time$ describe $velocity$. In this simulation, the initial time will always be equal to zero, meaning $t_1 = 0$. By substituting this into equation (1), and solving for $v$, you can get the first kinematics equation:

$$ (1)\quad \boxed{a_x = -\frac{c}{m} v v_x} $$


Deriving $ \bar{v} = \frac{v_0 + v}{2} $ from equation (b) can be accomplished using geometry or integration. From integration, start with equation (1): $v(t) = v_0 + at$, and integrate both sides of the equation with respect to time $t$ from $t_1$ to $t_2$. This gives $\int_{t_1}^{t_2} v dt = \int_{t_1}^{t_2} (v_0 + at)dt \rightarrow v(t) \left. \right|_{t_1}^{t_2} = v_0t \left. \right|_{t_1}^{t_2} + \frac{a t^2}{2}\left. \right|_{t_1}^{t_2} \rightarrow \bar{v} = v_0 + \frac{1}{2}a(t)$. Equation (a) can be rewritten as $at = v - v_0$ and plugged into equation (1) to get $\bar{v} = v_0 + \frac{1}{2}(v-v_0) \rightarrow \boxed{\bar{v} = \frac{v_0 + v}{2}}$. Using equation (b), which was just derived, and the relation $\Delta{x} = \bar{v}t$, you get the second kinematic equation 


$$ (2)\quad \boxed{\Delta{x} = \frac{1}{2}(v_0+v)t} $$


Next, substituting the expression for $v$ from the equation (1) into equation (2), you can get the third kinematics equation. 


$$ (3)\quad \boxed{\Delta{x} = v_0t + \frac{1}{2}at^2} $$


Finally, if you take equation (1), solve for $t$, and substitute $t$ into equation (2) and solve for $v^2$, you obtain the fourth kinematics equation.


$$ (4)\quad \boxed{v^2 = v_0^2 + 2a\Delta{x}} $$

The four kinematics equations that can be used to decribe the motion of a projectile have been derived. In this simulation these equations and knowledge with vector math will be used to model projectile motion. 

### Understanding The Drag Force
<hr>

Although these equations assume motion with constant acceleration, this simulation uses numerical integration because drag makes acceleration velocity-dependent. This means that drag acts as a force on projectiles and slows it down as it moves through the air. If this wasn't accounted, the projectiles would land much farther than you would see in a real-life demonstration. In order to account for drag, it is helpful to understand the various types of drag to most accurately account for it. Drag can take on three "classical" forms. Note: There are more than three types of drag such as drag on a spinning bullet (Magnus Effect) or drag that is wind-relative. This simulation will assume the projectile that is being launches has no rotation, no wind speed, etc.

* ${Linear\text{ }Drag:} \text{ }(F_d = -bv)$ <br>
  Best for small, slower moving objects where flow remains smooth.<br><br>
* ${Quadratic\text{ }Drag:} \text{ }(F_d = -cv^2)$ <br>
  Most accurate for larger, faster objects (e.g. baseballs, arrows, bullets) where flow is turbulent.<br><br>
* ${Mixed\text{ }Drag:} \text{ }(F_d = -bv - cv^2)$ <br>
  Applies when an object starts fast (turbulent flow) but slow enough for the flow to become smooth.

In order to determine if a medium's flow is laminar (smooth) or turbulent (chaotic), you measure the ratio of inertial forces to viscous forces in a fluid. This ratio is known as the Reynolds Number and can be calculated using.

$$ \boxed{R_e = \frac{uL}{v}} $$

The Reynolds Number is dependent on: $u$ = flow velocity ($\frac{m}{s}$), $L$ = characteristic length ($m$), $v$ = kinematic viscosity ($\frac{m}{s}$).
        
For now, do not worry about where $b$ or $c$ originate from, I will cover their derivation in the next section. In the simulation, the initial properties of the projectile will match a baseball. A baseball is large compared to air molecules and travels fast enough that turbulent flow dominates. With this in mind, a quadratic drag model will be most accurate to describe it's motion. Including gravity and quadratic dra, the net force on the projectile is: $$\boxed{\sum\vec{F} = m\vec{g} - c{v^2}{\hat{v}}}$$

You can break up the net force on the projectile into its x and y components using the velocity unit vector, $\hat{v} = \frac{\vec{v}}{||v||}$, where $||v|| = \sqrt{v_x^2 + v_y^2} = v$. Plugging the new velocities into the equation for the forces on the projectile, you end up with the x and y components describing the projectile's acceleration:

$$ &nbsp;  \boxed{a_x = -\frac{c}{m} v v_x} $$

$$ &nbsp; \boxed{a_y = g_y - \frac{c}{m} v v_y} $$

### Explaining Bernoulli's Equation
<hr>

When we covered drag there were variables such as $v$ and $c$. In the case of $c$ this comes from the equation $F_d = \frac{1}{2}\rho{C_d}A{v^2}$. This equation is derived from fluid mechanics concepts starting with Bernoulli's Equation.

$$ (5)\quad \boxed{p_1 + \frac{1}{2}\rho{v_1^2} + \rho{g}{h_1} = p_2 + \frac{1}{2}\rho{v_2^2} + \rho{g}{h_2}} $$

<div style="display:flex; justify-content:center; gap:15px;">
    
<span style="display:inline-block;">Where: $p_{1,2}$ = static pressure,</span>
<span style="display:inline-block;"> $\rho$ = density of the fluid,</span>
<span style="display:inline-block;"> $v_{1,2}$ = flow speed of fluid,</span>
<span style="display:inline-block;"> $g$ = gravitational acceleration,</span>
<span style="display:inline-block;">and $h_{1,2}$ = reference height.</span>
</div>

When both heights are the same, $\rho$, $g$, and $h$ cancels out. Using equation (5) to solve for $p_1$ you get the equation $p_1 = p_2 + \frac{1}{2}\rho{v^2}$. If you arrange it so that both static pressure is on one side of the equation you get $p_1 - p_2 = \frac{1}{2}\rho{v^2}$. Here, $p_1 - p_2$ is something called dynamic pressure which I will represent with $q$. Dynamic pressure is the kinetic energy per unit volume inside a moving fluid. It's formula is written as $q = \frac{1}{2}\rho{v^2}$. The relationship $Force$ = $Pressure$ $*$ $Area$ can be used to convert dynamic pressure into a force. Doing so gives $F_p = qA \rightarrow F_p = (\frac{1}{2}\rho{v^2})A$. This gives the drag force for an object that is flat. In order to get the drag force that accounts for an objects shape, you need to introduce a variable that is dimensionless that is known as a correction factor $C_d$. Doing so, this gives the final drag equation:

$$ (6)\quad \boxed{F_d = \frac{1}{2}\rho{C_d}{A}{v^2}} $$

To make things simpler you can use the lumped drag constant $c$, which has units $\frac{kg}{m}$:

 $$ (7)\quad \boxed{c = \frac{1}{2} \rho C_d A} $$ 

This simulation will use the lumped drag constant of various objects to model drag on various projectiles.
You have covered all of the math needed in our simulation (and then some). You can now move from the theoretical physics to computational physics. Note: For the simulation of a projectile that has no drag, the mass will not affect things. Therefore, you'll notice that selecting various presets does not affect the impact distance and impact speed.
