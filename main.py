import chess
from os import system
from stockfish import Stockfish
from fentoboardimage import fenToImage, loadPiecesFolder
board = chess.Board()
stockfish = Stockfish(path=r'./stockfish.exe')
stockfish.set_skill_level(20)

system("cls")

def nl():
    print("")

def getBestMove(fen):
    global isFlipped
    global blackview
    stockfish.set_fen_position(fen)

    best = stockfish.get_best_move()

    mateIn = stockfish.get_top_moves(1)[0]['Mate']

    board.push_san(best)


    stockfish.set_fen_position(board.fen())
    print(stockfish.get_board_visual(blackview))


    nl()
    print("=====[Best Move]=====")
    if mateIn != None:
        print(f"   {best}  -- Mate in {mateIn}")
    else:
        print(f"   {best}")
    print("=====================")

    boardImage = fenToImage(
        fen=board.fen(),
        squarelength=100,
        pieceSet=loadPiecesFolder("./pieces"),
        darkColor="#D18B47",
        lightColor="#FFCE9E",
        flipped = isFlipped
    )
    boardImage.save("chessboard.png", "PNG")



def main():
    global blackview
    global isFlipped
    for lp in range(200):
        nl()
        print("===============================")
        try:
            move = input("Oponent's move: ")
        except KeyboardInterrupt:
            exit()
        except:
            exit()
        try:
            board.push_san(move)
            getBestMove(board.fen())
        except:
            print("ERROR")
            main()
        nl()
try:
    nl()
    black = input("Start as black? (Y/N): ")
except KeyboardInterrupt:
    exit()
if black == "Y" or black == "y":
    isFlipped = True
    blackview = False
    main()
else:
    isFlipped = False
    blackview = True
    getBestMove(board.fen())
    nl()
    main()





