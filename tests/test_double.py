# Copyright 2022 Facundo Batista
# Licensed under the LGPL v2.1 License
# For further info, check https://github.com/facundobatista/tencdec

"""Tests to verify encoding and decoding."""

import pytest

from tencdec import encode, decode


@pytest.mark.parametrize("source", [
    [0, 1, 2, 3, 4],
    [4, 28, 87, 89],
    [500, 501, 507, 508],
    [23, 21338941],
    [1, 15, 16, 16, 17],
    [0, 1, 2, 3, 4, 28, 87, 87, 500, 501, 507, 913],
])
def test_sanity(source):
    enc = encode(source)
    dec = decode(enc)
    assert dec == source
