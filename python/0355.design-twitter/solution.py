# Created by princebillygk at 2023/08/10 06:18
# leetgo: dev
# https://leetcode.com/problems/design-twitter/
# TODO: Solve this using max heap

from typing import *
from leetgo_py import *

# @lc code=begin


class Tweet:
    def __init__(self, userId: int, tweetId: int):
        self.userId = userId
        self.tweetId = tweetId

    # def __str__(self):
    #     return f'User {self.userId} posted tweet {self.tweetId}'

    # def __repr__(self):
    #     return f'User {self.userId} posted tweet {self.tweetId}'


class Twitter:
    tweets: list[Tweet]
    follows: dict[int, set[int]]

    def __init__(self):
        self.tweets = []
        self.follows = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append(Tweet(userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        # print(self.tweets, self.follows, userId, sep="|")

        tweets: list[int] = []
        followees = self.follows.get(userId) or set([])

        counter = 0
        for i in range(len(self.tweets) - 1, -1, -1):
            if counter > 9:
                break
            tweet = self.tweets[i]
            if tweet.userId in followees or tweet.userId == userId:
                tweets.append(tweet.tweetId)
                counter += 1
        # print("Result:", tweets)
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
