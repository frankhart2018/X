from typing import List

from ...opcode.opcode import OpCode
from .node import Node


class ExprNode(Node):
    def __init__(self, expr: Node, dtype: str) -> None:
        self.__expr = expr
        self.__dtype = dtype

    @property
    def expr(self) -> Node:
        return self.__expr

    @property
    def dtype(self) -> str:
        return self.__dtype

    def walk_and_print(self, tab_level: int) -> str:
        ast_string: str = self._add_tabs(tab_level=tab_level)
        ast_string += "ExprNode(\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += "expr=(\n"
        tab_level += 1

        ast_string += self.__expr.walk_and_print(tab_level)

        tab_level -= 1
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += f"dtype='{self.__dtype}'\n"
        ast_string += self._add_tabs(tab_level=tab_level)
        ast_string += ")\n"

        return ast_string

    def walk_and_compile(self, opcodes: List[OpCode]) -> None:
        self.__expr.walk_and_compile(opcodes)
