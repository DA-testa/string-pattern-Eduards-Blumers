# python3




def read_input():
    input_type = input().rstrip()
    if "I" in input_type:
        pattern = input().rstrip()
        text = input().rstrip()
    elif "F" in input_type:
        with open("tests/06", "r") as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text





def print_occurrences(output):
    # this function should control output, it doesn't need any return
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):

    pattern_len = len(pattern)
    pattern_hash = get_hash(pattern)
    text_len = len(text)

    occurrences = []

    for i in range(0, text_len - pattern_len + 1):
        text_part = text[i:i + pattern_len]
        text_part_hash = get_hash(text_part)

        if pattern_hash == text_part_hash:
            if pattern == text_part:
                occurrences.append(i)

    return occurrences 





if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
