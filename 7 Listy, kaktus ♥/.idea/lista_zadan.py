class Thing:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority
        self.next = None

class ToDo:
    def __init__(self):
        self.head = None

    def add_element(self, name, priority):

        new_thing = Thing(name, priority)

        #if list empty
        if self.head == None:
            self.head = new_thing
            new_thing.next = None
        #if list not empty
        else:
            n = self.head
            if new_thing.priority >= n.priority:
                self.head = new_thing
                new_thing.next = n
            else:
                if not n.next:
                    n.next = new_thing
                    new_thing.next = None
                else:
                    while n.next:
                        if new_thing.priority < n.next.priority:
                            n = n.next
                        else:
                            break
                    if not n.next:
                        n.next = new_thing
                        new_thing.next = None
                    else:
                        new_thing.next = n.next
                        n.next = new_thing



    def print_things_to_do(self):
        print('Things to do:')
        n = self.head
        while n:
            print(n.priority, n.name)
            n = n.next

#creating a list
list_of_things = ToDo()
#adding elements
list_of_things.add_element('~ brush your teeth',4)
list_of_things.add_element('~ take a shower',6)
list_of_things.add_element('~ go to sleep',7)
list_of_things.add_element('~ watch a movie',5)
list_of_things.add_element('~ sing a song',2)
list_of_things.add_element('~ fuck programming',10)
#printing our list
list_of_things.print_things_to_do()