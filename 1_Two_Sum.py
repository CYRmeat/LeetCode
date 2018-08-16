#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 26 00:53:01 2018

@author: chenyirong
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
             for j in range(i+1,len(nums)):
                    if nums[i]+nums[j] == target:
                        if i != j:
                            return [i, j]
                        
                        
                        
class Solution_2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i in range(len(nums)):
            d[nums[i]] = i
        
        for i in range(len(nums)):
            left = target - nums[i]
            if d.__contains__(left) and d[left] != i:
                if i <= d[left]:
                    return [i, d[left]]
                else:
                    return [d[left], i]