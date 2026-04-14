This practice exam is designed to help you prepare for your 14 multiple-choice and 6 free-response questions, covering all eight units of your Mathematics II course. [cite_start]I have generated 10-15 questions per unit, categorized by difficulty (Easy, Medium, Hard), using the definitions, theorems, and examples from your textbook[cite: 654].

Since you are eventually putting these into a website, I have formatted the math using **LaTeX**, which is the industry standard for displaying math symbols (like $\lambda$, $A^T$, or $\sum$). You can save this text as a **Markdown (.md)** file or a **PDF** to ensure the symbols render correctly.

---

# Mathematics II Exam Prep: Practice Questions & Solutions

## Unit 1: Introduction to Matrices

**Easy**
1. [cite_start]**MCQ:** Which of the following defines an $m \times n$ matrix? [cite: 686, 687]
   * A) A square arrangement of real numbers with $m$ columns.
   * B) A rectangular numbering scheme of real numbers with $m$ rows and $n$ columns.
   * C) A single row of $n$ numbers.
   * D) A vertical column of $m$ numbers.
2. [cite_start]**MCQ:** If matrix $A$ is $2 \times 3$, what are the dimensions of its transpose $A^T$? [cite: 703, 704]
   * A) $2 \times 3$
   * B) $3 \times 3$
   * C) $3 \times 2$
   * D) $2 \times 2$
3. [cite_start]**MCQ:** In the matrix $A = (a_{ij})$, what does the index $i$ represent? [cite: 694]
   * A) Column index
   * B) Diagonal index
   * C) Row index
   * D) Scalar index

**Medium**
4. [cite_start]**MCQ:** Given $A = \begin{pmatrix} 2 & 1 \\ -1 & 3 \end{pmatrix}$ and $B = \begin{pmatrix} 3 & -2 \\ 0.3 & 0 \end{pmatrix}$, find $A + B$. [cite: 732, 738]
   * A) $\begin{pmatrix} 5 & -1 \\ -0.7 & 3 \end{pmatrix}$
   * B) $\begin{pmatrix} 5 & 3 \\ 1.3 & 3 \end{pmatrix}$
   * C) $\begin{pmatrix} -1 & 3 \\ -1.3 & 3 \end{pmatrix}$
   * D) $\begin{pmatrix} 6 & -2 \\ -0.3 & 0 \end{pmatrix}$
5. [cite_start]**MCQ:** What is the result of the scalar multiplication $1.2 \cdot \begin{pmatrix} 70 & 10 \\ 140 & 30 \end{pmatrix}$? [cite: 750, 757]
   * A) $\begin{pmatrix} 84 & 12 \\ 168 & 36 \end{pmatrix}$
   * B) $\begin{pmatrix} 71.2 & 11.2 \\ 141.2 & 31.2 \end{pmatrix}$
   * C) $\begin{pmatrix} 84 & 10 \\ 140 & 36 \end{pmatrix}$
   * D) $\begin{pmatrix} 70 & 12 \\ 168 & 30 \end{pmatrix}$
6. [cite_start]**MCQ:** Which statement correctly distinguishes between scalar multiplication and the dot product? [cite: 749, 760]
   * A) Scalar multiplication results in a matrix; the dot product results in a scalar.
   * B) Both result in a scalar.
   * C) Scalar multiplication is only for vectors; dot product is for any matrix.
   * D) There is no difference.
7. [cite_start]**MCQ:** A square matrix $A$ is called symmetric if: [cite: 739]
   * A) $A = -A^T$
   * B) $A = A^T$
   * C) $A = 0$
   * D) $A = E$

**Hard**
8. **Free Response:** Calculate the dot product of $\vec{a}^T = (3, -2, 1, 0, 4)$ and $\vec{b} = (4, -3, 2, 1, 4)$. [cite_start]Show your steps. [cite: 760]
9. [cite_start]**Free Response:** Decompose the matrix $A = \begin{pmatrix} 5 & -3 \\ -1 & 4 \end{pmatrix}$ into a symmetric matrix $B$ and a skew-symmetric matrix $C$ such that $A = B + C$. [cite: 742, 758]
10. [cite_start]**Free Response:** Prove using the definitions that $(A + B)^T = A^T + B^T$ for any two $m \times n$ matrices $A$ and $B$. [cite: 754]

---

## Unit 2: Inverting Matrices

**Easy**
1. [cite_start]**MCQ:** Two matrices $A$ and $B$ can be multiplied ($A \cdot B$) only if: [cite: 777]
   * A) They are of the same type.
   * B) The number of columns in $A$ equals the number of rows in $B$.
   * C) Both are square matrices.
   * D) $A$ is a row vector and $B$ is a column vector.
2. [cite_start]**MCQ:** What is the identity matrix $E$ of the 3rd order? [cite: 730]
   * A) $\begin{pmatrix} 0 & 0 & 1 \\ 0 & 1 & 0 \\ 1 & 0 & 0 \end{pmatrix}$
   * B) $\begin{pmatrix} 1 & 1 & 1 \\ 1 & 1 & 1 \\ 1 & 1 & 1 \end{pmatrix}$
   * C) $\begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$
   * D) $\begin{pmatrix} 1 & 0 & 0 \\ 1 & 0 & 0 \\ 1 & 0 & 0 \end{pmatrix}$

**Medium**
3. [cite_start]**MCQ:** Calculate $C = A \cdot B$ where $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}$ and $B = \begin{pmatrix} 1 & 2 \\ 3 & 4 \\ 5 & 6 \end{pmatrix}$. [cite: 778]
   * A) $\begin{pmatrix} 22 & 28 \\ 49 & 64 \end{pmatrix}$
   * B) $\begin{pmatrix} 14 & 32 \\ 32 & 77 \end{pmatrix}$
   * C) $\begin{pmatrix} 6 & 12 \\ 15 & 18 \end{pmatrix}$
   * D) Multiplication is not possible.
4. [cite_start]**MCQ:** Which of the following is an "unusual" property of matrix multiplication? [cite: 60, 771]
   * A) Associative law: $A(BC) = (AB)C$
   * B) Distributive law: $A(B+C) = AB + AC$
   * C) Non-commutativity: $A \cdot B \neq B \cdot A$ (generally)
   * D) $1 \cdot A = A$
5. [cite_start]**MCQ:** A $2 \times 2$ matrix $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ is invertible if and only if: [cite: 64]
   * A) $ad - bc = 0$
   * B) $ad - bc \neq 0$
   * C) $a + d \neq 0$
   * D) It is a diagonal matrix.
6. [cite_start]**MCQ:** For a diagonal matrix $D$, the inverse $D^{-1}$ exists if: [cite: 65, 716]
   * A) All elements on the main diagonal are zero.
   * B) All elements on the main diagonal are non-zero.
   * C) At least one element on the main diagonal is 1.
   * D) It is a square matrix.

**Hard**
7. **Free Response:** Using Falk’s scheme, multiply a $4 \times 3$ matrix $A$ by a $3 \times 2$ matrix $B$. [cite_start]Explain how you find the element $c_{32}$ in the resulting matrix. [cite: 780, 783]
8. [cite_start]**Free Response:** Explain the concept of an inverse matrix $A^{-1}$ and state the condition $A \cdot A^{-1} = ?$. [cite: 63, 771]
9. [cite_start]**Free Response:** If $A = \begin{pmatrix} 2 & 0 \\ 0 & 5 \end{pmatrix}$, calculate $A^{-1}$. [cite: 65, 771]

---

## Unit 3: Systems of Linear Equations

**Easy**
1. [cite_start]**MCQ:** How many solutions can a system of linear equations have? [cite: 84]
   * A) Exactly one or none.
   * B) Exactly one, none, or infinitely many.
   * C) Always exactly one.
   * D) Only two.
2. **MCQ:** The Gaussian algorithm uses "elementary row operations." [cite_start]Which of these is NOT one? [cite: 85]
   * A) Swapping two equations.
   * B) Multiplying an equation by a non-zero number.
   * C) Adding a multiple of one row to another.
   * D) Multiplying two different rows together.

**Medium**
3. [cite_start]**MCQ:** If a matrix is "singular," it means: [cite: 87]
   * A) It has an inverse.
   * B) It does not have an inverse.
   * C) It has exactly one row.
   * D) It is an identity matrix.
4. [cite_start]**MCQ:** During the Gaussian algorithm, if you arrive at a row like $(0 \ 0 \ 0 \ | \ 1)$, what does this indicate about the system? [cite: 84]
   * A) Infinitely many solutions.
   * B) Exactly one solution.
   * C) No solution.
   * D) The inverse exists.

**Hard**
5. **Free Response:** Explain how the Gaussian algorithm can be used to determine the inverse of a square matrix $A$. [cite_start]What is the setup? [cite: 69, 87]
6. **Free Response:** Given a $3 \times 3$ matrix $B$, you perform row operations on $(B | E)$ and reach $(E | B^{-1})$. [cite_start]If you instead reach a state where the left side has a row of zeros, what is your conclusion about $B$? [cite: 82]

---

## Unit 4: Introduction to Graphs

**Easy**
1. [cite_start]**MCQ:** In a graph $G = (V, E)$, what do $V$ and $E$ represent? [cite: 92]
   * A) Volume and Energy
   * B) Variables and Equations
   * C) Vertices (Nodes) and Edges
   * D) Vectors and Elements
2. [cite_start]**MCQ:** What is the "degree" of a node in an undirected graph? [cite: 122, 159]
   * A) The number of nodes in the graph.
   * B) The number of edges incident to that node.
   * C) The length of the shortest path.
   * D) The number of loops.

**Medium**
3. [cite_start]**MCQ:** According to the Handshaking Lemma, the sum of all node degrees in a graph is equal to: [cite: 123, 160]
   * A) The number of nodes.
   * B) The number of edges.
   * C) Twice the number of edges.
   * D) Half the number of edges.
4. [cite_start]**MCQ:** A graph is called "regular of degree $g$" if: [cite: 139]
   * A) Every node has degree $g$.
   * B) It has $g$ nodes.
   * C) It has $g$ edges.
   * D) It is a complete graph.
5. [cite_start]**MCQ:** If two graphs are isomorphic, their adjacency matrices are: [cite: 162]
   * A) Always different.
   * B) Equal (given the correct node ordering).
   * C) Inverses of each other.
   * D) Transposes of each other.

**Hard**
6. **Free Response:** A party has 11 people. Each person claims to know exactly 5 others. [cite_start]Use the handshaking lemma to prove whether this is possible. [cite: 124, 126]
7. [cite_start]**Free Response:** Construct the adjacency matrix for "Santa's House" (a 5-node graph) as described in the text. [cite: 157]
8. [cite_start]**Free Response:** Define a "planar graph" and state Euler's polyhedral formula ($v - e + f = ?$). [cite: 142, 149]

---

## Unit 5: Shortest Path Problem

**Easy**
1. [cite_start]**MCQ:** A directed graph is also called a: [cite: 261]
   * A) Weighted graph
   * B) Digraph
   * C) Subgraph
   * D) Shadow graph
2. [cite_start]**MCQ:** In a weighted graph, the numbers assigned to edges usually represent: [cite: 305]
   * A) Node IDs
   * B) Degrees
   * C) Costs, distances, or times
   * D) Number of nodes

**Medium**
3. [cite_start]**MCQ:** Dijkstra’s algorithm is used to find: [cite: 226, 670]
   * A) The longest path in a graph.
   * B) The shortest path from a starting node to all other nodes.
   * C) Whether a graph is Hamiltonian.
   * D) The minimum spanning tree.
4. [cite_start]**MCQ:** A digraph is "strongly connected" if: [cite: 264]
   * A) Its shadow graph is connected.
   * B) There is a directed path from every node $u$ to every node $v$ and vice versa.
   * C) It has no loops.
   * D) All nodes have the same outdegree.

**Hard**
5. [cite_start]**Free Response:** Describe the first two steps of Dijkstra’s algorithm when finding the shortest journey from Munich to other cities. [cite: 226, 227]
6. [cite_start]**Free Response:** Explain the difference between a "weakly connected" and a "strongly connected" digraph. [cite: 261, 264]

---

## Unit 6: The Königsberg Bridge Problem

**Easy**
1. [cite_start]**MCQ:** An Eulerian circuit must pass through: [cite: 295, 296]
   * A) Every node exactly once.
   * B) Every edge exactly once and return to the start.
   * C) Only the bridge edges.
   * D) The shortest path.
2. [cite_start]**MCQ:** Who developed an algorithm to find an Eulerian circuit? [cite: 280, 281]
   * A) Dijkstra
   * B) Kruskal
   * C) Hierholzer
   * D) Ore

**Medium**
3. [cite_start]**MCQ:** A connected undirected graph has an Eulerian circuit if and only if: [cite: 298, 299]
   * A) It has exactly two odd-degree nodes.
   * B) All its nodes have even degrees.
   * C) It is a complete graph.
   * D) It is a tree.
4. [cite_start]**MCQ:** The "Postman Problem" seeks a closed walk that: [cite: 301, 306]
   * A) Visits every node exactly once with minimum weight.
   * B) Covers every edge at least once with minimum total weight.
   * C) Is the shortest path between two specific nodes.
   * D) Finds the spanning tree.

**Hard**
5. [cite_start]**Free Response:** Briefly describe the "onion skin" approach of Hierholzer’s algorithm. [cite: 280, 281]
6. [cite_start]**Free Response:** If a graph is not Eulerian because it has two odd-degree nodes, how can it be made Eulerian to solve a routing problem? [cite: 299]

---

## Unit 7: Traveling Salesman Problem (TSP)

**Easy**
1. [cite_start]**MCQ:** A Hamiltonian cycle visits: [cite: 392]
   * A) Every edge exactly once.
   * B) Every node exactly once and returns to the start.
   * C) Only the main diagonal nodes.
   * D) All nodes with odd degrees.
2. [cite_start]**MCQ:** Which problem is NP-complete, meaning no exact algorithm solves it quickly for large graphs? [cite: 436]
   * A) Shortest Path
   * B) Traveling Salesman Problem
   * C) Finding a Spanning Tree
   * D) Matrix Addition

**Medium**
3. [cite_start]**MCQ:** What is the main difference between a Hamiltonian cycle problem and the Traveling Salesman Problem? [cite: 430]
   * A) One is for directed graphs, the other is not.
   * B) TSP involves a weighted graph and seeks the minimum weight.
   * C) Hamiltonian cycles only exist in bipartite graphs.
   * D) There is no difference.
4. [cite_start]**MCQ:** According to Dirac's Condition, a simple graph with $n \geq 3$ nodes is Hamiltonian if every node has a degree $d(v)$ such that: [cite: 462]
   * A) $d(v) \geq n$
   * B) $d(v) \geq n/2$
   * C) $d(v) \leq 2$
   * D) $d(v) = n-1$

**Hard**
5. [cite_start]**Free Response:** Why are "heuristics" used to solve the Traveling Salesman Problem in large-scale applications like PCB production? [cite: 441, 444]
6. [cite_start]**Free Response:** State Kuratowski’s Theorem regarding graph planarity and the "minor" graphs $K_5$ or $K_{3,3}$. [cite: 389, 458]

---

## Unit 8: Trees

**Easy**
1. [cite_start]**MCQ:** A tree is defined as a: [cite: 618]
   * A) Disconnected graph with no cycles.
   * B) Connected graph that does not contain a closed set of edges (cycles).
   * C) Complete graph with $n$ nodes.
   * D) Directed graph with only one path.
2. [cite_start]**MCQ:** A tree with $n$ nodes always has exactly how many edges? [cite: 619]
   * A) $n$
   * B) $n + 1$
   * C) $n - 1$
   * D) $2n$

**Medium**
3. [cite_start]**MCQ:** In a binary search tree, for any node, the key in the left subtree is: [cite: 531]
   * A) Larger than the node's key.
   * B) Smaller than the node's key.
   * C) Equal to the node's key.
   * D) Zero.
4. [cite_start]**MCQ:** Kruskal’s algorithm is used to find: [cite: 628]
   * A) The shortest path.
   * B) The minimum spanning tree.
   * C) The Hamiltonian cycle.
   * D) The Eulerian circuit.
5. [cite_start]**MCQ:** Which traversal of a binary search tree outputs keys in ascending order? [cite: 532, 624]
   * A) Pre-order
   * B) Post-order
   * C) In-order
   * D) Level-order

**Hard**
6. [cite_start]**Free Response:** Explain the difference between "Breadth-First Search" and "Depth-First Search" when finding a spanning tree. [cite: 585, 588, 627]
7. **Free Response:** Describe the steps of Kruskal’s algorithm. [cite_start]How do you decide which edge to add next? [cite: 606, 611, 628]

---

## Solutions

### Unit 1
1. [cite_start]**B** [cite: 686]
2. [cite_start]**C** [cite: 704]
3. [cite_start]**C** [cite: 694]
4. [cite_start]**A** ($2+3, 1-2, -1+0.3, 3+0$) [cite: 738]
5. [cite_start]**A** [cite: 757]
6. [cite_start]**A** [cite: 749, 760]
7. [cite_start]**B** [cite: 739]
8. [cite_start]**36** ($3 \cdot 4 + (-2)(-3) + 1 \cdot 2 + 0 \cdot 1 + 4 \cdot 4 = 12 + 6 + 2 + 0 + 16$) [cite: 760]
9. [cite_start]$B = \begin{pmatrix} 5 & -2 \\ -2 & 4 \end{pmatrix}$, $C = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ [cite: 759]
10. [cite_start]Show that $(a_{ij} + b_{ij})$ in the $i$-th row, $j$-th column of $A+B$ becomes the $j$-th row, $i$-th column in $(A+B)^T$, which is $a_{ji} + b_{ji}$ (the sum of elements in $A^T$ and $B^T$). [cite: 754]

### Unit 2
1. [cite_start]**B** [cite: 777]
2. [cite_start]**C** [cite: 730]
3. [cite_start]**A** [cite: 778]
4. [cite_start]**C** [cite: 60]
5. [cite_start]**B** [cite: 64]
6. [cite_start]**B** [cite: 65]
7. [cite_start]$c_{32}$ is the scalar product of the 3rd row of $A$ and the 2nd column of $B$. [cite: 783]
8. [cite_start]$A \cdot A^{-1} = E$ [cite: 63, 771]
9. [cite_start]$\begin{pmatrix} 1/2 & 0 \\ 0 & 1/5 \end{pmatrix}$ [cite: 65]

### Unit 3
1. [cite_start]**B** [cite: 84]
2. [cite_start]**D** [cite: 85]
3. [cite_start]**B** [cite: 87]
4. [cite_start]**C** [cite: 84]
5. [cite_start]Setup $(A | E)$ and use row operations to transform it to $(E | A^{-1})$. [cite: 87]
6. [cite_start]$B$ is singular (it has no inverse). [cite: 82, 87]

### Unit 4
1. [cite_start]**C** [cite: 92]
2. [cite_start]**B** [cite: 122]
3. [cite_start]**C** [cite: 160]
4. [cite_start]**A** [cite: 139]
5. [cite_start]**B** [cite: 162]
6. Sum of degrees $= 11 \cdot 5 = 55$. [cite_start]Since 55 is odd, this is impossible by the Handshaking Lemma (sum must be even). [cite: 123, 126]
7. [cite_start]See Matrix in[cite: 157].
8. Planar: can be drawn without edge intersections. [cite_start]Formula: $v - e + f = 2$. [cite: 142, 149]

### Unit 5
1. [cite_start]**B** [cite: 261]
2. [cite_start]**C** [cite: 305]
3. [cite_start]**B** [cite: 226]
4. [cite_start]**B** [cite: 264]
5. 1: Note journey times to adjacent nodes and pick the shortest (e.g., Landshut). [cite_start]2: Check if routes through that node shorten others. [cite: 226, 227]
6. Weakly: Shadow graph is connected. [cite_start]Strongly: Directed paths exist between all pairs. [cite: 261, 264]

### Unit 6
1. [cite_start]**B** [cite: 295]
2. [cite_start]**C** [cite: 280]
3. [cite_start]**B** [cite: 298]
4. [cite_start]**B** [cite: 306]
5. [cite_start]Start with a closed walk, then "nest" additional closed walks into it at shared nodes until all edges are used. [cite: 280, 281]
6. [cite_start]Add a "multiple edge" between the two odd-degree nodes to make all degrees even. [cite: 299]

### Unit 7
1. [cite_start]**B** [cite: 392]
2. [cite_start]**B** [cite: 436]
3. [cite_start]**B** [cite: 430]
4. [cite_start]**B** [cite: 462]
5. Exact solutions take too long (non-polynomial complexity). [cite_start]Heuristics find "good enough" solutions in acceptable time. [cite: 437, 441]
6. [cite_start]A graph is planar iff it doesn't contain $K_5$ or $K_{3,3}$ as a minor. [cite: 389]

### Unit 8
1. [cite_start]**B** [cite: 618]
2. [cite_start]**C** [cite: 619]
3. [cite_start]**B** [cite: 531]
4. [cite_start]**B** [cite: 628]
5. [cite_start]**C** [cite: 532]
6. BFS: Explores all neighbors of a node first (level by level). [cite_start]DFS: Follows a path as deep as possible before backtracking. [cite: 585, 588]
7. Sort all edges by weight. Add the smallest edge that does not create a cycle. [cite_start]Repeat until $n-1$ edges are chosen. [cite: 606, 628]