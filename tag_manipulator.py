import re
class TagManipulator():    
    def parse_string(self, tags, regex=""):
        result = []

        tempResult = re.split( regex, tags )
        for e in tempResult:
            if (len(e) > 0):
                result.append(e.strip())

        return result