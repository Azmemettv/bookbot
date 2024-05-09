def main():
    with open("books/frankenstein.txt") as f:
        book = f.read()
        words = book.split()
        print(len(words))
    
main()