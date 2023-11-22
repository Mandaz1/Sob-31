# A time traveler has suddenly appeared in your classroom!

# Create a variable representing the traveler's
# year of origin (e.g., year = 2000)
# and greet our strange visitor with a different message
# if he is from the distant past (before 1900),
# the present era (1900-2020) or from the far future (beyond 2020).

year = int(input("Greetings! What is your year of origin? ")) #removed =, and changed int.input to int(input, also changed ' at the end to " by muhammad bagosher

if year <= 1900: #added : by muhammad bagosher
    print ('Woah, thats the past!') #removed ' in the middle of the print statement by muhammad bagosher
elif year > 1900 and year < 2020: #changed && to and by muhammad bagosher
    print ("That's totally the present!")
else: #changed elif to else by muhammad bagosher
    print ("Far out, that's the future!!")
