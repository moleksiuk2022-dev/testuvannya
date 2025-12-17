from app import Figure


def test_get_angles():
    fig = "triangle"
    triangle = Figure(fig, 1)
    assert triangle.get_angles == 3

def test_square_angles():
    fig = "square"
    square = Figure(fig, 2)
    assert square.get_angles == 4
