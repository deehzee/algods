'''
UnionFind for disjoint set.

'''

class QuickFindUF:

    def __init__(self):
        self._parent = {}
        self.n_components = 0

    def __contains__(self, p):
        return p in self._parent

    def __len__(self):
        return len(self._parent)

    def add(self, p):
        if p not in self:
            self._parent[p] = p
            self.n_components += 1
        return self

    def update(self, elements):
        for p in elements:
            self.add(p)
        return self

    def union(self, p, q):
        if p not in self:
            self.add(p)
        if q not in self:
            self.add(q)

        if self.is_connected(p, q):
            return

        pp = self._parent[p]
        pq = self._parent[q]
        for x, px in self._parent.items():
            if px == pp:
                self.__parent[x] = pq
        self.n_componets -= 1
        return self

    def find(self, p):
        return self._parent[p]

    def is_connected(self, p, q):
        if p not in self or q not in self:
            raise IndexError('Element not in the UnionFind')
        return self.find(p) == self.find(q)

    def get_component

    def components(self):
        comp_ids = self._parent.values()


