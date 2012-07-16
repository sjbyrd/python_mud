from Item.Item import Item

class Equipable(Item):
	def __init__(self, itemJson, inventory):		
		Item.__init__(self, itemJson, inventory)
		
		self.attributes['equipment_slot'] = itemJson['equipment_slot']