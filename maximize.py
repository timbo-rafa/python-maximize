from functools import reduce

def f(numbers, m):
    s = reduce(lambda acc, i: acc + i**2,numbers, 0)
    print([s, numbers])
    return s % m

def readAll(k):
    sequences = []
    while (k > 0):
        sequence = []
        line = input().strip().split()
        n = int(line.pop(0))
        #sequences.append(n)
        while(n > 0):
            sequence.append(int(line.pop(0)))
            n -= 1
        sequences.append(sequence)
        k -= 1
    return sequences
        


def process(k,m, sequences, smax, si, numbers):
    print([k,m,sequences,smax,si,numbers])
    if (si >= k):
        s = f(numbers, m)
        if (s > smax):
            smax = s
        return smax

    curSeq = sequences[si]
    for n in curSeq:
        nextNumbers = list(numbers)
        nextNumbers.append(n)
        smax = process(k, m, sequences, smax, si + 1, nextNumbers)
    return smax

def main():
    line = input().strip().split()
    k = int(line[0])
    m = int(line[1])
    sequences = readAll(k)
    smax = process(k,m, sequences, 0, 0, [])
    print(smax)

if __name__ == "__main__":
    main()
