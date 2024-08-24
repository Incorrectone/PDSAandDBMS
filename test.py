def search(nums, target, l = 0, r = None):
        if r == None:
            r = len(nums) - 1
        if l > r:
            return -1
        
        mid_point = (l + r) // 2

        if nums[mid_point] == target:
            return mid_point
        elif nums[mid_point] > target:
            return search(nums, target, l, mid_point - 1)
        else:
            return search(nums, target, mid_point + 1, r)
        

print(search([5], -5))