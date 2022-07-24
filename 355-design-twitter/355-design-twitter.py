class Twitter:

    def __init__(self):
        self.tweets =defaultdict(list)
        self.following =defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append([self.time,tweetId])
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        recentTweets = [[-time,tweet] for [time,tweet] in self.tweets[userId]]
        for follow in self.following[userId]:
            recentTweets += [[-time,tweet] for [time,tweet] in self.tweets[follow]]
        heapq.heapify(recentTweets)
        n =10
        res = []
        while recentTweets and n:
            res.append(recentTweets[0][1])
            heapq.heappop(recentTweets)
            n-=1
        return res
   

    def follow(self, followerId: int, followeeId: int) -> None:
        if followeeId not in self.following[followerId]:
            self.following[followerId].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following: 
            self.following[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)