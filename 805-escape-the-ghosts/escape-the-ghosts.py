class Solution(object):
    def escapeGhosts(self, ghosts, target):
    
        start_position = [0, 0]
        for ghost in ghosts:
            if abs(target[0] - ghost[0]) + abs(target[1] - ghost[1]) <= abs(start_position[0] - target[0]) + abs(start_position[1] - target[1]):
                return False
        return True

        