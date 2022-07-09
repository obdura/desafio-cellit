from app.functions import get_id_from_plate, get_plate_from_id

def test_get_id_from_plate():
    assert get_id_from_plate('AAAA000') == 1
    assert get_id_from_plate('aaaa999') == 1000
    assert get_id_from_plate('aaab000') == 1001
    assert get_id_from_plate('aaac002') == 2003
    assert get_id_from_plate('zzzz998') == 456_975_999
    assert get_id_from_plate('ZZZZ999') == 456_976_000

def test_get_plate_from_id():
    assert get_plate_from_id(1) == 'aaaa000'
    assert get_plate_from_id(1001) == 'aaab000'
    assert get_plate_from_id('1002') == 'aaab001'
    assert get_plate_from_id(2001) == 'aaac000'
    assert get_plate_from_id(3000) == 'aaac999'
    assert get_plate_from_id(456_976_000) == 'zzzz999'