class Solution:
    def kidsWithCandies(self, candies: [int], extraCandies: int) -> [bool]:
        # Find the maximum number of candies any child currently has
        max_candies = max(candies)

        # Determine if each child can have the greatest number of candies
        result = [candy + extraCandies >= max_candies for candy in candies]

        return result


# Example usage:
solution = Solution()
candies = [2, 3, 5, 1, 3]
extraCandies = 3
print(solution.kidsWithCandies(candies, extraCandies))
