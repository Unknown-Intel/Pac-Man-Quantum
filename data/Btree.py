import py_trees
import random

class turnLeft(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(turnLeft, self).__init__(name)
        self.blackboard = self.attach_blackboard_client(name=self.name)
        self.blackboard.register_key("dir", access=py_trees.common.Access.WRITE)
        self.blackboard.register_key("dir", access=py_trees.common.Access.READ)

    def update(self):
        status = super().update()
        dir = self.blackboard.dir
        if dir == "Up":
            self.blackboard.dir = "Left"
        elif dir == "Left":
            self.blackboard.dir = "Down"
        elif dir == "Down":
            self.blackboard.dir = "Right"
        elif dir == "Right":
            self.blackboard.dir = "Up"
        status = py_trees.common.Status.SUCCESS
        return status

class turnRight(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(turnRight, self).__init__(name)
        self.blackboard = self.attach_blackboard_client(name=self.name)
        self.blackboard.register_key("dir", access=py_trees.common.Access.WRITE)
        self.blackboard.register_key("dir", access=py_trees.common.Access.READ)

    def update(self):
        status = super().update()
        dir = self.blackboard.dir
        if dir == "Up":
            self.blackboard.dir = "Right"
        elif dir == "Left":
            self.blackboard.dir = "Up"
        elif dir == "Down":
            self.blackboard.dir = "Left"
        elif dir == "Right":
            self.blackboard.dir = "Down"
        status = py_trees.common.Status.SUCCESS
        return status

class turnBack(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(turnBack, self).__init__(name)
        self.blackboard = self.attach_blackboard_client(name=self.name)
        self.blackboard.register_key("dir", access=py_trees.common.Access.WRITE)
        self.blackboard.register_key("dir", access=py_trees.common.Access.READ)

    def update(self):
        status = super().update()
        dir = self.blackboard.dir
        if dir == "Up":
            self.blackboard.dir = "Down"
        elif dir == "Left":
            self.blackboard.dir = "Right"
        elif dir == "Down":
            self.blackboard.dir = "Up"
        elif dir == "Right":
            self.blackboard.dir = "Left"
        status = py_trees.common.Status.SUCCESS
        return status

class isleftEmpty(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(isleftEmpty, self).__init__(name)

    def update(self):
        self.logger.debug("  %s [Foo::update()]" % self.name)
        decision = random.choice([True, False])

        if decision:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE


class isRightEmpty(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(isRightEmpty, self).__init__(name)

    def update(self):
        self.logger.debug("  %s [Foo::update()]" % self.name)
        decision = random.choice([True, False])

        if decision:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE

class cont(py_trees.behaviour.Behaviour):
    def __init__(self, name):
        super(cont, self).__init__(name)

    def update(self):
        self.logger.debug("  %s [Foo::update()]" % self.name)
        decision = random.choice([True, False])

        if decision:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE


def pre_tick_handler(behaviour_tree):
    print("\n--------- Run %s ---------\n" % behaviour_tree.count)

def config():
    configuration = py_trees.blackboard.Client(name="Tree Config")
    configuration.register_key("dir", access=py_trees.common.Access.WRITE)
    configuration.dir = "Up"

def retrieve_position():
    return [0,0]


if __name__ == '__main__':
    root = py_trees.composites.Selector("Root")
    cont = cont('Continue')
    isRightEmpty = isRightEmpty('Is Right Empty')
    isleftEmpty = isleftEmpty("Is Left Empty")
    turnLeft = turnLeft('Turn Left')
    turnRight = turnRight("Turn Right")
    turnBack = turnBack("Turn Back! MUDDAFUCKA")

    seq_right = py_trees.composites.Sequence("Seq Right")
    seq_left = py_trees.composites.Sequence("Seq Left")

    seq_right.add_children([isRightEmpty, turnRight])
    seq_left.add_children([isleftEmpty, turnLeft])
    root.add_children([cont, seq_right, seq_left, turnBack])

    behaviour_tree = py_trees.trees.BehaviourTree(root=root)
    behaviour_tree.add_pre_tick_handler(pre_tick_handler)
    behaviour_tree.visitors.append(py_trees.visitors.DisplaySnapshotVisitor(
            display_blackboard=False,
            display_activity_stream=True)
    )

    config()

    # py_trees.display.render_dot_tree(root=root)
    def print_tree(tree):
        print(py_trees.display.unicode_tree(root=root, show_status=True))
    
    behaviour_tree.tick_tock(
            period_ms=500,
            number_of_iterations=20,
            pre_tick_handler=None)
            # post_tick_handler=print_tree
        #)
