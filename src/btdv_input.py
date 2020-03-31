# =======================================================
# IMPORTS
# =======================================================
import sys



            

# ========================================================================================================
# FUNCTIONS (SINGLE VALUES)
# ========================================================================================================

# ---------------------------
# Read a single line (string)
# ---------------------------
def getOneSingleString():
    return input()

# ---------------------------
# Read a single line and convert it to integer
# ---------------------------
def getOneSingleInteger():
    return int(getOneSingleString())

# ---------------------------
# Read a single line and convert it to float
# ---------------------------
def getOneSingleFloat():
    return float(getOneSingleString())

    

# ========================================================================================================
# FUNCTIONS (VERTICAL VALUES)
# ========================================================================================================

# ---------------------------
# Read a vertical list of strings
# that means, each line of stdin is a single string
# and we read N lines from stdin
# ---------------------------
def getVerticalStrings(n):
    res = []
    for i in range(n):
        res.append( getOneSingleString() )
    return res

# ---------------------------
# Read a vertical list of integers
# that means, each line of stdin is a single integer
# and we read N lines from stdin
# ---------------------------
def getVerticalIntegers(n):
    res = []
    for i in range(n):
        res.append( getOneSingleInteger() )
    return res

# ---------------------------
# Read a vertical list of floats
# that means, each line of stdin is a single float
# and we read N lines from stdin
# ---------------------------
def getVerticalFloats(n):
    res = []
    for i in range(n):
        res.append( getOneSingleFloat() )
    return res

    
    
# ========================================================================================================
# FUNCTIONS (HORIZONTAL VALUES)
# ========================================================================================================
    
# ---------------------------
# Read a horizontal list of strings
# that means, one line of stdin contains several strings (words)
# separated by a specific delimiter
# ---------------------------
def getHorizontalStrings(m,d):
    print("Line",file=sys.stderr)
    res = getOneSingleString()
    if d=="":
        res = list(res)
    else:
        res = res.split(d)
    return res[:m]

# ---------------------------
# Read a horizontal list of integers
# that means, one line of stdin contains several integers
# separated by a specific delimiter
# ---------------------------
def getHorizontalIntegers(m,d):
    res = [int(x) for x in getHorizontalStrings(m,d)]
    return res[:m]
    
# ---------------------------
# Read a horizontal list of integers
# that means, one line of stdin contains several integers
# separated by a specific delimiter
# ---------------------------
def getHorizontalFloats(m,d):
    res = [float(x) for x in getHorizontalStrings(m,d)]
    return res[:m]
    
        
    
# ========================================================================================================
# FUNCTIONS (2D-MATRIX)
# ========================================================================================================

# ---------------------------
# Get a 2D matrix of strings (words)
# with N rows and M columns (M is not given as we take all the data)
# ---------------------------
def getMatrixStrings(n,m,d):
    res = []
    for i in range(n):
        res.append( getHorizontalStrings(m,d) )
    return res
    
# ---------------------------
# Get a 2D matrix of integers
# with N rows and M columns (M is not given as we take all the data)
# ---------------------------
def getMatrixIntegers(n,m,d):
    res = []
    for i in range(n):
        res.append( getHorizontalIntegers(m,d) )
    return res
    
# ---------------------------
# Get a 2D matrix of floats
# with N rows and M columns (M is not given as we take all the data)
# ---------------------------
def getMatrixFloats(n,m,d):
    res = []
    for i in range(n):
        res.append( getHorizontalFloats(m,d) )
    return res



# ========================================================================================================
# FUNCTIONS (GENERIC)
# ========================================================================================================

# ---------------------------
# Generic function to get STRING / INTEGER / FLOAT values from stdin
# you can get one value, a list of vertical or horizontal values,
#or you can get a 2D-matrix of integer values
# ---------------------------    
def getData(typ,nbRows,nbCols,delimiter): 
    # Function dictionary
    FUNCTIONS = {
        "strings" : {"single":getOneSingleString ,"vertical":getVerticalStrings ,"horizontal":getHorizontalStrings ,"matrix":getMatrixStrings },
        "integers": {"single":getOneSingleInteger,"vertical":getVerticalIntegers,"horizontal":getHorizontalIntegers,"matrix":getMatrixIntegers},
        "floats"  : {"single":getOneSingleFloat  ,"vertical":getVerticalFloats  ,"horizontal":getHorizontalFloats  ,"matrix":getMatrixFloats  },
    }
    # init result
    res = None
    # No Value
    if nbRows < 0 or nbCols < 0:
        # do nothing as the parameters are not correct
        error("number of rows or columns is below 0 !")
    # Only one value, just return the integer
    elif nbRows == 1 and nbCols == 1:
        res = FUNCTIONS[typ]["single"]
    # Vertical List
    elif nbRows > 1 and nbCols == 1:
        res = FUNCTIONS[typ]["vertical"](nbRows)
    # Horizontal List
    elif nbRows == 1 and nbCols > 1:
        res = FUNCTIONS[typ]["horizontal"](nbCols,delimiter)
    #2D Matrix
    else:
        res = FUNCTIONS[typ]["matrix"](nbRows,nbCols,delimiter)
    return res
        

        

        
# ========================================================================================================
# FUNCTIONS (USER INTERFACE)
# ========================================================================================================
        
# ---------------------------
# User function to get strings from stdin
# ---------------------------
def getString(nbRows=1,nbCols=1,delimiter=" "):
    return getData("strings",nbRows,nbCols,delimiter)
        
# ---------------------------
# User function to get integers from stdin
# ---------------------------
def getInt(nbRows=1,nbCols=1,delimiter=" "):
    return getData("integers",nbRows,nbCols,delimiter)
        
# ---------------------------
# User function to get floats from stdin
# ---------------------------
def getFloat(nbRows=1,nbCols=1,delimiter=" "):
    return getData("floats",nbRows,nbCols,delimiter)


