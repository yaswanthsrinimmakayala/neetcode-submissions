class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num_str = "".join(str(i) for i in digits)
        num = int(num_str)+1
        return [int(i) for i in str(num)]
