
#node class to store the data and pointer
class Node:
	def __init__(self,init_data):
		self.data= init_data
		self.next= None

	def get_data(self):
		return self.data

	def get_next(self):
		return self.next

	def set_data(self,new_data):
		self.data = new_data

	def set_next(self,new_next):
		self.next = new_next

#underdered Linkedlist class
class OrderedList:

	def __init__(self):
		self.head= None

	def is_empty(self):
		return self.head == None

	def add(self,item):
		current =self.head
		done = False
		previous = None

		if current != None and not done:

			#if current data is higher then add it before else continue
			if current.get_data() > item:
				done = True
			else:
				previous = current
				current = current.get_next()

		temp = Node(item)

		if previous == None:
			temp.set_next(self.head)
			self.head = temp
		else:
			temp.set_next(current)
			previous.set_next(temp)

	
	#traversing all elements and counting the items
	def size(self):
		current = self.head
		count =0

		while current !=None :
			count = count +1
			current = current.get_next()

		return count
	
	#method to search whether an item exists or not
	def search(self,item):
		found = False
		current = self.head  #get the first one


		#loop through all nodes and check if item matches data
		while current != None and not found :
			if current.get_data() == item :
				found = True
			else:
				#no need to search further
				if current.get_data() > item :
				   return False
				else:
				   current = current.get_next()

		return found

	# method to remove an item from linkedlist
	def remove(self,item):
		#store the previous node 
		current =self.head
		previous = None 
		found = False

		while not found:
			if current.get_data() == item :  #found at the head
				found = True

			else: #not at the head hence save the previous node
				previous = current
				current = current.get_next()

		#adjust the nodes
		if previous == None:
			self.head = current.get_next()
		else:
			previous.set_next(current.get_next)








