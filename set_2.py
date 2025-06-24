'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   
    #find position of letter
    letter_count = 0  
    for char in alphabet: 
        if char == letter: 
            break 
        else: 
            letter_count = letter_count + 1
    
    final_position = (letter_count + shift) % 26 
    return alphabet[final_position]
    

def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_message = "" #make an empty string where the message will be added onto

    for char in message: 
        #if the character is a space, keep it as is
        if char == " ": 
            final_message = final_message + " " 
            continue 
            
        #if its not a space, shift each letter accordingly
        else: 
            letter_count = 0  
            for letter in alphabet: 
                if letter == char: 
                    break
                else: 
                    letter_count = letter_count + 1
    
        final_position = (letter_count + shift) % 26 
        final_char = alphabet[final_position]
        final_message = final_message + final_char
    
    return final_message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter == " ":
        return " "
    
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
   
    #find position of letter
    letter_count = 0  
    for char in alphabet: 
        if char == letter: 
            break
        else: 
            letter_count = letter_count + 1
   
    #find position of letter_shift
    letter_shift_count = 0  
    for char in alphabet: 
        if char == letter_shift: 
            break
        else: 
            letter_shift_count = letter_shift_count + 1
    
    final_position = (letter_count + letter_shift_count) % 26 
    final_char = alphabet[final_position]
    return final_char

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the key is extended to match the length of the message.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    final_message = ""
    
    key_count = 0 # to keep track of which letter in the key we're currently using
 
    for char in message:

        # if key_count equals len(key), reset the count to 0
        if key_count == len(key):
            key_count = 0
        key_letter = key[key_count]
       
        # if char is a space, we leave it as a space
        if char == " ":
            final_message = final_message + " "
            
        else:
           
            """ comments
                if char is not a space,
                    1. find key_shift or the position of each letter in the key
                    2. find char_position or the position of each char in the message
                    3. find final_position of the message by adding key_shift and char_position
                    4. find the final_char of the message given the final_position 
                    5. find final_message by adding final_message and final_char
            """

            # 1. 
            key_shift = 0
            for letter in alphabet:
                if letter == key_letter:
                    break
                key_shift = key_shift + 1
            
            # 2.
            char_position = 0
            for letter in alphabet:
                if letter == char:
                    break
                char_position = char_position + 1
            
            # 3.
            final_position = (char_position + key_shift) % 26

            # 4.
            final_char = alphabet[final_position]

            # 5.
            final_message = final_message + final_char

        
        # move on to the next key letter
        key_count = key_count + 1
    
    return final_message

def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    remainder = len(message) % shift
    
    if remainder != 0:
        new_message = message + ("_" * (shift - remainder))
    else:
        new_message = message


    encrypted_message = []
    total_col = len(new_message) // shift 

    for i in range(len(new_message)):
        row = i // shift # the row where i is in
        col = i % shift # the column i is in
        
        source_position = row + (total_col * col)
        encrypted_char = new_message[source_position]
        encrypted_message.append(encrypted_char)
    
    return ''.join(encrypted_message) # join together without spaces

def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    decrypted_message = []
    total_col = len(message) // shift

    #do the reverse or switch shift with total_col
    for i in range(len(message)):
        row = i // total_col #col
        col = i % total_col #row
        
        source_pos = row + (col * shift)
        decrypted_char = message[source_pos]
        decrypted_message.append(decrypted_char)
    
    return ''.join(decrypted_message)  