import inspect
import re

################################################
###   Serialization to JSON

TAB = '\t'

def to_json(obj, level=0, ncb=True):
    '''Serializes the given object to JSON, printing to the console as it goes.'''
    if level ==0:
        print("{")
    level += 1
    par = obj.__dict__
    l = len(par)
    j = 1
    for i in par:
        nc = False
        if l==j:
            nc = True
        dtype = par[i].__class__.__qualname__.lower()
        if dtype == "bool":
            if par[i] is False:
                par[i] = "false"
            else:
                par[i] = "true"
            dothis(i,par,nc,False,level)
        elif dtype == "str":
            par[i] = re.sub(r"\\","\\\\\\\\",par[i])
            par[i] = re.sub(r'"',"\\\"",par[i])
            dothis(i,par,nc,False,level)
        elif dtype == "date" or dtype == "franchise" or dtype == "person":
            parsethis(i,par[i],level,obj,nc)
        elif dtype == "nonetype":
            par[i] = "null"
            dothis(i,par,nc,True,level)
        else:
            dothis(i,par,nc,True,level)
        j += 1
    if ncb:
        print(TAB*(level-1) + '}')
    else:
        print(TAB*(level-1) + '},')
    return ''

def parsethis(i, v, level, obj, nc):
    objout = getattr(obj,i)
    output = (TAB*level + '"' + str(i) + '": {')
    print(output)
    return to_json(objout,level,nc)

def dothis(i,par,nc,numeric,level):
    if numeric:
        if nc:
            out = (TAB*level + '"' + str(i) + '": ' + str(par[i]))
        else:
            out = (TAB*level + '"' + str(i) + '": ' + str(par[i]) + ',')
    else:
        if nc:
            out = (TAB*level + '"' + str(i) + '": "' + str(par[i]) + '"')
        else:
            out = (TAB*level + '"' + str(i) + '": "' + str(par[i]) + '",')
    print(out)