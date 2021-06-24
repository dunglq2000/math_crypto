from typing import List
def encrypt(pt: str, key: List[List]) -> str:
    ct = ''
    assert len(pt) % 2 == 0
    for i in range(0, len(pt), 2):
        p1 = ord(pt[i]) - ord('a')
        p2 = ord(pt[i+1]) - ord('a')
        ct += chr((p1 * key[0][0]
                + p2 * key[0][1]) % 26 + ord('a'))
        ct += chr((p1 * key[1][0]
                + p2 * key[1][1]) % 26 + ord('a'))
    return ct

print(encrypt('crypto', [[1, 2], [3, 5]]))
