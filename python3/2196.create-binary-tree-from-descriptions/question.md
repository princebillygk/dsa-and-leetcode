# [2196. Create Binary Tree From Descriptions][link] (Medium)

[link]: https://leetcode.com/problems/create-binary-tree-from-descriptions/

You are given a 2D integer array `descriptions` where `descriptions[i] = [parentᵢ, childᵢ, isLeftᵢ]`
indicates that `parentᵢ` is the **parent** of `childᵢ` in a **binary** tree of **unique** values.
Furthermore,

- If `isLeftᵢ == 1`, then `childᵢ` is the left child of `parentᵢ`.
- If `isLeftᵢ == 0`, then `childᵢ` is the right child of `parentᵢ`.

Construct the binary tree described by `descriptions` and return its **root**.

The test cases will be generated such that the binary tree is **valid**.

**Example 1:**

![](https://assets.leetcode.com/uploads/2022/02/09/example1drawio.png)

```
Input: descriptions = [[20,15,1],[20,17,0],[50,20,1],[50,80,0],[80,19,1]]
Output: [50,20,80,15,17,19]
Explanation: The root node is the node with value 50 since it has no parent.
The resulting binary tree is shown in the diagram.

```

**Example 2:**

![](https://assets.leetcode.com/uploads/2022/02/09/example2drawio.png)

```
Input: descriptions = [[1,2,1],[2,3,0],[3,4,1]]
Output: [1,2,null,null,3,4]
Explanation: The root node is the node with value 1 since it has no parent.
The resulting binary tree is shown in the diagram.

```

**Constraints:**

- `1 <= descriptions.length <= 10⁴`
- `descriptions[i].length == 3`
- `1 <= parentᵢ, childᵢ <= 10⁵`
- `0 <= isLeftᵢ <= 1`
- The binary tree described by `descriptions` is valid.
