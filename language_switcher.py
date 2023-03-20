#!/bin/python
import os
import csv

class Rofi:
    def __init__(self, args=None):
        self.args = args

    def select(self, prompt, options, selected):
        items = "\n".join(options)
        ans = os.popen(f"echo '{items}' | rofi -dmenu -p '{prompt}' -format i \
            -selected-row {selected} -me-select-entry ''\
            -me-accept-entry 'MousePrimary' {self.args}").read().strip()

        if ans == "":
            return -1

        return int(ans)

def show_menu(languages):
    rofi = Rofi()

    options = []
    for lang in languages:
        options.append(lang[1])

    selected = 0
    selected = rofi.select("Select layout", options, selected)

    if selected != -1:
        os.popen(f'setxkbmap {languages[selected][1]}')

if (__name__ == "__main__"):
    languages = []
    with open('languages.txt', 'r', encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            languages.append((row['language'], row['code']))

    show_menu(languages)