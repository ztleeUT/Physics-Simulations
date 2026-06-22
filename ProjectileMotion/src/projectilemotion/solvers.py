# -----------------------------------------------------------------------------------------
# Contains the functions needed to solve ODE's.
# Is, essentially, the brain of the project.
# -----------------------------------------------------------------------------------------

import numpy as np
from scipy.integrate import solve_ivp
from projectilemotion.physics import *

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

def update_simulation(m=0.15, c=0.00086, y_0=0, angle=45, v_0=30, display_results=True):

    # Statements to handle possible errors from unrealistic values.
    if m <= 0: raise ValueError("Mass must be positive.")
    if c < 0: raise ValueError("Lumped Drag Coefficient must be positive.")
    if v_0 < 0: raise ValueError("Speed cannot be negative.")
    if not (0 <= angle <= 90): raise ValueError("Launch angle must be between 0 and 90.")
    if y_0 < 0: raise ValueError("Initial Height cannot be negative.")

    # Cache key
    key = (float(m), float(c), float(y_0), float(angle), float(v_0), float(SimConfig["time_step"]))
    if key in _sim_cache:
        return _sim_cache[key]

    impact_values.clear_output()

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

    # Prints both sets of values of the projectiles.
    if display_results:
        with impact_values:
            print(f"Impact distance (drag):      {x_impact:.2f} m")
            print(f"Impact distance (no drag):   {x_nd_impact:.2f} m")
            print(f"Distance Difference:         {abs(x_impact - x_nd_impact):.2f} m")
            dbz_x = percent_difference(x_nd_impact, x_impact)
            print(f"Percent Error (no drag):     {dbz_x:.2f} %")
            print("---------------------------------------------------------------")
            print(f"Impact Speed (drag):         {v_impact:.2f} m/s")
            print(f"Impact Speed (no drag):      {v_nd_impact:.2f} m/s")
            print(f"Speed Difference:            {abs(v_impact - v_nd_impact):.2f} m/s")
            dbz_v = percent_difference(v_nd_impact, v_impact)
            print(f"Percent Error (no drag):     {dbz_v:.2f} %")
            print("---------------------------------------------------------------")
            print(f"Impact Energy (drag):        {E_impact:.2f} joules")
            print(f"Impact Energy (no drag):     {E_nd_impact:.2f} joules")
            print(f"Energy Difference:           {abs(E_impact - E_nd_impact):.2f} joules")
            dbz_E = percent_difference(E_nd_impact, E_impact)
            print(f"Percent Error (no drag):     {dbz_E:.2f} %")

    results_simulation = {
        "t": t, "x": x, "y": y, "v": v, "E_t": E_t,
        "t_nd": t_nd, "x_nd": x_nd, "y_nd": y_nd, "v_nd": v_nd, "E_t_nd": E_t_nd
    }

    _sim_cache[key] = results_simulation
    return results_simulation