class User:

    def __init__ (self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1
        

user_1 = User("1","shreya")
user_2 = User("2","suraj")
user_3 = User("3","anil")

user_1.follow(user_2)
user_3.follow(user_2)
user_2.follow(user_2)
print("User 1")
print(user_1.followers)
print(user_1.following)
print("User 2")
print(user_2.followers)
print(user_2.following)
print("User 3")
print(user_3.followers)
print(user_3.following)
