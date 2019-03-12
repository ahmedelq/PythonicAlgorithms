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
    nonLetterCount("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean est augue, accumsan sit amet ante sit amet, sollicitudin suscipit dolor. Ut sapien nisl, condimentum quis tempus non, facilisis sed erat. Nunc sodales eget ante non sollicitudin. Phasellus purus turpis, efficitur id placerat eget, porttitor in augue. Donec sed enim felis. Aenean venenatis mauris non risus lacinia semper. Suspendisse ornare est in vehicula fringilla. Cras eget ultricies sem. Mauris vitae leo interdum, interdum sem ut, tincidunt eros. Fusce dapibus sed nulla vel auctor. Quisque pretium libero augue, vel rhoncus justo rhoncus et.
    Nam nec dolor augue. Aliquam consequat sed lorem sit amet viverra. Donec orci erat, eleifend non leo a, lacinia egestas turpis. Nunc at ex pulvinar, finibus arcu gravida, aliquet tellus. Cras vestibulum urna eget dolor eleifend, posuere fermentum nulla hendrerit. Suspendisse porttitor ipsum a luctus egestas. Mauris dapibus bibendum tortor. Pellentesque tortor arcu, interdum sit amet aliquet eu, auctor quis sapien. Vivamus iaculis interdum rutrum. Interdum et malesuada fames ac ante ipsum primis in faucibus.""")