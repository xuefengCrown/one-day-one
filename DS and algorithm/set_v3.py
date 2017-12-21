"""
set based on binary search trees
基于二叉搜索树的集合实现(一个集合的内部表示是一棵二叉树)
创建集合: myset = build_bst([8, 3, 4, 7, 5, 16])
是否含有: set_cotains(myset, 7)
交集: intersection2bst(set1, set2)
添加元素: set_adjoin(myset, 46)
并集: union2bst(set1, set2)
中序遍历bst: in_order(bst)
"""
import random
class BST:
    empty_t = None #因为要判定左右子树是否空，故约定空树为None
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        # left, right must be a BST or None
        assert (isinstance(left, BST) or left is None)\
            and (isinstance(right, BST) or right is None)
        self.left = left
        self.right = right
    def __repr__(self):
        if self.left or self.right:
            return 'Tree({0}, {1})'.format(self.entry,
                                           repr((self.left, self.right)))
        else:
            return 'Tree({0})'.format(repr(self.entry))
    def is_empty(self):
        return self is BST.empty_t

# build a bst with list
def bst_helper(tree, ele):
    if tree is None:
        return BST(ele)
    else:
        entry = tree.entry
        if ele < entry:
            return BST(entry, bst_helper(tree.left, ele), tree.right)
        elif ele == entry:
            return tree
        else:
            return BST(entry, tree.left, bst_helper(tree.right, ele))
def build_bst(eles):
    assert len(eles) > 0, "args should not be []"
    bst = None
    for e in eles:
        bst = bst_helper(bst, e)
    return bst

# traversal in-order
"""
yield 时出现问题
google：Can generators be recursive?
https://stackoverflow.com/questions/38254304/can-generators-be-recursive
"""
def in_order(bst): # return a generator
    # if there's left subtree, then inorder(left)
    if bst.left is not None:
        yield from in_order(bst.left)
    if bst is not None:
        #print(bst.entry, end = ', ')
        yield bst.entry
    if bst.right is not None:
        yield from in_order(bst.right)

"""
Sets as binary search trees
"""

def set_contains(s, v):
    """searching the tree can be performed in a logarithmic number
       of steps rests on the assumption that the tree is balanced
    """
    if s is None:
        return False
    e = s.entry
    if e == v:
        return True
    elif e < v:
        return set_contains(s.right, v)
    elif e > v:
        return set_contains(s.left, v)
def set_adjoin(s, v):
    return bst_helper(s, v)

def set_intersection(ordered1, ordered2):
    if not ordered1 or not ordered2:
        return []
    else:
        o1_first, o2_first = ordered1[0], ordered2[0]
        if o1_first == o2_first:
            return [o1_first] + set_intersection(ordered1[1:],
                                    ordered2[1:])
        elif o1_first > o2_first:
            return set_intersection(ordered1, ordered2[1:])
        else:
            return set_intersection(ordered1[1:], ordered2)

def intersection2bst(set1, set2):
    unorder = set_intersection(list(in_order(set1)), list(in_order(set2)))
    random.shuffle(unorder)
    return build_bst(unorder)

def set_union(ordered1, ordered2):
    if not ordered1:
        return ordered2
    elif not ordered2:
        return ordered1
    else:
        o1_first, o2_first = ordered1[0], ordered2[0]
        if o1_first == o2_first:
            return [o1_first] + set_union(ordered1[1:],
                                    ordered2[1:])
        elif o1_first > o2_first:
            return [o2_first] + set_union(ordered1, ordered2[1:])
        else:
            return [o1_first] + set_union(ordered1[1:], ordered2)

def union2bst(set1, set2):
    unorder = set_union(list(in_order(set1)), list(in_order(set2)))
    random.shuffle(unorder)
    return build_bst(unorder)
def content_set(_set):
    return list(in_order(_set))
        
myset = build_bst([8, 3, 10, 1, 6, 14, 4, 7, 13])
newset = set_adjoin(myset, 23)
myset2 = build_bst([7, 6, 14, 3, 2, 1, 10, 28, 90])

print("intersection: ", content_set(intersection2bst(myset, myset2)))
print("union: ", content_set(union2bst(myset, myset2)))
