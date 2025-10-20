def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        current_sum=sum(nums[:k])
        max_sum=current_sum

        for i in range(k,n):
            current_sum += nums[i]-nums[i-k]
            if current_sum>max_sum:
                max_sum=current_sum

        return max_sum/k
