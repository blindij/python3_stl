import re

# ---------------------------
# Regex Flag Abbreviations
# ---------------------------
# ASCII          | a
# IGNORECASE     | i
# MULTILINE      | m
# DOTALL         | s
# VERBOSE        | x
# ----------------------------

text = 'This is some text -- with punctuation.'
pattern = r'(?i)\bT\w+'
regex = re.compile(pattern)
print('Text   :', text)
print('Pattern:', pattern)
print('Matches:', regex.findall(text))
