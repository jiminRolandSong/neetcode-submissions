from collections import defaultdict
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.posts = defaultdict(list)
        self.time = 1
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.posts[userId].append([-self.time, tweetId])


    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []

        for p in self.posts[userId]:
            feed.append(p)
        
        for ui in self.following[userId]:
            for p in self.posts[ui]:
                feed.append(p)
        
        heapq.heapify(feed)

        heap = []

        while feed and len(heap) < 10:
            time, ti = heapq.heappop(feed)
            heap.append(ti)
        
        return heap
                

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
        
