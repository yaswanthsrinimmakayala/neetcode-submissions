class Twitter:

    def __init__(self):
        self.users={}
        self.time = 0
        self.posts = []
        heapq.heapify(self.posts)
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time+=1
        heapq.heappush(self.posts,(-self.time,userId,tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        n=10
        result = []
        remaining = []
        followers= []
        if userId in self.users:
            followers = list(self.users[userId])
            followers.append(userId)
        if not followers:
            followers = [userId]
        while n>0 and self.posts:
            tweet = heapq.heappop(self.posts)
            remaining.append(tweet)
            if tweet[1] in followers:
                result.append(tweet[2])
                n-=1
        for i in remaining:
            heapq.heappush(self.posts,i)

        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users.keys():
            self.users[followerId] = set()
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users.keys():
            self.users[followerId].discard(followeeId)