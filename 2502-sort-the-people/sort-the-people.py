class Solution(object):
    def sortPeople(self, names, heights):
        people = {}
        for i in range(len(names)):
            people[heights[i]] = names[i]
        sorted_heights = sorted(people.keys(), reverse=True)
        sorted_names = [people[height] for height in sorted_heights]
        return sorted_names

            