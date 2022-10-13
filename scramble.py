def scramble(input_string, key, extra):
    key_sum=0
    for character in key:
        key_sum += ord(character)
    if key_sum%2 == 0:
        key_sum=int(key_sum/2)
    elif key_sum%3 == 0:
        key_sum=int(key_sum/3)

    scrambled_character_list=[]
    for character in input_string:
        new_character = chr(ord(character)+key_sum)
        scrambled_character_list.append(chr(ord(character)+key_sum))
    scramble_string = "".join(scrambled_character_list)
    print(f'{extra} = "{scramble_string}"\n')

def unscramble(input_string, key):
    key_sum=0
    for character in key:
        key_sum += ord(character)
    if key_sum%2 == 0:
        key_sum=int(key_sum/2)
    elif key_sum%3 == 0:
        key_sum=int(key_sum/3)

    unscrambled_character_list=[]
    for character in input_string:
        new_character = chr(ord(character)+key_sum)
        unscrambled_character_list.append(chr(ord(character)-key_sum))
    unscramble_string = "".join(unscrambled_character_list)
    print(unscramble_string)
