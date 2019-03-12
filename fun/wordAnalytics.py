#Author: ahmelq -  github.com/ahmedelq/
#License: MIT
#This is a solution of the challange: https://www.reddit.com/r/dailyprogrammer/comments/1e97ob/051313_challenge_125_easy_word_analytics/

def wc(txt):
    return len(txt.split())

def letterCount(txt):
    return sum(len(word) for word in txt)

def nonLetterCount(txt):
    from collections import Counter
    txt = txt.lower()
    letter_count = Counter(txt)
    word_count   = Counter(txt.split())

    total_white_space   = letter_count.get(' ', 0)
    del letter_count[' ']
    total_words         = len(txt.split())
    total_lines         = letter_count.get('\n', 0)
    total_letters       = sum(dict(letter_count).values())
    total_symbols       = sum(lc for l, lc in dict(letter_count).items() if not l.isalnum())
    top_3_words         = ', '.join([word + ": " + str(ct) for word, ct in word_count.most_common(3)])
    top_3_letters       = ', '.join([letter + ": " + str(ct) for letter, ct in letter_count.most_common(3)])
    

    print(
        "Total words: " + str(total_words),
        "Total letters: " + str(total_letters),
        "Total lines: " + str(total_lines),
        "Total symbols: " + str(total_symbols),
        "Top 3 words: " + top_3_words,
        "Top 3 letters: " + top_3_letters,
        
        "",
        sep="\n"
        )



if __name__ == "__main__":
    nonLetterCount("Hello world world hello ahmed ahmed helmig algle ** !! \n Hallo Welt")