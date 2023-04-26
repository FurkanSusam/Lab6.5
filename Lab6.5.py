#question1

arr1 = [5,10,15,20,25,30,35,40]
arr2 = [3,5,8,12,15,18,21,24,27,30]
def commElements(array1,array2):
    arr3 = []
    for a in arr1:
        for b in arr2:
            if a == b:
                arr3.append(a)
    return arr3
print("Common elements are : " + str(commElements(arr1, arr2)))
#question2

list1 = ["furkan","edip","adana", "sis", "ata","tenet","kazak","yay"]
def palindroms(list1):
    list2 = []
    for word in list1:
        nonRev = word
        rev=word[::-1]
        if nonRev == rev:
            list2.append(nonRev)
    return list2
print("Palindrome words are : " +str(palindroms(list1)))

#question3

list1 = [2,3,4,5,6,7,8,9,10,11,12,13]

def primes(list1):
    list2 = []
    for num in list1:
        prime = [True for i in range(num + 1)]
        a = 2
        while (a * a <= num):
            if (prime[a] == True):
                for i in range(a * a, num + 1, a):
                    prime[i] = False
            a += 1
        for a in range(2, num + 1):
            if prime[a]:
                if num == a:
                    list2.append(num)
    return list2
print("Prime numbers are : " +str(primes(list1)))


#question4

wordList = ["iceman", "cinema", "microsoft", "apple", "anemic", "cam", "furkan"]
def anagrams(word, wordList):
    sortedList=[]
    newItem=sorted(str(word.lower().replace(" ", "")))
    for word_List in wordList:
        newWord=sorted(str(word_List).lower().replace(" ",""))
        if newWord == newItem:
            sortedList.append(word_List)
    return sortedList
print(anagrams("na me ci",wordList))