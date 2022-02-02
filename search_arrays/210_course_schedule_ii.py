import collections

class Solution(object):

    def findOrder(self, numCourses, prerequisites):
        courses = collections.defaultdict(set)
        pres = collections.defaultdict(set)
        res = []
        for course, pre in prerequisites:
            courses[course].add(pre)
            pres[pre].add(course)
        stack=[n for n in range(numCourses) if not courses[n]]
        count = 0
        while stack:
            no_pre = stack.pop()
            res.append(no_pre)
            count+=1
            for course in pres[no_pre]:
                courses[course].remove(no_pre)
                if not courses[course]:
                    stack.append(course)
        return res if count==numCourses else []


if __name__ == '__main__':

    numCourses = 4; prerequisites = [[1,0],[2,0],[3,1],[3,2]]

    ss = Solution()
    res = ss.findOrder(numCourses, prerequisites)

    print(res)
