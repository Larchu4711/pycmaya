from pycmaya import format_now


def test_format_now():
    result = format_now()
    assert isinstance(result, str)
    assert 'T' in result and result.endswith('Z')
