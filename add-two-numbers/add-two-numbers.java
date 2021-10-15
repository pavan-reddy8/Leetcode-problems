/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode t1=l1;
        ListNode t2=l2;
        ListNode res =new ListNode(0);
        ListNode t3=res;
        int carry=0;
        while(t1!=null || t2!=null){
            
             int tres=0;
            if(t1!=null && t2!=null){
                tres=t1.val+t2.val+carry;
                carry=tres/10;
                tres=tres%10;            
                if(t1.next!=null||t2.next!=null)
                    t3.next=new ListNode(0);

            }
            else if(t1!=null){
                tres=t1.val+carry;
                carry=tres/10;
                tres=tres%10;
                if(t1.next!=null)
                    t3.next=new ListNode(0);
            }
            else if(t2!=null){
                tres=t2.val+carry;
                carry=tres/10;
                tres=tres%10;
                if(t2.next!=null)
                    t3.next=new ListNode(0);
            }
            t3.val=tres;
            if(carry>0)
                t3.next=new ListNode(carry);
            t3=t3.next;
            if(t1!=null)
                t1=t1.next;
            if(t2!=null)
                t2=t2.next;
            
            
        }
        return res;
    }
}