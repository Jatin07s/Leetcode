class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        brackets = [""]*(n*2)
        def solve(index , total , brackets , result):
            if index >= len(brackets):
                if total == 0:
                    result.append("".join(brackets))
                return

            if total > len(brackets)//2:
                return
            elif total < 0:
                return

            brackets[index] = "("
            summ = total + 1
            solve(index+1 , summ , brackets , result) 

            brackets[index] = ")"
            summ = total -1
            solve(index+1 , summ , brackets , result)

        solve(0 , 0 , brackets , result)

        return result                   