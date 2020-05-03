# we have a List of booleans. Let's check if the majority of elements are true

def is_majority(items: list) -> bool:
    true_counter = 0
    false_counter = 0
    for i in items:
        if i:
            true_counter += 1
        else:
            false_counter += 1
    if true_counter > false_counter: return True
    elif false_counter >= true_counter: return False


if __name__ == '__main__':
    assert is_majority([True, True, False, True, False]) == True
    assert is_majority([True, True, False]) == True
    assert is_majority([True, True, False, False]) == False
    assert is_majority([True, True, False, False, False]) == False
    assert is_majority([False]) == False
    assert is_majority([True]) == True
    assert is_majority([]) == False
