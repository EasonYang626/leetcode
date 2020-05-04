class Solution:
    def isPalindrome(self, x: int) -> bool: 
        # 特殊情况：
        # 如上所述，当 x < 0 时，x 不是回文数。
        # 同样地，如果数字的最后一位是 0，为了使该数字为回文，
        # 则其第一位数字也应该是 0
        # 只有 0 满足这一属性
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        # 当数字长度为奇数时，我们可以通过 revertedNumber/10 去除处于中位的数字。
        # 例如，当输入为 12321 时，在 while 循环的末尾我们可以得到 x = 12，revertedNumber = 123，
        # 由于处于中位的数字不影响回文（它总是与自己相等），所以我们可以简单地将其去除。
        # 现在的问题是，我们如何知道反转数字的位数已经达到原始数字位数的一半？
        # 我们将原始数字除以 10，然后给反转后的数字乘上 10，
        # 所以，当原始数字小于反转后的数字时
        # 意味着我们已经处理一半或者超过一半的数字了
        # 如果是偶数的回文数 在一半的时候应该是相等的 
        # 若不是则可能多处理一位数字 这样的出来的结果也必定是false
        reverted = 0
        while (x > reverted):
            reverted = reverted * 10 + x % 10
            x = x // 10
        return x == reverted or x == reverted // 10