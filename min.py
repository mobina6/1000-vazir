import random
import sys

def solve_n_queens(n):
    """
    حل مسئله N-وزیر با استفاده از الگوریتم Minimum Conflicts
    """
    if n == 2 or n == 3:
        return None
    
    max_attempts = 100 if n <= 100 else 500
    
    for attempt in range(max_attempts):
        board = [random.randint(0, n - 1) for _ in range(n)]
        
        rows = [0] * n
        diag1 = [0] * (2 * n - 1)
        diag2 = [0] * (2 * n - 1)
        
        for col in range(n):
            row = board[col]
            rows[row] += 1
            diag1[row - col + n - 1] += 1
            diag2[row + col] += 1
        
        max_steps = n * 100 if n <= 100 else n * 200
        
        for step in range(max_steps):
            conflicted_cols = []
            
            for col in range(n):
                row = board[col]
                conflicts = (
                    rows[row] +
                    diag1[row - col + n - 1] +
                    diag2[row + col] - 3
                )
                
                if conflicts > 0:
                    conflicted_cols.append(col)
            
            if not conflicted_cols:
                return board
            
            col = random.choice(conflicted_cols)
            old_row = board[col]
            
            rows[old_row] -= 1
            diag1[old_row - col + n - 1] -= 1
            diag2[old_row + col] -= 1
            
            best_rows = []
            min_conflicts = float('inf')
            
            if n > 500:
                sample_size = min(n, 200)
                row_indices = random.sample(range(n), sample_size)
                
                for row in row_indices:
                    conflicts = (
                        rows[row] +
                        diag1[row - col + n - 1] +
                        diag2[row + col]
                    )
                    
                    if conflicts < min_conflicts:
                        min_conflicts = conflicts
                        best_rows = [row]
                    elif conflicts == min_conflicts:
                        best_rows.append(row)
            else:
                for row in range(n):
                    conflicts = (
                        rows[row] +
                        diag1[row - col + n - 1] +
                        diag2[row + col]
                    )
                    
                    if conflicts < min_conflicts:
                        min_conflicts = conflicts
                        best_rows = [row]
                    elif conflicts == min_conflicts:
                        best_rows.append(row)
            
            new_row = random.choice(best_rows)
            board[col] = new_row
            
            rows[new_row] += 1
            diag1[new_row - col + n - 1] += 1
            diag2[new_row + col] += 1
    
    return None


def write_solution_to_file(n, solution):

    with open('output.txt', 'w', encoding='utf-8') as f:
        if solution is None:
            f.write("No solution found\n")
        else:
            f.write(f"{n}\n")
            for row in solution:
                f.write(f"{row + 1}\n")


def verify_solution(board):
    n = len(board)
    rows = [0] * n
    diag1 = [0] * (2 * n - 1)
    diag2 = [0] * (2 * n - 1)
    
    for col in range(n):
        row = board[col]
        rows[row] += 1
        diag1[row - col + n - 1] += 1
        diag2[row + col] += 1
        
        if rows[row] > 1 or diag1[row - col + n - 1] > 1 or diag2[row + col] > 1:
            return False
    
    return True



def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input())
    
    solution = solve_n_queens(n)
    
    if solution is None:
        write_solution_to_file(n, None)
    else:
        if verify_solution(solution):
            write_solution_to_file(n, solution)
        else:
            write_solution_to_file(n, None)


if __name__ == "__main__":
    main()