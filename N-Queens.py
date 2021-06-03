"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.


"""
import copy
def solveNQueens(n: int):
    board = [[' ' for i in range(n)] for j in range(n)]
    def NQueenRecur(board, curser):
        if curser == n:
            return [board]
        placement = []
        for i in range(n):
            if board[curser][i] == ' ':
                board_copy = copy.deepcopy(board)
                board_copy[curser] = ["."] * n
                board_copy[curser][i] = 'Q'
                distance_to_edge = n - curser
                for j in range(1, distance_to_edge):
                    board_copy[curser+j][i] = '.'
                    if i+j < n:
                        board_copy[curser+j][i+j] = '.'
                    if i-j >=0:
                        board_copy[curser+j][i-j] = '.'
                placement.extend(NQueenRecur(board_copy, curser+1))
        return placement
    result = []
    for sol in NQueenRecur(board, 0):
        for i in range(len(sol)):
            sol[i] = ''.join(sol[i])
        result.append(sol)
    return result


def solveNQueens2(n: int):
    
    def NQueenRecur(row, queens_loc):
        
        return placement
    result = []
    for sol in NQueenRecur(board, 0):
        for i in range(len(sol)):
            sol[i] = ''.join(sol[i])
        result.append(sol)
    return result


if __name__ == "__main__":
    import numpy as np
    n = 4
    solution = solveNQueens(n)
    print("Found {} solutions:".format(len(solution)))
    for sol in solution:
        print(np.array(sol))


