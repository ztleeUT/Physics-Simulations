# -----------------------------------------------------------------------------------------
# Handles input validation to prevent errors.
# -----------------------------------------------------------------------------------------

def validate_inputs(m, c, y_0, angle, v_0):
    if m <= 0: raise ValueError("Mass must be positive.")
    if c < 0: raise ValueError("Lumped Drag Coefficient must be positive.")
    if v_0 < 0: raise ValueError("Speed cannot be negative.")
    if not (0 <= angle <= 90): raise ValueError("Launch angle must be between 0 and 90.")
    if y_0 < 0: raise ValueError("Initial Height cannot be negative.")