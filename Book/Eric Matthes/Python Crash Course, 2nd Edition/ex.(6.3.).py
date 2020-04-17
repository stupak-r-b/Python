# glossary of programming terms
terms = {"dictionary": "A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries"
                      " are written with curly brackets, and they have keys and values.",
         "set": "A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets",
         "tuple": "A tuple is a collection which is ordered and unchangeable. In Python tuples are written "
                 "with round brackets.",
         "generator": "A Python generator is a function which returns a generator iterator (just an object we can "
                       "iterate over) by calling yield . yield may be called with a value, in which case that value "
                       "is treated as the 'generated' value",
         "conditions": "Python uses boolean variables to evaluate conditions. The boolean values True and False are "
                        "returned when an expression is compared or evaluated."}

# print each word and its meaning as neatly formatted output
print(f"\nDictionary: {terms['dictionary'.lower()]}\n")
print(f"Set: {terms['set'.lower()]}\n")
print(f"Tuple: {terms['tuple'.lower()]}\n")
print(f"Generator: {terms['generator'.lower()]}\n")
print(f"Conditions: {terms['conditions'.lower()]}\n")