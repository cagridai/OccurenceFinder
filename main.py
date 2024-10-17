'''
Problem:
t and z are strings consist of lowercase English letters.

Find all substrings for t, and return the maximum value of [ len(substring) x [how many times the substring occurs in z] ]

Example:
t = acldm1labcdhsnd
z = shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa

Solution:
abcd is a substring of t, and it occurs 5 times in Z, len(abcd) x 5 = 20 is the solution

'''

'''
def find_max(t, z):
    return max(len(sub) * z.count(sub) for i in range(len(t)) for j in range(i + 1, len(t) + 1) for sub in [t[i:j]])

Bir önceki soruda daha kısa olması halinde ekstra puan verileceği yazıyordu. Bu algoritmayı da daha kısa olarak bu şekilde yazabiliriz fakat çok karmaşık ve okunaksız bir hal almaktadır.
'''


def find_max(t,z):
    max_value = 0

    for i in range(len(t)):
        for j in range(i + 1, len(t) + 1):
            substring = t[i:j]
            occurrences = z.count(substring)

            value = len(substring) * occurrences

            if value > max_value:
                max_value = value

    return max_value


if __name__ == '__main__':
    print(find_max("acldm1labcdhsnd","shabcdacasklksjabcdfueuabcdfhsndsabcdmdabcdfa"))