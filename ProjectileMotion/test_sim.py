from projectilemotion.solver import update_simulation
from projectilemotion.plotting import plot_simulation
from projectilemotion.animation import create_animation
from projectilemotion.physics import percent_difference
import matplotlib.pyplot as plt


# -----------------------------
# Predefined Projectile Values
# -----------------------------

PROJECTILES = {
    "Ping-Pong Ball":   {"m": 0.0027, "c": 0.000362},
    "Baseball":   {"m": 0.145, "c": 0.00084},
    "Soccerball":   {"m": 0.450,  "c": 0.00582},
    "Coconut":      {"m": 2.00, "c": 0.00701},
    "Shotput": {"m": 7.62,   "c": 0.00326},   # example
    "Cannonball": {"m": 14.51,   "c": 0.00443}
}

def get_float(prompt, default):
    text = input(f"{prompt} [{default}]: ").strip()
    return float(text) if text else default

def get_value_or_preset(prompt, default):
    text = input(f"{prompt} [{default} or projectile name]: ").strip()

    if text in PROJECTILES:
        return PROJECTILES[text]["m"], PROJECTILES[text]["c"]

    if text == "":
        return default, None

    try:
        m = float(text)
        return m, None
    except ValueError:
        print("Invalid input. Using default.")
        return default, None

print("\nEnter simulation parameters (press Enter to use defaults):")

print("\nAvailable preset projectiles:")
for name in PROJECTILES:
    print(f"  - {name}")

m_input, preset_c = get_value_or_preset("Mass (kg)", 0.15)

if preset_c is not None:
    m = m_input
    c = preset_c
    print(f"Using preset projectile values: m={m}, c={c}")
else:
    m = m_input
    c = get_float("Drag constant", 0.00086)

y0    = get_float("Initial height (m)", 0)
angle = get_float("Launch angle (degrees)", 45)
v0    = get_float("Initial speed (m/s)", 30)

# -----------------------------
# Helper to print impact values
# -----------------------------
def print_impact_results(results):
    x_impact      = results["x_impact"]
    v_impact      = results["v_impact"]
    E_impact      = results["E_impact"]
    x_nd_impact   = results["x_nd_impact"]
    v_nd_impact   = results["v_nd_impact"]
    E_nd_impact   = results["E_nd_impact"]

    print("\n=== Impact Results ===")
    print(f"Impact distance (drag):      {x_impact:.2f} m")
    print(f"Impact distance (no drag):   {x_nd_impact:.2f} m")
    print(f"Distance Difference:         {abs(x_impact - x_nd_impact):.2f} m")
    print(f"Percent Error (no drag):     {percent_difference(x_nd_impact, x_impact):.2f} %")
    print("---------------------------------------------------------------")
    print(f"Impact Speed (drag):         {v_impact:.2f} m/s")
    print(f"Impact Speed (no drag):      {v_nd_impact:.2f} m/s")
    print(f"Speed Difference:            {abs(v_impact - v_nd_impact):.2f} m/s")
    print(f"Percent Error (no drag):     {percent_difference(v_nd_impact, v_impact):.2f} %")
    print("---------------------------------------------------------------")
    print(f"Impact Energy (drag):        {E_impact:.2f} joules")
    print(f"Impact Energy (no drag):     {E_nd_impact:.2f} joules")
    print(f"Energy Difference:           {abs(E_impact - E_nd_impact):.2f} joules")
    print(f"Percent Error (no drag):     {percent_difference(E_nd_impact, E_impact):.2f} %")

# -----------------------------
# Run simulation
# -----------------------------
result = update_simulation(
    m=m,
    c=c,
    y_0=y0,
    angle=angle,
    v_0=v0
)

print_impact_results(result)

# -----------------------------
# Plot + animation
# -----------------------------
fig, ax = plot_simulation(result)
anim = create_animation(fig, ax, result)

plt.show()
