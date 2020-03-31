# =======================================================
# IMPORTS
# =======================================================
import sys



# =======================================================
# FUNCTIONS
# =======================================================

# ---------------------------
# function used to get a line number from any frame context 
# ---------------------------
def getLineNumber(frame=0):
    return int(sys._getframe(frame+1).f_lineno)

# ---------------------------
# function used to get a file name from any frame context 
# ---------------------------
def getFileName(frame=0):
    return str(sys._getframe(frame+1).f_code.co_filename)

# ---------------------------
# function used to get a function name from any frame context 
# ---------------------------
def getFunctionName(frame=0):
    return str(sys._getframe(frame+1).f_code.co_name)

# ---------------------------
# function used to display an info message + line, function and file names 
# ---------------------------
def info(msg,frameNb=1,displayMessage=True):
    try:
        if displayMessage:
            print("[INFO] %s" % (msg),file=sys.stderr)
        lin = getLineNumber(frameNb)
        fil = getFileName(frameNb)
        fun = getFunctionName(frameNb)
        if ".py" not in fil or "run-" not in fil:
            print("  @%d : %s() in '%s'" % (lin,fun,fil),file=sys.stderr)
    except:
        pass

# ---------------------------
# function used to display an error message + all the call stack info 
# ---------------------------
def error(err,frameNb=2):
    try:
        print("[ERROR] %s" % (err),file=sys.stderr)
        for i in range(frameNb,100):
            info(err,i,False)
    except:
        pass
    print("",file=sys.stderr)

# ---------------------------
# function used to stop a script execution
# it displays an error message + all the call stack info
# ---------------------------    
def stop(err):
    error(err,3)
    exit()


