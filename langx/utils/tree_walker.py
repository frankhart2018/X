from ..parser.node.node import Node


class TreeWalker:
    def __init__(self, root: Node):
        self.__root: Node = root

    def walk(self) -> str:
        tab_level: int = 0
        ast_string: str = self.__root.walk_and_print(tab_level=tab_level)

        return ast_string
