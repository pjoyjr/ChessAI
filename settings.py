WHITEAI = False
BLACKAI = True
FPS = 18

BOARD_DIM = 8
GUI_BOARD_WIDTH = GUI_BOARD_HEIGHT = 512
TOTAL_SQUARES = BOARD_DIM * BOARD_DIM
GUI_SQ_SIZE = GUI_BOARD_WIDTH // BOARD_DIM

GUI_GRAVEYARD_HEIGHT = 150
GUI_GRAVEYARD_WIDTH = GUI_BOARD_WIDTH

GUI_SPACING_COLUMN_WIDTH = 25
GUI_SPACING_COLUMN_HEIGHT =  GUI_BOARD_HEIGHT*2+GUI_BOARD_HEIGHT

GUI_BOARD_HEIGHT_OFFSET = GUI_GRAVEYARD_HEIGHT
GUI_BOARD_WIDTH_OFFSET = GUI_SPACING_COLUMN_WIDTH

GUI_SIDEBAR_WIDTH = 300
GUI_SIDEBAR_HEIGHT = GUI_SPACING_COLUMN_HEIGHT

BOARD_COLOR_1='lightsalmon'
BOARD_COLOR_2='plum'
BOARD_COLOR_HIGHLIGHTED_TILES="palegoldenrod"

IMG_PATH = "png\\"
PIECE_IMG_MAPPING = {
    "B": IMG_PATH + "b.png",
    "K": IMG_PATH + "k.png",
    "N": IMG_PATH + "n.png",
    "P": IMG_PATH + "p.png",
    "Q": IMG_PATH + "q.png",
    "R": IMG_PATH + "r.png",
    "b": IMG_PATH + "Bb.png",
    "k": IMG_PATH + "Bk.png",
    "n": IMG_PATH + "Bn.png",
    "p": IMG_PATH + "Bp.png",
    "q": IMG_PATH + "Bq.png",
    "r": IMG_PATH + "Br.png",
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