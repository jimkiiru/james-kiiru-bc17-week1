class BinarySearch(list):
	def __init__(self, a, b):
		self.a = a
		self.b = b

	def search(self, itemToSearch):
		i = 0
		lowerItemIndex = 0
		higherItemIndex = self.a - 1
		midpoint = lowerItemIndex + (higherItemIndex - lowerItemIndex)//2

		if itemToSearch == midpoint:
			i = i + 1
			return {i: midpoint}
		elif itemToSearch > midpoint:
			# item is in the upper half of the list
			lowerItemIndex = midpoint + 1
			midpoint = lowerItemIndex + (higherItemIndex - lowerItemIndex)//2
			self.search(itemToSearch)
		elif itemToSearch < midpoint:
			# item is in the lower half of the listt
			higherItemIndex = midpoint - 1
			midpoint = lowerItemIndex + (higherItemIndex - lowerItemIndex)//2
                        self.search(itemToSearch)
