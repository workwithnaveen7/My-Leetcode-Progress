# Last updated: 6/7/2025, 2:16:20 PM
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        indegree=[0]*numCourses
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course]+=1
        queue=deque([i for i in range(numCourses) if indegree[i] == 0])
        order=[]
        while queue:
            curr=queue.popleft()
            order.append(curr)
            for neighbor in graph[curr]:
                indegree[neighbor]-=1
                if indegree[neighbor]==0:
                    queue.append(neighbor)
        return order if len(order)==numCourses else []
