from treelib import Node, Tree

class BehaviourTree():

    def __init__(self):
        self.height = 0
        self.noOfNodes = 0
        self.btree = Tree()
    
    def bTreeGenerate(self, i):
        #Create Root node
        self.btree.create_node("Root", "root")
        self.root = self.btree.get_node("root")
        self.btree.create_node("Hit wall", "hitwall", parent = "root")
        self.btree.create_node("Continue", "nowall", parent = "hitwall", data = 0)
        if i%2 == 0:
            self.btree.create_node("Is Left Empty", "IsLeftEmpty", parent = "hitwall", data = 1)
            self.btree.create_node("Left", "Left", parent = "IsLeftEmpty", data = 0)
            self.btree.create_node("Is Right Empty", "IsRightEmpty", parent = "IsLeftEmpty", data = 1)
            self.btree.create_node("Right", "Right", parent = "IsRightEmpty", data = 0)
            self.btree.create_node("Backward", "backward", parent = "IsRightEmpty", data = 1)
        else:
            self.btree.create_node("Is Right Empty", "IsRightEmpty", parent = "hitwall", data = 1)
            self.btree.create_node("Right", "Right", parent = "IsRightEmpty", data = 0)
            self.btree.create_node("Is Left Empty", "IsLeftEmpty", parent = "IsRightEmpty", data = 1)
            self.btree.create_node("Left", "Left", parent = "IsLeftEmpty", data = 0)
            self.btree.create_node("Backward", "backward", parent = "IsLeftEmpty", data = 1)

        self.height = self.btree.depth()


    def getBtree(self):
        return self.btree.show()        

    def getNodes(self):
        return self.btree.all_nodes()

    def getChildren(self, node):
        return self.btree.children(node.identifier)

    def getNode(self, string):
        return self.btree.get_node(string)
    


