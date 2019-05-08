import unittest
from NijenhuisAlgorithm.dijkstra import *


class TestDijkstra(unittest.TestCase):

    def test_dijkstra(self):
        graph = {}
        file = open('dijkstraData.txt', 'r')
        for line in file:
            b = list(line.split())
            graph[int(b[0])] = {}
            for i in b[1:]:  # 'node, distance'
                node, distance = i.split(',')
                graph[int(b[0])][int(node)] = int(distance)
        file.close()
        A = dijkstra(graph)
        self.assertEqual(A[7], 2599)
        self.assertEqual(A[37], 2610)
        self.assertEqual(A[59], 2947)
        self.assertEqual(A[82], 2052)
        self.assertEqual(A[99], 2367)
        self.assertEqual(A[115], 2399)
        self.assertEqual(A[133], 2029)
        self.assertEqual(A[165], 2442)
        self.assertEqual(A[188], 2505)
        self.assertEqual(A[197], 3068)


if __name__ == '__main__':
    unittest.main()
