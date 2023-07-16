class Solution(object):
    def dividePlayers(self, skill):
        skill.sort()
        left=len(skill)-2
        right=1
        sum=skill[0]+skill[len(skill)-1]
        prod=skill[0]*skill[len(skill)-1]
        while(right<left):
            if skill[left]+skill[right]==sum:
                prod+=skill[left]*skill[right]
                right+=1
                left-=1
            else:
                return -1
        return prod


        
       