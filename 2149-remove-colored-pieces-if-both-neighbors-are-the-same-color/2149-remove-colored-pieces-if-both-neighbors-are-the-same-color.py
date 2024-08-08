class Solution(object):
    def winnerOfGame(self, colors):
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
        