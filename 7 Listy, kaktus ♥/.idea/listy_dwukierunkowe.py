class Node:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.name)

    def __int__(self):
        return int(self.score)

class BiDirectionalList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_at_the_beginning(self, name, score):
        if(self.tail==None):
            n=Node(name, score)
            self.head=n
            self.tail=n
        else:
            n=self.head
            new_node=Node(name, score)
            n.prev=new_node
            new_node.next=n
            self.head=new_node
        self.size+=1

    def add_at_the_end(self, name, score):
        if(self.head==None):
            n=Node(name, score)
            self.head=n
            self.tail=n
        else:
            n=self.tail
            new_node=Node(name, score)
            n.next=new_node
            new_node.prev=n
            self.tail=new_node
        self.size+=1

    def add_at_n_position(self):
        print("Give the position of a new element (from 1 to 5): ")
        position=int(input())
        if (position<1 or position>5):
            print("Choose a different position!")
            BiDirectionalList.add_at_n_position(self)
        elif (position==1):
            print("Give the person's last name: ")
            name=input()
            print("Give the person's score: ")
            score=int(input())
            BiDirectionalList.add_at_the_beginning(self, name, score)
        elif (position==self.size+1):
            print("Give the person's last name: ")
            name = input()
            print("Give the person's score: ")
            score = int(input())
            BiDirectionalList.add_at_the_end(self, name, score)
        else:
            n=self.head
            for i in range(position-2):
                n=n.next
            print("Give the person's last name: ")
            name = input()
            print("Give the person's score: ")
            score = int(input())

            new_node=Node(name, score)
            new_node.next = n.next
            n.next=new_node
            new_node.prev=n
            new_node.next.prev=new_node

        self.size+=1

    def delete_first_element(self):
        n=self.head
        n.next.prev=None
        self.head=n.next
        self.size-=1

    def delete_last_element(self):
        n=self.tail
        n.prev.next=None
        self.tail=n.prev
        self.size-=1

    def print_list_from_the_beginning(self):
        n=self.head
        while n:
            print(n.name, n.score)
            n=n.next

    def print_list_from_the_end(self):
        n=self.tail
        while n:
            print(n.name, n.score)
            n=n.prev

    def find_the_highest_score(self):
        n=self.head
        largest_score=n.score
        best_student=n.name
        while n:
            if (largest_score<n.score):
                largest_score=n.score
                best_student=n.name
            n=n.next
        print("\nThe best student is: ", best_student)

#creation of a list
list=BiDirectionalList()
#adding 3 elements in the beginning
list.add_at_the_beginning("Yellow",5)
list.add_at_the_beginning("Blue",9)
list.add_at_the_beginning("Green",6)
#adding 3 elements at the end
list.add_at_the_end("Orange",14)
list.add_at_the_end("Pink",1)
list.add_at_the_end("Purple",18)
#deleting 1 element from the beginning
list.delete_first_element()
#deleting 1 element from the end
list.delete_last_element()
#adding an element on an optional position
list.add_at_n_position()
#printing the list from the begnning
print("\nList from the beginning:")
list.print_list_from_the_beginning()
#printing the list from the end
print("\nList from the end:")
list.print_list_from_the_end()
#choosing the best student
list.find_the_highest_score()