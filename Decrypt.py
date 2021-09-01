# Check Validation:
def checkDecryptedTextLength(decrypted_text, input_text):
    return decrypted_text == len(input_text)

# Methods:
def Route_Cipher_Decrypt(input_string, key, clock_wise):
    while len(input_string) % key != 0:
        input_string += "X"

    jagged_array = [[""] * key for i in range(len(input_string) // key)]
    index = 0

    # This variable help us to solve the main for loop issue when we have an odd number. For example:
    # if we have key=6 then: 6 % 2 = 3. but if we have 5 % 2 = 2. this difference between the two num can lead to a bug
    # in the program because we could get out of the loop before filling the cipher text proply.
    lenCalc = 0
    if key % 2 != 0:
        lenCalc = 1

    #  ############# CLOCK WISE #############
    if clock_wise:
        i = 0
        while i < key // 2 + lenCalc:
            # DOWN
            j = i
            while j <= len(jagged_array) - i - 1:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array]).strip('X')

                jagged_array[j][key - i - 1] = input_string[index]
                j += 1
                index += 1

            # LEFT
            j = key - i - 2
            while j >= i:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array]).strip('X')
                jagged_array[len(jagged_array) - i - 1][j] = input_string[index]
                j -= 1
                index += 1

            # UP
            j = len(jagged_array) - i - 2
            while j >= 0 + i:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array]).strip('X')
                jagged_array[j][i] = input_string[index]
                j -= 1
                index += 1

            # RIGHT
            j = i + 1
            while j <= key - i - 2:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array]).strip('X')
                jagged_array[i][j] = input_string[index]
                j += 1
                index += 1

            i += 1
        # we return .join().join() twice because of array.
        return ''.join([''.join(x) for x in jagged_array]).strip('X')

    #  ############# ANTI CLOCK WISE #############
    else:
        i = 0
        while i < key // 2 + lenCalc:
            # Left
            j = key - i - 1
            while j >= i:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array])
                jagged_array[i][j] = input_string[index]
                index += 1
                j -= 1

            # DOWN
            j = i + 1
            while j <= len(jagged_array) - i - 1:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array])
                jagged_array[j][i] = input_string[index]
                index += 1
                j += 1

            # RIGHT
            j = i + 1
            while j <= key - i - 1:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array])
                jagged_array[len(jagged_array) - i - 1][j] = input_string[index]
                index += 1
                j += 1

            # UP
            j = len(jagged_array) - i - 2
            while j > i:
                if checkDecryptedTextLength(index, input_string):
                    return ''.join([''.join(x) for x in jagged_array])
                jagged_array[j][key - i - 1] = input_string[index]
                index += 1
                j -= 1

            i += 1
    return ''.join([''.join(x) for x in jagged_array])

# #################### Decrypt #################### #

text = input("Enter a text to decrypt: ")
key = int(input("Enter a key: "))
clock_wise = input("Clockwise or anticlockwise : yes/no ")
if clock_wise == "yes":
    clock_wise = True
if clock_wise == "no":
    clock_wise = False
print(Route_Cipher_Decrypt(text, key, clock_wise))
