class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
    	if len(coordinates) <= 2:
    		return True
    	x1, y1 = coordinates[0]
    	x2, y2 = coordinates[1]
    	if x1 == x2:
    		for x, y in coordinates[2:]:
    			if x != x1:
    				return False
    	else:
    		k = (y2 - y1) / (x2 - x1)
    		b = y1 - k * x1
    		for x, y in coordinates[2:]:
    			if y != k * x + b:
    				return False
    	return True