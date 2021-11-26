import unittest
from typing import List, Any

from .utils_test.test_error import TestError
from .utils_test.test_tree_walker import TestTreeWalker
from .tokenizer_test.test_token import TestToken
from .tokenizer_test.test_token_type import TestTokenType
from .tokenizer_test.test_tokenizer import TestTokenizer
from .opcode_test.test_op_type import TestOpType
from .opcode_test.test_opcode import TestOpCode


def run_tests() -> None:
    test_classes_to_run: List[Any] = [
        TestError,
        TestTreeWalker,
        TestToken,
        TestTokenType,
        TestTokenizer,
    ]
    test_classes_to_run += [TestOpType, TestOpCode]

    loader: unittest.TestLoader = unittest.TestLoader()

    suites_list: List[unittest.TestSuite] = []
    for test_class in test_classes_to_run:
        suite: unittest.TestSuite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite: unittest.TestSuite = unittest.TestSuite(suites_list)

    runner: unittest.TextTestRunner = unittest.TextTestRunner()
    runner.run(big_suite)
