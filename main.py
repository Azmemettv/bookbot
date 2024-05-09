def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        words = book.split()
        wc = len(words)
        count = 0
        letterCounts = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,
                        'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,
                        'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,
                        'y':0,'z':0}
        for word in words:
            for char in word:
                for letter in letterCounts:
                    if char == letter:
                        letterCounts[letter] += 1
        print(letterCounts)

    
main()