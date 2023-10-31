#Fizzbuzz implemetation in python

def fizzbuzz(limit=100, fizz=3, buzz=5):
    wordMap = {"Fizz":fizz, "Buzz":buzz}

    for number in range(1, limit + 1):
        string = ''

        for word in wordMap:
            if number % wordMap[word] == 0:
                string += word
        if string == '':
            string += str(number)
        
        print(string)

#Main
if __name__ == '__main__':
    fizzbuzz(100, 3, 5)

