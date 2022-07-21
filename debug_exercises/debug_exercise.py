

# greeting = input("Hello, possible pirate! What's the password?")
# if greeting in "Arrr!":
#	print("Go away, pirate.")
# else:
#	print("Greetings, hater of pirates!")

# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

# authors = {
#    "Charles Dickens": "1870",
#    "William Thackeray": "1863",
#    "Anthony Trollope": "1882",
#    "Gerard Manley Hopkins": "1889"}

# for author, date in authors.items():
#	date = int(date)
#	print("%s" % author + " died in " + "%d." % date)


# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print ("Woah, that's the past!")
elif year > 1900 & year < 2020:
    print ("That's totally the present!")
else:
    print ("Far out, that's the future!!")
