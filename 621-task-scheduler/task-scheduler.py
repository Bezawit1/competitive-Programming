class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequent_tasks = Counter(tasks)
        print(frequent_tasks)
        most_frequent = max(frequent_tasks.values())
        print(most_frequent)
        counter = 0
        for i in frequent_tasks.values():
            if i == most_frequent :
                counter = counter + 1
                print(i , counter)

        cool_time = (most_frequent - 1) * (n + 1) + counter
        print(cool_time)
        return max(cool_time, len(tasks))