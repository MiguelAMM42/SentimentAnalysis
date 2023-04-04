import instaloader

# Create an instance of Instaloader class
L = instaloader.Instaloader()

# Get account by username
profile = instaloader.Profile.from_username(L.context, "sportingclubedeportugal")

# Print the number of followers
print("Number of followers:", profile.followers)
