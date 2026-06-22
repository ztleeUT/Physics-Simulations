# -----------------------------------------------------------------------------------------
# physics.py contains all of the code that governs the physics of the projectile.
# -----------------------------------------------------------------------------------------

import numpy as np

g = 9.81

# -----------------------------------------------------------------------------------------
# Kinematic Model Functions
# Handles the vector components and drag constant for kinematics with and without drag.
# -----------------------------------------------------------------------------------------
def make_kinematics_drag(m, c):
    
    def kinematics_drag(t, components):
        x, y, v_x, v_y = components
        v = np.hypot(v_x, v_y)
        a_x = -(c/m) * v_x * v          # Quadratic drag (x-component)
        a_y = -g - (c/m) * v_y * v      # Quadratic drag (y-component)
        return [v_x, v_y, a_x, a_y]
        
    return kinematics_drag


# Handles the components for a projectile without drag.
def make_kinematics_nd():
    
    def kinematics_nd(t, components):
        x_nd, y_nd, v_x_nd, v_y_nd = components
        return [v_x_nd, v_y_nd, 0.0, -g]
        
    return kinematics_nd


# Stops the simulation when y = 0 (projectile impacts ground).
def impact(t, components):
    return components[1]

impact.terminal = True
impact.direction = -1

# -----------------------------------------------------------------------------------------
# Error Prevention Functions
# Used to prevent a divide-by-zero error.
# I ran into a divide by zero error, and it took me more time than it should to realize.
# -----------------------------------------------------------------------------------------
def percent_difference(numerator, denominator):
    denom = denominator
    
    if denom == 0:
        return np.nan
        
    return (abs(numerator - denominator) / denom) * 100.0
    
# -----------------------------------------------------------------------------------------
# Place future functions that handles physics here.
# Examples include functions that handle atmospheric density, wind speed, and other forces
# that act on the projectile such as the Magnus Force.
# -----------------------------------------------------------------------------------------