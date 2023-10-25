class linked_list:
    def __init__(self, currentval=None):
        self.ll = []
        l_node = list((1,currentval,1))
        self.ll.append(l_node)

    def add_element(self, currentval):
        noofitems = len(self.ll)
        temp_list = self.ll[0]
        temp_list[0] = noofitems + 1
        self.ll[0] = temp_list
        temp_list = self.ll[noofitems-1]
        temp_list[0] = noofitems-1
        temp_list[2] = noofitems+1
        self.ll[noofitems-1] = temp_list
        temp_list = [noofitems,currentval,1]
        self.ll.append(temp_list)

    def del_element(self, node):
        if node != 1:
        # Adjust other nodes        
            self.ll.pop(node-1)
            i = 0
            for item in self.ll:
                item[0] = item[0] - 1
                if item[2] > 2:
                    item[2] = item[2] - 1
                self.ll[i] = item
                i += 1
        else:
            temp_list = self.ll[1]
            temp_list[1] = len(self.ll)
            self.ll[0] = temp_list
            self.ll.pop(node-1)
            i = 0
            for item in self.ll:
                item[0] = item[0] - 1
                if item[2] > 2:
                    item[2] = item[2] - 1
                self.ll[0] = item
                i += 1

    def traverse(self):
        for item in self.ll:
            print(item)

my_linked_list = linked_list(5)
my_linked_list.add_element(7)
my_linked_list.add_element(9)
my_linked_list.add_element(11)
my_linked_list.traverse()
my_linked_list.del_element(2)
my_linked_list.traverse()
"""
l1 = [[-1,2,2],[1,1,3],[2,5,4]]
print(l1[1])
print(l1[1][2])
"""