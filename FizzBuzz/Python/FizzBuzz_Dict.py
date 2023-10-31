#A simple FizzBuzz implementation in python with dictionaries

def fizzbuzz(limit=100, fizz=3, buzz=5):
    wordDict = {"Fizz":fizz, "Buzz":buzz}
    numIter = ''
    
    for number in range(1, limit + 1):
        numIter = ''
        for word in wordDict:
            if number % wordDict[word] == 0:
                numIter += word
        if numIter == '':
            numIter += str(number)
        print(numIter)

if __name__ == '__main__':
    fizzbuzz()
