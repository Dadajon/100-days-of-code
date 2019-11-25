def designer_pdf_viewer(h, word):
    """
    In this challenge, you will be given a list of letter heights in the alphabet and a string.
    Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide.

    :param h: an array of integers representing the heights of each letter
    :param word: a string
    :return: a single integer denoting the area in mm^2 of highlighted rectangle when the given word is selected.
    """
    a = 97
    alphabet = dict()
    for i in range(len(h)):
        alphabet.update({chr(a): h[i]})
        a += 1

    max_height = 0
    for i in word:
        if i in alphabet.keys():
            height = alphabet[i]
            if height > max_height:
                max_height = height

    return len(word) * 1 * max_height


if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))
    word = input()

    result = designer_pdf_viewer(h, word)
    print(str(result) + '\n')
