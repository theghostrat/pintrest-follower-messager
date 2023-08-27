import json
from pinterest_api import PinterestAPI

username = 'your_username'
password = 'your_password'

followers_file = 'followers.json'

with open(followers_file, 'r') as file:
    followers_data = json.load(file)

api = PinterestAPI(username, password)
followers = api.get_followers()
# Message to be sent
message = "Hello! This is a test message from the Pinterest bot."

for follower in followers:
    if follower['username'] in followers_data['username']:
      continue
    api.send_message(follower['username'], message)
    with open(followers_file, 'w') as file:
      new_follower = {'username': follower['username']}
      followers_data.append(new_follower)
      json.dump(followers_data, file, indent=4)


print("Messages sent successfully!")
