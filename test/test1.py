import unittest

import main.Ising as Ising
import main.exceptions as exc
import numpy as np

class FirstTest(unittest.TestCase):

    def test_init(self):
        # number of sites
        N = 31
        # Exchange term
        J_ij = 0.1
        ising = Ising.Ising(N, J_ij)
        self.assertEqual(N, ising.N, "System size does not match")
        self.assertEqual(J_ij, ising.J_ij, "System size does not match")

    def test_spinflip(self):
        ising= Ising.Ising(31, 0.2)
        s1=ising.spin(20)
        ising.spinflip(20)
        self.assertEqual(-s1, ising.spin(20), "Wrong spin")

    def test_boundaries(self):
        ising=Ising.Ising(31,0.1)
        self.assertRaises(exc.OutOfBoundary, ising.spinflip, 40)

    def test_spins(self):
        ising = Ising.Ising(31, 0.1)
        for s in ising.lattice:
            self.assertTrue(s == -1 or s == 1)

    def test_energy(self):
        N = 100
        J = 1.0
        ising= Ising.Ising(N, J, np.ones(N, dtype=int))
        E = self.compute_energy(ising)

        self.assertEqual(ising.energy(), E)

    def compute_energy(self, ising):
        E = 0.0
        for i in range(ising.N):
            for j in range(i):
                if abs(i - j) == 1:
                    E -= ising.J_ij
                elif (i == 0 and j == ising.N - 1) or (j == 0 and i == ising.N - 1):
                    E -= ising.J_ij
        return E

    def test_energy_spinflip(self):
        N = 50
        ising = Ising.Ising(N, 0.1, np.ones(N, dtype=int))
        E = self.compute_energy(ising)
        ising.spinflip(1)
        self.assertAlmostEqual(E+4.0*ising.J_ij, ising.energy(), places=8)



if __name__ == 'main' :
    unittest.main()