import pytest

require_xfail = False


def pytest_addoption(parser):
    parser.addoption(
        "--require-xfail", action="store_true", help="Require that all tests xfail."
    )


def pytest_configure(config):
    global require_xfail
    require_xfail = getattr(config.option, "require_xfail", False)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_call(item):
    outcome = yield
    outcome.get_result()  # raises if outcome is an exception
    # This runs _after_ successful tests only
    if require_xfail:
        raise RuntimeError(f"Test {item.name} did not xfail.")
