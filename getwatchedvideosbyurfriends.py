from collections import deque
class Solution:
 def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
    # BFS to find all people at exactly the given level
    visited = {id}
    queue = deque([id])
    current_level = 0

    while queue and current_level < level:
        for _ in range(len(queue)):
            person = queue.popleft()
            for friend in friends[person]:
                if friend not in visited:
                    visited.add(friend)
                    queue.append(friend)
        current_level += 1

    # count video frequencies from people at exactly this level
    freq = {}
    for person in queue:
        for video in watchedVideos[person]:
            freq[video] = freq.get(video, 0) + 1

    return sorted(freq.keys(), key=lambda v: (freq[v], v))