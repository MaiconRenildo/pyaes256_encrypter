from pyaes256_encrypter import __version__,encode_text,decode_text


def test_version():
    assert __version__ == '1.0.6'


def test_encode_and_decode_text():
    key = "password"
    text = "hello world"
    assert decode_text(encode_text(text,key),key) == text