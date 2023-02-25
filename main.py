from string import ascii_letters
import pyautogui
from time import sleep


with open("unfiltered_words.txt") as w:
    word_list = w.read().split()

center = input("Center Letter: ")[0]
inp = input("Side letters (6): ")
border = [i for i in inp]

eliminated = [i for i in ascii_letters if i not in border]
eliminated.remove(center)
print(eliminated)

with open("filtered.txt", "w") as f:
    valid_words = []
    for word in word_list:
        if center in word:
            valid_words.append(word)

    final_words = []
    for word in valid_words:
        for letter in eliminated:
            if letter in word:
                break
        else:
            final_words.append(word)
    print(f"Found {len(final_words)} theoretically valid words")
    final_words.sort(key=len)

    for word in final_words:
        f.write("\n" + word)

write = input("write? (y/n): ")
if write == "y":
    sleep(2)
    with open("filtered.txt") as f:
        for word in f.read().split():
            pyautogui.write(word)
            pyautogui.press('enter')
            sleep(0.2)

