class Queue(object):

    def __init__(self):
        self._q = []

    def put(self, x):
        self._q.append(x)
        self._q.sort(key=lambda x: x[0])

    def get(self):
        x = self._q[0]
        del self._q[0]
        return x

    def qsize(self):
        return len(self._q)

class HuffmanNode(object):

    def __init__(self, left, right):
        self.left = left
        self.right = right

freq = [
    (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
    (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
    (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
    (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'),
    (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'),
    (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
    (1.974, 'y'), (0.074, 'z') ]

def create_tree(frequencies):
    p = Queue()
    for value in frequencies:    # 1. Create a leaf node for each symbol
        p.put(value)             #    and add it to the priority queue
    while p.qsize() > 1:         # 2. While there is more than one node
        l, r = p.get(), p.get()  # 2a. remove two highest nodes
        node = HuffmanNode(l, r) # 2b. create internal node with children
        p.put((l[0]+r[0], node)) # 2c. add new node to queue
    return p.get()               # 3. tree is complete - return root node

node = create_tree(freq)


def side_by_side(a, b, w):
    a = a.split("\n") #결과를 list에 저장
    b = b.split("\n")
    n1 = len(a)
    n2 = len(b)
    if n1 < n2:
        a.extend([" "*len(a[0])]*(n2-n1))
    else:
        b.extend([" "*len(b[0])]*(n1-n2))
    r = [" "*len(a[0]) + "   ^   " + " "*len(b[0])]
    r += ["/" + "-"*(len(a[0])-1) + "%7.3f" % w + "-"*(len(b[0])-1) + "\\"]
    for l1, l2 in zip(a, b):
        r.append(l1 + "       " + l2)
    return "\n".join(r)

def print_tree(node):
    w, n = node
    if isinstance(n, str):
        return "%s = %.3f" % (n, w)
    else:
        l = print_tree(n.left)
        r = print_tree(n.right)
        return side_by_side(l, r, w)


def side_by_side(a, b, w):
    a = a.split("\n") #결과를 list에 저장
    b = b.split("\n")
    n1 = len(a)
    n2 = len(b)
    if n1 < n2:
        a.extend([" "*len(a[0])]*(n2-n1))
    else:
        b.extend([" "*len(b[0])]*(n1-n2))
    r = [" "*len(a[0]) + "   ^   " + " "*len(b[0])]
    r += ["/" + "-"*(len(a[0])-1) + "%7.3f" % w + "-"*(len(b[0])-1) + "\\"]
    for l1, l2 in zip(a, b):
        r.append(l1 + "       " + l2)
    return "\n".join(r)

def print_tree(node):
    w, n = node
    if isinstance(n, str):
        return "%s = %.3f" % (n, w)
    else:
        l = print_tree(n.left)
        r = print_tree(n.right)
        return side_by_side(l, r, w)


print(print_tree(node))

def walk_tree(node, prefix="", code={}):
    w, n = node
    if isinstance(n, str):
        code[n] = prefix
    else:
        walk_tree(n.left, prefix + "0")
        walk_tree(n.right, prefix + "1")
    return(code)

code = walk_tree(node)
for i in sorted(freq, reverse=True):
    print (i[1], '{:6.2f}'.format(i[0]), code[i[1]])
