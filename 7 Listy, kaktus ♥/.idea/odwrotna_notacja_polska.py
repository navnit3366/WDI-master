class Object:
    
    def __init__(self, number):
        self.number = number
        self.next = None
        
class Stack:
    
    def __init__(self):
        self.head = None
        
    def push(self, number):
        if self.head == None:
            new = Object(number)
            self.head = new
        else:
            new = Object(number)
            new.next = self.head
            self.head = new
    
    def pop(self):
        self.head = self.head.next
        
    def count(self, sign):
        if sign == '+':
            return self.head.next.number + self.head.number
        elif sign == '-':
            return self.head.next.number - self.head.number
        elif sign == '*':
            return self.head.next.number * self.head.number
        elif sign == '/':
            return self.head.next.number / self.head.number


expression = "12 2 3 4 * 10 5 / + * +"
rpn = Stack()
number = ''

for sign in expression:
    #jesli jest liczba dodaje do listy chwilowej liczby
    if sign.isdigit():
        number += sign
    #jesli jest spacja wstawia liczbe na stos i czysci liste chwilowej liczby
    elif sign == ' ':
        if len(number)!=0:
            rpn.push(int(number))
            number = ''
    #jesli jest znakiem dzialania wykonuje dzialanie i wynik wrzuca na stos
    else:
        result = rpn.count(sign)
        rpn.pop()
        rpn.pop()
        rpn.push(result)

print(result)