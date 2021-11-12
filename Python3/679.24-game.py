#
# @lc app=leetcode id=679 lang=python3
#
# [679] 24 Game
#

# @lc code=start
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        n1 = nums[0]
        n2 = nums[1]
        n3 = nums[2]
        n4 = nums[3]
        # 2 + 2
        for a, b, c, d in [(n1, n2, n3, n4), (n1, n3, n2, n4), (n1, n4, n2, n3), (n2, n3, n1, n4), (n2, n4, n3, n1), (n3, n4, n1, n2)]:
            for i in range(6):
                if i == 0:
                    r1 = a + b
                if i == 1:
                    r1 = a - b
                if i == 2:
                    r1 = a * b
                if i == 3:
                    r1 = a / b
                if i == 4:
                    r1 = b - a
                if i == 5:
                    r1 = b / a
                for j in range(6):
                    if j == 0:
                        r2 = c + d
                    if j == 1:
                        r2 = c - d
                    if j == 2:
                        r2 = c * d
                    if j == 3:
                        r2 = c / d
                    if j == 4:
                        r2 = d - c
                    if j == 5:
                        r2 = d / c
                    for k in range(6):
                        if k == 0:
                            r = r1 + r2
                            if r == 24:
                                return True
                        if k == 1:
                            r = r1 - r2
                            if r == 24:
                                return True
                        if k == 2:
                            r = r1 * r2
                            if r == 24:
                                return True
                        if k == 3:
                            if r2 != 0:
                                r = r1 / r2
                                if r > 23.99 and r < 24.01:
                                    return True
                        if k == 4:
                            r = r2 - r1
                            if r == 24:
                                return True
                        if k == 5:
                            if r1 != 0:
                                r = r2 / r1
                                if r > 23.99 and r < 24.01:
                                    return True
        # 2 + 1 + 1
        for a, b, c, d in [(n1, n2, n3, n4), (n1, n3, n2, n4), (n1, n4, n2, n3), (n2, n3, n1, n4), (n2, n4, n3, n1), (n3, n4, n1, n2)]:
            for i in range(6):
                if i == 0:
                    r1 = a + b
                if i == 1:
                    r1 = a - b
                if i == 2:
                    r1 = a * b
                if i == 3:
                    r1 = a / b
                if i == 4:
                    r1 = b - a
                if i == 5:
                    r1 = b / a
                for e, f in [(c, d), (d, c)]:
                    for j in range(6):
                        r2 = r1
                        if j == 0:
                            r2 += e
                        if j == 1:
                            r2 -= e
                        if j == 2:
                            r2 *= e
                        if j == 3:
                            r2 /= e
                        if j == 4:
                            r2 = e - r2
                        if j == 5:
                            if r2 != 0:
                                r2 = e / r2
                            else:
                                continue
                        for k in range(6):
                            r = r2
                            if k == 0:
                                r += f
                                if r == 24:
                                    return True
                            if k == 1:
                                r -= f
                                if r == 24:
                                    return True
                            if k == 2:
                                r *= f
                                if r == 24:
                                    return True
                            if k == 3:
                                r /= f
                                if  r > 23.99 and r < 24.01:
                                    return True
                            if k == 4:
                                r = f - r
                                if r == 24:
                                    return True
                            if k == 5:
                                if r != 0:
                                    r = f / r
                                    if r > 23.99 and r < 24.01:
                                        return True
        return False
# @lc code=end

