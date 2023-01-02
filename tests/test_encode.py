# Copyright 2022 Facundo Batista
# Licensed under the LGPL v2.1 License
# For further info, check https://github.com/facundobatista/tencdec

"""Tests for encoding particular cases."""

import pytest

from tencdec import encode


@pytest.mark.parametrize("source, should_encoded", [
    ([0, 1, 2], b"\x00\x01\x01"),
    ([4, 6, 8], b"\x04\x02\x02"),
    ([500, 1500], b"\xf4\x03\xe8\x07"),
    ([2, 3, 3, 3, 4], b"\x02\x01\x00\x00\x01"),
])
def test_simple(source, should_encoded):
    enc = encode(source)
    assert enc == should_encoded


def test_result_type():
    enc = encode([1, 2])
    assert isinstance(enc, bytes)


@pytest.mark.parametrize("source", [
    [0, 1.5, 2],
    [0, 1, (2 + 3j)],
])
def test_only_integers(source):
    with pytest.raises(TypeError):
        encode(source)


@pytest.mark.parametrize("source", [
    [0, 1, 2, 1, 3],
    [0, 0, -1, 0],
])
def test_increasing(source):
    with pytest.raises(AssertionError):
        encode(source)
