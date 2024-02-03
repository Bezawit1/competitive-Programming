class Solution(object):
    def defangIPaddr(self, address):
       defang = address.replace(".","[.]")
       return defang
        
        