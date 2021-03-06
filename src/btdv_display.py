# =======================================================
# IMPORTS
# =======================================================
import sys



# ========================================================================================================
# PARAMETERS
# ========================================================================================================
DEBUG = True



# =======================================================
# FUNCTIONS
# =======================================================
# ---------------------------
# display values on the stderr (used to debug)
# ---------------------------    
def debug(myStr):
    if DEBUG == True:
        if isinstance(myStr, list):
            print("----- List -----", file=sys.stderr)
            for m in myStr:
                print(str(m), file=sys.stderr)
        else:
            print("----- Variable -----", file=sys.stderr)
            print(str(myStr), file=sys.stderr)

            
            