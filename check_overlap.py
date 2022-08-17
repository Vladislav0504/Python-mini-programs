class Solution:
    def checkOverlap(self, radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        d = {0: [x1, x2, x_center], 1: [y1, y2, y_center]}
        for coord in d:
        	for el in d[coord][:2]:
        		c = radius**2 - (el - d[coord][2])**2
        		if c >= 0 and (d[1 - coord][0] <= d[1 - coord][2] + c**0.5 <= d[1 - coord][1] or d[1 - coord][0] <= d[1 - coord][2] - c**0.5 <= d[1 - coord][1]):
        			return True
        if x1 <= x_center <= x2 and y1 <= y_center <= y2 or ((x1 + x2) / 2 - x_center)**2 + ((y1 + y2) / 2 - y_center)**2 <= radius**2:
        	return True
        return False