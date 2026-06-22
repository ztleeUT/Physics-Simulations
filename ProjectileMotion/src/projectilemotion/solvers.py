# -----------------------------------------------------------------------------------------
# Contains the functions needed to solve ODE's.
# Is, essentially, the brain of the project.
# -----------------------------------------------------------------------------------------

import numpy as np
from scipy.integrate import solve_ivp
from projectilemotion.physics import *
from projectilemotion.validation import *

max_time = 30
time_step = 0.01

# SciPy integration configuration
SimConfig = {"time_step": time_step, "dense_output": False, "rtol": 1e-6, "atol": 1e-8}

# Cache to avoid recomputing identical simulations
try:
    _sim_cache
except NameError:
    _sim_cache = {}

# -----------------------------------------------------------------------------------------
# Simulation Functions
# Runs the projectile simulation (drag + no-drag).
# Returns both sets of values for use with the "Run" button.
# -----------------------------------------------------------------------------------------

def update_simulation(m=0.15, c=0.00086, y_0=0, angle=45, v_0=30):

    # Checks for input errors from validation.py
    validate_inputs(m, c, y_0, angle, v_0)

    # Cache key
    key = (float(m), float(c), float(y_0), float(angle), float(v_0), float(SimConfig["time_step"]))
    if key in _sim_cache:
        return _sim_cache[key]

    theta = np.radians(angle)
    v_x0 = v_0 * np.cos(theta)
    v_y0 = v_0 * np.sin(theta)
    components_0 = [0.0, y_0, v_x0, v_y0]

    t_eval = np.arange(0.0, max_time + SimConfig["time_step"], SimConfig["time_step"])

    f_d = make_kinematics_drag(m, c)
    f_nd = make_kinematics_nd()

    # Numerically solves both sets of kinematic equations for the projectile.
    solution = solve_ivp(
        f_d, (0.0, max_time), components_0,
        events=impact, t_eval=t_eval,
        dense_output=SimConfig["dense_output"],
        rtol=SimConfig["rtol"], atol=SimConfig["atol"]
    )

    solution_nd = solve_ivp(
        f_nd, (0.0, max_time), components_0,
        events=impact, t_eval=t_eval,
        dense_output=SimConfig["dense_output"],
        rtol=SimConfig["rtol"], atol=SimConfig["atol"]
    )

    # Extract results
    t = solution.t
    x, y, v_x, v_y = solution.y
    v = np.hypot(v_x, v_y)

    t_nd = solution_nd.t
    x_nd, y_nd, v_x_nd, v_y_nd = solution_nd.y
    v_nd = np.hypot(v_x_nd, v_y_nd)

    # Impact energy values
    KE = 0.5 * m * v**2
    PE = m * g * y
    E_t = KE + PE

    KE_nd = 0.5 * m * v_nd**2
    PE_nd = m * g * y_nd
    E_t_nd = KE_nd + PE_nd

    # Impact values
    x_impact = x[-1]
    v_impact = v[-1]
    E_impact = E_t[-1]

    x_nd_impact = x_nd[-1]
    v_nd_impact = v_nd[-1]
    E_nd_impact = E_t_nd[-1]
 
    results_simulation = {
    "t": t, "x": x, "y": y, "v": v, "E_t": E_t,
    "t_nd": t_nd, "x_nd": x_nd, "y_nd": y_nd, "v_nd": v_nd, "E_t_nd": E_t_nd,
    "x_impact": x_impact, "v_impact": v_impact, "E_impact": E_impact,
    "x_nd_impact": x_nd_impact, "v_nd_impact": v_nd_impact, "E_nd_impact": E_nd_impact}

    _sim_cache[key] = results_simulation
    
    return results_simulation
