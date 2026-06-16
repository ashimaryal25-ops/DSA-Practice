class Solution(object):
    def predictPartyVictory(self, senate):
        radiantq = deque()
        direq = deque()

        n = len(senate)
        count = 0
        for c in senate:
            if c == "R":
                radiantq.append(count)
            else:
                direq.append(count)

            count += 1    


        while radiantq and direq:
            radiant = radiantq.popleft()
            dire = direq.popleft()

            if radiant < dire:
                radiantq.append(radiant + n)
            else:
                direq.append(dire + n) 

        if not radiantq:
            return "Dire"
        else:
            return "Radiant" 