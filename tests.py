import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_rows,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_cols,
        )

    def test_maze_create_one_cell(self):
        num_cols = 1
        num_rows = 1
        m2 = Maze(0, 0 , num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m2._cells),
            num_rows,
        )
        self.assertEqual(
            len(m2._cells[0]),
            num_cols,
        )
    
    def test_entrance_and_exit_broken(self):
        num_cols = 12
        num_rows = 5
        m2 = Maze(0, 0 , num_rows, num_cols, 10, 10)
        self.assertEqual(
            m2._cells[0][0]._walls["TOP"],
            False,
        )
        self.assertEqual(
            m2._cells[4][11]._walls["BOTTOM"],
            False,
        )


if __name__ == "__main__":
    unittest.main()