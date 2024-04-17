import re

# Sample text
text = "Rbr RbbrR RbRbrr rbRBr rbrbrr"

# Regular expression pattern
pattern = r'[Rr]b+r'

# Find all matches
matches = re.findall(pattern, text)

# Print matches
print(matches)
