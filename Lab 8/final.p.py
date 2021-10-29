class Node:
    def __init__(self, value, next):
        self.val = value
        self.next = next
    def __repr__(self):
        return "val: %d, next: %s"%(self.val, self.next)

def split_list(val, int_list):
    lesser_list = Node(None, None)
    greater_list = Node(None, None)
    while int_list is not None:
        if int_list.val > val:
            greater_list.val = val
            greater_list = greater_list.next
        elif int_list.val < val:
            lesser_list.val = val
            lesser_list = lesser_list.next
        int_list = int_list.next
    return lesser_list, greater_list


int_list = Node(1, None)
node2 = Node(3, int_list)
node3 = Node(4, node2)
node4 = Node(8, node3)
print(split_list(5, int_list))