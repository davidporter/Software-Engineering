from evaluate import parse_integer

def test_parse_integer(capfd):
    assert parse_integer(99) == None 

    parse_integer(100)
    out, err = capfd.readouterr()
    assert out == "99 bottles to go\n"

