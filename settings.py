GUI_WIDTH = GUI_HEIGHT = 512
BOARD_DIM = 8
TOTAL_SQUARES = BOARD_DIM * BOARD_DIM
GUI_SQ_SIZE = GUI_WIDTH // BOARD_DIM
FPS = 18
BOARD_COLOR_1='lightsalmon'
BOARD_COLOR_2='plum'
BOARD_COLOR_HIGHLIGHTED_TILES="palegoldenrod"

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

FILE_INT_TO_STR_MAPPING = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}
FILE_STR_TO_INT_MAPPING = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
}