def counter(input_string):
    words = input_string.split()
    counter = {}
    for word in words:
        word = word.lower()
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    print(counter)

counter("apple banana apple orange banana apple")