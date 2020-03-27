# ========================================================================================================
# IMPORT
# ========================================================================================================
import sys
import itertools as IT
import math



# ========================================================================================================
# PARAMETERS
# ========================================================================================================
DEBUG = True



# ========================================================================================================
# DISPLAY FUNCTIONS
# ========================================================================================================

# -------------------------------------------------------------------------
# display values on the stdout (used to send answers)
def disp(myStr):
# -------------------------------------------------------------------------
    print(str(myStr))

# -------------------------------------------------------------------------
# display values on the stderr (used to debug)
def debug(myStr):
# -------------------------------------------------------------------------
    if DEBUG == True:
        if isinstance(myStr, list):
            for m in myStr:
                print(str(m), file=sys.stderr)
        else:
            print(str(myStr), file=sys.stderr)



# ========================================================================================================
# INPUT FUNCTIONS
# ========================================================================================================

# -------------------------------------------------------------------------
# Gets a simple integer value from the stdin.
# Can get an array of integers from the stdin (each integer value is on a different line).
# The 'n' (optional) parameter is strictly positive, and represents the count of lines to retrieve..
# If 'n' equals to '1', the result is a simple integer, if greater, the result is an integer list.
def getInt(n=1):
# -------------------------------------------------------------------------
    res = None
    if n == 1:
        res = int(input())
    elif n > 1:
        res = []
        for i in range(n):
            res.append(int(input()))
    return res

# -------------------------------------------------------------------------
# Gets a simple float value from the stdin.
# Can get an array of float from the stdin (each float value is on a different line).
# The 'n' (optional) parameter is strictly positive, and represents the count of lines to retrieve..
# If 'n' equals to '1', the result is a simple float, if greater, the result is a float list.
def getFloat(coma=".", n=1):
# -------------------------------------------------------------------------
    res = None
    if n == 1:
        res = float(input().replace(coma, "."))
    elif n > 1:
        res = []
        for i in range(n):
            res.append(float(input().replace(coma, ".")))
    return res

# -------------------------------------------------------------------------
# Gets a simple string value from the stdin.
# Can get an array of strings from the stdin (each string value is on a different line).
# The 'n' (optional) parameter is strictly positive, and represents the count of lines  to retrieve.
# If 'n' equals to '1', the result is a simple string, if greater, the result is a string  list.
def getStr(n=1):
# -------------------------------------------------------------------------
    res = None
    if n == 1:
        res = input()
    elif n > 1:
        res = []
        for i in range(n):
            try:
                res.append(input())
            except:
                pass
    return res

# -------------------------------------------------------------------------
# Gets an integer array from ONE or SEVERAL stdin lines
# the 'delimiter' (optional) parameter is a character used to separate different values contained in the same line.
# The 'n' (optional) parameter is strictly positive, and represents the count of lines to retrieve..
# If 'n' equals to '1', the result is a simple list of integers, if greater, the result is a list of list of integers.
def getIntArray(delimiter=" ", n=1):
# -------------------------------------------------------------------------
    res = None
    if n == 1:
        if delimiter == "" or delimiter is None:
            res = [ list(int(input())) ]
        else:
            res = [[int(x) for x in input().split(delimiter)]]
    elif n > 1:
        res = []
        for i in range(n):
            if delimiter == "" or delimiter is None:
                res.append(list(int(input())))
            else:
                res.append([int(x) for x in input().split(delimiter)])
    return res

# -------------------------------------------------------------------------
# Gets a float array from ONE or SEVERAL stdin lines
# the 'delimiter' (optional) parameter is a character used to separate different values contained in the same line.
# The 'n' (optional) parameter is strictly positive, and represents the count of lines to retrieve..
# If 'n' equals to '1', the result is a simple list of floats, if greater, the result is a list of list of floats.
def getFloatArray(delimiter=" ", coma=".", n=1):
# -------------------------------------------------------------------------
    res = None
    if n == 1:
        if delimiter == "" or delimiter is None:
            res = [ list(float(input().replace(coma, "."))) ]
        else:
            res = [ [float(x.replace(coma, ".")) for x in input().split(delimiter)] ]
    elif n > 1:
        res = []
        for i in range(n):
            if delimiter == "" or delimiter is None:
                res.append(list(float(input().replace(coma, "."))))
            else:
                res.append([float(x.replace(coma, ".")) for x in input().split(delimiter)])
    return res

# -------------------------------------------------------------------------
# Gets a string array from ONE or SEVERAL stdin lines
# the 'delimiter' (optional) parameter is a character used to separate different values contained in the same line.
# The 'n' (optional) parameter is strictly positive, and represents the count of lines to retrieve..
# If 'n' equals to '1', the result is a simple list of strings, if greater, the result is a list of list of integers.
def getStrArray(delimiter=" ", n=1):
# -------------------------------------------------------------------------
    res = None
    if n == 1:
        if delimiter == "" or delimiter is None:
            res = [ list(input()) ]
        else:
            res = [ [x for x in input().split(delimiter)] ]
    elif n > 1:
        res = []
        for i in range(n):
            try:
                if delimiter == "" or delimiter is None:
                    res.append(list(input()))
                else:
                    res.append([x for x in input().split(delimiter)])
            except:
                pass
    return res


    

# ========================================================================================================
# MATH FUNCTIONS
# ========================================================================================================

# -------------------------------------------------------------------------
# Rounds a float value to the upper integer value
def intCeil(v):
# -------------------------------------------------------------------------
    res = int(v)
    if int(v) - v < 0:
        res += 1
    return res

# -------------------------------------------------------------------------
# Rounds a float value to the lower integer value
def intFloor(v):
# -------------------------------------------------------------------------
    res = int(v)
    return res

# -------------------------------------------------------------------------
# Rounds a float value to the nearest integer value
def intRound(v):
# -------------------------------------------------------------------------
    res = int(v)
    if v - int(v) >= 0.5:
        res += 1
    return res



# ========================================================================================================
# STRING FUNCTIONS
# ========================================================================================================
def translate(msg, inLetters, outLetters, isCaseSensitive = False):
    if isCaseSensitive == True:
        inLetters += inLetters.upper()
        outLetters += outLetters.upper()
    res = ""
    for c in msg:
        if c in inLetters:
            idx = inLetters.index(c)
            res += outLetters[idx]
        else:
            res += c
    return res
    

    
# ========================================================================================================
# SORT/FILTER/PERMUTATIONS FUNCTIONS
# ========================================================================================================

# -------------------------------------------------------------------------
# Sorts a list of list
# just give the column index to filter and the increase(true)/decrease(false) information
def sort2D(var, colIdx, increase=True):
# -------------------------------------------------------------------------
    if increase == True:
        sortedVar = sorted(var, key=lambda x: x[colIdx])
    else:
        sortedVar = sorted(var, key=lambda x: -x[colIdx])
    return sortedVar

# -------------------------------------------------------------------------
# filters a column from a list of list
# just give the column index to filter
def filterCol2D(var, colIdx):
# -------------------------------------------------------------------------
    return [x[colIdx] for x in var]

# -------------------------------------------------------------------------
# Sums a column from a list of list
# just give the column index to sum
def sumCol2D(var, colIdx):
# -------------------------------------------------------------------------
    return sum([x[colIdx] for x in var])

# -------------------------------------------------------------------------
# Gets all permutations from a list
def permut(var):
# -------------------------------------------------------------------------
    return list(IT.permutations(var))


    