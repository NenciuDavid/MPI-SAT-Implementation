import copy
import time
import tracemalloc
import csv

csv_file = "results.csv"

def init_csv():
    with open(csv_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["SAT Algorithm", "Mode", "Satifiable/Unsatisfiable", "Time (seconds)", "Peak memory used (MB)"])

def saveResult(algorithm, mode="", sat="", seconds=0.0, memory=0.0):
    with open(csv_file, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([algorithm, mode, sat, seconds, memory])


def complement(literal):
    if literal[0]=='-':
        return literal[1:]
    return '-' + literal

def resolution(K):
    kPrime = copy.deepcopy(K)
    step=1
    while True:
        resolvent=findResolvent(kPrime)
        if(resolvent is None):
            return True
        if(resolvent == set()):
            return False
        kPrime.append(resolvent)
        print("Set of Clauses at step", step, ":", kPrime)
        step+=1

def resolutionShortestPair(K):
    kPrime = copy.deepcopy(K)
    step=1
    while True:
        resolvent=findResolventShortestPair(kPrime)
        if(resolvent is None):
            return True
        if(resolvent == set()):
            return False
        kPrime.append(resolvent)
        print("Set of Clauses at step", step, ":", kPrime)
        step+=1

def findResolvent(kPrime):
    for i in range(len(kPrime)-1):
        for j in range(i+1, len(kPrime)):
            resolventFound=isRez(kPrime[i],kPrime[j])
            if(resolventFound!=None and resolventFound not in kPrime):
                return resolventFound
    return None

def findResolventShortestPair(kPrime):
    resolventFoundShortestPair = None
    shortestPair = float('inf')
    for i in range(len(kPrime)-1):
        for j in range(i+1, len(kPrime)):
            resolventFound = isRez(kPrime[i],kPrime[j])
            if(resolventFound!=None and resolventFound not in kPrime):
                pairSize = len(kPrime[i]) + len(kPrime[j])
                if(pairSize<shortestPair):
                    resolventFoundShortestPair = resolventFound
                    shortestPair = pairSize
    return resolventFoundShortestPair

def isRez(clause1, clause2):
    for l in clause1:
        complementary = complement(l)
        if(complementary in clause2):
            clause3=[]
            for i in clause1:
                if i!=l:
                    clause3.append(i)
            for j in clause2:
                if j!=complementary:
                    clause3.append(j)
            if(len(clause3)>0):
                clause3=set(clause3)
            else:
                clause3=set()
            return clause3
    return None

def verifyOneLiteralRule(kPrime):
    for clause in kPrime:
        if(len(clause)==1):
            return next(iter(clause))

def applyOneLiteralRule(kPrime, unitLiteral):
    kPrimeCopy = copy.deepcopy(kPrime)
    for clause in kPrime[:]:
        complementUnitLiteral = complement(unitLiteral)
        if(unitLiteral in clause):
            kPrime.remove(clause)
        elif(complementUnitLiteral in clause):
            clause.remove(complementUnitLiteral)

def verifyPureLiteralRule(kPrime):
    literals = []
    for clause in kPrime:
        for literal in clause:
            literals.append(literal)
    for literal in literals:
        if complement(literal) not in literals:
            return literal
    return None

def applyPureLiteralRule(kPrime, pureLiteral):
    for clause in kPrime:
        if(pureLiteral in clause):
            kPrime.remove(clause)

def davisPutnam(K):
    kPrime = K.copy()
    while(set() not in kPrime or kPrime==[]):
        isOneLiteralRuleAplicable=verifyOneLiteralRule(kPrime)
        if(isOneLiteralRuleAplicable!=None):
            print("Applying one literal rule for: ", isOneLiteralRuleAplicable)
            applyOneLiteralRule(kPrime, isOneLiteralRuleAplicable)
            print("kPrime after applying one literal rule: ", kPrime)
        else:
            isPureLiteralRuleAplicable=verifyPureLiteralRule(kPrime)
            if(isPureLiteralRuleAplicable!=None):
                print("Applying pure literal rule for: ", isPureLiteralRuleAplicable)
                applyPureLiteralRule(kPrime, isPureLiteralRuleAplicable)
                print("kPrime after applying pure literal rule: ", kPrime)
            else:
                return resolution(kPrime)
    if(set() in kPrime):
        print("Empty clause found in kPrime")
        return False
    if(kPrime==[]):
        print("Empty set of clauses")
        return True

def davisPutnamShortestPair(K):
    kPrime = K.copy()
    while(set() not in kPrime or kPrime==[]):
        isOneLiteralRuleAplicable=verifyOneLiteralRule(kPrime)
        if(isOneLiteralRuleAplicable!=None):
            print("Applying one literal rule for: ", isOneLiteralRuleAplicable)
            applyOneLiteralRule(kPrime, isOneLiteralRuleAplicable)
            print("kPrime after applying one literal rule: ", kPrime)
        else:
            isPureLiteralRuleAplicable=verifyPureLiteralRule(kPrime)
            if(isPureLiteralRuleAplicable!=None):
                print("Applying pure literal rule for: ", isPureLiteralRuleAplicable)
                applyPureLiteralRule(kPrime, isPureLiteralRuleAplicable)
                print("kPrime after applying pure literal rule: ", kPrime)
            else:
                return resolutionShortestPair(kPrime)
    if(set() in kPrime):
        print("Empty clause found in kPrime")
        return False
    if(kPrime==[]):
        print("Empty set of clauses")
        return True

def DPLL(K):
    kPrime = K.copy()
    while True:
        if(set() in kPrime):
            print("Empty clause found in kPrime")
            return False
        if(kPrime==[]):
            print("Empty set of clauses")
            return True
        isOneLiteralRuleAplicable=verifyOneLiteralRule(kPrime)
        if(isOneLiteralRuleAplicable!=None):
            print("Applying one literal rule for: ", isOneLiteralRuleAplicable)
            applyOneLiteralRule(kPrime, isOneLiteralRuleAplicable)
            print("kPrime after applying one literal rule: ", kPrime)
        else:
            isPureLiteralRuleAplicable=verifyPureLiteralRule(kPrime)
            if(isPureLiteralRuleAplicable!=None):
                print("Applying pure literal rule for: ", isPureLiteralRuleAplicable)
                applyPureLiteralRule(kPrime, isPureLiteralRuleAplicable)
                print("kPrime after applying pure literal rule: ", kPrime)
            else:
                literalSplit = next(iter(kPrime[0]))
                print("Spliting on literal: ", literalSplit)
                kPrimeSplit1 = copy.deepcopy(kPrime)
                kPrimeSplit1.append(set(literalSplit))
                raspunsDPLL = DPLL(kPrimeSplit1)
                if(raspunsDPLL == True):
                    return True
                else:
                    kPrimeSplit2 = copy.deepcopy(kPrime)
                    kPrimeSplit2.append(set(complement(literalSplit)))
                    raspunsDPLL = DPLL(kPrimeSplit2)
                    if(raspunsDPLL == True):
                        return True
                    else:
                        return False
    

def MOMS(K):
    minSize = None
    for clause in K:
        if(minSize == None or len(clause)<minSize):
            minSize = len(clause)
    count = {}
    for clause in K:
        if(len(clause) == minSize):
            for literal in clause:
                count[literal] = count.get(literal, 0) + 1
    maxOccurrences = 0
    literalMaxOccurrences = None
    for key in count.keys():
        if(count[key]>maxOccurrences):
            maxOccurrences = count[key]
            literalMaxOccurrences = key
    return literalMaxOccurrences

def DPLLMOMS(K):
    kPrime = K.copy()
    while True:
        if(set() in kPrime):
            print("Empty clause found in kPrime")
            return False
        if(kPrime==[]):
            print("Empty set of clauses")
            return True
        isOneLiteralRuleAplicable=verifyOneLiteralRule(kPrime)
        if(isOneLiteralRuleAplicable!=None):
            print("Applying one literal rule for: ", isOneLiteralRuleAplicable)
            applyOneLiteralRule(kPrime, isOneLiteralRuleAplicable)
            print("kPrime after applying one literal rule: ", kPrime)
        else:
            isPureLiteralRuleAplicable=verifyPureLiteralRule(kPrime)
            if(isPureLiteralRuleAplicable!=None):
                print("Applying pure literal rule for: ", isPureLiteralRuleAplicable)
                applyPureLiteralRule(kPrime, isPureLiteralRuleAplicable)
                print("kPrime after applying pure literal rule: ", kPrime)
            else:
                literalSplit = MOMS(kPrime);
                print("Splitting on literal: ", literalSplit)
                kPrimeSplit1 = copy.deepcopy(kPrime)
                kPrimeSplit1.append(set(literalSplit))
                raspunsDPLL = DPLL(kPrimeSplit1)
                if(raspunsDPLL == True):
                    return True
                else:
                    kPrimeSplit2 = copy.deepcopy(kPrime)
                    kPrimeSplit2.append(set(complement(literalSplit)))
                    raspunsDPLL = DPLL(kPrimeSplit2)
                    if(raspunsDPLL == True):
                        return True
                    else:
                        return False

setOfClauses = list() 
clause = input()
while clause!="0":
    clause = set(clause.split())
    setOfClauses.append(clause)
    clause = input()
print(setOfClauses)
init_csv()
# Resolution clasic
SOC = copy.deepcopy(setOfClauses)
tracemalloc.start()
startingTime = time.perf_counter()
responseResolution=resolution(SOC)
endingTime = time.perf_counter()
currentMemory, peakMemoryUsed = tracemalloc.get_traced_memory()
tracemalloc.stop()
memoryInMB = peakMemoryUsed / 10**6
totalTime = endingTime - startingTime
satis = None
print(f"Result of resolution clasic obtained in {totalTime}, using {memoryInMB} MB peak memory.")
if(responseResolution==True):
    print("satisfiable")
    satis = "Satisfiable"
else:
    print("unsatisfiable")
    satis = "Unsatisfiable"
saveResult("Resolution", "Clasic", satis, totalTime, memoryInMB)
# Resolution shortest pair
SOC = copy.deepcopy(setOfClauses)
tracemalloc.start()
startingTime = time.perf_counter()
responseResolution=resolutionShortestPair(SOC)
endingTime = time.perf_counter()
currentMemory, peakMemoryUsed = tracemalloc.get_traced_memory()
tracemalloc.stop()
memoryInMB = peakMemoryUsed / 10**6
totalTime = endingTime - startingTime
satis = None
print(f"Result of resolution shortest pair obtained in {totalTime}, using {memoryInMB} MB peak memory.")
if(responseResolution==True):
    print("satisfiable")
    satis = "Satisfiable"
else:
    print("unsatisfiable")
    satis = "Unsatisfiable"
saveResult("Resolution", "Shortest Pair", satis, totalTime, memoryInMB)
# DP clasic
SOC = copy.deepcopy(setOfClauses)
tracemalloc.start()
startingTime = time.perf_counter()
responseDP = davisPutnam(SOC)
endingTime = time.perf_counter()
currentMemory, peakMemoryUsed = tracemalloc.get_traced_memory()
tracemalloc.stop()
memoryInMB = peakMemoryUsed / 10**6
totalTime = endingTime - startingTime
satis = None
print(f"Result of DP clasic obtained in {totalTime}, using {memoryInMB} MB peak memory.")
if(responseDP==True):
    print("satisfiable")
    satis = "Satisfiable"
else:
    print("unsatisfiable")
    satis = "Unsatisfiable"
saveResult("Davis Putnam", "Clasic", satis, totalTime, memoryInMB)
# DP shortest pair
SOC = copy.deepcopy(setOfClauses)
tracemalloc.start()
startingTime = time.perf_counter()
responseDP = davisPutnamShortestPair(SOC)
endingTime = time.perf_counter()
currentMemory, peakMemoryUsed = tracemalloc.get_traced_memory()
tracemalloc.stop()
memoryInMB = peakMemoryUsed / 10**6
totalTime = endingTime - startingTime
satis = None
print(f"Result of DP shortest pair obtained in {totalTime}, using {memoryInMB} MB peak memory.")
if(responseDP==True):
    print("satisfiable")
    satis = "Satisfiable"
else:
    print("unsatisfiable")
    satis = "Unsatisfiable"
saveResult("Davis Putnam", "Shortest Pair", satis, totalTime, memoryInMB)
# DPLL clasic
SOC = copy.deepcopy(setOfClauses)
tracemalloc.start()
startingTime = time.perf_counter()
responseDPLL = DPLL(SOC)
endingTime = time.perf_counter()
currentMemory, peakMemoryUsed = tracemalloc.get_traced_memory()
tracemalloc.stop()
memoryInMB = peakMemoryUsed / 10**6
totalTime = endingTime - startingTime
satis = None
print(f"Result of DPLL clasic obtained in {totalTime}, using {memoryInMB} MB peak memory.")
if(responseDPLL==True):
    print("satisfiable")
    satis = "satisfiable"
else:
    print("unsatisfiable")
    satis = "unsatisfiable"
saveResult("DPLL", "Clasic", satis, totalTime, memoryInMB)
# DPLL MOMS
SOC = copy.deepcopy(setOfClauses)
tracemalloc.start()
startingTime = time.perf_counter()
responseDPLL = DPLLMOMS(SOC)
endingTime = time.perf_counter()
currentMemory, peakMemoryUsed = tracemalloc.get_traced_memory()
tracemalloc.stop()
memoryInMB = peakMemoryUsed / 10**6
totalTime = endingTime - startingTime
satis = None
print(f"Result of DPLL MOMS obtained in {totalTime}, using {memoryInMB} MB peak memory.")
if(responseDPLL==True):
    print("satisfiable")
    satis = "Satisfiable"
else:
    print("unsatisfiable")
    satis = "Unsatisfiable"
saveResult("DPLL", "MOMS", satis, totalTime, memoryInMB)
