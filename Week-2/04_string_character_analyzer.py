# Given a string, count vowels, consonants, digits, and special characters separately.

sentence = "vvjhsvjhaeisdjv4343. ?(*&^%)"
vowels = "aeiou"
consonants = "bcdfghjklmnpqrstvwxyz"
digit = "1234567890"
vowels_count = 0
consonants_count = 0
special_char_count = 0
digit_count = 0
for ch in sentence:
    if ch.lower() in vowels:
        vowels_count+=1
    elif ch.lower() in consonants:
        consonants_count += 1
    elif ch in digit:
        digit_count += 1
    else:
        special_char_count += 1
print(f"Vowels = {vowels_count}\nConsonant = {consonants_count}\nDigits = {digit_count}\nSpecial Characters = {special_char_count}")