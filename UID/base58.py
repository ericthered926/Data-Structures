from baseX import BaseXConverter
_conv = BaseXConverter("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")

def convert(val):
    out = _conv.convert(val)
    out = out.lstrip('1')
    return out

def invert(bXval):
    out = _conv.invert(bXval)
    out = out.lstrip('1')
    return out
