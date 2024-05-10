def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        words = book.split()
        wc = len(words)
        count = 0
        letterCounts = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,
                        'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,
                        'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,
                        'y':0,'z':0}#theyre all there
        for word in words:
            for char in word:
                for letter in letterCounts:
                    if char.lower() == letter:
                        letterCounts[letter] += 1
    sorted = sortByCount(letterCounts)
    print(f"in the {wc} words of \"frankenstein\" the letter:")
    for dicts in sorted:
        print(f"{dicts["letter"]} appears {dicts["count"]} times")

def sortByCount(dict):
    def sort_on(dict): #idk
        return dict["count"]
    sortedDict = []
    for char in dict:
        sortedDict.append({"letter":char,"count":dict[char]})
    sortedDict.sort(reverse=True,key=sort_on)
    return sortedDict  
main()