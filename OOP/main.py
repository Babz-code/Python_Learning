class User:

    def __init__(self, id_tag, user_tag):
        self.id = id_tag
        self.username = user_tag
        self.followers = 0
        self.following = 0

    def follow(self, more_user):
        more_user.followers += 1
        self.following += 1





user_1 = User("chi", "chinnybabz")
user_2 = User("toyo", "babzie")
print(user_2)
user_1.follow(user_2)
print(user_1.followers)
print(user_2.followers)
print(user_1.following)
print(user_2.following)
print("I added this new line of code to test out git branch")