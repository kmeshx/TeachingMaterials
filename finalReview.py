def isPalindrome(s):
    return s == s[::-1] and len(s) > 1

def getAllPalsFromI(s, i):
    allPals = []
    for index in range(i, len(s)):
        print(index)
        word = s[i:index+1]
        # print(word)
        if word!="" and isPalindrome(word):
            allPals.append(word)
    return allPals

def palindromePartition(s, i = 0, res = None):
    if res == None: res = []
    #if all characters are single string, u are not gud
    if len(res) == len(s):
        return None #no soln
    #if you're done you good
    if "".join(res) == s:
        return res
    pals = getAllPalsFromI(s, i)
    #no palnidromes here, get rid of first character
    if pals == []:
        res.append(s[i])
        print(res)
        return palindromePartition(s, i + 1, res)
    #for loop through moves
    for word in pals:
        res.append(word)
        temp = palindromePartition(s, i+(len(word)), res)
        if temp!= None:
            return res
        res.pop()
    




import copy
def ct1(L):
    a = L
    b = copy.copy(L)
    a[0] = b[1]
    c = copy.deepcopy(L)
    c[1] = a.pop()
    b[2][1] += 2
    b[0][0] += a[1].pop()
    L = c
    return b + c

L = [[2],[3,9],[0,4]]



#print(ct1(L))
#print(L)

def ct2(s):
    print("initial:", s)
    if len(s) < 2:
        return s
    result = ""
    for elem in reversed(s):
        if elem.isdigit():
            result += chr(int(elem)%3
                     + ord("a"))
        else:
            result += str(ord(elem) 
                     - ord("a"))
    print("result:", result)
    ct2(result[1:-1])

#print(ct2("1c2b3a"))


def ct3(x, depth = 0):
    print("__"*depth + "$%s"%x)
    if (x < 3):
        result = x
    else:
        result = (3*ct3(x-2, depth+1) 
 + ct3(x-1, depth+1))
    print("__"* depth + str(result))
    return result

#print("tuition: $%s" %ct3(4))




def bigOh1(L): 
    N = len(L)
    result = 0
    for i in range(2*N, N**2, 3): 
        if (i not in N):
            for j in range(i, N):
                result += (i * j)//N
    return result

#bigOh1([1, 2, 3])

def permutationBingo(L):
    permutations = dict()
    for i in range(len(L) - 2):
        subset = L[i : i + 3]
        sortedSubset = tuple(sorted(subset))
        if sortedSubset in permutations:
            permutations[sortedSubset].add(tuple(subset))
        else:
            permutations[sortedSubset] = set()
            permutations[sortedSubset].add(tuple(subset))

    for subset in permutations:
        if len(permutations[subset]) == 6:
            return list(subset)
    return None
    
    
import os

def isSwaggy(filename):
    
    if "wean" in filename: return "no swag detected"
    
    swag  = 0
    if filename[-3:] == '.py': swag += 112
    
    nestedNess = filename.count('/') - 1
    swag = swag + nestedNess*42
    
    if swag == 0: return "no swag detected"
    return (swag, filename)
    
        
        
def swaggy(path):
    maxSwagInit = 0
    swagFileInit = ""
    
    def help(path, maxSwag, swagFile):
        if (os.path.isdir(path) == False):
            swag = isSwaggy(path)
            if  swag == "no swag detected":
                return "no swag detected"
            else:
                if swag > maxSwag:
                    maxSwag = swag
                    swagFile = path
            return (maxSwag, swagFile)
            
        else:
            resfinal = 'no swag detected'
            for filename in os.listdir(path):
                newPath = path + "/" + filename
                res = help(newPath, maxSwag, swagFile)
                if res != 'no swag detected':
                    (curSwag, curFile) = res
                    
                    if curSwag > maxSwag:
                        maxSwag = curSwag
                        swagFile = curFile
                        
            return (maxSwag, swagFile)
            
    answer = help(path, maxSwagInit, swagFileInit)
    print(answer)
    if answer == 'no swag detected':
        return answer
    else: return answer[1]

#print(swaggy("sampleFiles1/folderA"))

def swaggy2(path):
   
    
    def help(path):
        if (os.path.isdir(path) == False):
            return isSwaggy(path)
            
        else:
            resfinal = 'no swag detected'
            maxSwag = 0
            swagFile = ""
            
            for filename in os.listdir(path):
                newPath = path + "/" + filename
                res = help(newPath)
                if res != 'no swag detected':
                    (curSwag, curFile) = res
                    
                    if curSwag > maxSwag:
                        maxSwag = curSwag
                        swagFile = curFile
                        
            return (maxSwag, swagFile)
            
    answer = help(path)
    print("s2:", answer)
    if answer == 'no swag detected':
        return answer
    else: return answer[1]
                
"""
folderA/
       folderB/
           fileC.txt
           cool.py
           weanHall/
               finalsAnswerKey.py
       fileB.py
folderD/
"""
#print(swaggy2("sampleFiles1/folderA"))

def getSubMatrix(L, row, col, n, m):
    res = 0
    for i in range(row, row+m):
        for j in range(col, col+n):
            res += L[i][j]
    return res
                
    
    
def findRectOfSizeNM(L, n, m):
    
    rows, cols = len(L), len(L[0])
    
    for row in range(rows - m + 1):
        for col in range(cols - n + 1):
            if getSubMatrix(L, row, col, n, m) == n*m:
                return True
                
    return False

L1 = [[1, 1, 0, 0, 0],
 [0, 0, 0, 0, 1],
 [0, 0, 0, 0, 1],
 [1, 1, 1, 0, 0],
 [1, 1, 1, 0, 1]]
 
L2 = [[1, 1, 0, 0, 0],
 [0, 0, 0, 0, 1],
 [0, 0, 0, 0, 1],
 [1, 1, 0, 0, 0],
 [1, 1, 0, 0, 1]]
 
assert(findRectOfSizeNM(L1, 3, 2) == True)
assert(findRectOfSizeNM(L2, 3, 2) == False)
            
            
    
    
    
    




