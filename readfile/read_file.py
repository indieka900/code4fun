def decode(message_file):
    # Read the message file
    with open(message_file, 'r') as file:
        lines = file.readlines()

    # Split each line into the number and the word
    data = [line.strip().split() for line in lines]
    data = [(int(num), word) for num, word in data]

    # Sort the data by the numbers
    data.sort(key=lambda x: x[0])

    # Find the numbers that represent the end of each line in the "pyramid"
    pyramid_ends = []
    current_sum = 0
    for i in range(1, len(data) + 1):
        current_sum += i
        if current_sum > len(data):
            pyramid_ends.append(current_sum - i)
            break
        pyramid_ends.append(current_sum)

    # Extract the words corresponding to the pyramid end numbers
    message_words = [data[num - 1][1] for num in pyramid_ends]

    # Join the message words into a string
    decoded_message = ' '.join(message_words)

    return decoded_message

# decoded_message = decode('C:\\Users\\omuya\\code4fun\\readfile\\input_file.txt')

decoded_message = decode('input_file.txt')
print(decoded_message)