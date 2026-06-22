# -----------------------------------------------------------------------------------------
# Plotting and Animation
# Creates static trajectory plots and an animated projectile visualization.
# The animation uses a fading trail and supports optional no-drag comparison.
# -----------------------------------------------------------------------------------------

import matplotlib.pyplot as plt

figsize = (9,6)
dpi = 100

def plot_simulation(results, show_nodrag_path=True):

    # Extract simulation results
    t = results["t"]
    x = results["x"]
    y = results["y"]

    # Single plot only
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
    
    # Plots the static trajectories.
    ax.plot(x, y, label="With Drag", color="blue", linestyle="--")

    if show_nodrag_path:
        ax.plot(results["x_nd"], results["y_nd"],
                label="Without Drag", color="red", linestyle="--")

    ax.set_xlabel("Distance (meters)")
    ax.set_ylabel("Height (meters)")
    ax.set_title("Projectile Motion: Drag vs No Drag")
    ax.grid(True)
    ax.legend()
    plt.tight_layout()
    
    return fig, ax  