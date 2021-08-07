import unittest

def find_min(arr):
    count = 1
    min = arr[0]
    lengh = len(arr)
    for i in range(1, lengh):
        if arr[i] < min:
            min = arr[i]
            count = 1
        elif arr[i] == min:
            count += 1

    return f"N = {min}, Count = {count}"


class TestStringMethods(unittest.TestCase):

    def test_find_min(self):
        self.assertEqual(find_min([1,9,15,3,29,19]), "N = 1, Count = 1")
        self.assertEqual(find_min([9,15,3,29,19,1,3,7,2,2,2,1]), "N = 1, Count = 2")
        self.assertEqual(find_min([2897,4683,5555,1456,6464,6464,1456,9999,1456]), "N = 1456, Count = 3")

# 執行本程式時會直接跑測試，若通過所有測資最下面一行會顯示 "OK"
if __name__ == "__main__":
    unittest.main()