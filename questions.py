# questions.py

questions_data = [
    # --- Unit 1: Introduction to Matrices ---
    {
        "id": 1, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "Which of the following describes an $m \\times n$ matrix?", 
        "answer": "A rectangular numbering scheme of real numbers consisting of $m$ rows and $n$ columns.",
        "options": [
            "A single row of real numbers.",
            "A rectangular numbering scheme of real numbers consisting of $m$ rows and $n$ columns.",
            "A set of vectors that must always be square.",
            "A collection of numbers where the number of rows always equals the number of columns."
        ]
    },
    {
        "id": 2, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "In the double index notation $a_{ij}$ for matrix elements, what does the first index $i$ represent?", 
        "answer": "The row index.",
        "options": [
            "The column index.",
            "The row index.",
            "The value of the element.",
            "The total number of elements in the matrix."
        ]
    },
    {
        "id": 3, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "What is a scalar?", 
        "answer": "A real number.",
        "options": [
            "The identity matrix of 1st order.",
            "A natural number.",
            "A real number.",
            "A column vector with at least 2 elements."
        ]
    },
    {
        "id": 4, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "What is the result of transposing a matrix $A$ twice, i.e., $(A^T)^T$?", 
        "answer": "The initial matrix $A$.",
        "options": [
            "The zero matrix.",
            "The identity matrix.",
            "The initial matrix $A$.",
            "The negative of the initial matrix $-A$."
        ]
    },
    {
        "id": 5, 
        "unit": 1,
        "difficulty": "Easy",
        "question": "A matrix with exactly one column is known as a:", 
        "answer": "Column vector.",
        "options": [
            "Row vector.",
            "Square matrix.",
            "Column vector.",
            "Zero matrix."
        ]
    },
    {
        "id": 6, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "Under what condition can two matrices $A$ and $B$ be added?", 
        "answer": "They must be of the same type (same number of rows and columns).",
        "options": [
            "They must both be square matrices.",
            "They must be of the same type (same number of rows and columns).",
            "The number of columns in $A$ must equal the number of rows in $B$.",
            "One must be the transpose of the other."
        ]
    },
    {
        "id": 7, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "Which of the following is an identity matrix $E$ of the 3rd order?", 
        "answer": "A $3 \\times 3$ matrix with 1s on the main diagonal and 0s elsewhere.",
        "options": [
            "A $3 \\times 3$ matrix with all elements equal to 1.",
            "A $3 \\times 3$ matrix with 1s on the main diagonal and 0s elsewhere.",
            "A $3 \\times 1$ column vector with all elements equal to 1.",
            "A diagonal matrix where all diagonal elements are 0."
        ]
    },
    {
        "id": 8, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "If matrix $A = \\begin{pmatrix} 2 & 4 \\\\ 6 & 8 \\end{pmatrix}$, what is the result of the scalar multiplication $0.5 \\cdot A$?", 
        "answer": "\\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}",
        "options": [
            "\\begin{pmatrix} 1 & 2 \\\\ 3 & 4 \\end{pmatrix}",
            "\\begin{pmatrix} 2.5 & 4.5 \\\\ 6.5 & 8.5 \\end{pmatrix}",
            "\\begin{pmatrix} 4 & 8 \\\\ 12 & 16 \\end{pmatrix}",
            "The identity matrix $E$."
        ]
    },
    {
        "id": 9, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "A square matrix $A$ is considered symmetric if:", 
        "answer": "$A = A^T$",
        "options": [
            "$A = -A^T$",
            "$A = E$",
            "$A = A^T$",
            "All its elements are positive."
        ]
    },
    {
        "id": 10, 
        "unit": 1,
        "difficulty": "Medium",
        "question": "Which law states that $A + B = B + A$ for matrices of the same type?", 
        "answer": "The commutative law.",
        "options": [
            "The associative law.",
            "The distributive law.",
            "The commutative law.",
            "The transposition law."
        ]
    },
    {
        "id": 11, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "What is the defining characteristic of an upper (right) triangular matrix?", 
        "answer": "All elements below the main diagonal are zero ($a_{ij} = 0$ for all $i > j$).",
        "options": [
            "All elements above the main diagonal are zero ($a_{ij} = 0$ for all $i < j$).",
            "All elements below the main diagonal are zero ($a_{ij} = 0$ for all $i > j$).",
            "Only the main diagonal contains non-zero elements.",
            "All elements on the main diagonal are zero."
        ]
    },
    {
        "id": 12, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "Given the vectors $\\vec{a}=\\begin{pmatrix} 6 \\\\ 5 \\\\ -3 \\end{pmatrix}$ and $\\vec{b}=\\begin{pmatrix} 1 \\\\ -11 \\\\ 0.5 \\end{pmatrix}$, what is the result of the scalar product $\\vec{b} \\cdot \\vec{a}$?", 
        "answer": "-50.5",
        "options": [
            "-95.5",
            "-50.5",
            "This operation is not defined.",
            "62.5"
        ]
    },
    {
        "id": 13, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "According to the decomposition theorem, how is the skew-symmetric component $C$ of a square matrix $A$ calculated?", 
        "answer": "$C = \\frac{1}{2}(A - A^T)$",
        "options": [
            "$C = \\frac{1}{2}(A + A^T)$",
            "$C = A^T$",
            "$C = \\frac{1}{2}(A - A^T)$",
            "$C = A - E$"
        ]
    },
    {
        "id": 14, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "Which of the following must be true for a skew-symmetric matrix?", 
        "answer": "All elements on the main diagonal must be zero.",
        "options": [
            "All elements on the main diagonal must be ones.",
            "The matrix must be a diagonal matrix.",
            "All elements on the main diagonal must be zero.",
            "It is only defined for $2 \\times 2$ matrices."
        ]
    },
    {
        "id": 15, 
        "unit": 1,
        "difficulty": "Hard",
        "question": "What is the difference between scalar multiplication and the scalar product?", 
        "answer": "Scalar multiplication results in a matrix; the scalar product results in a real number.",
        "options": [
            "Scalar multiplication is only for vectors; scalar product is for matrices.",
            "Scalar multiplication results in a matrix; the scalar product results in a real number.",
            "There is no difference; they are two names for the same operation.",
            "Scalar multiplication is commutative; the scalar product is not."
        ]
    },
    # --- Unit 2: Inverting Matrices ---
    {
        "id": 16,
        "unit": 2,
        "difficulty": "Easy",
        "question": "What is the primary condition for two matrices $A$ and $B$ to be multiplied ($A \\cdot B$)?",
        "answer": "The number of columns in $A$ must equal the number of rows in $B$.",
        "options": [
            "They must both be square matrices of the same order.",
            "They must have the same total number of elements.",
            "The number of columns in $A$ must equal the number of rows in $B$.",
            "The number of rows in $A$ must equal the number of columns in $B$."
        ]
    },
    {
        "id": 17,
        "unit": 2,
        "difficulty": "Easy",
        "question": "If $A$ is an $m \\times n$ matrix and $B$ is an $n \\times p$ matrix, what is the dimension of the resulting matrix $C = A \\cdot B$?",
        "answer": "$m \\times p$",
        "options": ["$n \\times n$", "$m \\times p$", "$p \\times m$", "$n \\times p$"]
    },
    {
        "id": 18,
        "unit": 2,
        "difficulty": "Easy",
        "question": "Which of the following is the 'neutral element' for matrix multiplication?",
        "answer": "The identity matrix $E$.",
        "options": [
            "The zero matrix $0$.", 
            "The identity matrix $E$.", 
            "The transposed matrix $A^T$.", 
            "A matrix where all elements are 1."
        ]
    },
    {
        "id": 19,
        "unit": 2,
        "difficulty": "Easy",
        "question": "What is true about the product of a matrix $A$ and the identity matrix $E$?",
        "answer": "$A \\cdot E = E \\cdot A = A$",
        "options": [
            "$A \\cdot E = E$", 
            "$A \\cdot E = 0$", 
            "$A \\cdot E = E \\cdot A = A$", 
            "$A \\cdot E = A^T$"
        ]
    },
    {
        "id": 20,
        "unit": 2,
        "difficulty": "Easy",
        "question": "The inverse matrix $A^{-1}$ exists for a square matrix $A$ only if:",
        "answer": "$A$ is non-singular.",
        "options": [
            "$A$ is a zero matrix.", 
            "$A$ is non-singular.", 
            "$A$ is a row vector.", 
            "$A$ has only positive elements."
        ]
    },
    {
        "id": 21,
        "unit": 2,
        "difficulty": "Medium",
        "question": "Which algebraic property does matrix multiplication generally NOT satisfy?",
        "answer": "Commutative law ($A \\cdot B = B \\cdot A$)",
        "options": [
            "Associative law", 
            "Distributive law", 
            "Commutative law ($A \\cdot B = B \\cdot A$)", 
            "The rule for multiplication by a scalar"
        ]
    },
    {
        "id": 22,
        "unit": 2,
        "difficulty": "Medium",
        "question": "Which property allows us to write $(A \\cdot B) \\cdot C = A \\cdot (B \\cdot C)$?",
        "answer": "Associative law",
        "options": [
            "Commutative law", 
            "Distributive law", 
            "Associative law", 
            "Transposition law"
        ]
    },
    {
        "id": 23,
        "unit": 2,
        "difficulty": "Medium",
        "question": "What is the formula for the inverse of a $2 \\times 2$ matrix $A = \\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$?",
        "answer": "$A^{-1} = \\frac{1}{ad - bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$",
        "options": [
            "$A^{-1} = \\frac{1}{ad + bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$",
            "$A^{-1} = \\frac{1}{ad - bc} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$",
            "$A^{-1} = \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$",
            "$A^{-1} = \\frac{1}{ad - bc} \\begin{pmatrix} a & c \\\\ b & d \\end{pmatrix}$"
        ]
    },
    {
        "id": 24,
        "unit": 2,
        "difficulty": "Medium",
        "question": "If $A$ and $B$ are invertible matrices, what is $(A \\cdot B)^{-1}$ equal to?",
        "answer": "$B^{-1} \\cdot A^{-1}$",
        "options": [
            "$A^{-1} \\cdot B^{-1}$", 
            "$B^{-1} \\cdot A^{-1}$", 
            "$(A+B)^{-1}$", 
            "$A \\cdot B$"
        ]
    },
    {
        "id": 25,
        "unit": 2,
        "difficulty": "Medium",
        "question": "What happens when you multiply a matrix $A$ by its inverse $A^{-1}$?",
        "answer": "You get the identity matrix $E$.",
        "options": [
            "You get the zero matrix.", 
            "You get the identity matrix $E$.", 
            "You get the transpose $A^T$.", 
            "The operation results in a scalar value."
        ]
    },
    {
        "id": 26,
        "unit": 2,
        "difficulty": "Hard",
        "question": "Which of the following matrix power equations is NOT satisfied for a square matrix $A$?",
        "answer": "$A^{(2^3)} = (A^2)^3$",
        "options": [
            "$A^{12} = (A^3)^4$", 
            "$A^{(2^3)} = (A^2)^3$", 
            "$A^{12} = A^{10} \\cdot A^2$", 
            "$A^8 = (A^2 \\cdot A^2)^2$"
        ]
    },
    {
        "id": 27,
        "unit": 2,
        "difficulty": "Hard",
        "question": "Under what condition does $(A \\cdot B)^T = A^T \\cdot B^T$ hold?",
        "answer": "Only if $A$ and $B$ commute ($A \\cdot B = B \\cdot A$).",
        "options": [
            "It is true for all matrices $A$ and $B$.",
            "Only if $A$ and $B$ are the same dimension.",
            "Only if $A$ and $B$ commute ($A \\cdot B = B \\cdot A$).",
            "Only if $A$ is an identity matrix."
        ]
    },
    {
        "id": 28,
        "unit": 2,
        "difficulty": "Hard",
        "question": "What is the transpose of a product $(A \\cdot B)^T$ always equal to?",
        "answer": "$B^T \\cdot A^T$",
        "options": [
            "$A^T \\cdot B^T$", 
            "$B^T \\cdot A^T$", 
            "$(B \\cdot A)^T$", 
            "$A \\cdot B$"
        ]
    },
    {
        "id": 29,
        "unit": 2,
        "difficulty": "Hard",
        "question": "Which of the following is true regarding the zero divisor property in matrices?",
        "answer": "The product of two non-zero matrices can be the zero matrix ($A \\cdot B = 0$).",
        "options": [
            "If $A \\cdot B = 0$, then either $A=0$ or $B=0$.",
            "The product of two non-zero matrices can be the zero matrix ($A \\cdot B = 0$).",
            "Matrix multiplication always follows the zero-product property of real numbers.",
            "A zero matrix can never be the result of multiplying two square matrices."
        ]
    },
    {
        "id": 30,
        "unit": 2,
        "difficulty": "Hard",
        "question": "What is the result of applying the inverse operation twice, i.e., $(A^{-1})^{-1}$?",
        "answer": "The initial matrix $A$.",
        "options": [
            "The identity matrix $E$.",
            "The transpose $A^T$.",
            "The initial matrix $A$.",
            "The negative inverse $-A^{-1}$."
        ]
    }, 
    # --- Unit 3: Systems of Linear Equations ---
    {
        "id": 31,
        "unit": 3,
        "difficulty": "Easy",
        "question": "Which of the following describes a system of linear equations in matrix form?",
        "answer": "$A \\cdot \\vec{x} = \\vec{b}$",
        "options": [
            "$A + \\vec{x} = \\vec{b}$",
            "$A \\cdot \\vec{x} = \\vec{b}$",
            "$\\vec{x}^T \\cdot A = \\vec{b}$",
            "$A \\cdot B = E$"
        ]
    },
    {
        "id": 32,
        "unit": 3,
        "difficulty": "Easy",
        "question": "Which case for the solvability of a linear system of equations does NOT exist?",
        "answer": "There are exactly two solutions.",
        "options": [
            "There is no solution.",
            "There is exactly one solution.",
            "There are infinitely many solutions.",
            "There are exactly two solutions."
        ]
    },
    {
        "id": 33,
        "unit": 3,
        "difficulty": "Easy",
        "question": "What is the primary goal of the Gaussian algorithm (elimination method)?",
        "answer": "To transform the coefficient matrix into an upper triangular form.",
        "options": [
            "To calculate the transpose of the matrix.",
            "To transform the coefficient matrix into an upper triangular form.",
            "To multiply two matrices together.",
            "To find the sum of all elements in the vector $\\vec{b}$."
        ]
    },
    {
        "id": 34,
        "unit": 3,
        "difficulty": "Easy",
        "question": "In a system $A \\cdot \\vec{x} = \\vec{b}$, if the matrix $A$ is square and its inverse $A^{-1}$ exists, how can $\\vec{x}$ be calculated?",
        "answer": "$\\vec{x} = A^{-1} \\cdot \\vec{b}$",
        "options": [
            "$\\vec{x} = \\vec{b} \\cdot A^{-1}$",
            "$\\vec{x} = A \\cdot \\vec{b}$",
            "$\\vec{x} = A^{-1} \\cdot \\vec{b}$",
            "$\\vec{x} = \\vec{b} / A$"
        ]
    },
    {
        "id": 35,
        "unit": 3,
        "difficulty": "Easy",
        "question": "What happens to the solutions of a system if you swap two equations?",
        "answer": "The solution set remains unchanged.",
        "options": [
            "The solutions are doubled.",
            "The solution set remains unchanged.",
            "The system becomes unsolvable.",
            "All variables change signs."
        ]
    },
    {
        "id": 36,
        "unit": 3,
        "difficulty": "Medium",
        "question": "A system of equations has no solution if the Gaussian algorithm results in a row like:",
        "answer": "$(0 \\ 0 \\ 0 \\ | \\ 3)$",
        "options": [
            "$(1 \\ 0 \\ 0 \\ | \\ 0)$",
            "$(0 \\ 0 \\ 0 \\ | \\ 0)$",
            "$(0 \\ 0 \\ 0 \\ | \\ 3)$",
            "$(0 \\ 1 \\ 0 \\ | \\ 1)$"
        ]
    },
    {
        "id": 37,
        "unit": 3,
        "difficulty": "Medium",
        "question": "When using the Gaussian algorithm to find the inverse of matrix $A$, you start with the augmented matrix:",
        "answer": "$(A \\ | \\ E)$",
        "options": [
            "$(A \\ | \\ 0)$",
            "$(A \\ | \\ \\vec{b})$",
            "$(A \\ | \\ E)$",
            "$(E \\ | \\ A)$"
        ]
    },
    {
        "id": 38,
        "unit": 3,
        "difficulty": "Medium",
        "question": "A linear system with more variables than equations ($n > m$) usually results in:",
        "answer": "Either no solution or infinitely many solutions.",
        "options": [
            "Exactly one solution.",
            "Either no solution or infinitely many solutions.",
            "Always a unique solution.",
            "The zero solution only."
        ]
    },
    {
        "id": 39,
        "unit": 3,
        "difficulty": "Medium",
        "question": "Which operation is NOT allowed in the Gaussian algorithm?",
        "answer": "Multiplying two rows by each other.",
        "options": [
            "Multiplying a row by a non-zero scalar.",
            "Swapping two rows.",
            "Adding a multiple of one row to another row.",
            "Multiplying two rows by each other."
        ]
    },
    {
        "id": 40,
        "unit": 3,
        "difficulty": "Medium",
        "question": "If the Gaussian algorithm leads to a row of zeros $(0 \\ 0 \\ 0 \\ | \\ 0)$, it typically indicates:",
        "answer": "The system has infinitely many solutions (if no contradictions exist elsewhere).",
        "options": [
            "The system is inconsistent.",
            "The system has infinitely many solutions (if no contradictions exist elsewhere).",
            "The variables must all be zero.",
            "The matrix $A$ is non-singular."
        ]
    },
    {
        "id": 41,
        "unit": 3,
        "difficulty": "Hard",
        "question": "For which value of $s$ is the system $A = \\begin{pmatrix} 1 & -s \\\\ s & -1 \\end{pmatrix}, \\vec{b} = \\begin{pmatrix} -3 \\\\ -2 \\end{pmatrix}$ NOT solvable or has no unique solution?",
        "answer": "$s = 1, s = -1$",
        "options": ["$s = 0$", "$s = 3, s = 2$", "$s = 1, s = -1$", "For all $s \\in \\mathbb{R}$"]
    },
    {
        "id": 42,
        "unit": 3,
        "difficulty": "Hard",
        "question": "What is the solution set for the system $A = \\begin{pmatrix} 12 & -8 \\\\ 15 & -10 \\end{pmatrix}, \\vec{b} = \\begin{pmatrix} 28 \\\\ 35 \\end{pmatrix}$?",
        "answer": "$\\vec{x} = \\begin{pmatrix} \\frac{7}{3} + \\frac{2}{3}t \\\\ t \\end{pmatrix}, t \\in \\mathbb{R}$",
        "options": [
            "$\\vec{x} = \\begin{pmatrix} 3 \\\\ 1 \\end{pmatrix}$",
            "This system is not solvable.",
            "$\\vec{x} = \\begin{pmatrix} \\frac{7}{3} + \\frac{2}{3}t \\\\ t \\end{pmatrix}, t \\in \\mathbb{R}$",
            "$\\vec{x} = \\begin{pmatrix} 0 \\\\ 0 \\end{pmatrix}$"
        ]
    },
    {
        "id": 43,
        "unit": 3,
        "difficulty": "Hard",
        "question": "Three wheat rolls cost as much as two whole grain rolls. Five wheat rolls are 15 cents more expensive than three whole grain rolls. What are the prices?",
        "answer": "Wheat: 30 cents, Whole grain: 45 cents",
        "options": [
            "Wheat: 20 cents, Whole grain: 30 cents",
            "Wheat: 30 cents, Whole grain: 45 cents",
            "Wheat: 15 cents, Whole grain: 10 cents",
            "Wheat: 45 cents, Whole grain: 30 cents"
        ]
    },
    {
        "id": 44,
        "unit": 3,
        "difficulty": "Hard",
        "question": "When applying the Gaussian algorithm to find $A^{-1}$, if you cannot reach the identity matrix $E$ on the left side, what does it mean?",
        "answer": "The matrix $A$ is singular and has no inverse.",
        "options": [
            "You made a calculation error.",
            "The matrix $A$ is singular and has no inverse.",
            "The inverse is the zero matrix.",
            "The inverse is equal to the transpose."
        ]
    },
    {
        "id": 45,
        "unit": 3,
        "difficulty": "Hard",
        "question": "In the context of the Gaussian algorithm, what is 'back-substitution'?",
        "answer": "The process of solving for variables starting from the bottom row of an upper triangular matrix.",
        "options": [
            "Replacing variables with their initial values.",
            "The process of solving for variables starting from the bottom row of an upper triangular matrix.",
            "Adding the first row to the last row.",
            "A method to check if the matrix is symmetric."
        ]
    },
    # --- Unit 4: Introduction to Graphs ---
    {
        "id": 46,
        "unit": 4,
        "difficulty": "Easy",
        "question": "In graph theory, what is the 'degree' of a node?",
        "answer": "The number of edges incident to the node.",
        "options": [
            "The total number of nodes in the graph.",
            "The number of edges incident to the node.",
            "The weight assigned to an edge.",
            "The number of loops at a node."
        ]
    },
    {
        "id": 47,
        "unit": 4,
        "difficulty": "Easy",
        "question": "Which of the following defines a 'simple graph'?",
        "answer": "A graph with no loops or multiple edges between the same two nodes.",
        "options": [
            "A graph with only one node.",
            "A graph that has no edges.",
            "A graph with no loops or multiple edges between the same two nodes.",
            "A graph where every node is connected to every other node."
        ]
    },
    {
        "id": 48,
        "unit": 4,
        "difficulty": "Easy",
        "question": "What does the handshaking lemma state about the sum of the degrees of all nodes in a graph?",
        "answer": "It is equal to twice the number of edges.",
        "options": [
            "It is equal to the number of edges.",
            "It is equal to the square of the number of nodes.",
            "It is equal to twice the number of edges.",
            "It is always an odd number."
        ]
    },
    {
        "id": 49,
        "unit": 4,
        "difficulty": "Easy",
        "question": "An adjacency matrix for a simple undirected graph is always:",
        "answer": "Symmetric.",
        "options": [
            "Skew-symmetric.",
            "Symmetric.",
            "A row vector.",
            "Diagonal."
        ]
    },
    {
        "id": 50,
        "unit": 4,
        "difficulty": "Easy",
        "question": "If an entry $a_{ij}$ in an adjacency matrix is 1, what does it signify?",
        "answer": "There is an edge between node $i$ and node $j$.",
        "options": [
            "Node $i$ and node $j$ are the same node.",
            "There is no path between node $i$ and node $j$.",
            "There is an edge between node $i$ and node $j$.",
            "The graph is disconnected."
        ]
    },
    {
        "id": 51,
        "unit": 4,
        "difficulty": "Medium",
        "question": "If a graph has 5 nodes and the degrees of the nodes are 2, 3, 2, 1, and 4, how many edges does the graph have?",
        "answer": "6",
        "options": ["12", "5", "6", "10"]
    },
    {
        "id": 52,
        "unit": 4,
        "difficulty": "Medium",
        "question": "Two graphs are considered 'isomorphic' if:",
        "answer": "There is a one-to-one correspondence between their node sets that preserves adjacency.",
        "options": [
            "They have the same number of nodes, regardless of edges.",
            "They are both simple and connected.",
            "There is a one-to-one correspondence between their node sets that preserves adjacency.",
            "One is a subgraph of the other."
        ]
    },
    {
        "id": 53,
        "unit": 4,
        "difficulty": "Medium",
        "question": "What is the degree of every node in a complete graph $K_n$?",
        "answer": "$n - 1$",
        "options": ["$n$", "$n - 1$", "$n/2$", "1"]
    },
    {
        "id": 54,
        "unit": 4,
        "difficulty": "Medium",
        "question": "In an adjacency matrix of a simple graph (no loops), what are the elements on the main diagonal?",
        "answer": "All zeros.",
        "options": [
            "All ones.",
            "All zeros.",
            "The degrees of the nodes.",
            "The number of edges in the graph."
        ]
    },
    {
        "id": 55,
        "unit": 4,
        "difficulty": "Medium",
        "question": "According to the handshaking lemma, why is it impossible to have a graph with an odd number of odd-degree nodes?",
        "answer": "The sum of degrees must be even, and an odd number of odd values would result in an odd sum.",
        "options": [
            "Because edges must always be square.",
            "The sum of degrees must be even, and an odd number of odd values would result in an odd sum.",
            "Odd-degree nodes can only exist in directed graphs.",
            "Nodes must always have an even degree in simple graphs."
        ]
    },
    {
        "id": 56,
        "unit": 4,
        "difficulty": "Hard",
        "question": "A graph has 10 edges and every node has a degree of 4. How many nodes does this graph have?",
        "answer": "5",
        "options": ["4", "5", "10", "20"]
    },
    {
        "id": 57,
        "unit": 4,
        "difficulty": "Hard",
        "question": "Which of the following is an 'invariant' of isomorphic graphs (a property they must share)?",
        "answer": "The sequence of the degrees of the nodes.",
        "options": [
            "The specific names/labels of the nodes.",
            "The way the graph is drawn on paper.",
            "The sequence of the degrees of the nodes.",
            "The size of the adjacency matrix only."
        ]
    },
    {
        "id": 58,
        "unit": 4,
        "difficulty": "Hard",
        "question": "How can you determine the number of walks of length 2 between node $i$ and node $j$ using the adjacency matrix $A$?",
        "answer": "By looking at the entry in the $i$-th row and $j$-th column of the matrix $A^2$.",
        "options": [
            "By adding the entries of $A$.",
            "By calculating $A^T$.",
            "By looking at the entry in the $i$-th row and $j$-th column of the matrix $A^2$.",
            "By finding the inverse matrix $A^{-1}$."
        ]
    },
    {
        "id": 59,
        "unit": 4,
        "difficulty": "Hard",
        "question": "What characterizes a bipartite graph?",
        "answer": "The node set can be split into two disjoint sets such that no two nodes within the same set are connected by an edge.",
        "options": [
            "Every node has exactly two edges.",
            "The graph can be split into two identical subgraphs.",
            "The node set can be split into two disjoint sets such that no two nodes within the same set are connected by an edge.",
            "The adjacency matrix is an identity matrix."
        ]
    },
    {
        "id": 60,
        "unit": 4,
        "difficulty": "Hard",
        "question": "In a graph with $n$ nodes and $e$ edges, what is the sum of the entries in its adjacency matrix?",
        "answer": "$2e$",
        "options": ["$e$", "$2e$", "$n^2$", "$n+e$"]
    },
    # --- Unit 5: Shortest Path Problem ---
    {
        "id": 61,
        "unit": 5,
        "difficulty": "Easy",
        "question": "What is the primary difference between an undirected graph and a directed graph (digraph)?",
        "answer": "In a digraph, edges have a specific direction, meaning an edge from A to B is not the same as an edge from B to A.",
        "options": [
            "Digraphs cannot have weights on edges.",
            "In a digraph, edges have a specific direction, meaning an edge from A to B is not the same as an edge from B to A.",
            "Digraphs must always be complete graphs.",
            "Undirected graphs cannot contain loops, but digraphs must."
        ]
    },
    {
        "id": 62,
        "unit": 5,
        "difficulty": "Easy",
        "question": "In the context of weighted graphs, what does the 'weight' of an edge typically represent?",
        "answer": "A numerical value representing cost, distance, or time associated with that edge.",
        "options": [
            "The number of nodes the edge connects.",
            "The degree of the starting node.",
            "A numerical value representing cost, distance, or time associated with that edge.",
            "The total number of edges in the graph."
        ]
    },
    {
        "id": 63,
        "unit": 5,
        "difficulty": "Easy",
        "question": "What is the goal of Dijkstra's algorithm?",
        "answer": "To find the shortest path from a starting node to all other nodes in a graph with non-negative edge weights.",
        "options": [
            "To find the longest possible path in a graph.",
            "To find the shortest path from a starting node to all other nodes in a graph with non-negative edge weights.",
            "To determine if a graph is Hamiltonian.",
            "To calculate the inverse of the adjacency matrix."
        ]
    },
    {
        "id": 64,
        "unit": 5,
        "difficulty": "Easy",
        "question": "When initializing Dijkstra’s algorithm, what distance value is assigned to all nodes except the starting node?",
        "answer": "Infinity ($\infty$ or 'inf')",
        "options": ["Zero", "One", "Infinity ($\infty$ or 'inf')", "The number of nodes in the graph"]
    },
    {
        "id": 65,
        "unit": 5,
        "difficulty": "Easy",
        "question": "In a digraph, if an edge exists from node $u$ to node $v$, node $v$ is called the:",
        "answer": "Successor of $u$.",
        "options": ["Predecessor of $u$.", "Successor of $u$.", "Parent of $u$.", "Isomorph of $u$."]
    },
    {
        "id": 66,
        "unit": 5,
        "difficulty": "Medium",
        "question": "How does Dijkstra’s algorithm decide which node to 'visit' or 'settle' next?",
        "answer": "It chooses the unvisited node with the smallest current distance from the start node.",
        "options": [
            "It chooses the node with the highest degree.",
            "It chooses nodes in alphabetical or numerical order.",
            "It chooses the unvisited node with the smallest current distance from the start node.",
            "It chooses the node furthest from the start node."
        ]
    },
    {
        "id": 67,
        "unit": 5,
        "difficulty": "Medium",
        "question": "If you are updating distances in Dijkstra's algorithm and find that $d(current) + weight(current, neighbor) < d(neighbor)$, what should you do?",
        "answer": "Update $d(neighbor)$ with the new, smaller value.",
        "options": [
            "Ignore the new value and keep the old one.",
            "Update $d(neighbor)$ with the new, smaller value.",
            "Add both values together.",
            "Mark the neighbor as unvisitable."
        ]
    },
    {
        "id": 68,
        "unit": 5,
        "difficulty": "Medium",
        "question": "In a weighted digraph, an adjacency matrix $A$ usually contains:",
        "answer": "The weights of the edges as entries (and $\infty$ or 0 if no edge exists).",
        "options": [
            "Only 1s and 0s.",
            "The weights of the edges as entries (and $\infty$ or 0 if no edge exists).",
            "The degrees of the nodes.",
            "Only the distances calculated by Dijkstra's algorithm."
        ]
    },
    {
        "id": 69,
        "unit": 5,
        "difficulty": "Medium",
        "question": "Why can Dijkstra's algorithm fail if a graph contains negative edge weights?",
        "answer": "Because it assumes that once a node is settled, its shortest distance cannot be further reduced.",
        "options": [
            "It cannot perform subtraction.",
            "Because it assumes that once a node is settled, its shortest distance cannot be further reduced.",
            "It only works on undirected graphs.",
            "The algorithm would take an infinite amount of time."
        ]
    },
    {
        "id": 70,
        "unit": 5,
        "difficulty": "Medium",
        "question": "What is a 'path' in a directed graph?",
        "answer": "A sequence of nodes where each consecutive pair is connected by a directed edge following the direction of the arrows.",
        "options": [
            "Any collection of nodes in the graph.",
            "A sequence of nodes where each consecutive pair is connected by a directed edge following the direction of the arrows.",
            "A cycle that visits every node once.",
            "A set of edges that connects all nodes without cycles."
        ]
    },
    {
        "id": 71,
        "unit": 5,
        "difficulty": "Hard",
        "question": "Suppose you run Dijkstra from node A. Current settled distances are: B=5, C=10. Node B is settled. There is an edge from B to C with weight 2. What is the new distance to C?",
        "answer": "7",
        "options": ["10", "7", "12", "5"]
    },
    {
        "id": 72,
        "unit": 5,
        "difficulty": "Hard",
        "question": "In a digraph with $n$ nodes, what is the maximum possible number of edges (excluding loops)?",
        "answer": "$n(n - 1)$",
        "options": ["$n^2$", "$n(n - 1) / 2$", "$n(n - 1)$", "$2n$"]
    },
    {
        "id": 73,
        "unit": 5,
        "difficulty": "Hard",
        "question": "When presenting the steps of Dijkstra's algorithm in a table, what does the 'predecessor' column help you reconstruct?",
        "answer": "The actual shortest path (the sequence of nodes) from the start to the destination.",
        "options": [
            "The total number of nodes in the graph.",
            "The weight of the heaviest edge.",
            "The actual shortest path (the sequence of nodes) from the start to the destination.",
            "The degree of the nodes."
        ]
    },
    {
        "id": 74,
        "unit": 5,
        "difficulty": "Hard",
        "question": "Which of the following describes a 'dag' (Directed Acyclic Graph)?",
        "answer": "A directed graph that contains no directed cycles.",
        "options": [
            "A graph where every node has a directed edge to every other node.",
            "A directed graph that contains no directed cycles.",
            "A graph with only negative weights.",
            "A graph where every node's in-degree equals its out-degree."
        ]
    },
    {
        "id": 75,
        "unit": 5,
        "difficulty": "Hard",
        "question": "If a graph is disconnected, what will the settled distance be for nodes that cannot be reached from the starting node?",
        "answer": "Infinity ($\infty$)",
        "options": ["Zero", "The sum of all edge weights", "Infinity ($\infty$)", "-1"]
    },
    # --- Unit 6: The Königsberg Bridge Problem ---
    {
        "id": 76,
        "unit": 6,
        "difficulty": "Easy",
        "question": "In graph theory, what is a 'walk'?",
        "answer": "A sequence of nodes where each consecutive pair is connected by an edge.",
        "options": [
            "A cycle that visits every node exactly once.",
            "A sequence of nodes where each consecutive pair is connected by an edge.",
            "A set of edges that contains no cycles.",
            "A graph where every node has the same degree."
        ]
    },
    {
        "id": 77,
        "unit": 6,
        "difficulty": "Easy",
        "question": "What is the specific requirement for a walk to be considered a 'trail'?",
        "answer": "No edge is visited more than once.",
        "options": [
            "No node is visited more than once.",
            "No edge is visited more than once.",
            "The start and end nodes must be the same.",
            "It must visit every node in the graph."
        ]
    },
    {
        "id": 78,
        "unit": 6,
        "difficulty": "Easy",
        "question": "What was the conclusion of Leonhard Euler regarding the Königsberg Bridge Problem?",
        "answer": "A tour crossing every bridge exactly once and returning to the start was impossible because the nodes had odd degrees.",
        "options": [
            "The problem could be solved by starting at any bridge.",
            "A tour crossing every bridge exactly once and returning to the start was impossible because the nodes had odd degrees.",
            "The number of bridges must be even for a solution to exist.",
            "The problem was only solvable if the graph was a tree."
        ]
    },
    {
        "id": 79,
        "unit": 6,
        "difficulty": "Easy",
        "question": "A graph is called 'Eulerian' if it contains:",
        "answer": "A closed trail that visits every edge exactly once.",
        "options": [
            "A path that visits every node exactly once.",
            "A closed trail that visits every edge exactly once.",
            "Only nodes with odd degrees.",
            "No cycles."
        ]
    },
    {
        "id": 80,
        "unit": 6,
        "difficulty": "Easy",
        "question": "What is the purpose of the Postman Problem (Chinese Postman Problem)?",
        "answer": "To find the shortest closed route that visits every edge at least once.",
        "options": [
            "To find the shortest path between two specific cities.",
            "To find a route that visits every node exactly once.",
            "To find the shortest closed route that visits every edge at least once.",
            "To find the maximum flow in a network."
        ]
    },
    {
        "id": 81,
        "unit": 6,
        "difficulty": "Medium",
        "question": "According to Euler's Theorem, a connected graph has an Eulerian cycle if and only if:",
        "answer": "Every node has an even degree.",
        "options": [
            "Every node has an odd degree.",
            "The number of edges is even.",
            "Every node has an even degree.",
            "The graph is a complete graph."
        ]
    },
    {
        "id": 82,
        "unit": 6,
        "difficulty": "Medium",
        "question": "What does it mean for a graph to have an 'Eulerian trail' (but not a cycle)?",
        "answer": "The graph has exactly two nodes of odd degree.",
        "options": [
            "The graph has exactly zero nodes of odd degree.",
            "The graph has exactly two nodes of odd degree.",
            "The graph is disconnected.",
            "The graph contains at least one loop."
        ]
    },
    {
        "id": 83,
        "unit": 6,
        "difficulty": "Medium",
        "question": "How does Hierholzer’s algorithm differ from simply finding any cycle?",
        "answer": "It combines several sub-cycles into one comprehensive Eulerian cycle.",
        "options": [
            "It only works for directed graphs.",
            "It finds the shortest path between two nodes.",
            "It combines several sub-cycles into one comprehensive Eulerian cycle.",
            "It removes edges to create a spanning tree."
        ]
    },
    {
        "id": 84,
        "unit": 6,
        "difficulty": "Medium",
        "question": "In the Postman Problem, if a graph is NOT Eulerian, what must be done to find the optimal route?",
        "answer": "Certain edges must be traversed more than once (effectively 'doubling' edges between odd-degree nodes).",
        "options": [
            "Delete all odd-degree nodes.",
            "Certain edges must be traversed more than once (effectively 'doubling' edges between odd-degree nodes).",
            "Only visit the even-degree nodes.",
            "Change the graph into a directed graph."
        ]
    },
    {
        "id": 85,
        "unit": 6,
        "difficulty": "Medium",
        "question": "If a graph has exactly four nodes of odd degree, what is the minimum number of trails needed to cover every edge exactly once?",
        "answer": "2",
        "options": ["1", "2", "3", "4"]
    },
    {
        "id": 86,
        "unit": 6,
        "difficulty": "Hard",
        "question": "A connected graph has 10 nodes. Six nodes have degree 4, and four nodes have degree 3. Does an Eulerian cycle exist?",
        "answer": "No, because there are nodes with odd degrees.",
        "options": [
            "Yes, because the sum of degrees is even.",
            "No, because there are nodes with odd degrees.",
            "Yes, because it is connected.",
            "No, because it has more than two odd-degree nodes."
        ]
    },
    {
        "id": 87,
        "unit": 6,
        "difficulty": "Hard",
        "question": "Carl Hierholzer published his algorithm in 1873. What is the fundamental step of this algorithm?",
        "answer": "Finding a cycle, then finding another cycle from a node in the first cycle, and merging them.",
        "options": [
            "Finding the shortest path using weights.",
            "Using an adjacency matrix to calculate powers.",
            "Finding a cycle, then finding another cycle from a node in the first cycle, and merging them.",
            "Triangulating the graph nodes."
        ]
    },
    {
        "id": 88,
        "unit": 6,
        "difficulty": "Hard",
        "question": "In the Postman Problem, which algorithm is typically used as a sub-step to find the shortest path between pairs of odd-degree nodes?",
        "answer": "Dijkstra's algorithm.",
        "options": [
            "Hierholzer's algorithm.",
            "Gaussian algorithm.",
            "Dijkstra's algorithm.",
            "Kruskal's algorithm."
        ]
    },
    {
        "id": 89,
        "unit": 6,
        "difficulty": "Hard",
        "question": "What is the relationship between the number of odd-degree nodes and the solvability of the Königsberg Bridge Problem?",
        "answer": "A solution requires exactly zero or two odd-degree nodes; Königsberg had four.",
        "options": [
            "A solution requires an even number of bridges regardless of nodes.",
            "A solution requires exactly zero or two odd-degree nodes; Königsberg had four.",
            "Königsberg had only even-degree nodes, making it unsolvable.",
            "The nodes in Königsberg all had degree 1."
        ]
    },
    {
        "id": 90,
        "unit": 6,
        "difficulty": "Hard",
        "question": "When solving the Postman Problem for a non-Eulerian graph, the total length of the optimal tour is:",
        "answer": "The sum of all edge weights plus the sum of the weights of the 'doubled' edges.",
        "options": [
            "Exactly the sum of all edge weights.",
            "The sum of the shortest paths only.",
            "The sum of all edge weights plus the sum of the weights of the 'doubled' edges.",
            "Double the sum of all edge weights."
        ]
    },
    # --- Unit 7: A City Tour in Which Exactly Every City is Visited Once ---
    {
        "id": 91,
        "unit": 7,
        "difficulty": "Easy",
        "question": "What is a 'Hamiltonian cycle' in a graph?",
        "answer": "A closed walk that visits every node in the graph exactly once.",
        "options": [
            "A walk that visits every edge exactly once.",
            "A closed walk that visits every node in the graph exactly once.",
            "A path that starts and ends at different nodes.",
            "A tree that connects all nodes."
        ]
    },
    {
        "id": 92,
        "unit": 7,
        "difficulty": "Easy",
        "question": "What is the primary difference between an Eulerian cycle and a Hamiltonian cycle?",
        "answer": "Eulerian focuses on visiting every edge; Hamiltonian focuses on visiting every node.",
        "options": [
            "Eulerian cycles are only for directed graphs.",
            "Eulerian focuses on visiting every edge; Hamiltonian focuses on visiting every node.",
            "Hamiltonian cycles must contain all edges of the graph.",
            "There is no difference; they are the same concept."
        ]
    },
    {
        "id": 93,
        "unit": 7,
        "difficulty": "Easy",
        "question": "A graph that contains a Hamiltonian cycle is called a:",
        "answer": "Hamiltonian graph.",
        "options": [
            "Eulerian graph.",
            "Hamiltonian graph.",
            "Complete graph.",
            "Bipartite graph."
        ]
    },
    {
        "id": 94,
        "unit": 7,
        "difficulty": "Easy",
        "question": "What is the main goal of the Traveling Salesman Problem (TSP)?",
        "answer": "To find a Hamiltonian cycle with the minimum total weight in a weighted graph.",
        "options": [
            "To find the shortest path between two specific cities.",
            "To visit every edge in a graph at minimum cost.",
            "To find a Hamiltonian cycle with the minimum total weight in a weighted graph.",
            "To determine if a graph is planar."
        ]
    },
    {
        "id": 95,
        "unit": 7,
        "difficulty": "Easy",
        "question": "In a complete graph $K_n$, does a Hamiltonian cycle always exist for $n \\ge 3$?",
        "answer": "Yes, always.",
        "options": ["Yes, always.", "No, never.", "Only if $n$ is even.", "Only if $n$ is a prime number."]
    },
    {
        "id": 96,
        "unit": 7,
        "difficulty": "Medium",
        "question": "What does Dirac's Theorem state as a sufficient condition for a graph with $n \\ge 3$ nodes to be Hamiltonian?",
        "answer": "Every node must have a degree $d(v) \\ge n/2$.",
        "options": [
            "Every node must have a degree $d(v) \\ge n-1$.",
            "The sum of degrees must be $2n$.",
            "Every node must have a degree $d(v) \\ge n/2$.",
            "The graph must be a tree."
        ]
    },
    {
        "id": 97,
        "unit": 7,
        "difficulty": "Medium",
        "question": "What is the condition required by Ore's Theorem for a graph to be Hamiltonian?",
        "answer": "For every pair of non-adjacent nodes $u$ and $v$, $d(u) + d(v) \\ge n$.",
        "options": [
            "For every pair of nodes, $d(u) + d(v) \\ge n/2$.",
            "The total number of edges must be greater than $n$.",
            "For every pair of non-adjacent nodes $u$ and $v$, $d(u) + d(v) \\ge n$.",
            "All nodes must have the same degree."
        ]
    },
    {
        "id": 98,
        "unit": 7,
        "difficulty": "Medium",
        "question": "Which of the following statements about the Dirac condition is correct?",
        "answer": "A graph can be Hamiltonian even if it does not satisfy the Dirac condition.",
        "options": [
            "A graph is Hamiltonian if and only if it satisfies the Dirac condition.",
            "A graph can be Hamiltonian even if it does not satisfy the Dirac condition.",
            "If a graph does not satisfy the Dirac condition, it is definitely not Hamiltonian.",
            "The Dirac condition applies to edges, not node degrees."
        ]
    },
    {
        "id": 99,
        "unit": 7,
        "difficulty": "Medium",
        "question": "Why is the Traveling Salesman Problem considered difficult to solve for large $n$?",
        "answer": "The number of possible cycles grows factorially, making exhaustive comparison too expensive.",
        "options": [
            "Because matrix inversion is required.",
            "The number of possible cycles grows factorially, making exhaustive comparison too expensive.",
            "It can only be solved for bipartite graphs.",
            "Dijkstra's algorithm cannot be used on weighted graphs."
        ]
    },
    {
        "id": 100,
        "unit": 7,
        "difficulty": "Medium",
        "question": "For a complete graph $K_n$, how many distinct Hamiltonian cycles are there?",
        "answer": "$(n - 1)! / 2$",
        "options": ["$n!$", "$(n - 1)!$", "$(n - 1)! / 2$", "$n^2$"]
    },
    {
        "id": 101,
        "unit": 7,
        "difficulty": "Hard",
        "question": "Which case cannot occur regarding the Dirac condition and Hamiltonian properties?",
        "answer": "A graph satisfies the Dirac condition and is NOT Hamiltonian.",
        "options": [
            "A graph does not satisfy the Dirac condition and is Hamiltonian.",
            "A graph satisfies the Dirac condition and is Hamiltonian.",
            "A graph does not satisfy the Dirac condition and is NOT Hamiltonian.",
            "A graph satisfies the Dirac condition and is NOT Hamiltonian."
        ]
    },
    {
        "id": 102,
        "unit": 7,
        "difficulty": "Hard",
        "question": "In which case does the complete bipartite graph $K_{m,n}$ satisfy the Dirac condition?",
        "answer": "When $m = n$ and $m \\ge n/2$ (meaning $m=n$).",
        "options": [
            "Always, for any $m$ and $n$.",
            "Only if $m + n$ is an even number.",
            "When $m = n$.",
            "Never, because bipartite graphs cannot be Hamiltonian."
        ]
    },
    {
        "id": 103,
        "unit": 7,
        "difficulty": "Hard",
        "question": "A 'Hamiltonian path' differs from a 'Hamiltonian cycle' in that:",
        "answer": "The path visits every node exactly once but does not need to return to the start node.",
        "options": [
            "The path does not visit every node.",
            "The path visits every node exactly once but does not need to return to the start node.",
            "The path only exists in trees.",
            "The path must visit every edge."
        ]
    },
    {
        "id": 104,
        "unit": 7,
        "difficulty": "Hard",
        "question": "If a graph has a bridge (an edge whose removal increases the number of connected components), can it be Hamiltonian?",
        "answer": "No, because a cycle would have to cross the bridge twice to return, violating the 'visit once' rule.",
        "options": [
            "Yes, always.",
            "No, because a cycle would have to cross the bridge twice to return, violating the 'visit once' rule.",
            "Yes, but only if the bridge has a weight of zero.",
            "Only if the graph is directed."
        ]
    },
    {
        "id": 105,
        "unit": 7,
        "difficulty": "Hard",
        "question": "Because TSP is computationally expensive (NP-hard), what approach is often used in practice to find solutions?",
        "answer": "Heuristics (algorithms that find 'good enough' solutions quickly).",
        "options": [
            "The Gaussian algorithm.",
            "Heuristics (algorithms that find 'good enough' solutions quickly).",
            "Manually checking every possible path.",
            "Converting the graph into a tree."
        ]
    },
    # --- Unit 8: Trees ---
    {
        "id": 106,
        "unit": 8,
        "difficulty": "Easy",
        "question": "In graph theory, what is the definition of a 'tree'?",
        "answer": "A connected graph that contains no cycles.",
        "options": [
            "A graph where every node has a degree of at least 2.",
            "A connected graph that contains no cycles.",
            "A graph where every node is connected to every other node.",
            "A directed graph with weighted edges."
        ]
    },
    {
        "id": 107,
        "unit": 8,
        "difficulty": "Easy",
        "question": "If a tree has $n$ nodes, how many edges must it have?",
        "answer": "$n - 1$",
        "options": ["$n$", "$n - 1$", "$n + 1$", "$2n$"]
    },
    {
        "id": 108,
        "unit": 8,
        "difficulty": "Easy",
        "question": "What is a 'leaf' in a tree?",
        "answer": "A node with a degree of 1.",
        "options": [
            "The starting node of a search.",
            "A node with a degree of 1.",
            "A node that is part of a cycle.",
            "The node with the highest degree."
        ]
    },
    {
        "id": 109,
        "unit": 8,
        "difficulty": "Easy",
        "question": "What characterizes a 'rooted tree'?",
        "answer": "A tree in which one specific node is designated as the root.",
        "options": [
            "A tree where all edges are directed upwards.",
            "A tree in which one specific node is designated as the root.",
            "A tree that has no leaves.",
            "A tree used only for binary calculations."
        ]
    },
    {
        "id": 110,
        "unit": 8,
        "difficulty": "Easy",
        "question": "In a rooted tree, nodes that share the same parent are called:",
        "answer": "Siblings.",
        "options": ["Children.", "Ancestors.", "Siblings.", "Leaves."]
    },
    {
        "id": 111,
        "unit": 8,
        "difficulty": "Medium",
        "question": "What is a 'spanning tree' of a graph $G$?",
        "answer": "A subgraph of $G$ that is a tree and contains all the nodes of $G$.",
        "options": [
            "A subgraph that contains all the edges of $G$.",
            "A subgraph of $G$ that is a tree and contains all the nodes of $G$.",
            "A path that visits every node exactly once.",
            "The largest possible cycle within the graph."
        ]
    },
    {
        "id": 112,
        "unit": 8,
        "difficulty": "Medium",
        "question": "Which of the following is the goal of Kruskal's algorithm?",
        "answer": "To find a spanning tree with the minimum total edge weight.",
        "options": [
            "To find the shortest path between two nodes.",
            "To find a spanning tree with the minimum total edge weight.",
            "To determine if a graph is Hamiltonian.",
            "To count the number of cycles in a graph."
        ]
    },
    {
        "id": 113,
        "unit": 8,
        "difficulty": "Medium",
        "question": "What is the defining property of a 'Binary Search Tree' (BST)?",
        "answer": "For any node, the left subtree contains smaller values and the right subtree contains larger values.",
        "options": [
            "Each node has exactly two children.",
            "It is a tree with exactly $2^n$ nodes.",
            "For any node, the left subtree contains smaller values and the right subtree contains larger values.",
            "The root is always the median value of the dataset."
        ]
    },
    {
        "id": 114,
        "unit": 8,
        "difficulty": "Medium",
        "question": "How does Prim's algorithm differ from Kruskal's algorithm?",
        "answer": "Prim's grows a single tree from a starting node; Kruskal's picks the smallest edges from anywhere in the graph.",
        "options": [
            "Prim's only works on directed graphs.",
            "Prim's grows a single tree from a starting node; Kruskal's picks the smallest edges from anywhere in the graph.",
            "Kruskal's algorithm is used for shortest paths, not spanning trees.",
            "There is no difference; they follow the exact same steps."
        ]
    },
    {
        "id": 115,
        "unit": 8,
        "difficulty": "Medium",
        "question": "A tree is a 'bipartite graph'. This statement is:",
        "answer": "Always true.",
        "options": ["Always true.", "Always false.", "Only true if the tree is rooted.", "Only true if the tree is binary."]
    },
    {
        "id": 116,
        "unit": 8,
        "difficulty": "Hard",
        "question": "In Kruskal's algorithm, why is an edge rejected even if it has a low weight?",
        "answer": "Because adding it would create a cycle within the set of selected edges.",
        "options": [
            "Because it is not connected to the root.",
            "Because it has a higher weight than the current average.",
            "Because adding it would create a cycle within the set of selected edges.",
            "Because it connects to a leaf node."
        ]
    },
    {
        "id": 117,
        "unit": 8,
        "difficulty": "Hard",
        "question": "If you are removing edges from a connected graph with $n$ nodes and $e$ edges to make it a tree, how many edges must you remove?",
        "answer": "$e - (n - 1)$",
        "options": ["$e - n$", "$e - (n - 1)$", "$e / 2$", "$n - 1$"]
    },
    {
        "id": 118,
        "unit": 8,
        "difficulty": "Hard",
        "question": "What is the height of a tree?",
        "answer": "The maximum length of a path from the root to any leaf.",
        "options": [
            "The total number of nodes.",
            "The maximum length of a path from the root to any leaf.",
            "The number of leaves in the tree.",
            "The degree of the root node."
        ]
    },
    {
        "id": 119,
        "unit": 8,
        "difficulty": "Hard",
        "question": "When inserting the key '7' into a Binary Search Tree where the root is '5' and its right child is '10', where will '7' be placed?",
        "answer": "As the left child of '10'.",
        "options": [
            "As the left child of '5'.",
            "As the right child of '10'.",
            "As the left child of '10'.",
            "It will replace '5' as the root."
        ]
    },
    {
        "id": 120,
        "unit": 8,
        "difficulty": "Hard",
        "question": "Cayley's Formula states that the number of distinct spanning trees in a complete graph $K_n$ is:",
        "answer": "$n^{n-2}$",
        "options": ["$2^{n-1}$", "$n(n-1)/2$", "$n^{n-2}$", "$n!$"]
    }
]