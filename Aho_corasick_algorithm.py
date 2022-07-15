
from collections import deque, defaultdict
from itertools import count

def aho_corasick():
    G = defaultdict(count(1).__next__)  # transitions
    W = defaultdict(set)                # alphabet
    F = defaultdict(lambda: 0)          # fallbacks
    O = defaultdict(set)                # outputs

    # automaton
    return G, W, F, O
def add_word(word, G, W, F, O):
    state = 0
    # add transitions between states
    for w in word:
        W[state].add(w)
        state = G[state, w]

    # add output
    O[state].add(word)
def build_fsa(G, W, F, O):
    # initial states
    queue = deque(G[0, w] for w in W[0])

    while queue:
        state = queue.popleft()

        # for each letter in alphabet
        for w in W[state]:
            # find fallback state
            t = F[state]
            while t and (t, w) not in G:
                t = F[t]

            # for next state define its fallback and output
            s = G[state, w]
            F[s] = G[t, w] if (t, w) in G else 0
            O[s] |= O[F[s]]

            queue.append(s)
def search(text, G, W, F, O):
    state = 0

    for i, t in enumerate(text):
        # fallback
        while state and (state, t) not in G:
            state = F[state]

        # transition
        state = G[state, t] if (state, t) in G else 0

        # output
        if O[state]:
            print('@', i, O[state])


AC = aho_corasick()
add_word('bar', *AC)
add_word('ara', *AC)
add_word('bara', *AC)
add_word('barbara', *AC)
build_fsa(*AC)
search('barbarian barbara said: barabum', *AC)

'''
@ 2 {'bar'}
@ 5 {'bar'}
@ 12 {'bar'}
@ 15 {'bar'}
@ 16 {'bara', 'barbara', 'ara'}
@ 26 {'bar'}
@ 27 {'bara', 'ara'}

코드 출처
https://github.com/coells/100days/blob/master/day%2034%20-%20aho-corasick.ipynb
'''




### 다른 사람 코드 ###

from queue import Queue

class Node(dict):
    def __init__(self):
        super().__init__()
        self.final = False;

        self.out = set();
        self.fail = None;

    def addout(self, out):
        if type(out) is set:
            self.out = self.out.union(out)
        else:
            self.out.add(out)

    def addchild(self, alphabet, node=None):
        self[alphabet] = Node() if node is None else node

class AC():

    def __init__(self, patterns):
        self.patterns = patterns
        self.head = Node()

        self.maketrie()
        self.constructfail()

    def search(self, sentence):
        crr = self.head
        ret = []
        for c in sentence:
            while crr is not self.head and c not in crr:
                crr = crr.fail
            if c in crr:
                crr = crr[c]

            if crr.final:
                ret.extend(list(crr.out))
        return ret

    def maketrie(self):
        for pattern in self.patterns:
            crr = self.head
            for c in pattern:
                if c not in crr:
                    crr.addchild(c)
                crr = crr[c]
            crr.final = True
            crr.addout(pattern)

    def constructfail(self):
        queue = Queue()
        self.head.fail = self.head
        queue.put(self.head)
        while not queue.empty():
            crr = queue.get()
            for nextc in crr:
                child = crr[nextc]

                if crr is self.head:
                    child.fail = self.head
                else:
                    f = crr.fail
                    while f is not self.head and nextc not in f:
                        f = f.fail
                    if nextc in f:
                        f = f[nextc]
                    child.fail = f

                child.addout(child.fail.out)
                child.final |= child.fail.final

                queue.put(child)

'''
코드 출처
https://tempdev.tistory.com/16
'''