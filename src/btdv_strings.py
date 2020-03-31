# =======================================================
# IMPORTS
# =======================================================
import sys



# ========================================================================================================
# FUNCTIONS
# ========================================================================================================

# ---------------------------
# Replace some letters in a string by some other letters given in parameters
# by default, strings are in lower case, but you can handle both upper and lower case by setting the parameter flag
# ---------------------------
def translate(msg, inLetters, outLetters, isCaseSensitive = False):
    res = ""
    if isCaseSensitive == True:
        inLetters += inLetters.upper()
        outLetters += outLetters.upper()
    for c in msg:
        if c in inLetters:
            idx = inLetters.index(c)
            res += outLetters[idx]
        else:
            res += c
    return res
    
    
    