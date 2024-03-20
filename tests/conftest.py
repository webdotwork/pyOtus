import pytest


@pytest.fixture()
def rectangle_data_d():
    side_a, side_b, name = 3, 5, "YYY"

    yield side_a, side_b, name


@pytest.fixture()
def triangle_data_d():
    side_a, side_b, side_c = 3, 5, 4

    yield side_a, side_b, side_c


@pytest.fixture(scope="session")
def circle_data_n():
    name = "YYY"
    print(f"\nbefore test {name}")

    yield

    side_a, side_b, name = 3, 5, "YYY"
    print(f"\nafter test {side_a} {name} {side_b}")


@pytest.fixture(scope="function")
def square_data_sf():
    name = "XXX"
    print(f"\nbefore test {name}")

    yield

    side_a, side_b, name = 3, 5, "XXX"
    print(f"\nafter test {side_a} {name} {side_b}")


@pytest.fixture()
def rectangle_data_w():

    def _wrapper(data: str):
        if data == "integer":
            return 3, 5, "YYY"
        if data == "float":
            return 1, 2, "XXX"

    yield _wrapper
