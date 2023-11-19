from data import *

print("1. ", element["description"])  # {} , because it's an empty dictionary
print(
    "2. ", "description" in element
)  # True, because the dict exists regardless it's content
print(
    "3. ", not element["description"]
)  # True, because an empty dict exists anyway, regardless it's content
print(
    "4. ", not not element["description"]
)  # False, because converting back an empty dict returns False if it's empty
print(
    "5. ", bool(element["description"])
)  # False, because Python evaluates an empty dict as false when converted to boolean
print("6. ", "class" in element)  # False, because class doesn't exist inside element
# Lists
print("7. ", "content" in element)  # True
