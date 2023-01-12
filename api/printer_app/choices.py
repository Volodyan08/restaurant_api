from enum import Enum, auto


class CHECK_TYPE(Enum):
    KITCHEN = auto()
    CLIENT = auto()


class PRINTER_TYPE(CHECK_TYPE):
    pass


class CHECK_STATUS(Enum):
    NEW = auto()
    RENDERED = auto()
    PRINTED = auto()
