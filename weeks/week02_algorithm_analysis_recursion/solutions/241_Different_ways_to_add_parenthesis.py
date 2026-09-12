class Solution(object):
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        def recursion(expr):
            if expr.isdigit():
                return [int(expr)]
            
            res = []
            operator = ("+", "-", "*")
            
            for i in range(len(expr)):
                char = expr[i]
                
                if char in operator:
                    left_results = recursion(expr[:i])
                    right_results = recursion(expr[i+1:])
                    
                    for l in left_results:
                        for r in right_results:
                            if char == "+":
                                res.append(l + r)
                            elif char == "-":
                                res.append(l - r)
                            elif char == "*":
                                res.append(l * r)
            
            return res

        return recursion(expression)