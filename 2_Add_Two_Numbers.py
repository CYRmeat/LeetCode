#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 16:24:05 2018

@author: chenyirong
"""

# Definition for singly-linked list.
#class ListNode:
#    def __init__(self, x):
#        self.val = x
#        self.next = None

class Solution:
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None
            
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""
        while l1.next != None:
            num1 += str(l1.val)
            l1 = l1.next
        num1 += str(l1.val)
        while l2.next != None:
            num2 += str(l2.val)
            l2 = l2.next
        num2 += str(l2.val)
        
        ll1 = list(num1)
        ll2 = list(num2)
        ll1.reverse()
        ll2.reverse()
        num1 = "".join(ll1)
        num2 = "".join(ll2)
        
        l = []
        num3 = str(int(num1) + int(num2))
        for i in num3:
            l.append(int(i))
        
        l.reverse()
        
        l3 = ListNode(l[0])
        pre_node = l3
        for i in range(1,len(l)):            
            node = ListNode(l[i])
            pre_node.next = node
            pre_node = node
        
        return l3