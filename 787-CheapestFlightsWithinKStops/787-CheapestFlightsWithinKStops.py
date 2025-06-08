# Last updated: 6/8/2025, 8:45:50 PM
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj=[[] for _ in range(n)]
        for i in flights:
            f,t,w=i
            adj[f].append([t,w])
        dist=[float('inf')]*n 
        dist[src]=0
        l=[[0,src,0]]
        while l:
            st,n,w=l.pop(0)
            if st>k:continue
            for i in adj[n]:
                if w+i[1]<dist[i[0]] and st<=k:
                    dist[i[0]]=w+i[1]
                    
                    l.append([st+1,i[0],dist[i[0]]])  
        
        if dist[dst]==float('inf'):
            return -1
        return dist[dst]                 