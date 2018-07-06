import numpy as np
import main.exceptions as exc

class Ising:
    def __init__(self, N, J, lattice = None):
        self.N= N
        if lattice is None:
            self.lattice = np.array(np.array(np.random.rand(self.N)+0.5, dtype=np.int)*2 - 1, dtype=np.int)
        else:
            if len(lattice) != N :
                raise exc.WrongLatticeSize()
            self.lattice = lattice
        self.J_ij=J

    def spin(self, s):
        return self.lattice[s]

    def spinflip(self, s):
        if s > self.N :
            raise exc.OutOfBoundary()
        self.lattice[s] = -self.lattice[s]

    def energy(self):
        E = 0.0
        for i in range(self.N):
            for j in range(i):
                if abs(i - j) == 1:
                    E -= self.J_ij * self.lattice[i] * self.lattice[j]
                elif (i == 0 and j == self.N - 1) or (j == 0 and i == self.N - 1):
                    E -= self.J_ij * self.lattice[i] * self.lattice[j]
        return E