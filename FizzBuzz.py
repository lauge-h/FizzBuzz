"""
FizzBuzz, made by Lauge Heiberg. No rights reserved.
The idea is to have a list of items set at the start, making it more modular.
"""

endValue = 100

itemList = {
    "Fizz": 3,
    "Buzz": 5
}

# Counter - from 1 to endValue
for count in range(1, endValue+1):
    # Initialize string - will have either fizz or buzz concatinated onto it
    stringOnCount = ""
    # Loop through the dict itemList
    for key, value in itemList.items():
        # If current count is divisible by key, add it to stringOnCount
        if count % value == 0:
            stringOnCount = stringOnCount + key
    # Print stringOnCount, if that's empty, print count
    if stringOnCount:
        print(stringOnCount)
    else:
        print(count)