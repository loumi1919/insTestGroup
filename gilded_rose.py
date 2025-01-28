class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        update = UpdateItem()
        
        for item in self.items:
            if item.name == 'Aged Brie':
                update.aged_brie(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                update.backstage_passes(item)
            elif item.name == 'Sulfuras, Hand of Ragnaros':
                update.sulfuras(item)
            elif item.name == 'Conjured Mana Cake':
                update.conjured(item)
            else:
                update.base_item(item)



class UpdateItem(object):  
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def base_item(self, item):
        if item.sell_in > 0: 
            quality_down = -1
        else:
            quality_down = -2
        item.quality = max((item.quality + quality_down), self.MIN_QUALITY)
        item.sell_in += -1

    def aged_brie(self, item):
        if item.sell_in > 0:
            quality_up = 1
        else:
            quality_up = 2
        item.quality = min((item.quality + quality_up), self.MAX_QUALITY)
        item.sell_in += -1
    
    def sulfuras(self, item):
        pass

    def backstage_passes(self, item):

        def get_quality(item, quality_up):
            item.quality = min(item.quality + quality_up , self.MAX_QUALITY)

        if item.sell_in > 10:
            quality_up = 1
            get_quality(item, quality_up)
        elif item.sell_in > 5:
            quality_up = 2
            get_quality(item, quality_up)
        elif item.sell_in > 0:
            quality_up = 3
            get_quality(item, quality_up)
        else:
            item.quality = 0
        item.sell_in += -1

    def conjured(self, item):
        if item.sell_in > 0:
            quality_down = -2
        else:
            quality_down = -4

        item.quality = max((item.quality + quality_down), self.MIN_QUALITY)
        item.sell_in += -1
        
        


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)