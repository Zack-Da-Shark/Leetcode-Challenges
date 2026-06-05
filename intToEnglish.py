class Solution:
    simple =["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberShorts(self, num: int, numeral: str) -> str:
        result = ""
        # Assume the number is always 3 characters long
        if num == 0:
            return ""
        
        # Manage digit in the hundreds then drop it
        if num >= 100:
            result += self.simple[num // 100] + " Hundred"
            num = num % 100
            #check if I need to exit early or add a space
            if num != 0:
                result += " "
            

        # Manage the digit in the tens now and drop it
        if num == 10 or num >= 20:
            result += self.tens[num // 10]
            num = num % 10
            # Check again
            if num != 0:
                result += " "

        elif num > 10:
            # If the number is in the teens
            result += self.teens[num - 10]
            num = 0

        # Single digits now
        if num > 0:
            result += self.simple[num]
        if numeral != "":
            result += " " + numeral

        return result


    def numberToWords(self, num: int) -> str:
        # Number is always positive
        result = ""

        # Simple base case
        if num == 0:
            return "Zero"

        quantity = ["", "Thousand", "Million" , "Billion"]
        i = 0
        while num > 0:
            current = num % 1000
            if current > 0:
                result = self.numberShorts(current, quantity[i]) + result 
            i += 1
            num = num // 1000
            if num > 0 and current != 0:
                result = " " + result
        return result
