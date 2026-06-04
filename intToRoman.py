class Solution:
    def intToRoman(self, num: int) -> str:

        # Now to do it all in 1 run 
        result = ""
        # Values correspond to their positon value and their array alignemnt
        thousand = ["","M","MM","MMM"] # Only 4 needed as 4000 is out of the scope
        hundred  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ten      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        unit     = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        # Get the digit in the corresponding position it is in then convert it into its Roman equivalent
        result += thousand[num // 1000]        # Get the digit in the thousands
        result += hundred[(num % 1000) // 100] # Get the digit in the hundreds 
        result += ten[(num % 100) // 10]       # Get the digit in the tens 
        result += unit[(num % 10)]             # Get the digit in the unit positon
        return result
