class Solution(object):
    def compareVersion(self, version1, version2):
        version1Array = version1.split(".")
        version2Array = version2.split(".")
        if len(version1Array) > len(version2Array):
            while len(version2Array) < len(version1Array):
                  version2Array.append("0")
        if len(version1Array) < len(version2Array):
            while len(version1Array) < len(version2Array):
                  version1Array.append("0")
        i = 0
        j = 0
        print(version1Array , version2Array)
        while i < len(version1Array) and j < len(version2Array):
            if int(version1Array[i]) > int(version2Array[j]):
                return 1
            elif int(version1Array[i] )< int(version2Array[j]):
                return -1
            i+=1
            j+=1
        return 0
   
       
        