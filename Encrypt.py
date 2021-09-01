# Check Validation:
def checkEncryptedTextLength(encrepted_text, input_text):
    return len(encrepted_text) == len(input_text)

# Methods:
def Route_Cipher_Encrypt(input_string, key, clock_wise):
    # Here we add X (character) to the input_text variable if the the text % key will result a decimal number. example:
    # 24 % 6 = 0 <-- so we don't add 'X'
    # 25 % 6 = 1 <-- so we add  'X' to the input string. we keep adding until we reach a number like 30 % 6 <- Whole num
    while len(input_string) % key != 0:
        input_string += "X"

    jagged_array = [[""] * key for i in range(len(input_string) // key)]
    index = 0
    # Filling the text in the jagged array
    for i in range(len(jagged_array)):
        for j in range(key):
            jagged_array[i][j] = input_string[index]
            index += 1

    # This variable help us to solve the main for loop issue when we have an odd number. For example:
    # if we have key=6 then: 6 % 2 = 3. but if we have 5 % 2 = 2. this difference between the two num can lead to a bug
    # in the program because we could get out of the loop before filling the cipher text proply.
    lenCalc = 0
    if key % 2 != 0:
        lenCalc = 1

    encrypted_text = ""
# ############# CLOCK WISE #############
    if clock_wise:
        i = 0
        while i < key // 2 + lenCalc:
            # DOWN
            j = i
            while j <= len(jagged_array) - i - 1:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text.strip('X')
                encrypted_text += jagged_array[j][key - i - 1]
                j += 1

            # LEFT
            j = key - 2 - i
            while j >= i:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text.strip('X')
                encrypted_text += jagged_array[len(jagged_array) - i - 1][j]
                j -= 1

            # UP
            j = len(jagged_array) - 2 - i
            while j >=  i:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text.strip('X')
                encrypted_text += jagged_array[j][i]
                j -= 1

            # RIGHT
            j = i + 1
            while j <= key - 2 - i:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text.strip('X')
                encrypted_text += jagged_array[i][j]
                j += 1

            i += 1
        return encrypted_text
    #  ############# ANTI CLOCK WISE #############
    else:
        i = 0
        while i < key // 2 + lenCalc:
            # Left
            j = key - i - 1
            while j >= i:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text
                encrypted_text += jagged_array[i][j]
                j -= 1

            # DOWN
            j = i+1
            while j <= len(jagged_array) - i - 1:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text
                encrypted_text += jagged_array[j][i]
                j += 1

            # RIGHT
            j = i + 1
            while j <= key - i - 1:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text
                encrypted_text += jagged_array[len(jagged_array) - i - 1][j]
                j += 1

            # UP
            j = len(jagged_array) - i - 2
            while j > i:
                if checkEncryptedTextLength(encrypted_text, input_string):
                    return encrypted_text
                encrypted_text += jagged_array[j][key - i - 1]
                j -= 1

            i += 1
    return encrypted_text

# #################### Encrypt #################### #


text1 = input("Enter a text to encrypt: ")
text1 = text1.upper()
key = int(input("Enter a key: "))
clock_wise = input("Clockwise or anticlockwise : yes/no ")
if clock_wise == "yes":
    clock_wise = True
if clock_wise == "no":
    clock_wise = False
cipher_text = print(Route_Cipher_Encrypt(text1, key, clock_wise))
