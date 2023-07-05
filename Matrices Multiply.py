import tkinter as tk

def multiply_matrices():
    matrix1 = [[int(entry.get()) for entry in row] for row in matrix1_entries]
    matrix2 = [[int(entry.get()) for entry in row] for row in matrix2_entries]

    result_matrix = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    # Update the result matrix entries in the GUI
    for i in range(len(result_matrix)):
        for j in range(len(result_matrix[0])):
            result_entries[i][j].delete(0, tk.END)
            result_entries[i][j].insert(tk.END, result_matrix[i][j])

# Create the GUI window
root = tk.Tk()
root.title("Matrix Multiplication")

# Create the matrix 1 input grid
matrix1_entries = []
for i in range(3):
    row = []
    for j in range(3):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j)
        row.append(entry)
    matrix1_entries.append(row)

# Create the matrix 2 input grid
matrix2_entries = []
for i in range(3):
    row = []
    for j in range(3):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j + 5)
        row.append(entry)
    matrix2_entries.append(row)

# Create the multiply button
multiply_button = tk.Button(root, text="Multiply", command=multiply_matrices)
multiply_button.grid(row=4, column=2, pady=10)

# Create the result matrix grid
result_entries = []
for i in range(3):
    row = []
    for j in range(3):
        entry = tk.Entry(root, width=10)
        entry.grid(row=i, column=j + 10)
        entry.config(state=tk.DISABLED)  # Disable editing
        row.append(entry)
    result_entries.append(row)

# Run the GUI main loop
root.mainloop()
