import re
import os

class ColorHighlighter:
    COLOR_CODES = {
        'red': '\033[91m',
        'green': '\033[92m',
        'yellow': '\033[93m',
        'blue': '\033[94m',
        'violet': '\033[95m',
        'reset': '\033[0m'
    }

    def __init__(self, color):
        self.color = color

    def highlight(self, text):
        color_code = self.COLOR_CODES.get(self.color, '')
        return f"{color_code}{text}{self.COLOR_CODES['reset']}"

class TextFileSearch:
    def __init__(self, folder='.'):
        self.folder = folder
        self.highlighter = ColorHighlighter('yellow')

    def highlight_word(self, text, word):
        return self.highlighter.highlight(text.replace(word, self.highlighter.highlight(word)))

    def highlight_filename(self, filename):
        self.highlighter.color = 'green'
        highlighted_filename = self.highlighter.highlight(filename)
        self.highlighter.color = 'yellow'  # Reset color for subsequent highlighting
        return highlighted_filename

    def search_files(self, regex):
        pattern = re.compile(regex)
        for filename in os.listdir(self.folder):
            if filename.endswith('.txt'):
                with open(os.path.join(self.folder, filename), 'r') as file:
                    lines = file.readlines() # contains list of lines in that particular file
                    file_has_match = False  # Flag to indicate if any match is found in the file
                    for i, line in enumerate(lines):
                        matches = pattern.finditer(line)
                        for match in matches:
                            if not file_has_match:
                                highlighted_filename = self.highlight_filename(filename)
                                print(f"[{highlighted_filename}]")
                                print("|")
                                file_has_match = True  # Set flag to True if a match is found
                            start_index = max(0, match.start() - 5)
                            end_index = min(len(line), match.end() + 5)
                            snippet = line[start_index:end_index]
                            highlighted_snippet = self.highlight_word(snippet, match.group())
                            print(f"|_____Line {i+1}: {highlighted_snippet}...")
                    if file_has_match:
                        print()  # Add an empty line after printing matches in a file



if __name__ == "__main__":
    while(1):
        regex = input("Enter the regular expression: ")
        searcher = TextFileSearch()
        searcher.search_files(regex)
        print("|\n|\n")
'''
- `\A`: Matches the specified characters at the beginning of the string.
- `\b`: Matches the specified characters at the beginning or end of a word.
- `\B`: Matches the specified characters present but not at the beginning or end of a word.
- `\d`: Matches digits (numbers from 0 to 9).
- `\D`: Matches non-digit characters.
- `\s`: Matches whitespace characters.
- `\S`: Matches non-whitespace characters.
- `\w`: Matches word characters (alphabetic characters, digits, and underscores).
- `\W`: Matches non-word characters.
- `\Z`: Matches the specified characters at the end of the string.
'''