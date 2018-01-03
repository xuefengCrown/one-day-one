import insertsort as inss

"""当排序10000个元素时，会达到递归最大深度。
   我不知道能否通过使用尾递归来纠正。
   如果不行的话，就得修改为迭代版本。"""
def merge(ordereda, orderedb):
    "merge two sorted list"
    if len(ordereda) == 0: return orderedb
    if len(orderedb) == 0: return ordereda
    heada = ordereda[0]
    headb = orderedb[0]
    if heada <= headb:
        return [heada] + merge(ordereda[1:], orderedb)
    else:
        return [headb] + merge(ordereda, orderedb[1:])
    
def merge_iter(ordereda, orderedb):
    "merge two sorted list"
    res = []
    while True:
        # 当其中一个到达末尾时，任务结束
        if len(ordereda) == 0: return res + orderedb
        if len(orderedb) == 0: return res + ordereda
        heada = ordereda[0]
        headb = orderedb[0]
        if heada <= headb:
            res.append(heada)
            ordereda = ordereda[1:]
        else:
            res.append(headb)
            orderedb = orderedb[1:]

    return res
    
    
def mergesort(nums):
    if len(nums) == 1: return nums # 只有一个元素时，已经有序
    mid = len(nums)//2
    return merge_iter(mergesort(nums[:mid]), mergesort(nums[mid:]))
    
    
if __name__ == '__main__':
    nums = inss.genlist(40000, 0, 10000)
    
    #res, inserts_time = inss.timed(inss.insert_sort, nums)
    res2, merges_time = inss.timed(mergesort, nums)
    #print(res2)
    print('insertsort time:{}s \nmergesort time:{}s'.format(0, merges_time))
