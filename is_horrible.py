class Solution:
    def isHorrible(self, n: int) -> bool:
    	if n < 2:
    		return False
    	s = (2, 3, 5)
    	for el in s:
    		while n % el == 0:
    			n = n // el
    	if n > 1:
    		return False
    	return True