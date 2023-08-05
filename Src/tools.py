def number_to_letter(num):
    if (num<=0) or (num>702):
        return None
    if num <= 26:
        return chr(ord('A') + num - 1)
    else:
        first_letter = chr(ord('A') + ((num - 1) // 26) - 1)
        second_letter = chr(ord('A') + ((num - 1) % 26))
        return f"{first_letter}{second_letter}"
    

def print_text_list(text_list):
        print(f"\n--> print_text_list")
        for index, line in enumerate(text_list):
            print(f"{index}) {line=}")
        print("<--")


if __name__ == '__main__':
    for n in range(-3,1000):
        print(n, " -> ", number_to_letter(n))