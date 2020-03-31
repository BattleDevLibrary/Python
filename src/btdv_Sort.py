# =======================================================
# IMPORTS
# =======================================================
import itertools as IT
import math


    
# ========================================================================================================
# SORT/FILTER/PERMUTATIONS FUNCTIONS
# ========================================================================================================

# -------------------------------------------------------------------------
# Sorts a list of list
# just give the column index to filter and the increase(true)/decrease(false) information
# -------------------------------------------------------------------------
def sort2D(var, colIdx, increase=True):
    if increase == True:
        sortedVar = sorted(var, key=lambda x: x[colIdx])
    else:
        sortedVar = sorted(var, key=lambda x: -x[colIdx])
    return sortedVar

# -------------------------------------------------------------------------
# filters a column from a list of list
# just give the column index to filter
# -------------------------------------------------------------------------
def filterCol2D(var, colIdx):
    return [x[colIdx] for x in var]

# -------------------------------------------------------------------------
# Sums a column from a list of list
# just give the column index to sum
# -------------------------------------------------------------------------
def sumCol2D(var, colIdx):
    return sum([x[colIdx] for x in var])

# -------------------------------------------------------------------------
# Gets all permutations from a list
# -------------------------------------------------------------------------
def permut(var):
    return list(IT.permutations(var))

    
    
