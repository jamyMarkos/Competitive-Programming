class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        arr = [0] * 2
        arr[0], arr[1] = (celsius + 273.15), (celsius * 1.80 + 32.00)
        return arr
        
        
        