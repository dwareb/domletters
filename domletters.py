from sys import stdin

if __name__ == "__main__":
    
    #Get the STDIN expected input to be piped in
    txt = ""

    #Below method of inputting to EOF by arekolek, https://stackoverflow.com/questions/21235855/how-to-read-user-input-until-eof
    for intext in stdin:
        txt += intext
    words = txt.split()

    #Remove all the words that aren't just letters.
    for w in words:
        if not w.isalpha():
            words.remove(w)
    #Counting most letters in each words.
    letters = {}
    total = 0
    for w in words:
        
        #Method of counting frequency found here: https://www.geeksforgeeks.org/python-frequency-of-each-character-in-string/
        for l in w:
            if l in letters:
                letters[l] += 1
            else:
                letters[l] = 1
        
        total += max(letters.values())
        letters.clear()
        

    print("Total Dominant Letters: ")
    print(total)
    print("\n")
