from collections import deque
class Solution(object):
    def averageOfLevels(self, root):
        if not root:
            return []
        ans=[]
        queue=deque([root])

        while queue:
            level=0
            level_size=len(queue)
            for _ in range(level_size):
                node=queue.popleft()
                level+=node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(level/float(level_size))
            
        return ans
        