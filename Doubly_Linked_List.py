class Node:
    def __init__(self,key=None, data=None, next=None,prev=None):
        self.key=key
        self.data = data
        self.next = next
        self.prev=prev

class LinkedList:
    def __init__(self):
        self.head = None
    
    def checkKey(self,key):
        itr=self.head
        temp=None
        while(itr!=None):
            if(itr.key==key):
                return True
            itr=itr.next
        return False

    def insertAtEnd(self,key,data):
        if(self.checkKey(key)==True):
            print("Element already found please enter different element.")
        else:
            if(self.head==None):
                node=Node(key,data)
                self.head=node
            else:
                itr=self.head
                while(itr.next!=None):
                    itr=itr.next
                node=Node(key,data)
                itr.next=node
                node.prev=itr
    
    def insertAtBegining(self,key,data):
        if(self.checkKey(key)==True):
            print("Element already found please enter different element.")
        else:
            node=Node(key,data,self.head)
            self.head=node
            head.next.prev=head

    def deleteNode(self,key):
        itr=self.head
        if(head.key==key):
            self.head=self.head.next
            slef.head.prev=None
        else:
            itr=self.head.next
            while(itr.key!=key and itr.next!=None):
                itr=itr.next
            if(itr.key==key):
                itr.next.prev=itr.prev
                itr.prev.next=itr.next
            elif(itr.next==None and itr.key==key):
                itr.prev.next=None
            else:
                print("Key value not present")


    def printList(self):
        itr=self.head
        while(itr!=None):
            print(str(itr.key)+"-->"+str(itr.data),end=" ")
            itr=itr.next

    def insertAtPosition(self,keyaft,key,data):
        if(self.checkKey(key)==True):
            print("Element already found please enter different element.")     
        elif(self.checkKey(keyaft)!=True):
            print("No After key element found")       
        else:
            itr=self.head
            while(itr.next!=None):
                if(itr.key==keyaft):
                    node=Node(key,data)
                    node.next=itr.next
                    node.prev=itr
                    node.next.prev=node
                    itr.next=node
                    break
                itr=itr.next
    
    def updateNode(self,key,data):
        if(self.checkKey(key)!=True):
            print("Key Not found") 
        else: 
            itr=self.head
            while(itr.next!=None):
                if(itr.key==key):
                    itr.data=data
                    break
                itr=itr.next




if __name__ == '__main__':
    ll = LinkedList()
    while(True):
        option=int(input())
        if option==0:
            break;
        elif option==1:
            key=int(input("Enter Key of data: "))
            val=int(input("Enter data to be entered at begining: "))
            ll.insertAtBegining(key,val)
        elif option==2:
            key=int(input("Enter Key of data: "))
            val=int(input("Enter data to be entered at End: "))
            ll.insertAtEnd(key,val)
        elif option==3:
            ll.printList()
        elif option==4:
            val=int(input("Enter key value to delete: "))
            ll.deleteNode(val)
        elif option==5:
            aftkey=int(input("Enter after key element: "))
            key=int(input("Enter Key of data: "))
            val=int(input("Enter the data to be entered: "))
            ll.insertAtPosition(aftkey,key,val)
        elif option==6:
            key=int(input("Enter the key element to be changed: "))
            val=int(input("Enter data to be changes: "))
            ll.updateNode(key,val)