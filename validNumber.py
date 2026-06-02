import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Get a + or minus in the begining, catch decimals if it is
        if re.match("^([+-]?(((\d+\.)|(\.\d+))|\d+)\d*([eE][-+]?\d+)?)$", s):        
        #if re.match("^(((\d+[.])|([.]\d+))|\d+)$", s):      # Catches decimals
        #if re.match("^[+-]?[0-9]+([eE][-|+]?[0-9]+)?$", s):          # catches exponents
            return True
        return False
