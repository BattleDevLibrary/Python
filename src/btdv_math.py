# =======================================================
# IMPORTS
# =======================================================
import sys



# ========================================================================================================
# FUNCTIONS
# ========================================================================================================

# ---------------------------
# Rounds a float value to the upper integer value
# ---------------------------
def intCeil(v):
    res = int(v)
    if int(v) - v < 0:
        res += 1
    return res

# ---------------------------
# Rounds a float value to the lower integer value
# ---------------------------
def intFloor(v):
    res = int(v)
    return res

# ---------------------------
# Rounds a float value to the nearest integer value
# ---------------------------
def intRound(v):
    res = int(v)
    if v - res >= 0.5:
        res += 1
    return res

    
    