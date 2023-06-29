class Solution(object):
    def findDuplicate(self, paths):
        fileCont= defaultdict(list)
        for i in paths:
            files =i.split(' ')
            filePath=files[0]
            for j in files[1:]:
                fileName,fileContent = j.split('(')
                fileCont[fileContent[:-1]].append(filePath + '/'+fileName)
        return [fileCont[fileContent] for fileContent in fileCont if len(fileCont    [fileContent]) > 1]
