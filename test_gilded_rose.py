import unittest
from gilded_rose import GildedRose, Item


class GildedRoseTest(unittest.TestCase):

    def update_test(obj = GildedRose, days = 1):
        for i in range(days):
            obj.update_quality()

    def test_base_item(self):
        # Créer Item
        item = Item("+5 Dexterity Vest", 10, 20)
        gilded_rose = GildedRose([item])

        # Un jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)    
        
        # Après date de péremption
        GildedRoseTest.update_test(gilded_rose, item.sell_in + 1)
        self.assertEqual(item.sell_in, -1)

        # Dégradation de la qualité 2 fois plus vite 
        self.assertEqual(item.quality, 8)
        GildedRoseTest.update_test(gilded_rose, 14)
        self.assertEqual(item.sell_in, -15)
        self.assertEqual(item.quality, 0)  # Jamais négatif


    def test_aged_brie(self):
        # Créer Item
        item = Item("Aged Brie", 16, 22)
        gilded_rose = GildedRose([item])
        
        # Un jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 15)
        self.assertEqual(item.quality, 23)

        # Après date de péremption
        GildedRoseTest.update_test(gilded_rose, item.sell_in + 2)
        self.assertEqual(item.sell_in, -2)

        # Dégradation de la qualité 2 fois plus vite
        self.assertEqual(item.quality, 42)
        GildedRoseTest.update_test(gilded_rose, 14)
        self.assertEqual(item.sell_in, -16)
        self.assertEqual(item.quality, 50) 


    def test_sulfuras(self):
        # Création Item
        item = Item("Sulfuras, Hand of Ragnaros", 13, 80)
        gilded_rose = GildedRose([item])

        # Un jour après
        gilded_rose.update_quality()
        self.assertNotEqual(item.sell_in, 14)
        self.assertEqual(item.sell_in, 13)
        self.assertEqual(item.quality, 80)
        
        # Après date de péremption
        GildedRoseTest.update_test(gilded_rose, item.sell_in + 1)
        self.assertEqual(item.sell_in, 13)
        self.assertNotEqual(item.sell_in, -1)

    def test_backstage_passes(self):
        # Création Item
        item = Item("Backstage passes to a TAFKAL80ETC concert", 20, 20)
        gilded_rose = GildedRose([item])

        # Un jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 19)
        self.assertEqual(item.quality, 21)
        GildedRoseTest.update_test(gilded_rose, 9)

        # Sell in 10 or less
        self.assertEqual(item.sell_in, 10)
        self.assertEqual(item.quality, 30)
        GildedRoseTest.update_test(gilded_rose)
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 32)

        # Sell in 5 or less
        GildedRoseTest.update_test(gilded_rose, 4)
        self.assertEqual(item.sell_in, 5)
        self.assertEqual(item.quality, 40)
        GildedRoseTest.update_test(gilded_rose)
        self.assertEqual(item.sell_in, 4)
        self.assertEqual(item.quality, 43)
        GildedRoseTest.update_test(gilded_rose, 2)
        self.assertEqual(item.sell_in, 2)
        self.assertEqual(item.quality, 49)

        # Never gets beyond 50 and drops to 0 once sell in passed
        GildedRoseTest.update_test(gilded_rose)
        self.assertEqual(item.sell_in, 1)
        self.assertEqual(item.quality, 50)

        GildedRoseTest.update_test(gilded_rose, 2)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_conjured(self):
        # Création Item
        item = Item("Conjured Mana Cake", 20, 50)
        gilded_rose = GildedRose([item])

        # Un jour après
        gilded_rose.update_quality()
        self.assertEqual(item.sell_in, 19)
        self.assertEqual(item.quality, 48)
        GildedRoseTest.update_test(gilded_rose, item.sell_in + 1)

        # Après date de péremption -- will decrease twice as fast as normal items (-4)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 6)

        GildedRoseTest.update_test(gilded_rose)
        self.assertEqual(item.sell_in, -2)
        self.assertEqual(item.quality, 2)

        GildedRoseTest.update_test(gilded_rose)
        self.assertEqual(item.sell_in, -3)
        self.assertEqual(item.quality, 0)

if __name__ == '__main__':
    unittest.main()


if __name__ == '__main__':
    unittest.main()