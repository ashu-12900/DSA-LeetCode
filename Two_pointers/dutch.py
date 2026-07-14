class Solution:
    def sortColors(self, nums: List[int]) -> None:
        arr=nums
        low=0
        mid=0
        high=len(arr)-1
        while mid<=high:
            if arr[mid]==0:
                a=arr[mid]
                arr[mid]=arr[low]
                arr[low]=a
                low+=1
                mid+=1
            elif arr[mid]==1:
                mid+=1
            elif arr[mid]==2:
                b=arr[mid]
                arr[mid]=arr[high]
                arr[high]=b
                high-=1
        