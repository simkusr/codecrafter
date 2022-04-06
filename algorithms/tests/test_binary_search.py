import pytest

from algorithms.binary_search import binary_search

@pytest.mark.parametrize("arr, search_val, exp_val",
        [
            ([1,2,3], 2, (1,2)),
            (list(range(1,101)), 55, (54, 8)),
            ([4,6,8,9], 10, (None, 4)),
        ]
)
def test_binary_search(arr, search_val, exp_val):
    result = binary_search(arr, search_val)
    assert result == exp_val

