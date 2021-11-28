'''
키위주스문제
'''


class KiwiJuiceEasy:
    def thePouring(self, capacities, bottles, fromId, toId):
        for i in range(0, len(fromId)):
            quantity = bottles[fromId[i]] + bottles[toId[i]]

            if quantity > capacities[toId[i]]:
                bottles[fromId[i]] = abs(bottles[fromId[i]] - (capacities[toId[i]] - bottles[toId[i]]))
                bottles[toId[i]] = capacities[toId[i]]
            else:
                bottles[fromId[i]] = 0
                bottles[toId[i]] = quantity
        return bottles


if __name__ == "__main__":
    k = KiwiJuiceEasy()
    print(k.thePouring([30, 20, 10], [10, 5, 5], [0, 1, 2], [1, 2, 0]))
    print(KiwiJuiceEasy().thePouring([14,35,86,58,25,62],[6,34,27,38,9,60],[1,2,4,5,3,3,1,0],[0,1,2,4,2,5,3,1]))


