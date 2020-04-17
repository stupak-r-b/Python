"""
    The function should recognise if a subject line is stressful. A stressful subject line means that all letters are in
uppercase, and/or ends by at least 3 exclamation marks, and/or contains at least one of the following “red” words: "help",
"asap", "urgent". Any of those "red" words can be spelled in different ways - "HELP", "help", "HeLp", "H!E!L!P!", "H-E-L-P",
even in a very loooong way "HHHEEEEEEEEELLP," they just can't have any other letters interspersed between them.

Input: Subject line as a string.
Output: Boolean.
"""


def is_stressful(subj):
    if "!!!!" in subj or subj.isupper():
        return True

    # replace all dots, dashes and exclamation points
    subj = subj.replace("-", "").replace(".", "").replace("!", "")
    for el in subj.split(" "):
        if el.lower() in ["help", "asap", "urgent"]:
            return True

        # added unique letters to the string to make up the word
        word = "".join(i for i in {i: el.count(i) for i in el}.keys()).lower()
        if word in ["help", "asap", "urgent"]:
            return True

    return False
