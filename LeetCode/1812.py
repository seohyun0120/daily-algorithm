class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        print(coordinates[0], coordinates[1])
        
        if coordinates[0] in 'aceg' and coordinates[1] in '1357':
            return False
        
        if coordinates[0] in 'bdfh' and coordinates[1] in '2468':
            return False
        
        return True