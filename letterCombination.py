class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        alphabet = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        
        output = []
        
        # ATTEMPT TO DO SOME COMPLICATED STUFF
        for x in digits:
            current = alphabet[x]
            # Check if the output even has stuff
            if output != []:
                # If output has stuff

                output = [item for item in output for _ in range(len(current))]
                iter = 0
                while iter < len(output):
                    output[iter] = output[iter] + (current[iter % len(current)])
                    iter += 1
            else:
                # output was empty
                output = current
                
                
        return output
        
        #print([item for item in two for _ in range(3)])
                
            
                    
