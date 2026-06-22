# -----------------------------------------------------------------------------------------
# Widgets, UI Layout, and Callbacks
# Creates sliders, buttons, dropdowns, and output areas for interactive control.
# Includes presets, reset functionality, CSV export, GIF saving, and angle sweep.
# -----------------------------------------------------------------------------------------

import numpy as np
import pandas as pd
import ipywidgets as widgets
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter
from IPython.display import HTML, display
from projectilemotion.solvers import update_simulation
from projectilemotion.plotting import plot_simulation
from projectilemotion.plotting import plot_simulation, figsize, dpi
from projectilemotion.physics import percent_difference

impact_values = widgets.Output()
plot_output = widgets.Output()
error_output = widgets.Output()
sweep_output = widgets.Output()
save_notice_output = widgets.Output()
save_dialog_output = widgets.Output()

# Text containing relevant values.
def display_impact_results(results):
    x_impact      = results["x_impact"]
    v_impact      = results["v_impact"]
    E_impact      = results["E_impact"]
    x_nd_impact   = results["x_nd_impact"]
    v_nd_impact   = results["v_nd_impact"]
    E_nd_impact   = results["E_nd_impact"]

    with impact_values:
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

# Sliders.
m_slider = widgets.FloatSlider(value=0.145, min=0.01, max=20, step=0.001,
                               description="Mass (kg)")
c_slider = widgets.FloatSlider(value=0.00086, min=0.0, max=0.005, step=0.0001,
                               description="Lumped Drag Coefficient",
                               readout_format=".5f")
y_0_slider = widgets.FloatSlider(value=0, min=0, max=100, step=1,
                                 description="Initial Height (m)")
angle_slider = widgets.FloatSlider(value=45, min=0, max=90, step=1,
                                   description="Angle (degrees)")
v_0_slider = widgets.FloatSlider(value=30, min=1, max=100, step=1,
                                 description="Initial Speed (m/s)")
                                 
# Buttons
reset_button = widgets.Button(description="Reset", button_style="warning",
                              tooltip="Reset all sliders to initial values")
run_button = widgets.Button(description="Run", button_style="primary",
                            tooltip="Run the simulation")
save_gif_button = widgets.Button(description="Save Animation as GIF",
                                 button_style="success",
                                 tooltip="Save current animation as GIF")
export_csv_button = widgets.Button(description="Export Trajectory to CSV",
                                   button_style="info",
                                   tooltip="Export Data to CSV")
sweep_button = widgets.Button(description="Run Angle Sweep",
                              button_style="primary",
                              tooltip="Show range vs. launch angle")
                              
# Presets of various projectiles using real-world mass and lumped drag constants.
projectile_preset = widgets.Dropdown(
    options={
        "Ping-Pong Ball (Mass: = 0.0027 kg, LC_d: = 0.000362 kg/m)": (0.0027, 0.000362),
        "Baseball (Mass: 0.145 kg, LC_d: = 0.00084 kg/m)": (0.145, 0.00084),
        "Soccerball (Mass: = 0.450 kg, LC_d: = 0.00582 kg/m)": (0.450, 0.00582),
        "Coconut (Mass: 2.00 kg, LC_d: = 0.00701 kg/m)": (2.00, 0.00701),
        "Shotput (Mass: = 7.26 kg, LC_d = 0.00326 kg/m)": (7.26, 0.00324),
        "Large Cannonball (Mass: = 14.51 kg, LC_d: = 0.00443 kg/m)": (14.51, 0.00443)
    },
    value=(0.145, 0.00084),
    description="Projectile Presets"
)

# Update sliders when preset changes
def update_slider(update):
    mass, c = update["new"]
    m_slider.value = mass
    c_slider.value = c

projectile_preset.observe(update_slider, names="value")

# Checkbox for toggling no-drag line
nodrag_path_toggle = widgets.Checkbox(
    value=True, description="Show No-Drag Line", indent=False
)

# File save dialog helper
def file_save_notice(default_name, callback):
    filename_box = widgets.Text(
        value=default_name, description="Filename:",
        layout=widgets.Layout(width="300px")
    )
    save_button = widgets.Button(description="Save", button_style="success")
    status = widgets.Label(value="")

    def on_save_clicked(b):
        name = filename_box.value.strip()
        if not name:
            status.value = "Invalid Filename"
            return
        callback(name)
        status.value = f"Saved as {name}"

    save_button.on_click(on_save_clicked)
    return widgets.VBox([filename_box, save_button, status])
    
# Run button callback
def run_and_plot(b):
    error_output.clear_output()
    plot_output.clear_output()
    impact_value.clear_output()

    try:
        results = update_simulation(
            m_slider.value, c_slider.value, y_0_slider.value,
            angle_slider.value, v_0_slider.value
        )

        progress = widgets.IntProgress(
            value=0, min=0, max=100,
            description="Rendering", bar_style="info"
        )

        with plot_output:
            display(progress)

        fig, anim = plot_simulation(results, nodrag_path_toggle.value)
        html = anim.to_jshtml()

        plot_output.clear_output()
        with plot_output:
            display(HTML(html))
            
        display_impact_results(results)

    except Exception as e:
        with error_output:
            print(f"Unexpected error: {e}")

run_button.on_click(run_and_plot)

# Reset button callback
def reset_slider(b):
    m_slider.value = 0.145
    c_slider.value = 0.00084
    y_0_slider.value = 0
    angle_slider.value = 45
    v_0_slider.value = 30
    projectile_preset.value = (0.145, 0.00084)

reset_button.on_click(reset_slider)

# Save GIF callback
def save_gif(b):
    save_dialog_output.clear_output()

    def do_save(filename):
        results = update_simulation(
            m_slider.value, c_slider.value, y_0_slider.value,
            angle_slider.value, v_0_slider.value
        )
        fig, anim = plot_simulation(results, nodrag_path_toggle.value)

        anim.save(filename, writer=PillowWriter(fps=30))

    dialog = file_save_notice(
        default_name=f"projectile_{int(angle_slider.value)}deg.gif",
        callback=do_save
    )

    with save_dialog_output:
        display(dialog)

save_gif_button.on_click(save_gif)

# Export CSV callback
def export_csv(b):
    save_dialog_output.clear_output()

    def do_save(filename):
        results = update_simulation(
            m_slider.value, c_slider.value, y_0_slider.value,
            angle_slider.value, v_0_slider.value
        )
        df = pd.DataFrame({
            "Time (s)": results["t"],
            "x (m)": results["x"],
            "y (m)": results["y"],
            "Speed (m/s)": results["v"]
        })
        df.to_csv(filename, index=False)

    dialog = file_save_notice(
        default_name=f"projectile_angle_{int(angle_slider.value)}deg.csv",
        callback=do_save
    )

    with save_dialog_output:
        display(dialog)

export_csv_button.on_click(export_csv)

# Angle sweep callback
def run_sweep(b):
    try:
        angles = np.arange(10, 85, 5)
        ranges_drag = []
        ranges_nd = []

        progress = widgets.IntProgress(
            value=0, min=0, max=len(angles),
            description="Sweeping:", bar_style="info"
        )

        with sweep_output:
            display(progress)

        for i, ang in enumerate(angles):
            res = update_simulation(
                m_slider.value, c_slider.value, y_0_slider.value,
                ang, v_0_slider.value
            )
            ranges_drag.append(res["x"][-1])
            ranges_nd.append(res["x_nd"][-1])
            progress.value = i + 1

        sweep_output.clear_output()

        with sweep_output:
            plt.figure(figsize=figsize, dpi=dpi)
            plt.plot(angles, ranges_drag, "b-o", label="With Drag")
            plt.plot(angles, ranges_nd, "r--o", label="No Drag")
            plt.xlabel("Launch Angle (°)")
            plt.ylabel("Range (meters)")
            plt.title("Projectile Range vs Launch Angle")
            plt.grid(True)
            plt.legend()
            plt.show()

    except Exception as e:
        with sweep_output:
            print("Sweep Error:", e)

sweep_button.on_click(run_sweep)

# Final UI assembly
ui = widgets.VBox([
    error_output,
    m_slider, c_slider, y_0_slider, angle_slider, v_0_slider,
    projectile_preset, nodrag_path_toggle,
    widgets.HBox([
        run_button, reset_button, sweep_button,
        save_gif_button, export_csv_button
    ]),
    save_dialog_output,
    plot_output,
    sweep_output,
    impact_values
])

# Shows everything on the screen.
display(ui)