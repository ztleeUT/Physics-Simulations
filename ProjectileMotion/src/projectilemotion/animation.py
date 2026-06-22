 # -----------------------------------------------------------------------------------------
 # Creates the animations to use on our trajectory plot.
 # Animation includes a moving "projectile" with a moving trail.
 # Contains controls to limit the frames of animation to improve generation time.
 # -----------------------------------------------------------------------------------------
 
 from matplotlib.animation import FuncAnimation
 
# Creates the projectile's marker and it's trail. 
 def initialize_animation(ax):
 
    point_d, = ax.plot([], [], 'o', color='blue', markersize=11,
                       label="Projectile")
    trail_d, = ax.plot([], [], color='blue', alpha=0.6, linewidth=3.5)
    
    return point_d, trail_d
    
# Resets the animation of the projectile and it's trail.
def init_animation(point_d, trail_d):
    
    point_d.set_data([], [])
    trail_d.set_data([], [])
    
    return point_d, trail_d
    
# Handles updating each animation frame.    
def update_animation(frame, x, y, point_d, trail_d, trail_length=25):
    
    idx = min(frame, len(x) - 1)
    point_d.set_data([x[idx]], [y[idx]])

    # Creates a trail that fades.
    trail_len = min(trail_length, idx + 1)
    trail_d.set_data(x[idx - trail_len + 1:idx + 1],
                     y[idx - trail_len + 1:idx + 1])

    return point_d, trail_d

# Creates the animation using the above.
def create_animation(fig, ax, results, trail_length = 25, interval = 45):
    
    t = results["t"]
    x = results["x"]
    y = results["y"]
    
    point_d, trail_d = initialize_animation(ax)
    
    n_frames = len(t)
    
    step = max(1, n_frames//120)
    frames = range(0, n_frames, step)
    
    anim = FuncAnimation(fig, lambda frame:
        update_animation(frame, x, y, point_d, trail_length),
        init_funct = lambda: init_animation(point_d, trail_d), 
        frames = frames, interval = interval, repeat = True, blit = False)
        
    return anim