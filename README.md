# Leetcode

* Starting from 2020/08/02
* Leetcode practice with Python (for now)
* Daily Challenge + Selected Questions From [algorithm-pattern](https://github.com/greyireland/algorithm-pattern)
* Using Leetcode Plugin for [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=LeetCode.vscode-leetcode)

## Solutions

|  ID  |               English Title               |      中文题目名称      |                         Category                          |                          Notes URI                           |          Description           |
| :--: | :---------------------------------------: | :--------------------: | :-------------------------------------------------------: | :----------------------------------------------------------: | :----------------------------: |
|  17  |   Letter Combinations of a Phone Number   |   电话号码的字母组合   |            回溯法，递归 / Backtrack，Recursion            |                          回溯+递归                           |   Daily Challenge 2020/08/26   |
|  20  |             Valid Parentheses             |       有效的括号       |                        Stack / 栈                         |                         用栈实现配对                         |   Daily Challenge 2020/08/14   |
|  28  |            Implement strStr()             |     实现 strStr()      |                      String / 字符串                      |                         循环遍历即可                         | algorithm-pattern: quick start |
|  43  |             Multiply Strings              |       字符串相乘       |                      String / 字符串                      | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/43.multiply-strings.md) |   Daily Challenge 2020/08/13   |
|  78  |                  Subsets                  |          子集          |                     回溯 / backtrack                      | 标准回溯法，[参考解析](https://leetcode-cn.com/problems/subsets/solution/78zi-ji-hui-su-fa-xiang-jie-pythonshi-xi-2aul/) | algorithm-pattern: quick start |
|  93  |           Restore IP Addresses            |       复原IP地址       |                     Recursion / 递归                      | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/93.restore-ip-addresses.md) |   Daily Challenge 2020/08/09   |
|  98  |        Validate Binary Search Tree        |     验证二叉搜索树     |              Binary Search Tree / 二叉搜索树              | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/98.validate-binary-search-tree.md) | algorithm-pattern: binary tree |
|  99  |        Recover Binary Search Tree         |     恢复二叉搜索树     |                     BST / 二叉搜索树                      | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/99.recover-binary-search-tree.md) |   Daily Challenge 2020/08/08   |
| 100  |                 Same Tree                 |        相同的树        |                   Binary Tree / 二叉树                    |                         递归遍历即可                         |   Daily Challenge 2020/08/07   |
| 102  |     Binary Tree Level Order Traversal     |    二叉树的层序遍历    |             Binary Tree, Queue / 二叉树，队列             | 从第一层的惟一的根节点开始，每次遍历访问一层树的节点，并将每个节点的左右子节点按顺序放入队列，直到队列为空 | algorithm-pattern: binary tree |
| 103  | Binary Tree Zigzag Level Order Traversal  |   二叉树蛇形层序遍历   |             Binary Tree, Queue / 二叉树，队列             | 对102中的每层中间结果进行一次判断，若层数为奇数，则翻转该层结果，翻转操作为result = result[::-1] | algorithm-pattern: binary tree |
| 107  |   Binary Tree Level Order Traversal ii    |   二叉树的层序遍历ii   |             Binary Tree, Queue / 二叉树，队列             |   对102中得到的结果进行数组翻转即可: result = result[::-1]   | algorithm-pattern: binary tree |
| 104  |       Maximum Depth of Binary Tree        |    二叉树的最大深度    |                Binary Tree / 二叉树，分治                 |                      递归左右子树再合并                      | algorithm-pattern: binary tree |
| 109  | Convert Sorted List to Binary Search Tree | 有序链表转换二叉搜索树 | Binary Tree, Linked List, Recursion / 二叉树，链表 ，递归 |                    获取链表中点，递归建树                    |   Daily Challenge 2020/08/18   |
| 110  |           Balanced Binary Tree            |       平衡二叉树       |                   Binary Tree / 二叉树                    |                         递归求树深度                         |   Daily Challenge 2020/08/17   |
| 111  |       Minimum Depth of Binary Tree        |    二叉树的最小深度    |                   Binary Tree / 二叉树                    |                       注意特殊情况处理                       |   Daily Challenge 2020/08/21   |
| 114  |    Flatten Binary Tree to Linked List     |    二叉树展开为链表    |                   Binary Tree / 二叉树                    | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/114.flatten-binary-tree-to-linked-list.md) |   Daily Challenge 2020/08/02   |
| 124  |       Binary Tree Maximum Path Sum        |  二叉树中的最大路径和  |                Binary Tree / 二叉树， 分治                |                     递归+更新全局最大值                      | algorithm-pattern: binary tree |
| 130  |            Surrounded Regions             |      被围绕的区域      |                   BFS, DFS / 深搜，广搜                   | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/130.surrounded-regions.md) |   Daily Challenge 2020/08/11   |
| 133  |                Clone Graph                |         克隆图         |                   BFS, DFS / 深搜，广搜                   | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/133.clone-graph.md) |   Daily Challenge 2020/08/12   |
| 201  |       Bitwise AND of Numbers Range        |     数字范围按位与     |                     Bitwise / 位操作                      | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/201.bitwise-and-of-numbers-range.md) |   Daily Challenge 2020/08/23   |
| 207  |              Course Schedule              |         课程表         |         Topological Sorting, Graph / 拓扑排序, 图         | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/207.course-schedule.md) |   Daily Challenge 2020/08/04   |
| 214  |            Shortest Palindrome            |       最短回文串       |                      String / 字符串                      |                  翻转，再去掉与原串重合部分                  |   Daily Challenge 2020/08/29   |
| 236  |  Lowest Common Ancestor of a Binary Tree  |  二叉树的最近公共祖先  |                Bianry Tree / 二叉树，分治                 | 从root开始递归二叉树，是pq或pq的公共祖先则返回root，否则返回null | algorithm-pattern: binary tree |
| 332  |           Reconstruct Itinerary           |      重新安排行程      |                DFS, AdjList / 深搜，邻接表                | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/332.reconstruct-itinerary.md) |   Daily Challenge 2020/08/27   |
| 336  |             Palindrome Pairs              |         回文对         |          Hash Table, Trie Tree / 哈希表，字典树           | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/336.palindrome-pairs.md) |   Daily Challenge 2020/08/06   |
| 337  |             House Robber III              |        打家劫舍        |            DP, Binary Tree / 动态规划，二叉树             | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/337.house-robber-iii.md) |   Daily Challenge 2020/08/05   |
| 415  |                Add Strings                |       字符串相加       |           String, Two Pointers / 字符串，双指针           | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/415.add-strings.md) |   Daily Challenge 2020/08/03   |
| 459  |        Repeated Substring Pattern         |     重复的子字符串     |                      String / 字符串                      |                        循环取子串检验                        |   Daily Challenge 2020/08/24   |
| 491  |          Increasing Subsequences          |       递增子序列       |                DFS, Recursion / 深搜，递归                | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/491.increasing-subsequences.md) |   Daily Challenge 2020/08/25   |
| 529  |                Minesweeper                |        扫雷游戏        |                   BFS, DFS / 深搜，广搜                   |                       注意搜索不要重复                       |   Daily Challenge 2020/08/20   |
| 546  |               Remove Boxes                |        移除盒子        |                       DP / 动态规划                       |                                                              |   Daily Challenge 2020/08/15   |
| 557  |       Reverse Words in a String III       | 反转字符串中的单词 III |                      String / 字符串                      |                       split翻转再join                        |   Daily Challenge 2020/08/30   |
| 647  |          Palindromic Substrings           |        回文子串        |                      String / 字符串                      |                          纯暴力即可                          |   Daily Challenge 2020/08/19   |
| 657  |          Robot Return to Origin           |   机器人能否返回原点   |                        Loop / 循环                        |                         循环计数即可                         |   Daily Challenge 2020/08/28   |
| 679  |                  24 Game                  |        24点游戏        |           Recursion or enumeration / 递归或枚举           |                            枚举法                            |   Daily Challenge 2020/08/22   |
| 696  |          Count Binary Substrings          |     计数二进制子串     |                      String / 字符串                      | [md](https://github.com/williamlwclwc/leetcode/blob/master/Notes/696.count-binary-substrings.md) |   Daily Challenge 2020/08/10   |
| 701  |     Insert into a Binary Search Tree      | 二叉搜索树中的插入操作 |              Binary Search Tree / 二叉搜索树              | 找到可插入的叶节点位置None(当前节点小于插入值，则向左子树root.left继续搜索，当前节点大于插入值，则向右子树root.right继续搜索，由于每个节点数值唯一，不考虑等于的情况)，将root.left / root.right的None改为要插入的节点即可 | algorithm-pattern: binary tree |
| 733  |                Flood Fill                 |        图像渲染        |                     Recursion / 递归                      |                           递归即可                           |   Daily Challenge 2020/08/16   |
| 841  |              Keys and Rooms               |       钥匙和房间       |                   DFS, BFS / 深搜，广搜                   |                       转换为图搜索即可                       |   Daily Challenge 2020/08/31   |
