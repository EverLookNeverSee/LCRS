from typing import List


def is_isomorphic(s: str, t: str) -> bool:
    """
    Given two strings s and t, determine if they are isomorphic.
    Two strings s and t are isomorphic if the characters in s can be replaced to get t.
    All occurrences of a character must be replaced with another character while preserving
    the order of characters. No two characters may map to the same character, but a character
    may map to itself.
    Level of difficulty: Easy
    :param s: First given string
    :param t: Second given string
    :return: Whether two string is isomorphic or not
    """
    mapping_s_t = {}
    mapping_t_s = {}
    for c1, c2 in zip(s, t):
        if (c1 not in mapping_s_t) and (c2 not in mapping_t_s):
            mapping_s_t[c1] = c2
            mapping_t_s[c2] = c1
        elif mapping_s_t.get(c1) != c2 or mapping_t_s.get(c2) != c1:
            return False
    return True


def number_of_one_bits(n: int) -> int:
    """
    Write a function that takes an unsigned integer and returns the number of '1' bits,
    It has (also known as the Hamming weight).
    https://en.wikipedia.org/wiki/Hamming_weight
    Lever of difficulty: Easy
    :param n: An unsigned integer
    :return: Number of 1 bits
    """
    return bin(n).count("1")


def number_of_good_pairs(nums: List[int]) -> int:
    """
    Given an array of integers nums, return the number of good pairs.
    A pair (i, j) is called good if nums[i] == nums[j] and i < j.
    Level of difficulty: Easy
    :param nums: List of integers
    :return: Number of good pairs
    """
    count = 0
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                count += 1
    return count


def median_of_two_sorted_arrays(nums_1: List[int], nums_2: List[int]) -> float:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
    The overall run time complexity should be O(log (m+n)).
    Level of difficulty: Hard
    :param nums_1: List of integers
    :param nums_2: List of integers
    :return: The median of two sorted arrays
    """
    merged = sorted(nums_1 + nums_2)
    idx = (len(merged) - 1) // 2
    if len(merged) % 2 != 0:
        median = merged[idx]
        return median
    else:
        median = (merged[idx] + merged[idx + 1]) / 2
        return median
