# questions.py

questions_data = [
    # --- Unit 1: Introduction to Matrices ---
    {
        "id": 1, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "Which of the following defines an $m \\times n$ matrix?", 
        "answer": "A rectangular numbering scheme of real numbers with $m$ rows and $n$ columns."
    },
    {
        "id": 2, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "If matrix $A$ is $2 \\times 3$, what are the dimensions of its transpose $A^T$?", 
        "answer": "$3 \\times 2$"
    },
    {
        "id": 3, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "In the matrix $A = (a_{ij})$, what does the index $i$ represent?", 
        "answer": "Row index"
    },
    {
        "id": 4, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "Given $A = \\begin{pmatrix} 2 & 1 \\\\ -1 & 3 \\end{pmatrix}$ and $B = \\begin{pmatrix} 3 & -2 \\\\ 0.3 & 0 \\end{pmatrix}$, find $A + B$.", 
        "answer": "$\\begin{pmatrix} 5 & -1 \\\\ -0.7 & 3 \\end{pmatrix}$"
    },
    {
        "id": 5, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "What is the result of the scalar multiplication $1.2 \\cdot \\begin{pmatrix} 70 & 10 \\\\ 140 & 30 \\end{pmatrix}$?", 
        "answer": "$\\begin{pmatrix} 84 & 12 \\\\ 168 & 36 \\end{pmatrix}$"
    },
    {
        "id": 6, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "Which statement correctly distinguishes between scalar multiplication and the dot product?", 
        "answer": "Scalar multiplication results in a matrix; the dot product results in a scalar."
    },
    {
        "id": 7, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "A square matrix $A$ is called symmetric if:", 
        "answer": "$A = A^T$"
    },
    {
        "id": 8, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "Calculate the dot product of $\\vec{a}^T = (3, -2, 1, 0, 4)$ and $\\vec{b} = (4, -3, 2, 1, 4)$.", 
        "answer": "$36$ (Calculated as $3 \\cdot 4 + (-2)(-3) + 1 \\cdot 2 + 0 \\cdot 1 + 4 \\cdot 4$)"
    },
    {
        "id": 9, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "Decompose the matrix $A = \\begin{pmatrix} 5 & -3 \\\\ -1 & 4 \\end{pmatrix}$ into a symmetric matrix $B$ and a skew-symmetric matrix $C$ such that $A = B + C$.", 
        "answer": "$B = \\begin{pmatrix} 5 & -2 \\\\ -2 & 4 \\end{pmatrix}$, $C = \\begin{pmatrix} 0 & -1 \\\\ 1 & 0 \\end{pmatrix}$"
    },
    {
        "id": 10, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "Prove using the definitions that $(A + B)^T = A^T + B^T$ for any two $m \\times n$ matrices $A$ and $B$.", 
        "answer": "The $ij$-th element of $(A+B)^T$ is the $ji$-th element of $A+B$, which is $a_{ji} + b_{ji}$. This is the sum of the $ij$-th elements of $A^T$ and $B^T$."
    },

    # --- Unit 2: Inverting Matrices ---
    {
        "id": 11, 
        "unit": 2,
        "difficulty": "Easy",
        "question": "Two matrices $A$ and $B$ can be multiplied ($A \\cdot B$) only if:", 
        "answer": "The number of columns in $A$ equals the number of rows in $B$."
    },
    {
        "id": 12, 
        "unit": 2,
        "difficulty": "Easy",
        "question": "What is the identity matrix $E$ of the 3rd order?", 
        "answer": "$\\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$"
    },
    {
        "id": 13, 
        "unit": 2,
        "difficulty": "Medium",
        "question": "Calculate $C = A \\cdot B$ where $A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\end{pmatrix}$ and $B = \\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\\\ 5 & 6 \\end{pmatrix}$.", 
        "answer": "$\\begin{pmatrix} 22 & 28 \\\\ 49 & 64 \\end{pmatrix}$"
    },
    {
        "id": 14, 
        "unit": 2,
        "difficulty": "Medium",
        "question": "Which of the following is an 'unusual' property of matrix multiplication?", 
        "answer": "Non-commutativity: $A \\cdot B \\neq B \\cdot A$ (generally)."
    },
    {
        "id": 15, 
        "unit": 2,
        "difficulty": "Medium",
        "question": "A $2 \\times 2$ matrix $A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ is invertible if and only if:", 
        "answer": "$ad - bc \\neq 0$"
    },
    {
        "id": 16, 
        "unit": 2,
        "difficulty": "Medium",
        "question": "For a diagonal matrix $D$, the inverse $D^{-1}$ exists if:", 
        "answer": "All elements on the main diagonal are non-zero."
    },
    {
        "id": 17, 
        "unit": 2,
        "difficulty": "Hard",
        "question": "Using Falk’s scheme, explain how you find the element $c_{32}$ in the resulting matrix $C = A \\cdot B$.", 
        "answer": "$c_{32}$ is the scalar (dot) product of the 3rd row of $A$ and the 2nd column of $B$."
    },
    {
        "id": 18, 
        "unit": 2,
        "difficulty": "Hard",
        "question": "Explain the concept of an inverse matrix $A^{-1}$ and state the condition $A \\cdot A^{-1} = ?$.", 
        "answer": "An inverse matrix undoes the operation of matrix $A$ such that $A \\cdot A^{-1} = E$ (the identity matrix)."
    },
    {
        "id": 19, 
        "unit": 2,
        "difficulty": "Hard",
        "question": "If $A = \\begin{pmatrix} 2 & 0 \\\\ 0 & 5 \\end{pmatrix}$, calculate $A^{-1}$.", 
        "answer": "$\\begin{pmatrix} 1/2 & 0 \\\\ 0 & 1/5 \\end{pmatrix}$"
    },

    # --- Unit 3: Systems of Linear Equations ---
    {
        "id": 20, 
        "unit": 3,
        "difficulty": "Easy",
        "question": "How many solutions can a system of linear equations have?", 
        "answer": "Exactly one, none, or infinitely many."
    },
    {
        "id": 21, 
        "unit": 3,
        "difficulty": "Easy",
        "question": "The Gaussian algorithm uses 'elementary row operations.' Which of these is NOT one?", 
        "answer": "Multiplying two different rows together."
    },
    {
        "id": 22, 
        "unit": 3,
        "difficulty": "Medium",
        "question": "If a matrix is 'singular,' it means:", 
        "answer": "It does not have an inverse."
    },
    {
        "id": 23, 
        "unit": 3,
        "difficulty": "Medium",
        "question": "During the Gaussian algorithm, if you arrive at a row like $(0 \\ 0 \\ 0 \\ | \\ 1)$, what does this indicate?", 
        "answer": "The system has no solution."
    },
    {
        "id": 24, 
        "unit": 3,
        "difficulty": "Hard",
        "question": "Explain how the Gaussian algorithm determines the inverse of a square matrix $A$.", 
        "answer": "Set up the augmented matrix $(A | E)$ and use row operations to transform it into $(E | A^{-1})$."
    },
    {
        "id": 25, 
        "unit": 3,
        "difficulty": "Hard",
        "question": "If you reach a state where the left side of $(A | E)$ has a row of zeros, what is the conclusion about $A$?", 
        "answer": "Matrix $A$ is singular and has no inverse."
    },

    # --- Unit 4: Introduction to Graphs ---
    {
        "id": 26, 
        "unit": 4,
        "difficulty": "Easy",
        "question": "In a graph $G = (V, E)$, what do $V$ and $E$ represent?", 
        "answer": "Vertices (Nodes) and Edges."
    },
    {
        "id": 27, 
        "unit": 4,
        "difficulty": "Easy",
        "question": "What is the 'degree' of a node in an undirected graph?", 
        "answer": "The number of edges incident to that node."
    },
    {
        "id": 28, 
        "unit": 4,
        "difficulty": "Medium",
        "question": "According to the Handshaking Lemma, the sum of all node degrees is:", 
        "answer": "Twice the number of edges."
    },
    {
        "id": 29, 
        "unit": 4,
        "difficulty": "Medium",
        "question": "A graph is called 'regular of degree $g$' if:", 
        "answer": "Every node has degree $g$."
    },
    {
        "id": 30, 
        "unit": 4,
        "difficulty": "Medium",
        "question": "If two graphs are isomorphic, their adjacency matrices are:", 
        "answer": "Equal, provided the node ordering is consistent."
    },
    {
        "id": 31, 
        "unit": 4,
        "difficulty": "Hard",
        "question": "A party has 11 people. Each claims to know exactly 5 others. Is this possible?", 
        "answer": "No. Sum of degrees = $11 \\cdot 5 = 55$. By the Handshaking Lemma, the sum must be even."
    },
    {
        "id": 32, 
        "unit": 4,
        "difficulty": "Hard",
        "question": "Define a 'planar graph' and state Euler's polyhedral formula.", 
        "answer": "A graph that can be drawn in a plane without edges crossing. Formula: $v - e + f = 2$."
    },

    # --- Unit 5: Shortest Path Problem ---
    {
        "id": 33, 
        "unit": 5,
        "difficulty": "Easy",
        "question": "A directed graph is also called a:", 
        "answer": "Digraph"
    },
    {
        "id": 34, 
        "unit": 5,
        "difficulty": "Easy",
        "question": "In a weighted graph, the numbers assigned to edges represent:", 
        "answer": "Costs, distances, or times."
    },
    {
        "id": 35, 
        "unit": 5,
        "difficulty": "Medium",
        "question": "Dijkstra’s algorithm is used to find:", 
        "answer": "The shortest path from a starting node to all other nodes."
    },
    {
        "id": 36, 
        "unit": 5,
        "difficulty": "Medium",
        "question": "A digraph is 'strongly connected' if:", 
        "answer": "There is a directed path from every node $u$ to every node $v$ and vice versa."
    },
    {
        "id": 37, 
        "unit": 5,
        "difficulty": "Hard",
        "question": "Explain the difference between 'weakly connected' and 'strongly connected' digraphs.", 
        "answer": "Weakly: The underlying undirected graph is connected. Strongly: All nodes are reachable from each other via directed paths."
    },

    # --- Unit 6: The Königsberg Bridge Problem ---
    {
        "id": 38, 
        "unit": 6,
        "difficulty": "Easy",
        "question": "An Eulerian circuit must pass through:", 
        "answer": "Every edge exactly once and return to the start."
    },
    {
        "id": 39, 
        "unit": 6,
        "difficulty": "Easy",
        "question": "Who developed an algorithm to find an Eulerian circuit?", 
        "answer": "Hierholzer"
    },
    {
        "id": 40, 
        "unit": 6,
        "difficulty": "Medium",
        "question": "A connected undirected graph has an Eulerian circuit if and only if:", 
        "answer": "All its nodes have even degrees."
    },
    {
        "id": 41, 
        "unit": 6,
        "difficulty": "Medium",
        "question": "The 'Postman Problem' seeks a closed walk that:", 
        "answer": "Covers every edge at least once with minimum total weight."
    },
    {
        "id": 42, 
        "unit": 6,
        "difficulty": "Hard",
        "question": "Briefly describe the 'onion skin' approach of Hierholzer’s algorithm.", 
        "answer": "Find a closed walk, then recursively find and 'nest' additional closed walks from unused edges into the main circuit."
    },
    {
        "id": 43, 
        "unit": 6,
        "difficulty": "Hard",
        "question": "If a graph has exactly two odd-degree nodes, how do you make it Eulerian for routing?", 
        "answer": "Add a duplicate (multiple) edge between the two odd-degree nodes."
    },

    # --- Unit 7: Traveling Salesman Problem (TSP) ---
    {
        "id": 44, 
        "unit": 7,
        "difficulty": "Easy",
        "question": "A Hamiltonian cycle visits:", 
        "answer": "Every node exactly once and returns to the start."
    },
    {
        "id": 45, 
        "unit": 7,
        "difficulty": "Easy",
        "question": "Which problem is considered NP-complete (hard to solve exactly)?", 
        "answer": "Traveling Salesman Problem (TSP)."
    },
    {
        "id": 46, 
        "unit": 7,
        "difficulty": "Medium",
        "question": "What is the difference between TSP and a Hamiltonian cycle problem?", 
        "answer": "TSP involves finding the minimum total weight in a weighted graph."
    },
    {
        "id": 47, 
        "unit": 7,
        "difficulty": "Medium",
        "question": "According to Dirac's Condition, a graph is Hamiltonian if every node's degree $d(v)$ is:", 
        "answer": "$d(v) \\geq n/2$ (where $n$ is the number of nodes)."
    },
    {
        "id": 48, 
        "unit": 7,
        "difficulty": "Hard",
        "question": "Why are heuristics used for large-scale TSP problems?", 
        "answer": "Because exact solutions take exponential time; heuristics find good solutions in a reasonable timeframe."
    },
    {
        "id": 49, 
        "unit": 7,
        "difficulty": "Hard",
        "question": "State Kuratowski’s Theorem regarding graph planarity.", 
        "answer": "A graph is planar iff it contains no subgraph that is a minor of $K_5$ or $K_{3,3}$."
    },

    # --- Unit 8: Trees ---
    {
        "id": 50, 
        "unit": 8,
        "difficulty": "Easy",
        "question": "A tree is defined as a:", 
        "answer": "Connected graph with no cycles."
    },
    {
        "id": 51, 
        "unit": 8,
        "difficulty": "Easy",
        "question": "A tree with $n$ nodes has how many edges?", 
        "answer": "$n - 1$"
    },
    {
        "id": 52, 
        "unit": 8,
        "difficulty": "Medium",
        "question": "In a binary search tree, the key in the left subtree is always:", 
        "answer": "Smaller than the node's key."
    },
    {
        "id": 53, 
        "unit": 8,
        "difficulty": "Medium",
        "question": "Kruskal’s algorithm is used to find:", 
        "answer": "The minimum spanning tree."
    },
    {
        "id": 54, 
        "unit": 8,
        "difficulty": "Medium",
        "question": "Which binary tree traversal outputs keys in ascending order?", 
        "answer": "In-order traversal."
    },
    {
        "id": 55, 
        "unit": 8,
        "difficulty": "Hard",
        "question": "Explain the difference between BFS and DFS for finding spanning trees.", 
        "answer": "BFS explores level-by-level (all neighbors first); DFS explores as deep as possible before backtracking."
    },
    {
        "id": 56, 
        "unit": 8,
        "difficulty": "Hard",
        "question": "Describe the core step of Kruskal's algorithm.", 
        "answer": "Sort edges by weight and add the smallest edge that does not form a cycle until $n-1$ edges are picked."
    }
]