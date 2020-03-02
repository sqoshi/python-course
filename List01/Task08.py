A = [1000, 500, 100, 50, 10, 5, 1]
R = ['M', 'D', 'C', 'L', 'X', 'V', 'I']


def romeToArab(num):
    i = 0
    j = 0
    result = 0
    while i < len(A) and j < len(num):
        if num[j] == R[i]:
            result += A[i]
            j += 1
        elif i % 2 == 0 and i < len(A) - 2 and j < len(num) - 1 \
                and num[j] == R[i + 2] and num[j + 1] == R[i]:
            result += A[i] - A[i + 2]
            j += 2
            i += 1
        elif i % 2 == 1 and i < len(A) - 1 and j < len(num) - 1 \
                and num[j] == R[i + 1] and num[j + 1] == R[i]:
            result += A[i] - A[i + 1]
            j += 2
            i += 1
        else:
            i += 1
    print(result)
    return result


def arabToRome(num):
    result = []
    i = 0
    while num > 0 and i < len(A):
        if num >= A[i]:
            num -= A[i]
            result.append(R[i])
        elif i % 2 == 0 and i < len(A) - 2 and \
                A[i + 2] != A[i] - A[i + 2] and (num >= A[i] - A[i + 2]):
            result.append(R[i + 2])
            result.append(R[i])
            num -= A[i] - A[i + 2]
            i += 1
        elif i % 2 == 1 and i < len(A) - 1 and \
                A[i + 1] != A[i] - A[i + 1] and (num >= A[i] - A[i + 1]):
            result.append(R[i + 1])
            result.append(R[i])
            num -= A[i] - A[i + 1]
            i += 1
        else:
            i += 1
    print(''.join(result))
    return ''.join(result)


def converter(s=input("Input : ")):
    try:
        val = int(s)
        arabToRome(val)
    except ValueError:
        try:
            val = str(s)
            romeToArab(val)
        except ValueError:
            print('String Error')


converter()
