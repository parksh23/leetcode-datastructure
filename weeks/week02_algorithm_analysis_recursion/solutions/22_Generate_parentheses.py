class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        answer = []
        
        def recursion(current_str, left, right):
            if len(current_str) == n * 2:
                answer.append(current_str)
                return
            
            if left < n:
                recursion(current_str + "(", left + 1, right)
            
            if right < left:
                recursion(current_str + ")", left, right + 1)

        recursion("", 0, 0)
        
        return answer

        