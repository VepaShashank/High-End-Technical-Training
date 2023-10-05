#subset sum using backtracking
def is_subset_sum(nums, target_sum, current_sum, index):
    if current_sum == target_sum:
        return True

    if current_sum > target_sum or index == len(nums):
        return False

    if is_subset_sum(nums, target_sum, current_sum + nums[index], index + 1):
        return True

    if is_subset_sum(nums, target_sum, current_sum, index + 1):
        return True

    return False

def subset_sum(nums, target_sum):
    return is_subset_sum(nums, target_sum, 0, 0)

if __name__ == "__main__":
    Input = input("Enter a list of numbers separated by spaces: ")
    nums = [int(x) for x in Input.split()]
    target_sum = int(input("Enter the target sum: "))
    result = subset_sum(nums, target_sum)

    if result:
        print("Subset with the target sum exists.")
    else:
        print("No subset with the target sum found.")

