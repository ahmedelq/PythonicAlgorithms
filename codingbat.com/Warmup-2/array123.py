def array123(nums):
  for i in range(len(nums) - 2):
    if [1,2,3] == nums[i:i + 3]:
      return True
  return False