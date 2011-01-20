import unittest


class Grid(object):
	def __init__(self):
		self._state = {}
	
	def birth_cell(self, x, y):
		self._state[x, y] = 'birth'
		
	def state(self):
		return sorted(self._state.keys())


class Evolver(object):
	def evolve(self, grid):
		for a, b in grid.state():
			neighbours = 0
			for x in (a-1, a, a+1):
				for y in (b-1, b, b+1):
					if a == x and b == y:
						continue
					if (x, y) in grid._state:
						neighbours += 1
			# live
			
					
		grid._state = {}


class TestEvolver(unittest.TestCase):
	def test_evolve_blank_grid(self):
		g = Grid()
		e = Evolver()
		e.evolve(g)
		self.assertEqual(g.state(), [])
	
	def test_grid_state(self):
		# empty grid
		g = Grid()
		self.assertEqual(g.state(), [])
		# birth single cell
		g.birth_cell(0, 0)
		self.assertEqual(g.state(), [(0, 0)])
		# birth many cells
		g = Grid()
		for a in (0, 1):
			for b in (0, 1):
				g.birth_cell(a, b)
		self.assertEqual(g.state(), [(0, 0), (0, 1), (1, 0), (1, 1)])
	
	def test_evolve_single_cell(self):
		g = Grid()
		g.birth_cell(0, 0)
		e = Evolver()
		e.evolve(g)
		self.assertEqual(g.state(), [])
	
	def test_populated_grid(self):
		g = Grid()
		for a in (0, 1):
			for b in (0, 1):
				g.birth_cell(a, b)
		e = Evolver()
		e.evolve(g)
		self.assertEqual(g.state(), [(0, 0), (0, 1), (1, 0), (1, 1)])
		

if __name__ == '__main__':
	unittest.main()
