class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        combined_list = nums1 + nums2
        combined_list.sort()
        total_elements_number = len(combined_list)

        #Calculate the median for odd lists(total)
        if total_elements_number % 2 != 0:
            mid_element_index = total_elements_number // 2 + 1
            return combined_list[mid_element_index-1]
        
        #Calculate the median for even lists(total)
        initial_mid_element_index = total_elements_number // 2 
        final_mid_element_index = initial_mid_element_index + 1
        median = (combined_list[initial_mid_element_index-1] + combined_list[final_mid_element_index-1]) / 2
        return median


nums1 = [1,2]
nums2 = [3,4]

test = Solution()
test.findMedianSortedArrays(nums1, nums2)