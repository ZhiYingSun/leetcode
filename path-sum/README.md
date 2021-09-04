<h2>112. Path Sum</h2><h3>Easy</h3><hr><div><p>Given the <code>root</code> of a binary tree and an integer <code>targetSum</code>, return <code>true</code> if the tree has a <strong>root-to-leaf</strong> path such that adding up all the values along the path equals <code>targetSum</code>.</p>

<p>A <strong>leaf</strong> is a node with no children.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum1.jpg" style="width: 500px; height: 356px;">
<pre><strong>Input:</strong> root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/01/18/pathsum2.jpg">
<pre><strong>Input:</strong> root = [1,2,3], targetSum = 5
<strong>Output:</strong> false
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> root = [1,2], targetSum = 0
<strong>Output:</strong> false
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[0, 5000]</code>.</li>
	<li><code>-1000 &lt;= Node.val &lt;= 1000</code></li>
	<li><code>-1000 &lt;= targetSum &lt;= 1000</code></li>
</ul>
</div>

<p><strong>Base case</strong></p>

1. This question wants to find a path from node to the leaf, so the node who satisfies must be a leaf (not node.left and not nood.right)
2. I want to recursively subtract the sum by current node's value, so the leaf node of correct path must have the same value of its assigned sum

<p><strong>Recursive step</strong></p>

1. We want to traverse all the nodes, so node.left and node.right must be called parallelly
2. One valid path is enough, so we want to use or to connect two "branches"
3. Considering each node as the root of its children, sum should be modified from its parent
