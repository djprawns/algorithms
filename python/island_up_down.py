class Solution(object):
    
    def dfs(self, grid, i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
            return
        
        grid[i][j] = '#'
        
        self.dfs(grid, i+1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j-1)
        
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        counter = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    counter += 1
        return counter

# from collections import deque 

# class Solution(object):
        
#     def find_neighbouring_ones(self, grid, i, j, visited_map, queue, row_len, col_len):
#         visited_map[str(i)+str(j)] = True
#         try:
#             new_i = i
#             new_i_str = str(new_i)
#             new_j = j+1
#             new_j_str = str(new_j)
#             if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len and not visited_map.get(new_i_str + new_j_str, None):
#                 if int(grid[new_i][new_j]):
#                     visited_map, queue = self.find_neighbouring_ones(grid, new_i, new_j, visited_map, queue, row_len, col_len)
#                 else:
#                     visited_map[new_i_str+new_j_str] = True
#                     queue.append((new_i, new_j))
#         except:
#             pass
#         try:
#             new_i = i+1
#             new_i_str = str(new_i)
#             new_j = j
#             new_j_str = str(new_j)
#             if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len and not visited_map.get(new_i_str + new_j_str, None):
#                 if int(grid[new_i][new_j]):
#                     visited_map, queue = self.find_neighbouring_ones(grid, new_i, new_j, visited_map, queue, row_len, col_len)
#                 else:
#                     visited_map[new_i_str+new_j_str] = True
#                     queue.append((new_i, new_j))
#         except:
#             pass
#         try:
#             new_i = i-1
#             new_i_str = str(new_i)
#             new_j = j
#             new_j_str = str(new_j)
#             if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len and not visited_map.get(new_i_str + new_j_str, None):
#                 if int(grid[new_i][new_j]):
#                     visited_map, queue = self.find_neighbouring_ones(grid, new_i, new_j, visited_map, queue, row_len, col_len)
#                 else:
#                     visited_map[new_i_str+new_j_str] = True
#                     queue.append((new_i, new_j))
#         except:
#             pass
#         try:
#             new_i = i
#             new_i_str = str(new_i)
#             new_j = j-1
#             new_j_str = str(new_j)
#             if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len and not visited_map.get(new_i_str + new_j_str, None):
#                 if int(grid[new_i][new_j]):
#                     visited_map, queue = self.find_neighbouring_ones(grid, new_i, new_j, visited_map, queue, row_len, col_len)
#                 else:
#                     visited_map[new_i_str+new_j_str] = True
#                     queue.append((new_i, new_j))
#         except:
#             pass
#         return visited_map, queue
    
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
#         # queue will have only zero elements
#         visited_map = {}
#         queue = deque([])
#         queue.append((0,0))
#         count = 0
#         if not grid:
#             return 0
#         row_len = len(grid)
#         col_len = len(grid[0])
#         while queue:
#             i, j = queue.popleft()
#             if int(grid[i][j]):
#                 # count 1s here
#                 if not visited_map.get(str(i)+str(j), None):
#                     visited_map, queue = self.find_neighbouring_ones(grid, int(i), int(j), visited_map, queue, row_len, col_len)
#                     count += 1
#             else:   
#                 new_i = i+1
#                 new_j = j
#                 if not visited_map.get(str(new_i)+str(new_j), None):
#                     if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len:
#                         if not grid[new_i][new_j]:
#                             visited_map[str(new_i)+str(new_j)] = True
#                             queue.append((new_i, new_j))
#                         else:
#                             queue.append((new_i, new_j))
#                 new_i = i
#                 new_j = j+1
#                 if not visited_map.get(str(new_i)+str(new_j), None):
#                     if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len:
#                         if not grid[new_i][new_j]:
#                             visited_map[str(new_i)+str(new_j)] = True
#                             queue.append((new_i, new_j))
#                         else:
#                             queue.append((new_i, new_j))
#                 new_i = i-1
#                 new_j = j
#                 if not visited_map.get(str(new_i)+str(new_j), None):
#                     if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len:
#                         if not grid[new_i][new_j]:
#                             visited_map[str(new_i)+str(new_j)] = True
#                             queue.append((new_i, new_j))
#                         else:
#                             queue.append((new_i, new_j))
#                 new_i = i
#                 new_j = j-1
#                 if not visited_map.get(str(new_i)+str(new_j), None):
#                     if new_i >=0 and new_i<row_len and new_j>=0 and new_j<col_len:
#                         if not grid[new_i][new_j]:
#                             visited_map[str(new_i)+str(new_j)] = True
#                             queue.append((new_i, new_j))
#                         else:
#                             queue.append((new_i, new_j))
#         return count