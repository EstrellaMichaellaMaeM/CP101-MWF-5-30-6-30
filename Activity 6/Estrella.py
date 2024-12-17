# Basic f-string formatting 
Attempt = input("My name is: ") 
attempt2 = input("I like to play: ")
print(f"I am !{Attempt}, My habit is playing {attempt2}. nice to meet you")

print("\n")
# using .format
Status = "Single"
years = 82
variable1 = "I am currently {} and I want to be healthy even I am {} years old".format( Status,years)
print(variable1)


print("\n")
# Legacy % formatting.
term = "beautiful"
years = 82
print("I am beautiful and %s right now; and I want to be beautiful if ever I will be %d years of age." % (term, years))
