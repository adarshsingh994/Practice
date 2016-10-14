package LinkedList;

public class MyLinkedListPractice {
    
    Node head;

    static class Node{
        int data;
        Node next;
        Node(int d){
            data = d;
        }
    }
    
    public void insertDataAtFront(int data){
        Node node = new Node(data);
        node.next = head;
        head = node;
    }
    
    public void insertDataAfterAGivenNode(Node prev, int data){
        if(prev == null){
            System.out.println("The prev node cannot be null!");
        }else{
            Node node = new Node(data);
            node.next = prev.next;
            prev.next = node;
        }
    }
    
    public int countLength(){
        Node node = head;
        if(node == null){
            return 0;
        }else{
            int c = 1;
            while(node != null && node.next != null){
                c++;
                node = node.next;
            }
            return c;
        }
    }
    
    public int countLengthRec(Node head){
        if(head == null){
            return 0;
        }else{
            return (1 + countLengthRec(head.next));
        }
    }
    
    public void insertAtEnd(int data){
        Node node = new Node(data);
        if(head == null){
            head = node;
        }else{
            node.next = null;
            Node last = head;
            while(last.next != null){
                last = last.next;
            }
            last.next = node;
        }
    }
    
    public void printList(){
        Node n = head;
        while(n != null){
            System.out.println(n.data + " ");
            n = n.next;
        }
    }
    
    public void deleteAtPosition(int position){
        Node temp = head, prev = null;
        int c = 0;
        if(position == 0){
            head = temp.next;
        }else{
            while(temp != null && c < position){
                c++;
                prev = temp;
                temp = temp.next;
            }
            if(c == position){
                prev.next = temp.next;
            }
            else{
                System.out.println("Given position does not exist!!");
            }
        }
    }
    
    public void deleteNodeAtKey(int key){
        Node temp = head, prev = null;
        if(temp != null && temp.data == key){
            head = temp.next;
        }
        else{
            while(temp != null && temp.data != key){
                prev = temp;
                temp = temp.next;
            }
            if(temp == null){
                System.out.println("Given key is not present in the list!!");
            }else{
                prev.next = temp.next;
            }
        }
    }
    
    public void swapNodes(int x, int y){
        
        if(x == y){
            System.out.println("No need to swap!!");
        }else{
            //Get the node with value x and set its previous node 
            Node currx = head, prevx = null;
            while(currx != null && currx.data != x){
                prevx = currx;
                currx = currx.next;
            }
            //Get the node with value y and set its previous node
            Node curry = head, prevy = null;
            while(curry != null && curry.data != y){
                prevy = curry;
                curry = curry.next;
            }
            
            //Check if node with value x and y was found or not
            if(currx == null || curry == null){
                System.out.println("Swappable nodes not found!!");
            }else{
                //Check if x node is not head
                if(prevx != null)
                    prevx.next = curry;
                else
                    head = curry;
                
                //Check id y node is not head
                if(prevy != null)
                    prevy.next = currx;
                else
                    head = currx;
                
                // Swap next pointers
                Node temp = currx.next;
                currx.next = curry.next;
                curry.next = temp;
            }
        }
    }
    
    public void reverseListIter() {
        Node prev = null;
        Node current = head;
        Node next = null;
        while (current != null) {
            next = current.next;
            current.next = prev;
            prev = current;
            current = next;
        }
        head = prev;
    }
    
    public static void main(String[] args) {
        // TODO code application logic here
        MyLinkedListPractice llist = new MyLinkedListPractice();
        llist.insertDataAtFront(1);
        llist.insertDataAtFront(2);
        llist.insertDataAtFront(3);
        llist.insertDataAfterAGivenNode(llist.head, 0);
        llist.insertAtEnd(4);
        //Print before deleting
        System.out.println("Before Deleting:");
        llist.printList();
        
        //Print the length before deletion
        System.out.println("Length before deletion is: " + llist.countLengthRec(llist.head));
        
        //Delete a node at a given key
        //llist.deleteNodeAtKey(4);
        
        //Delete a node at a given position
        llist.deleteAtPosition(4);

        //Swap 2 nodes
        llist.swapNodes(3, 2);
                
        //Print the list
        System.out.println("After Deleting and Swapping:");
        llist.printList();
        
        //Print the length after deleting
        System.out.println("Length after deletion is: " + llist.countLength());
        
        //Reversing the Linked List
        System.out.println("List after reversing:");
        llist.reverseListIter();
        llist.printList();
    }
    
}
