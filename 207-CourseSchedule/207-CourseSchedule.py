# Last updated: 6/7/2025, 2:41:25 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph =defaultdict(list)
        indegree=[0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        queue=deque([i for i in range(numCourses) if indegree[i]==0])
        completed=0
        while queue:
            curr=queue.popleft()
            completed+=1
            for neighbor in graph[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)

        return completed==numCourses
