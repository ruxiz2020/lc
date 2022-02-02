import collections

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        '''
        Time Complexity: O(E+V) where V is the number of courses, and E is the number of dependencies.
        '''
        courses = collections.defaultdict(set)
        pres = collections.defaultdict(set)
        for course, pre in prerequisites:
            courses[course].add(pre)
            pres[pre].add(course)

        no_pre_courses = [n for n in range(numCourses) if not courses[n]]
        count = 0
        while no_pre_courses:
            print(no_pre_courses)
            no_pre = no_pre_courses.pop()
            count+=1
            for course in pres[no_pre]:
                courses[course].remove(no_pre)
                if not courses[course]:
                    no_pre_courses.append(course)
        print(count)
        return count == numCourses


if __name__ == '__main__':

    numCourses = 2; prerequisites = [[1,0], [2,1]]

    ss = Solution()
    res = ss.canFinish(numCourses, prerequisites)

    print(res)
