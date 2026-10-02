import pytest
from age_checker import check_age


@pytest.mark.parametrize("age, expected", [
    (17, "Too young"),
    (101, "Too old")
])


@pytest.mark.asyncio
async def test_age_failure(age, expected):
    with pytest.raises(ValueError, match=expected):
        await check_age(age)


@pytest.mark.asyncio
async def test_age_success():
    assert await check_age(31) == "OK"