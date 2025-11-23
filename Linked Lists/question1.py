class node:
    def __init__(self, data: int, nextNode: int):
        self.data = data
        self.nextNode = nextNode



linkedList = []

linkedList.append(node(1, 1))
linkedList.append(node(5, 4))
linkedList.append(node(6, 7))
linkedList.append(node(7, -1))
linkedList.append(node(2, 2))
linkedList.append(node(0, 6))
linkedList.append(node(0, 8))
linkedList.append(node(56, 3))
linkedList.append(node(0, 9))
linkedList.append(node(0, -1))

startPointer = 0
emptyList = 5



def outputNodes(linkedList, startPointer):

    endPointer = startPointer

    while endPointer != -1:

        print(linkedList[endPointer].data)

        endPointer = linkedList[endPointer].nextNode



def addNode(linkedList, startPointer_copy, emptyList_copy):
    global emptyList, startPointer


    data_to_add = int(input("Enter data to add: "))

    if startPointer_copy == -1:

        if emptyList_copy == -1:
            return False
        
        else:

            startPointer = emptyList_copy

            linkedList[emptyList_copy].data = data_to_add

            emptyList = linkedList[emptyList_copy].nextNode

            linkedList[emptyList_copy].nextNode = -1


            return True
        
    else:

        if emptyList_copy == -1:
            return False
        
        else:

            while linkedList[startPointer_copy].nextNode != -1:
                startPointer_copy = linkedList[startPointer_copy].nextNode

            linkedList[startPointer_copy].nextNode = emptyList_copy

            linkedList[emptyList_copy].data = data_to_add

            emptyList = linkedList[emptyList_copy].nextNode

            linkedList[emptyList_copy].nextNode = -1


            return True



outputNodes(linkedList, startPointer)

flag = addNode(linkedList, startPointer, emptyList)
if flag == True:
    print("Node added successfully.")
    print("Updated linked list:")

    outputNodes(linkedList, startPointer)
else:
    print("No empty node available to add data.")

    outputNodes(linkedList, startPointer)