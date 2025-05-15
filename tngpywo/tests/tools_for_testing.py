import ast
import inspect
import os
from contextlib import contextmanager
from textwrap import dedent

from asserts import assert_true
from astsearch import ASTPatternFinder, prepare_pattern


@contextmanager
def temporary_working_directory(file):
    old_dir = os.getcwd()
    os.chdir(os.path.dirname(os.path.abspath(file)))
    try:
        yield
    finally:
        os.chdir(old_dir)


def check_contains_code_pattern(source_function, ast_pattern):
    source = dedent(inspect.getsource(source_function))
    ast_of_function = ast.parse(source)
    finder = ASTPatternFinder(prepare_pattern(ast_pattern))
    return any(finder.scan_ast(ast_of_function))


def assert_contains_code_pattern(source_function, ast_pattern, hint):
    assert_true(
        check_contains_code_pattern(source_function, ast_pattern),
        escape_message(
            f'While your solution works, it does not look "Pythonic". {hint}: {ast_pattern}'
        ),
    )


def check_calls_function(source_function, builtin_function_name):
    source = dedent(inspect.getsource(source_function))
    ast_of_function = ast.parse(source)
    finder = ASTPatternFinder(
        ast.Call(func=ast.Name(id=builtin_function_name), ctx=ast.Load())
    )
    return any(finder.scan_ast(ast_of_function))


def assert_calls_builtin_function(source_function, builtin_function_name, hint=None):
    if not hint:
        hint = 'While your solution works, it does not look "Pythonic". '
        f'Please use the built-in function "{builtin_function_name}"'
    assert_true(
        check_calls_function(source_function, builtin_function_name),
        escape_message(hint),
    )


def escape_message(hint):
    # assert_true runs the messages through str.format.
    # Because patterns commonly contain { or }, we need to escape them.
    return hint.replace("{", "{{").replace("}", "}}")
