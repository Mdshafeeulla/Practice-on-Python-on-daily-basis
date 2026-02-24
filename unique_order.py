# Take a list with duplicate elements and return a list of only the
# unique elements while maintaining the original order.

def unique_elements(elem):
    seen = set()
    unique = []
    for word in elem:
        if word not in seen:
            seen.add(word)
            unique.append(word)
    print(unique)

unique_elements(["Shafi","Ulla","Shafi","Shafee"])

