# questions_prior.py

questions_data = [
    # --- Lesson 1.1: Basic concepts of matrices ---
    {
        "id": 1,
        "unit": 1,
        "difficulty": "Easy",
        "question": "How would you represent the following table as a matrix?\nNorth: (Prod A: 120, Prod B: 277)\nMiddle: (Prod A: 150, Prod B: 259)\nSouth: (Prod A: 100, Prod B: 310)",
        "answer": "$\\begin{pmatrix} 120 & 150 & 100 \\\\ 277 & 259 & 310 \\end{pmatrix}$",
        "options": [
            "$\\begin{pmatrix} 120 & 277 \\\\ 150 & 259 \\\\ 100 & 310 \\end{pmatrix}$",
            "$\\begin{pmatrix} 120 & 150 & 100 \\\\ 277 & 259 & 310 \\end{pmatrix}$",
            "$\\begin{pmatrix} 120 & 150 \\\\ 277 & 259 \\\\ 100 & 310 \\end{pmatrix}$",
            "$\\begin{pmatrix} 120 & 150 & 100 & 277 & 259 & 310 \\end{pmatrix}$"
        ]
    },
    {
        "id": 2,
        "unit": 1,
        "difficulty": "Easy",
        "question": "For the matrix $A = \\begin{pmatrix} 2 & 4 & 6 \\\\ 1 & 2 & 3 \\end{pmatrix}$, what is the transposed matrix $A^T$?",
        "answer": "$A^T = \\begin{pmatrix} 2 & 1 \\\\ 4 & 2 \\\\ 6 & 3 \\end{pmatrix}$",
        "options": [
            "$A^T = \\begin{pmatrix} 1 & 2 & 3 \\\\ 2 & 4 & 6 \\end{pmatrix}$",
            "$A^T = \\begin{pmatrix} 2 & 4 & 6 \\\\ 1 & 2 & 3 \\end{pmatrix}$",
            "$A^T = \\begin{pmatrix} 2 & 1 \\\\ 4 & 2 \\\\ 6 & 3 \\end{pmatrix}$",
            "$A^T = \\begin{pmatrix} 6 & 3 \\\\ 4 & 2 \\\\ 2 & 1 \\end{pmatrix}$"
        ]
    },
    {
        "id": 3,
        "unit": 1,
        "difficulty": "Medium",
        "question": "Which of the following correctly pairs a column vector $\\vec{a}$ and a row vector $\\vec{b}^T$?",
        "answer": "$\\vec{a} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$, $\\vec{b}^T = \\begin{pmatrix} 4 & 5 & 6 \\end{pmatrix}$",
        "options": [
            "$\\vec{a} = \\begin{pmatrix} 1 & 2 & 3 \\end{pmatrix}$, $\\vec{b}^T = \\begin{pmatrix} 4 \\\\ 5 \\\\ 6 \\end{pmatrix}$",
            "$\\vec{a} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$, $\\vec{b}^T = \\begin{pmatrix} 4 & 5 & 6 \\end{pmatrix}$",
            "$\\vec{a} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$, $\\vec{b}^T = \\begin{pmatrix} 4 \\\\ 5 \\\\ 6 \\end{pmatrix}^T$",
            "$\\vec{a} = \\begin{pmatrix} 1 & 2 & 3 \\end{pmatrix}$, $\\vec{b}^T = \\begin{pmatrix} 4 & 5 & 6 \\end{pmatrix}$"
        ]
    },
    {
        "id": 4,
        "unit": 1,
        "difficulty": "Medium",
        "question": "What are the main diagonal elements and the classification of the matrix $A = \\begin{pmatrix} 1 & 2 & 3 \\\\ 0 & 7 & 8 \\\\ 0 & 0 & 9 \\\\ 0 & 0 & 0 \\end{pmatrix}$?",
        "answer": "$a_{11}=1, a_{22}=7, a_{33}=9$; Type 4x3; Upper triangular matrix",
        "options": [
            "$a_{11}=1, a_{22}=7, a_{33}=9$; Type 3x4; Lower triangular matrix",
            "$a_{11}=1, a_{22}=7, a_{33}=9$; Type 4x3; Upper triangular matrix",
            "$a_{11}=1, a_{22}=7, a_{33}=9$; Type 4x3; Diagonal matrix",
            "$a_{11}=0, a_{22}=0, a_{33}=0$; Type 4x3; Zero matrix"
        ]
    },
    {
        "id": 5,
        "unit": 1,
        "difficulty": "Hard",
        "question": "Which of the following statements regarding matrix properties is true?",
        "answer": "Both: If $A^T$ is a diagonal matrix, then $A$ is diagonal; and if $A$ is a zero matrix, $A^T$ is also a zero matrix.",
        "options": [
            "If $A^T$ is a diagonal matrix, then $A$ is a triangular matrix.",
            "If $A$ is a zero matrix, then $A^T$ must be an identity matrix.",
            "Only square matrices have a transposed matrix that remains the same type.",
            "Both: If $A^T$ is a diagonal matrix, then $A$ is diagonal; and if $A$ is a zero matrix, $A^T$ is also a zero matrix."
        ]
    },
    # --- Lesson 1.2: Addition of matrices ---
    {
        "id": 6,
        "unit": 1,
        "difficulty": "Easy",
        "question": "Given $A = \\begin{pmatrix} -1 & 4 & 6 \\\\ 2 & -3 & 7 \\end{pmatrix}$ and $B = \\begin{pmatrix} 2 & 3 & 5 \\\\ 0 & 4 & 7 \\end{pmatrix}$, what is $A + B$?",
        "answer": "$C = \\begin{pmatrix} 1 & 7 & 11 \\\\ 2 & 1 & 14 \\end{pmatrix}$",
        "options": [
            "$C = \\begin{pmatrix} 3 & 1 & 1 \\\\ 2 & -7 & 0 \\end{pmatrix}$",
            "$C = \\begin{pmatrix} 1 & 7 & 11 \\\\ 2 & 1 & 14 \\end{pmatrix}$",
            "$C = \\begin{pmatrix} 1 & 1 & 1 \\\\ 2 & 1 & 14 \\end{pmatrix}$",
            "$C = \\begin{pmatrix} -1 & 7 & 11 \\\\ 2 & 1 & 0 \\end{pmatrix}$"
        ]
    },
    {
        "id": 7,
        "unit": 1,
        "difficulty": "Easy",
        "question": "Can the operation $A - B$ be performed if $A = \\begin{pmatrix} 4 & 2 & 7 \\\\ 3 & 1 & 0 \\end{pmatrix}$ and $B = \\begin{pmatrix} 1 & -1 \\\\ 0 & 2 \\end{pmatrix}$?",
        "answer": "No, the operation is not possible because the matrices are of different types.",
        "options": [
            "Yes, the result is a 2x2 matrix.",
            "Yes, the result is a 2x3 matrix.",
            "No, the operation is not possible because the matrices are of different types.",
            "Yes, if you add a column of zeros to matrix B."
        ]
    },
    {
        "id": 8,
        "unit": 1,
        "difficulty": "Medium",
        "question": "Given $A = \\begin{pmatrix} 1 & 3 & 2 \\\\ -3 & 4 & 5 \\end{pmatrix}$ and $B = \\begin{pmatrix} 2 & -1 \\\\ 0 & 4 \\\\ 1 & 5 \\end{pmatrix}$, calculate $A - B^T$.",
        "answer": "$\\begin{pmatrix} -1 & 3 & 1 \\\\ -2 & 0 & 0 \\end{pmatrix}$",
        "options": [
            "$\\begin{pmatrix} 1 & 3 & 1 \\\\ -2 & 0 & 0 \\end{pmatrix}$",
            "$\\begin{pmatrix} -1 & 3 & 1 \\\\ -2 & 0 & 0 \\end{pmatrix}$",
            "$\\begin{pmatrix} -1 & 4 & 1 \\\\ -3 & 0 & 0 \\end{pmatrix}$",
            "The operation is not defined."
        ]
    },
    {
        "id": 9,
        "unit": 1,
        "difficulty": "Medium",
        "question": "If you add two lower triangular matrices $A$ and $B$, what is the result?",
        "answer": "A lower triangular matrix.",
        "options": [
            "An upper triangular matrix.",
            "A diagonal matrix.",
            "A lower triangular matrix.",
            "A symmetric matrix."
        ]
    },
    {
        "id": 10,
        "unit": 1,
        "difficulty": "Hard",
        "question": "Given two diagonal matrices $A$ and $B$, what type of matrix is $A + B^T$?",
        "answer": "Diagonal matrix",
        "options": [
            "Upper triangular matrix",
            "Diagonal matrix",
            "Skew-symmetric matrix",
            "Identity matrix"
        ]
    },
    # --- Lesson 1.3: Scalar multiplication and product ---
    {
        "id": 11,
        "unit": 1,
        "difficulty": "Easy",
        "question": "Given $A = \\begin{pmatrix} 0 & 2 & -1 \\\\ 1 & 4 & 5 \\end{pmatrix}$ and $B = \\begin{pmatrix} 2 & 3 & 4 \\\\ 2 & 1 & 0 \\end{pmatrix}$, calculate $2 \\cdot A + B$.",
        "answer": "$\\begin{pmatrix} 2 & 7 & 2 \\\\ 4 & 9 & 10 \\end{pmatrix}$",
        "options": [
            "$\\begin{pmatrix} 2 & 7 & 2 \\\\ 4 & 9 & 10 \\end{pmatrix}$",
            "$\\begin{pmatrix} 0 & 4 & -2 \\\\ 2 & 8 & 10 \\end{pmatrix}$",
            "$\\begin{pmatrix} 2 & 5 & 3 \\\\ 3 & 5 & 5 \\end{pmatrix}$",
            "$\\begin{pmatrix} 2 & 7 & 3 \\\\ 4 & 9 & 5 \\end{pmatrix}$"
        ]
    },
    {
        "id": 12,
        "unit": 1,
        "difficulty": "Easy",
        "question": "Calculate the scalar product $\\vec{a}^T \\cdot \\vec{b}$ for $\\vec{a} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$ and $\\vec{b} = \\begin{pmatrix} 0 \\\\ 4 \\\\ 5 \\end{pmatrix}$.",
        "answer": "23",
        "options": ["0", "23", "8", "15"]
    },
    {
        "id": 13,
        "unit": 1,
        "difficulty": "Medium",
        "question": "Given $A = \\begin{pmatrix} 0 & 1 & 2 \\\\ -2 & 2 & 3 \\end{pmatrix}$ and $B = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\\\ 0 & 1 \\end{pmatrix}$, calculate $2 \\cdot A - 3 \\cdot B^T$.",
        "answer": "$\\begin{pmatrix} -6 & 2 & 4 \\\\ -7 & -5 & 3 \\end{pmatrix}$",
        "options": [
            "$\\begin{pmatrix} 0 & 2 & 4 \\\\ -4 & 4 & 6 \\end{pmatrix}$",
            "$\\begin{pmatrix} 6 & 0 & 0 \\\\ 3 & 9 & 3 \\end{pmatrix}$",
            "$\\begin{pmatrix} -6 & 2 & 4 \\\\ -7 & -5 & 3 \\end{pmatrix}$",
            "$\\begin{pmatrix} -6 & 2 & 2 \\\\ -4 & -1 & 3 \\end{pmatrix}$"
        ]
    },
    {
        "id": 14,
        "unit": 1,
        "difficulty": "Medium",
        "question": "Which of the following operations is defined for $\\vec{b} = \\begin{pmatrix} 3 \\\\ 2 \\end{pmatrix}$ and $\\vec{c} = \\begin{pmatrix} 4 \\\\ 1 \\end{pmatrix}$?",
        "answer": "$\\vec{b}^T \\cdot \\vec{c}$",
        "options": [
            "$\\vec{b} \\cdot \\vec{c}$",
            "$\\vec{b}^T \\cdot \\vec{c}$",
            "$\\vec{a} \\cdot \\vec{b}$ (where $\\vec{a}$ is length 4)",
            "None of these operations are defined."
        ]
    },
    {
        "id": 15,
        "unit": 1,
        "difficulty": "Hard",
        "question": "Can the matrix $A = \\begin{pmatrix} 0 & 1 & 2 \\\\ -2 & 2 & 3 \\end{pmatrix}$ be represented as the sum of a symmetric and a skew-symmetric matrix?",
        "answer": "No, because the matrix is not square.",
        "options": [
            "Yes, any matrix can be represented this way.",
            "No, because it contains negative numbers.",
            "No, because the matrix is not square.",
            "Yes, but only if all elements are integers."
        ]
    },
    {
        "id": 16,
        "unit": 2,
        "difficulty": "Easy",
        "question": "Given $A = \\begin{pmatrix} 0 & 1 & 2 \\\\ -2 & 2 & 3 \\end{pmatrix}$, $B = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\\\ 0 & 1 \\end{pmatrix}$, and $C = \\begin{pmatrix} 2 & 1 \\\\ 0 & 3 \\\\ 0 & 1 \\end{pmatrix}$, which operation is defined and what is its result?",
        "answer": "$A \\cdot B = \\begin{pmatrix} 0 & 5 \\\\ -4 & 7 \\end{pmatrix}$",
        "options": [
            "$A \\cdot B = \\begin{pmatrix} 0 & 5 \\\\ -4 & 7 \\end{pmatrix}$",
            "$B \\cdot C = \\begin{pmatrix} 4 & 1 \\\\ 0 & 9 \\\\ 0 & 1 \\end{pmatrix}$",
            "$A \\cdot B$ is not possible because types do not match.",
            "$B \\cdot C = \\begin{pmatrix} 2 & 5 \\\\ -4 & 7 \\end{pmatrix}$"
        ]
    },
    {
        "id": 17,
        "unit": 2,
        "difficulty": "Easy",
        "question": "Calculate $A \\cdot B$ for $A = \\begin{pmatrix} 0 & 1 \\\\ -2 & 2 \\end{pmatrix}$ and $B = \\begin{pmatrix} 1 & 3 \\\\ 0 & 2 \\end{pmatrix}$. Why is this possible?",
        "answer": "$C = \\begin{pmatrix} 0 & 2 \\\\ -2 & -2 \\end{pmatrix}$; possible because columns of $A$ equal rows of $B$.",
        "options": [
            "$C = \\begin{pmatrix} 0 & 2 \\\\ -2 & -2 \\end{pmatrix}$; possible because columns of $A$ equal rows of $B$.",
            "$C = \\begin{pmatrix} 1 & 3 \\\\ -2 & 2 \\end{pmatrix}$; possible because both are 2x2.",
            "$C = \\begin{pmatrix} 0 & 3 \\\\ 0 & 4 \\end{pmatrix}$; possible because rows of $A$ equal columns of $B$.",
            "The operation is not possible."
        ]
    },
    {
        "id": 18,
        "unit": 2,
        "difficulty": "Medium",
        "question": "What is the result of the dyadic product of vectors $\\vec{a} = \\begin{pmatrix} 1 \\\\ 2 \\\\ 3 \\end{pmatrix}$ and $\\vec{b} = \\begin{pmatrix} 3 \\\\ 2 \\\\ 1 \\end{pmatrix}$?",
        "answer": "$\\begin{pmatrix} 3 & 2 & 1 \\\\ 6 & 4 & 2 \\\\ 9 & 6 & 3 \\end{pmatrix}$",
        "options": [
            "10 (Scalar product)",
            "$\\begin{pmatrix} 3 & 2 & 1 \\\\ 6 & 4 & 2 \\\\ 9 & 6 & 3 \\end{pmatrix}$",
            "$\\begin{pmatrix} 3 \\\\ 4 \\\\ 3 \\end{pmatrix}$",
            "$\\begin{pmatrix} 1 & 2 & 3 \\\\ 3 & 2 & 1 \\end{pmatrix}$"
        ]
    },
    {
        "id": 19,
        "unit": 2,
        "difficulty": "Medium",
        "question": "If $A$ is a lower triangular matrix and $B$ is an identity matrix $E$, what is the classification of $C = A \\cdot B$?",
        "answer": "Lower triangular matrix",
        "options": [
            "Upper triangular matrix",
            "Diagonal matrix",
            "Lower triangular matrix",
            "Zero matrix"
        ]
    },
    {
        "id": 20,
        "unit": 2,
        "difficulty": "Hard",
        "question": "Which matrix identity is confirmed by calculating $B^T \\cdot A^T$ and $(A \\cdot B)^T$?",
        "answer": "$B^T \\cdot A^T = (A \\cdot B)^T$",
        "options": [
            "$A^T \\cdot B^T = (A \\cdot B)^T$",
            "$B^T \\cdot A^T = (A \\cdot B)^T$",
            "$(A \\cdot B)^T = A^T \\cdot B^T$",
            "$A \\cdot B = B \\cdot A$"
        ]
    },
    # --- Lesson 2.2: Properties of matrix multiplication ---
    {
        "id": 21,
        "unit": 2,
        "difficulty": "Easy",
        "question": "What is the result of $A \\cdot E$, where $E$ is the identity matrix?",
        "answer": "$A \\cdot E = A$ (The matrix remains unchanged)",
        "options": [
            "$A \\cdot E = E$",
            "$A \\cdot E = A^T$",
            "$A \\cdot E = A$ (The matrix remains unchanged)",
            "$A \\cdot E = 0$"
        ]
    },
    {
        "id": 22,
        "unit": 2,
        "difficulty": "Easy",
        "question": "Given two diagonal matrices $A$ and $B$, what is the result of $C = A \\cdot B$?",
        "answer": "A diagonal matrix where corresponding diagonal elements are multiplied.",
        "options": [
            "An identity matrix.",
            "A diagonal matrix where corresponding diagonal elements are added.",
            "A diagonal matrix where corresponding diagonal elements are multiplied.",
            "A full matrix where all elements are non-zero."
        ]
    },
    {
        "id": 23,
        "unit": 2,
        "difficulty": "Medium",
        "question": "Does the commutative law ($A \\cdot B = B \\cdot A$) generally apply to matrix multiplication?",
        "answer": "No, matrix multiplication is generally not commutative.",
        "options": [
            "Yes, it always applies for square matrices.",
            "No, matrix multiplication is generally not commutative.",
            "Yes, it applies if both matrices are triangular.",
            "No, it only applies if one matrix is a zero matrix."
        ]
    },
    {
        "id": 24,
        "unit": 2,
        "difficulty": "Medium",
        "question": "If a 3x3 matrix $A$ is multiplied by a zero matrix $O$ such that $A \\cdot O$ is defined, what must be true?",
        "answer": "The zero matrix must have 3 rows; the result is a zero matrix.",
        "options": [
            "The zero matrix must have 3 columns; the result is $A$.",
            "The zero matrix must have 3 rows; the result is a zero matrix.",
            "The zero matrix can be any type; the result is always 0.",
            "The result is an identity matrix."
        ]
    },
    {
        "id": 25,
        "unit": 2,
        "difficulty": "Hard",
        "question": "When multiplying a lower triangular matrix $A$ (with zeros on diagonal) and an upper triangular matrix $B$ (with zeros on diagonal), which elements of $C = A \\cdot B$ can be non-zero?",
        "answer": "Only specific interior elements like $c_{22}, c_{23}, c_{32}, c_{33}$ depending on matrix size.",
        "options": [
            "All elements $c_{ij}$ will be non-zero.",
            "All elements $c_{ij}$ will be zero.",
            "Only the main diagonal elements.",
            "Only specific interior elements like $c_{22}, c_{23}, c_{32}, c_{33}$ depending on matrix size."
        ]
    },
    # --- Lesson 2.3: Inverse matrices ---
    {
        "id": 26,
        "unit": 2,
        "difficulty": "Easy",
        "question": "Which of these matrices is NOT invertible?",
        "answer": "A diagonal matrix with at least one zero on the main diagonal.",
        "options": [
            "A square matrix with a non-zero determinant.",
            "A diagonal matrix with all non-zero elements.",
            "A diagonal matrix with at least one zero on the main diagonal.",
            "Any square matrix."
        ]
    },
    {
        "id": 27,
        "unit": 2,
        "difficulty": "Easy",
        "question": "Is the matrix $A = \\begin{pmatrix} 2 & 1 \\\\ 3 & 4 \\end{pmatrix}$ invertible?",
        "answer": "Yes, because the determinant ($8 - 3 = 5$) is not equal to zero.",
        "options": [
            "No, because it is not a diagonal matrix.",
            "Yes, because the determinant ($8 - 3 = 5$) is not equal to zero.",
            "No, because the sum of the rows is not equal.",
            "Yes, because it is a square matrix."
        ]
    },
    {
        "id": 28,
        "unit": 2,
        "difficulty": "Medium",
        "question": "What is the inverse of the matrix $A = \\begin{pmatrix} -2 & 3 \\\\ 1 & 4 \\end{pmatrix}$?",
        "answer": "$A^{-1} = \\begin{pmatrix} -4/11 & 3/11 \\\\ 1/11 & 2/11 \\end{pmatrix}$",
        "options": [
            "$A^{-1} = \\begin{pmatrix} 4 & -3 \\\\ -1 & -2 \\end{pmatrix}$",
            "$A^{-1} = \\begin{pmatrix} -4/11 & 3/11 \\\\ 1/11 & 2/11 \\end{pmatrix}$",
            "$A^{-1} = \\begin{pmatrix} 4/11 & -3/11 \\\\ -1/11 & -2/11 \\end{pmatrix}$",
            "The matrix is not invertible."
        ]
    },
    {
        "id": 29,
        "unit": 2,
        "difficulty": "Medium",
        "question": "What is the inverse of the diagonal matrix $D = \\begin{pmatrix} 2 & 0 & 0 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 4 \\end{pmatrix}$?",
        "answer": "$D^{-1} = \\begin{pmatrix} 1/2 & 0 & 0 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 1/4 \\end{pmatrix}$",
        "options": [
            "$D^{-1} = \\begin{pmatrix} -2 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & -4 \\end{pmatrix}$",
            "$D^{-1} = \\begin{pmatrix} 1/2 & 0 & 0 \\\\ 0 & -1 & 0 \\\\ 0 & 0 & 1/4 \\end{pmatrix}$",
            "$D^{-1} = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$",
            "Diagonal matrices cannot be inverted."
        ]
    },
    {
        "id": 30,
        "unit": 2,
        "difficulty": "Hard",
        "question": "Which property defines the relationship between a matrix $A$ and its inverse $A^{-1}$?",
        "answer": "$A \\cdot A^{-1} = A^{-1} \\cdot A = E$",
        "options": [
            "$A \\cdot A^{-1} = 0$",
            "$A \\cdot A^{-1} = A$",
            "$A \\cdot A^{-1} = A^{-1} \\cdot A = E$",
            "$A + A^{-1} = E$"
        ]
    },
    # --- Lesson 3.1: Gauss algorithm ---
    {
        "id": 31,
        "unit": 3,
        "difficulty": "Easy",
        "question": "Decide whether the following system of equations is linear:\n$2x_1 - 3x_2 = 5$\n$3(x_1 - 2)^2 + x_2 = x_1$",
        "answer": "No, because the variable $x_1$ is squared.",
        "options": [
            "Yes, because it consists of two equations with two unknowns.",
            "No, because the variable $x_1$ is squared.",
            "Yes, because all terms can be moved to one side.",
            "No, because it contains the number 5 as a constant."
        ]
    },
    {
        "id": 32,
        "unit": 3,
        "difficulty": "Easy",
        "question": "What are the three possible solution cases for a system of linear equations?",
        "answer": "Exactly one solution, infinitely many solutions, or no solution.",
        "options": [
            "Exactly one solution, exactly two solutions, or no solution.",
            "Exactly one solution, infinitely many solutions, or no solution.",
            "Positive solutions, negative solutions, or zero.",
            "Real solutions, imaginary solutions, or no solution."
        ]
    },
    {
        "id": 33,
        "unit": 3,
        "difficulty": "Medium",
        "question": "Based on the augmented matrix $\\left(\\begin{array}{cc|c} 1 & 1 & 2 \\\\ 2 & 2 & 3 \\\\ 0 & 0 & 0 \\end{array}\\right)$, what is the solvability of the system?",
        "answer": "The system is not solvable because it leads to a contradiction ($0 = -1$).",
        "options": [
            "The system has exactly one solution.",
            "The system has infinitely many solutions.",
            "The system is not solvable because it leads to a contradiction ($0 = -1$).",
            "The system is solvable because the last row is a zero row."
        ]
    },
    {
        "id": 34,
        "unit": 3,
        "difficulty": "Medium",
        "question": "Based on the augmented matrix $\\left(\\begin{array}{ccc|c} 1 & 1 & 1 & 1 \\\\ 1 & 2 & 1 & 3 \\end{array}\\right)$, what can be said about the solution set?",
        "answer": "There are infinitely many solutions because there are more unknowns than equations.",
        "options": [
            "There is exactly one solution.",
            "There are infinitely many solutions because there are more unknowns than equations.",
            "The system has no solution.",
            "The system is only solvable if all variables are equal to 1."
        ]
    },
    {
        "id": 35,
        "unit": 3,
        "difficulty": "Hard",
        "question": "Which of the following augmented matrices with four equations and two unknowns is uniquely solvable?",
        "answer": "$\\left(\\begin{array}{cc|c} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 2 & 2 & 2 \\\\ 2 & 4 & 6 \\end{array}\\right)$",
        "options": [
            "$\\left(\\begin{array}{cc|c} 1 & 1 & 1 \\\\ 1 & 2 & 3 \\\\ 2 & 2 & 2 \\\\ 2 & 4 & 6 \\end{array}\\right)$",
            "$\\left(\\begin{array}{cc|c} 1 & 1 & 1 \\\\ 1 & 1 & 2 \\\\ 2 & 2 & 2 \\\\ 0 & 0 & 0 \\end{array}\\right)$",
            "$\\left(\\begin{array}{cc|c} 0 & 0 & 1 \\\\ 0 & 0 & 2 \\\\ 0 & 0 & 3 \\\\ 0 & 0 & 4 \\end{array}\\right)$",
            "$\\left(\\begin{array}{cc|c} 1 & 2 & 3 \\\\ 4 & 5 & 6 \\\\ 7 & 8 & 9 \\\\ 10 & 11 & 12 \\end{array}\\right)$"
        ]
    },
    # --- Lesson 3.2: Solution examples with the Gauss algorithm ---
    {
        "id": 36,
        "unit": 3,
        "difficulty": "Easy",
        "question": "Solve the following system of linear equations: $\\left(\\begin{array}{ccc|c} 1 & 2 & 2 & 1 \\\\ 2 & 1 & 2 & 0 \\\\ 1 & 1 & 1 & 2 \\end{array}\\right)$",
        "answer": "$x_1 = 3, x_2 = 4, x_3 = -5$",
        "options": [
            "$x_1 = 1, x_2 = 2, x_3 = 3$",
            "$x_1 = 3, x_2 = 4, x_3 = -5$",
            "$x_1 = -3, x_2 = -4, x_3 = 5$",
            "$x_1 = 0, x_2 = 1, x_3 = -1$"
        ]
    },
    {
        "id": 37,
        "unit": 3,
        "difficulty": "Easy",
        "question": "Solve the following system: $\\left(\\begin{array}{ccc|c} 1 & 2 & 1 & 0 \\\\ 1 & 3 & 1 & 0 \\\\ 1 & 1 & 1 & 1 \\end{array}\\right)$",
        "answer": "The system is not solvable (contradiction).",
        "options": [
            "$x_1 = 0, x_2 = 0, x_3 = 1$",
            "The system has infinitely many solutions.",
            "The system is not solvable (contradiction).",
            "$x_1 = -1, x_2 = 0, x_3 = 1$"
        ]
    },
    {
        "id": 38,
        "unit": 3,
        "difficulty": "Medium",
        "question": "Determine the solution for the system: $\\left(\\begin{array}{ccc|c} 2 & 3 & 1 & 1 \\\\ 1 & 1 & 2 & 2 \\\\ 2 & 1 & 0 & 1 \\end{array}\\right)$",
        "answer": "$x_1 = 5/7, x_2 = -3/7, x_3 = 6/7$",
        "options": [
            "$x_1 = 5/7, x_2 = -3/7, x_3 = 6/7$",
            "$x_1 = 1/2, x_2 = 1/2, x_3 = 0$",
            "$x_1 = 3, x_2 = -2, x_3 = 1$",
            "$x_1 = 1, x_2 = 1, x_3 = 1$"
        ]
    },
    {
        "id": 39,
        "unit": 3,
        "difficulty": "Medium",
        "question": "Solve the system of linear equations: $\\left(\\begin{array}{ccc|c} 2 & 3 & 1 & 1 \\\\ 1 & 1 & 0 & 1 \\\\ 4 & 6 & 1 & 2 \\end{array}\\right)$",
        "answer": "$x_1 = 2, x_2 = -1, x_3 = 0$",
        "options": [
            "$x_1 = 1, x_2 = 0, x_3 = 1$",
            "$x_1 = 2, x_2 = -1, x_3 = 0$",
            "$x_1 = -2, x_2 = 1, x_3 = 0$",
            "The system is inconsistent."
        ]
    },
    {
        "id": 40,
        "unit": 3,
        "difficulty": "Hard",
        "question": "Calculate the inverse of the matrix $A = \\begin{pmatrix} 1 & 1 & 2 \\\\ 1 & 0 & 1 \\\\ 2 & 1 & 1 \\end{pmatrix}$ using the Gauss-Jordan method.",
        "answer": "$A^{-1} = \\begin{pmatrix} -1/2 & 1/2 & 1/2 \\\\ 1/2 & -3/2 & 1/2 \\\\ 1/2 & 1/2 & -1/2 \\end{pmatrix}$",
        "options": [
            "$A^{-1} = \\begin{pmatrix} 1 & 0 & 0 \\\\ 0 & 1 & 0 \\\\ 0 & 0 & 1 \\end{pmatrix}$",
            "$A^{-1} = \\begin{pmatrix} -1/2 & 1/2 & 1/2 \\\\ 1/2 & -3/2 & 1/2 \\\\ 1/2 & 1/2 & -1/2 \\end{pmatrix}$",
            "$A^{-1} = \\begin{pmatrix} 1 & 1 & 1 \\\\ 1 & 0 & 1 \\\\ 1 & 1 & 1 \\end{pmatrix}$",
            "The matrix is singular and cannot be inverted."
        ]
    },
    # --- Lesson 4.1: Undirected graph ---
    {
        "id": 41,
        "unit": 4,
        "difficulty": "Easy",
        "question": "Given a graph with nodes $\{w_1, w_2, w_3, w_4\}$, multiple edges between $w_2$ and $w_3$, and a loop at $w_3$, which statement is true?",
        "answer": "The graph is NOT a simple graph.",
        "options": [
            "The graph is a simple graph.",
            "The graph is NOT a simple graph.",
            "Nodes $w_3$ and $w_4$ are adjacent if no edge exists between them.",
            "The graph consists of five nodes."
        ]
    },
    {
        "id": 42,
        "unit": 4,
        "difficulty": "Easy",
        "question": "If a graph has an edge $e_5$ that starts and ends at node $w_3$, how is this represented in the incidence mapping $\\phi$?",
        "answer": "$\\phi(e_5) = \{w_3\}$ (a loop)",
        "options": [
            "$\\phi(e_5) = \{w_3, w_1\}$",
            "$\\phi(e_5) = \\emptyset$",
            "$\\phi(e_5) = \{w_3\}$ (a loop)",
            "$\\phi(e_5) = \{w_3, w_3, w_3\}$"
        ]
    },
    {
        "id": 43,
        "unit": 4,
        "difficulty": "Medium",
        "question": "A graph has a finite number of nodes, one loop, and some isolated nodes. Which classification is correct?",
        "answer": "It is a finite graph, but not a simple or connected graph.",
        "options": [
            "It is a simple and connected graph.",
            "It is an infinite graph.",
            "It is a finite graph, but not a simple or connected graph.",
            "It is connected because it is finite."
        ]
    },
    {
        "id": 44,
        "unit": 4,
        "difficulty": "Medium",
        "question": "If a graph consists of two separate groups of nodes that are not connected by any edges, what can be said about it?",
        "answer": "The graph consists of at least two subgraphs and is not connected.",
        "options": [
            "The graph is a simple connected graph.",
            "The graph has a loop at every node.",
            "The graph consists of at least two subgraphs and is not connected.",
            "All nodes in the graph are adjacent."
        ]
    },
    {
        "id": 45,
        "unit": 4,
        "difficulty": "Hard",
        "question": "A graph contains only a single node and no edges. Which statement is true?",
        "answer": "It is a simple graph and it is contiguous (connected).",
        "options": [
            "It is not a graph because it has no edges.",
            "It is a simple graph and it is contiguous (connected).",
            "It is a multi-graph.",
            "It is a disconnected graph."
        ]
    },
    # --- Lesson 4.2: Further properties of graphs ---
    {
        "id": 46,
        "unit": 4,
        "difficulty": "Easy",
        "question": "In a graph where one node has degree 1 and three nodes have degree 3, what must be true about the sum of all degrees?",
        "answer": "The sum is 10, which is even (consistent with the Handshaking Lemma).",
        "options": [
            "The sum is 9.",
            "The sum is 10, which is even (consistent with the Handshaking Lemma).",
            "The sum must be odd.",
            "A graph with these degrees cannot exist."
        ]
    },
    {
        "id": 47,
        "unit": 4,
        "difficulty": "Easy",
        "question": "If node $w_3$ has one edge connecting to $w_1$, two edges connecting to $w_2$, and one loop, what is the degree of $w_3$?",
        "answer": "5",
        "options": ["3", "4", "5", "6"]
    },
    {
        "id": 48,
        "unit": 4,
        "difficulty": "Medium",
        "question": "Is it sufficient for two graphs to have the same number of nodes and edges to be isomorphic?",
        "answer": "No, the structural connection (mapping) between nodes must also be preserved.",
        "options": [
            "Yes, that is the definition of isomorphism.",
            "No, they must also have the same number of loops.",
            "No, the structural connection (mapping) between nodes must also be preserved.",
            "Yes, as long as the nodes are labeled the same."
        ]
    },
    {
        "id": 49,
        "unit": 4,
        "difficulty": "Medium",
        "question": "When checking if two graphs are isomorphic, what are you allowed to do to the 'edges' of the first graph to match the second?",
        "answer": "Bend, stretch, or contract them, but not cut or knot them.",
        "options": [
            "Cut them and reconnect them elsewhere.",
            "Add new nodes if needed.",
            "Bend, stretch, or contract them, but not cut or knot them.",
            "Only rotate the graph 90 degrees."
        ]
    },
    {
        "id": 50,
        "unit": 4,
        "difficulty": "Hard",
        "question": "According to Euler's formula for planar graphs, what is the relationship between nodes ($v$), edges ($e$), and faces ($f$)?",
        "answer": "$v - e + f = 2$",
        "options": [
            "$v + e + f = 2$",
            "$v - e + f = 2$",
            "$v + e - f = 2$",
            "$v - e - f = 0$"
        ]
    },
    # --- Lesson 4.3: Adjacency matrix ---
    {
        "id": 51,
        "unit": 4,
        "difficulty": "Easy",
        "question": "In an adjacency matrix, how is a loop at node $i$ typically represented?",
        "answer": "The diagonal element $a_{ii}$ is 2.",
        "options": [
            "The diagonal element $a_{ii}$ is 1.",
            "The diagonal element $a_{ii}$ is 2.",
            "The entire row $i$ is filled with 1s.",
            "Loops are not represented in adjacency matrices."
        ]
    },
    {
        "id": 52,
        "unit": 4,
        "difficulty": "Easy",
        "question": "Given the adjacency matrix row for node B: $[1, 2, 1, 1]$, how many loops does node B have?",
        "answer": "1",
        "options": ["0", "1", "2", "4"]
    },
    {
        "id": 53,
        "unit": 4,
        "difficulty": "Medium",
        "question": "If an adjacency matrix $A$ for a graph with nodes $\{A, B, C, D\}$ has $a_{11} = 2$ and $a_{12} = 1$, what edges are connected to node A?",
        "answer": "One loop at A and one edge to B.",
        "options": [
            "Two edges to A and two edges to B.",
            "One loop at A and one edge to B.",
            "One edge to A and one loop to B.",
            "Node A is isolated."
        ]
    },
    {
        "id": 54,
        "unit": 4,
        "difficulty": "Medium",
        "question": "If the 5th row and 5th column of a 5x5 adjacency matrix are all zeros, what does this indicate about node 5?",
        "answer": "Node 5 is an isolated node.",
        "options": [
            "Node 5 has a loop.",
            "Node 5 is connected to all other nodes.",
            "Node 5 is an isolated node.",
            "The graph is a complete graph."
        ]
    },
    {
        "id": 55,
        "unit": 4,
        "difficulty": "Hard",
        "question": "How can you use adjacency matrices to prove two graphs $G$ and $H$ are isomorphic?",
        "answer": "By finding a node mapping such that the adjacency matrix of $G$ is identical to the adjacency matrix of $H$.",
        "options": [
            "By checking if the sum of all elements in both matrices is the same.",
            "By finding a node mapping such that the adjacency matrix of $G$ is identical to the adjacency matrix of $H.",
            "By ensuring both matrices have the same number of zeros.",
            "Adjacency matrices cannot be used to prove isomorphism."
        ]
    }
]