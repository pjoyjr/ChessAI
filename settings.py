GUI_WIDTH = GUI_HEIGHT = 512
BOARD_DIM = 8
TOTAL_SQUARES = BOARD_DIM * BOARD_DIM
GUI_SQ_SIZE = GUI_WIDTH // BOARD_DIM
FPS = 18
BOARD_COLOR_1='lightsalmon'
BOARD_COLOR_2='plum'


IMG_PATH = "png\\"
PIECE_IMG_MAPPING = {
    "b": IMG_PATH + "b.png",
    "k": IMG_PATH + "k.png",
    "n": IMG_PATH + "n.png",
    "p": IMG_PATH + "p.png",
    "q": IMG_PATH + "q.png",
    "r": IMG_PATH + "r.png",
    "B": IMG_PATH + "Bb.png",
    "K": IMG_PATH + "Bk.png",
    "N": IMG_PATH + "Bn.png",
    "P": IMG_PATH + "Bp.png",
    "Q": IMG_PATH + "Bq.png",
    "R": IMG_PATH + "Br.png",
}

RANK_MAPPING = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
}