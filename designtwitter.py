from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)       # userId -> [(time, tweetId)]
        self.following = defaultdict(set)     # userId -> set of followeeIds

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        # collect all relevant users
        users = self.following[userId] | {userId}

        # max heap: push last tweet of each user, expand as needed
        heap = []
        for uid in users:
            if self.tweets[uid]:
                idx = len(self.tweets[uid]) - 1
                t, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-t, tid, uid, idx))

        feed = []
        while heap and len(feed) < 10:
            t, tid, uid, idx = heapq.heappop(heap)
            feed.append(tid)
            if idx > 0:
                idx -= 1
                nt, ntid = self.tweets[uid][idx]
                heapq.heappush(heap, (-nt, ntid, uid, idx))

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)