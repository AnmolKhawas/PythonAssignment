#Function that takes a sentence as an input parameter and displays the number of words in the sentence.

def no(string):
    numbers=len(string.split())
    print("Number of words:"+str(numbers))

string=input("Enter sentence:")
if __name__=="__main__":
    no(string)
