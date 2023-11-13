class Solution(object):
    def totalFruit(self,fruits):
        fruit_count = {}
        max_fruits = 0
        left = 0

        for i in range(len(fruits)):
            fruit_count[fruits[i]] = fruit_count.get(fruits[i], 0) + 1

            while len(fruit_count) > 2:
                fruit_count[fruits[left]] -= 1
                if fruit_count[fruits[left]] == 0:
                    del fruit_count[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, i - left + 1)

        return max_fruits
