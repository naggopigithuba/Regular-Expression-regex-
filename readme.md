# Description
This Python script allows searching for a regular expression (regex) pattern across .txt files in a specified folder and highlights matches in both the filenames and the text content. The ColorHighlighter class adds colored highlighting to the text, and the TextFileSearch class manages searching through the files and displaying matches.
# Additional Explanation
Additional Explanation:
The main script allows users to input a regular expression, and it will perform a search across all .txt files in the current folder, displaying results in a highlighted format. You can customize the colors and further adapt the functionality as needed.

# Description about the regex
\A: Matches the specified characters at the beginning of the string.

Input: ^\AThis
Description: This will search for the word "This" only at the beginning of a line.
\b: Matches the specified characters at the beginning or end of a word.

Input: \bapple\b
Description: This will search for the word "apple" as a whole word.
\B: Matches the specified characters present but not at the beginning or end of a word.

Input: \Bland
Description: This will search for the word "land" not at the beginning of a word.
\d: Matches digits (numbers from 0 to 9).

Input: \d+
Description: This will search for any sequence of digits in the text.
\D: Matches non-digit characters.

Input: \D+
Description: This will search for any sequence of non-digit characters in the text.
\s: Matches whitespace characters.

Input: \s+
Description: This will search for any sequence of whitespace characters in the text.
\S: Matches non-whitespace characters.

Input: \S+
Description: This will search for any sequence of non-whitespace characters in the text.
\w: Matches word characters (alphabetic characters, digits, and underscores).

Input: \w+
Description: This will search for any sequence of word characters (letters, digits, or underscores) in the text.
\W: Matches non-word characters.

Input: \W+
Description: This will search for any sequence of non-word characters in the text.
\Z: Matches the specified characters at the end of the string.

Input: end\Z
Description: This will search for the word "end" only at the end of the text.
