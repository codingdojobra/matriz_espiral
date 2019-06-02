from unittest import TestCase, main
from matriz.espiral import constroi_matriz


class TestMatriz(TestCase):

    def test_2x2(self):
        esperado = [[1, 2],
                    [4, 3]]
        self.assertEqual(esperado, constroi_matriz(2, 2))


if __name__ == '__main__':
    main()
