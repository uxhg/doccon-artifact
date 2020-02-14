from datalog.newtypes import FunctionName
from enum import Enum, auto
from typing import List


class Expr:
    def __init__(self, content: str):
        self.content = content

    def __str__(self) -> str:
        return f"$Literal(\"{self.content}\")"


class FnApply(Expr):
    func: FunctionName
    args: List[Expr]


class UnaryOp(Enum):
    NEG = auto


class BinLogicOp(Enum):
    OR = auto()
    AND = auto()


class BinOp(Enum):
    LT = auto()
    LEQ = auto()
    EQ = auto()
    NEQ = auto()
    GT = auto()
    GEQ = auto()


class Cmp(Expr):
    def __init__(self, op: BinOp, left: Expr, right: Expr):
        super().__init__("")
        self.op = op
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"$Cmp({self.left}, {self.right}, {self.op.name})"


class NegExpr(Expr):
    def __init__(self, e: Expr):
        super().__init__("")
        self.e = e

    def __str__(self) -> str:
        return f"$Neg({self.e})"


class Bool(Expr):
    def __init__(self, b: bool):
        super().__init__("")
        self.b = b

    def __str__(self) -> str:
        return f"$Bool({self.b})"
