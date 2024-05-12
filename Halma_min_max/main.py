from copy import deepcopy
from game import Board
import random
from time import time
from strategies import Strategies
from minmax import minimax, alfabeta
from const import P1_START_POSITIONS, P2_START_POSITIONS




def simulate_game(heuristic, depth=3):
    board = Board()
    turn_num = 1
    while not board.is_game_over():
        print(f'Turn: {int(turn_num)}, Player: {board.turn}')
        player = board.turn
        best_move = None
        best_move = alfabeta(
            board, 2, True, player, heuristic)
        print(board)
        board.move_pawn(*best_move[1][0], *best_move[1][1])
        turn_num += 0.5

    print(board)
    print('\n\n----------------------------')
    print(f'Game won by: {board.is_game_over()}')


def simulate_game_adaptive(player1_heuristics, player2_heuristics, depth):
    board = Board()
    turn_num = 1
    while not board.is_game_over():
        print(f'Turn: {int(turn_num)}, Player: {board.turn}')
        player = board.turn
        if player == 1:
            keys = sorted(key for key in player1_heuristics.keys()
                          if key > turn_num)
            heuristic = player1_heuristics[keys[0]] if keys else player1_heuristics[list(player1_heuristics.keys())[-1]]
            best_move = alfabeta(board, 1, True, player, heuristic)
        else:
            keys = sorted(key for key in player2_heuristics.keys()
                          if key > turn_num)
            heuristic = player2_heuristics[keys[0]] if keys else player2_heuristics[list(player2_heuristics.keys())[-1]]
            best_move = alfabeta(board, depth, True, player, heuristic)
        print(board)
        board.move_pawn(*best_move[1][0], *best_move[1][1])
        turn_num += 0.5

    print(board)
    print('\n\n----------------------------')
    print(f'Game won by: {board.is_game_over()}')


if __name__ == '__main__':
    p1_heuristics = {5: Strategies.halfrandom, 200: Strategies.complex}
    p2_heuristics = {1: Strategies.complex}
    p3_heuristics = {1: Strategies.halfrandom}
    #simulate_game_adaptive(p2_heuristics, p2_heuristics, 2)
    simulate_game(Strategies.complex, 2)
