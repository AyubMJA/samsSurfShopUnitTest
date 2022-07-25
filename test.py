import surfshop
import unittest

class SurfShopTest(unittest.TestCase):
    def setUp(self):
        self.cart = surfshop.ShoppingCart()


    def test_add_surfboard(self):
        message = self.cart.add_surfboards(quantity=1)
        self.assertEqual(message, f'Successfully added 1 surf board to cart!')

    def test_add_surfboards(self):
        for i in range(2,5):
            with self.subTest(i=i):
                message = self.cart.add_surfboards(i)
                self.assertEqual(message, f'Successfully add {i} surfboards to cart!')
                self.cart = surfshop.ShoppingCart()

unittest.main()