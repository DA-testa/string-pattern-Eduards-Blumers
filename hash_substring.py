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
    text_len = len(text)

    pattern_hash = sum(ord(pattern[i]) * 31**(pattern_len-i-1) for i in range(pattern_len))
    text_hash = sum(ord(text[i]) * 31**(pattern_len-i-1) for i in range(pattern_len))

    occurrences = []

    for i in range(0, text_len - pattern_len + 1):
        if pattern == text[i:i+pattern_len]:
            occurrences.append(i)
        if i < text_len - pattern_len:
            text_hash = 31 * (text_hash - ord(text[i]) * 31**(pattern_len-1) + ord(text[i+pattern_len]))

    return occurrences


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
