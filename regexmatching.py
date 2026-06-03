class Solution:

   
    def isMatch(self, string: str, pattern: str) -> bool:
        memory = {}
        # Store the result to keep computational costs low

        # Start of the function
        def dynamo( i : int, j: int) -> bool:
            if (i, j) not in memory: # Compute this combo if it hasn't
                if j == len(pattern):
                    answer = i == len(string)
                else:
                    # First character matching or the .
                    first = i <len(string) and pattern [j] in {string[i], "."}

                    # Handling the *, 
                    if j + 1 < len(pattern) and pattern[j + 1] == "*":
                        answer = dynamo(i, j + 2) or first and dynamo(i + 1, j)
                    else:
                        # 
                        answer = first and dynamo(i + 1, j + 1)
                    
                # Save the answer
                memory[i, j] = answer
            return memory[i, j]
        return dynamo(0, 0)
