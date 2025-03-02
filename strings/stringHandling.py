# Autor: Jose Lopez Li
# Practice String Handling in python

import random

def switchEvenPositionsWithNextOne(text: str) -> str:
    text_list = list(text) # convert string to a list (muteable)

    for i in range(0, len(text)-1, 2): # iterate over even numbers range(start, stop, step)
        text_list[i], text_list[i + 1] = text_list[i + 1], text_list[i] #swap characters. There is not lost information here, because the execution in one step (it works in python)

    return "".join(text_list)

def reversetheString(text: str) ->str:
    text_list = list(text)
    text_size = int((len(text)))

    for i in range(0, int(text_size / 2)):
        text_list[i], text_list[text_size - i - 1] = text_list[text_size - i -1], text_list[i]
        #print("Swicth number: {}".format(i))
    
    return "".join(text_list)

def checkIfAStringIsAPalindrome(text: str)->bool:
    reverse = reversetheString(text)

    return True if reverse == text else False

def checkIfAStringIsAPalindromeOP(text: str) -> bool:
    return text == text[::-1]  # Compara el texto con su versión invertida


def removeVowels(text: str) -> str:
    vowels_list = list("aeiou")
    text_list = list(text)
    for vowel in vowels_list:
        text_list = [item for item in text_list if item != vowel]
    return "".join(text_list)

def removeVowelsOP(text: str) -> str:
    vowels = {"a", "e", "i", "o", "u"}  # Use a set for fast lookup
    return "".join([char for char in text if char not in vowels])

def countOccurrencesofEachCharacter(text: str)->dict:
    occur = {}
    for char in text:
        if char not in occur:
            occur[char] = 0
        occur[char] += 1
    return occur

def countOccurrencesofEachCharacterOP(text: str) -> dict:
    occur = {}
    for char in text:
        occur[char] = occur.get(char, 0) + 1  # Use `get()` to handle missing keys
    return occur


def findtheFirstNonRepeatingCharacter(text: str)-> str:
    text_list = list(text)
    count = 0
    for char in text_list:
        for each in text_list:
            if (char == each):
                count += 1
            if (count >= 2): # to save for cycles
                count = 0
                break
        if (count == 1):
            return char

def findtheFirstNonRepeatingCharacterOP(text: str)-> str:
    count_dict = countOccurrencesofEachCharacterOP(text)

    for char in text:
        if count_dict[char] == 1:
            return char
    
    return ""


def swap_first_last(text: str) -> str:
    if len(text) < 2:
        return text  # Retorna la misma cadena si tiene 1 o 0 caracteres
    
    return text[-1] + text[1:-1] + text[0]


def removeDuplicateCharacters(text: str) -> str:
    single_chars = {}

    for char in text:
        single_chars[char] = single_chars.get(char, 0) + 1

    for char in list(single_chars.keys()):
        if single_chars[char] > 1:
            del single_chars[char]
    
    return("".join(str(value) for value in single_chars.keys()))


def insertACharacterAtEveryNPositions(text: str, N: int) -> int:
    return "-".join(text[n:(n + N)] for n in range(0, len(text), N))

def shiftCharactersToTheRight(text: str, N: int)->str:
    
    for n in range(0, N):
        text = text[len(text)-1:] + text[:len(text)-1]
    return text

def shiftCharactersToTheRightOP(text: str, N: int) -> str:
    if not text:
        return text  # Evita errores con strings vacíos
    N = N % len(text)  # Optimización para evitar ciclos innecesarios
    return text[-N:] + text[:-N]  # Desplazamiento en una sola línea 


def shiftCharactersToTheLeftOP(text: str, N: int) -> str:
    if not text:
        return text 
    N = N % len(text)
    return text[N:] + text[:N]

def removeAspecificcharacter(text: str, remove: str) -> str:
    return "".join(char for char in text if char != remove)

def replaceACharacterWithAnother(text: str, l1: str, l2: str) -> str:
    return "".join(l2 if char == l1 else char for char in text)

def repeatNTimesEachLetterInTheString(text: str, N: int) -> str:
    return "".join(char * N for char in text)

def convertEachLetterToItsASCIICode(text: str):
    text_list = list(text)
    return_list = []
    for char in text_list:
        return_list.append(ord(char))
    return return_list

def convertEachLetterToItsASCIICodeOP(text: str) -> list:
    return [ord(char) for char in text]


def rearrangeTheLettersInARandomOrder(text: str) -> str:
    text_list = list(text)
    for char in text_list:
        rand1 = random.randint(0, len(text) - 1)
        rand2 = random.randint(0, len(text) - 1)
        text_list[rand1], text_list[rand2] = text_list[rand2], text_list[rand1]
    return "".join(text_list)

def rearrangeTheLettersInARandomOrderOP(text: str) -> str:
    text_list = list(text)
    random.shuffle(text_list)  # Shuffle the list randomly
    return "".join(text_list)

def removeAllConsonants(text: str) -> str:
    text_list = list(text)
    vowels = {"a", "e", "o", "u", "i"}

    return "".join(char for char in text_list if char in vowels)

def capitalizeEveryOtherLetter(text: str) -> str:
    return "".join(text[n].upper() if n % 2 == 0 else text[n] for n in range(len(text)))

def removeDuplicateCharacters(text: str) -> str:
    occurs = {}

    for char in text:
        occurs[char] = occurs.get(char, 0) + 1
    
    return "".join(k for k, v in occurs.items())

def removeDuplicateCharactersOP(text: str) -> str:
    occurs = set()  # Usamos un set para hacer un seguimiento de los caracteres ya vistos

    result = []
    for char in text:
        if char not in occurs:  # Solo añadimos el carácter si no ha sido visto antes
            occurs.add(char)
            result.append(char)
    
    return "".join(result)


print("============== Swap Even Positions with Next One ==============")
# input str = "abcdfghi"
# output str = "badcgfih"
text = "abcdfghi"
print("{} -> {}".format(text, switchEvenPositionsWithNextOne(text)))
print("".join(text[n:n+2][::-1] for n in range(0, len(text), 2)))  # 1032547698
print("-".join(text[n:n+2][::-1] for n in range(0, len(text), 2))) # 10-32-54-76-98

print("============== Reverse the String ==============")
# input str = "abcdfghi"
# output str = "ihgfdcba"
text = "abcdfghi"
print("{} -> {}".format(text, reversetheString(text)))
print("{} -> {}".format(text, text[::-1]))  # sequence[start:stop:step]    

print("============== Check if a String is a Palindrome ==============")
# Input: "racecar"
# Output: True
text = "racecar"
print("{} -> {}".format(text, checkIfAStringIsAPalindrome(text)))
print("{} -> {}".format(text, checkIfAStringIsAPalindromeOP(text)))          

print("============== Remove Vowels ==============")
# input str = "abcdfghiaaaaouuu"
# output str = "cdfgh"
text = "abcdfghiaaaaouuu"
print("{} -> {}".format(text, removeVowels(text)))
print("{} -> {}".format(text, removeVowelsOP(text)))


print("============== Count Occurrences of Each Character ==============")
# input str = "abcdfghiaaaaouuu"
# Output: {a:1, b:1, c:1, d:1, f:1, g:1, h:1, i:1}
text = "abcdfghiaaaaouuu"
print("{} -> {}".format(text, countOccurrencesofEachCharacter(text)))
print("{} -> {}".format(text, countOccurrencesofEachCharacterOP(text)))


print("============== Find the First Non-Repeating Character ==============")
# input str = "aabbcdeffg"
# Output: "c"
text = "abbcdeffga"
print("{} -> {}".format(text, findtheFirstNonRepeatingCharacter(text)))
print("{} -> {}".format(text, findtheFirstNonRepeatingCharacterOP(text)))


print("============== Remove Duplicate Characters ==============")
# Input: "aabbcdeffg"
# Output: "cdeg"
text = "aabbcdeffg"
print("{} -> {}".format(text, removeDuplicateCharacters(text)))

print("============== Insert a Character at Every N Positions ==============")
# Input: "abcdfghi", N=2
# Output: "ab-cd-fg-hi"
text = "abcdfghi"
N=2
print("{} -> {}".format(text, insertACharacterAtEveryNPositions(text, N)))

print("============== Shift Characters to the Right==============")
# Input: "abcdfghi"
# Output: "iabcdfgh"
text = "abcdfghi"
N=1
print("{} -> {}".format(text, shiftCharactersToTheRight(text,N)))
print("{} -> {}".format(text, shiftCharactersToTheRightOP(text,N)))

print("============== Shift Characters to the Left==============")
# Input: "abcdfghi"
# Output: "bcdfghia"
text = "abcdfghi"
N=1
print("{} -> {}".format(text, shiftCharactersToTheLeftOP(text,N)))

print("============== Remove a specific character ==============")
# Input: "abcdfghi"  R = "d"
# Output: "abcfghi"
text = "abcdfghi"
remove = "d"
print("{} -> {}".format(text, removeAspecificcharacter(text, remove)))


print("============== Replace a character with another ==============")
# Input: "abcdfghi"  l1 = "d"   l2 = "2"
# Output: "abczfghi"
text = "abcdfghi"
l1 = "d"
l2 = "z"
print("{} -> {}".format(text, replaceACharacterWithAnother(text, l1, l2)))

print("============== Convert the string to uppercase or lowercase ==============")
# Input: "ABCDFGHI" 
# Output: "abcdfghi"
text = "ABCDFGHI"
print("{} -> {}".format(text, text.lower()))
text = "abcdfghi"
print("{} -> {}".format(text, text.upper()))

print("============== Repeat N times each letter in the string ==============")
# Input: "abcdfghi"
# Output: "aabbccddffgghhii"
text = "abcdfghi"
N = 2
print("{} -> {}".format(text, repeatNTimesEachLetterInTheString(text, N)))

print("============== Convert each letter to its ASCII code ==============")
# Input: "abcdfghi"
# Output: "[97, 98, 99, 100, 102, 103, 104, 105]"
text = "abcdfghi"
print("{} -> {}".format(text, convertEachLetterToItsASCIICode(text)))
print("{} -> {}".format(text, convertEachLetterToItsASCIICodeOP(text)))


print("============== Add a prefix and/or suffix to the string ==============")
# Input: "abcdfghi"
# Output: "start-abcdfghi-end"
text = "abcdfghi"
print("{} -> {}".format(text, "start-" + text + "-end"))

print("============== Rearrange the letters in a random order ==============")
# Input: "abcdfghi"
# Output: 
text = "abcdfghi"
print("{} -> {}".format(text, rearrangeTheLettersInARandomOrder(text)))
print("{} -> {}".format(text, rearrangeTheLettersInARandomOrderOP(text)))


print("============== Remove all consonants ==============")
# Input: "abcdfghi"
# Output: "ai"
text = "abcdfghi"
print("{} -> {}".format(text, removeAllConsonants(text)))

print("============== Capitalize every other letter ==============")
# Input: "abcdfghi"
# Output: "AbCdFgHi"
text = "abcdfghi"
print("{} -> {}".format(text, capitalizeEveryOtherLetter(text)))

print("============== Join the characters with a space separator ==============")
# Input: "abcdfghi"
# Output: "a b c d f g h i"
text = "abcdfghi"
print("{} -> {}".format(text, " ".join(char for char in text)))

print("============== Find the index of a specific letter ==============")
# Input: "abcdfghi"  char = "g"
# Output: 5-8-9-10-11
text = "abcdfghigggg"
print("{} -> {}".format(text, "-".join(str(n) for n in range(len(text)) if text[n] == "g")))

print("============== Remove duplicate characters ==============")
# Input: "aabbccdffgghi"  char = "g"
# Output: "abcdfghi"
text = "aabbccdffgghi"
print("{} -> {}".format(text, removeDuplicateCharacters(text)))
print("{} -> {}".format(text, removeDuplicateCharactersOP(text)))



print ("============== Handling strings with sequence[start:stop:step] ==============")

text = "0123456789"

print("{} -> {} -> {}".format(text, "text[1:4]", text[1:4])) # 123
print("{} -> {} -> {}".format(text, "text[:3]", text[:3])) # 012  
print("{} -> {} -> {}".format(text, "text[2:]", text[2:])) # 23456789  
print("{} -> {} -> {}".format(text, "text[::2]", text[::2])) # 02468
print("{} -> {} -> {}".format(text, "text[1::2]", text[1::2])) # 13579
print("{} -> {} -> {}".format(text, "text[::-1]", text[::-1])) # 9876543210


print("========================================================================================")

print ("============== Swap First with Last ==============")
print("String: {}".format(text))
print(text[::-1][0:1] + text[1:(len(text) -1)] + text[::-1][(len(text) -1):]) # 9123456780
swapSides = list(text)
swapSides[0], swapSides[-1] = swapSides[-1], swapSides[0]
print("".join(swapSides)) # 9123456780
print(swap_first_last(text)) # 9123456780

print ("============== Get first and last three chars ==============")
print("{} -> {} -> {}".format(text, "text[:3] + text[len(text)-3:]", text[:3] + text[len(text)-3:])) # 012789

print ("============== Get first and last three chars and swap both ==============")
print("{} -> {} -> {}".format(text, "text[:3][::-1] + text[len(text)-3:][::-1]", text[:3][::-1] + text[len(text)-3:][::-1])) # 210987

print ("============== Sum every chat of the string ==============")
print(sum(int(text[n]) for n in range(len(text)))) # 45 = 0+1+2+3+4+5+6+7+8+9

print ("============== Mul every chat of the string, less 0 ==============")
mul = 1
for n in range(len(text[1:])):
    mul *= int(text[1:][n])
print(mul) # 362880 = 1*2*3*4*5*6*7*8*9


