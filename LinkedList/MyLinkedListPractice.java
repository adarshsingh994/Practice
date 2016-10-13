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
        
        //Delete a node at a given key
        //llist.deleteNodeAtKey(4);
        
        //Delete a node at a given position
        llist.deleteAtPosition(4);

        //Print the list
        System.out.println("After Deleting:");
        llist.printList();
    }
    
}
