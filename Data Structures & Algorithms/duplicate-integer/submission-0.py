class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        Understand:
            inputs: list of ints
            outputs: boolean - return true if list has duplicates, else false


        P:

        I:

        """
        
        nums.sort()

        for i in range(len(nums)):
            if i == 0:
                continue
                
            previous = nums[i-1]
            current = nums[i]

            if previous==current:
                return True
        
        return False


        # seen = []
        # for num in nums:
        #     if num in seen:
        #         return true
            
        # return false