class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prefix_product = [1]

        for i in range (len(nums)-1): 
            result = nums[i]*prefix_product[-1]
            prefix_product.append(result)

        suffix_product = [1]

        for num in reversed(nums[1:]): 
            result = num*suffix_product[-1]
            suffix_product.append(result)
        suffix_product = list(reversed(suffix_product))

        answer = []
        for i in range(len(prefix_product)): 
            result = prefix_product[i] * suffix_product[i]
            answer.append(result)

        return answer
        