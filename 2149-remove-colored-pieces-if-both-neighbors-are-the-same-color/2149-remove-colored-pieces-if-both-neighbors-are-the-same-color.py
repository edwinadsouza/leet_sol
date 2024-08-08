class Solution(object):
    def winnerOfGame(self, colors):
        '''
        n = len(colors)
        alice = 0
        bob = 0
        for i in range(1,n-1):
            if colors[i-1] == colors[i] == colors[i+1]:
                if colors[i] == 'A':
                    alice +=1
                else:
                    bob +=1
        return alice > bob
'''
        alice = 0
        bob = 0
        consecutive_A = 0
        consecutive_B = 0

        for color in colors:
            if color == 'A':
                consecutive_A += 1
                consecutive_B = 0
                if consecutive_A >= 3:
                    alice += 1
            elif color == 'B':
                consecutive_B += 1
                consecutive_A = 0
                if consecutive_B >= 3:
                    bob += 1
        
        return alice > bob
