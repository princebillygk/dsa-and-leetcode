# Created by princebillygk at 2023/08/10 06:18
# leetgo: dev
# https://leetcode.com/problems/design-twitter/

from typing import *
from leetgo_py import *

# @lc code=begin


class Tweet:
    def __init__(self, userId, tweetId):
        self.userId = userId
        self.tweetId = tweetId


class Twitter:
    tweets: list[Tweet]
    follows: dict[int, set[int]]

    def __init__(self):
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(Tweet(userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets: list[int] = []
        followees = self.follows[userId]

        for i in range(len(self.tweets) - 1, 0, -1):
            tweet = self.tweets[i]
            if tweet.userId in followees or tweet.userId == userId:
                tweets.append(tweetId)

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows:
            self.follows[followerId].add(followeeId)
        else:
            self.follows[followerId] = set([followeeId])

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].remove(followeeId)


if __name__ == "__main__":
    ops: List[str] = deserialize("List[str]", read_line())
    params = split_array(read_line())
    output = ["null"]

    obj = Twitter()

    for i in range(1, len(ops)):
        match ops[i]:
            case "postTweet":
                method_params = split_array(params[i])
                userId: int = deserialize("int", method_params[0])
                tweetId: int = deserialize("int", method_params[1])
                obj.postTweet(userId, tweetId)
                output.append("null")
            case "getNewsFeed":
                method_params = split_array(params[i])
                userId: int = deserialize("int", method_params[0])
                ans = serialize(obj.getNewsFeed(userId))
                output.append(ans)
            case "follow":
                method_params = split_array(params[i])
                followerId: int = deserialize("int", method_params[0])
                followeeId: int = deserialize("int", method_params[1])
                obj.follow(followerId, followeeId)
                output.append("null")
            case "unfollow":
                method_params = split_array(params[i])
                followerId: int = deserialize("int", method_params[0])
                followeeId: int = deserialize("int", method_params[1])
                obj.unfollow(followerId, followeeId)
                output.append("null")

    print("\noutput:", join_array(output))
