print("AVERAGE SNAIL SPEED 🐌\n")
days = int(input())

print("❔How long can a snail go:")

counter = 0
distance = 43

while counter < days:
    counter += 1
    distance *= 2
    print("In " + str(counter) + " days | " + str(distance) + " meters")

print("\n🗨️The snail's speed varies depending on its species and environmental conditions.  On average, snails can crawl about 0.03 meters per minute.  In an hour this is only 1.8 meters, and in a day - approximately 43.2 meters.  Snails live approximately 2 to 7 years, depending on the species.")    