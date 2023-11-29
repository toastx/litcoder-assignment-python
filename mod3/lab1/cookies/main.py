def min_steps_to_target_sweetness(target_sweetness, candies):
    candies.sort()
    steps = 0

    while candies[0] < target_sweetness:
        least_sweet = candies.pop(0)
        second_least_sweet = candies.pop(0)
        new_candy = least_sweet + 2 * second_least_sweet
        candies.insert(0, new_candy)
        candies.sort() 
        steps += 1

    return steps

# Example usage:
target_sweetness1 = 7
candies1 = [1, 2, 3, 4, 5]
result1 = min_steps_to_target_sweetness(target_sweetness1, candies1)
print(result1)  # Output: 3

target_sweetness2 = 11
candies2 = [2, 5, 3, 7, 6, 1]
result2 = min_steps_to_target_sweetness(target_sweetness2, candies2)
print(result2)  # Output: 4