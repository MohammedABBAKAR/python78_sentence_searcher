# Sentence Searcher
# Create a function that returns the whole of the first sentence which contains a specific word. Include the full stop at the end of the sentence.

# Examples
# txt = "I have a cat. I have a mat. Things are going swell."

# sentence_searcher(txt, "have") ➞ "I have a cat."

# sentence_searcher(txt, "MAT") ➞ "I have a mat."

# sentence_searcher(txt, "things") ➞ "Things are going swell."

# sentence_searcher(txt, "flat") ➞ ""
# Notes
# Sentences will always end with a period.
# Your function should not be case sensitive.
# Return an empty string if the word isn't found in the sentence.




def sentence_searcher(txt, word):
  lst2 = []
  lst3 = []
  lst= txt.split(".")
  lst.pop()
  for x in lst:
    lst2.append(x.split())
  for y in lst2:
    if word in y:
      lst3.append(" ".join(y))
  return lst3[0]
print(sentence_searcher("I have a cat. I have a mat. Things are going swell.","have"))


def sentence_searcher(txt, word):
    lst2 = []
    lst3 = []
    lst = txt.split(".")
    
   
    lst.pop()

    
    for x in lst:
        lst2.append(x.split())
    
    
    for y in lst2:
        if word.lower() in [w.lower() for w in y]:
            lst3.append(" ".join(y).strip())
    
    
    if lst3:
        return lst3[0] + "."
    else:
        return ""

print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "have"))  # Expected: "I have a cat."
print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "MAT"))   # Expected: "I have a mat."
print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "things"))  # Expected: "Things are going swell."
print(sentence_searcher("I have a cat. I have a mat. Things are going swell.", "flat"))  # Expected: ""



def sentence_searcher(txt, word):
    # Ensure all sentences end with a period, even after split
    sentences = txt.split(". ")
    
    # Loop through the sentences and check for the word (case insensitive)
    for sentence in sentences:
        if word.lower() in sentence.lower():
            return sentence.strip() + "."
    
    # Return an empty string if no sentence contains the word
    return ""

# Test cases
txt = "I have a cat. I have a mat. Things are going swell."

print(sentence_searcher(txt, "have"))  # Expected: "I have a cat."
print(sentence_searcher(txt, "MAT"))   # Expected: "I have a mat."
print(sentence_searcher(txt, "things"))  # Expected: "Things are going swell."
print(sentence_searcher(txt, "flat"))  # Expected: ""
