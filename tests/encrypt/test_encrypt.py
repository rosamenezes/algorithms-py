import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(0, 1)

    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("banana", 3.5)

    assert encrypt_message("message", 200) == "egassem"
    assert encrypt_message("message", 2) == "egass_em"
    assert encrypt_message("message", 3) == "sem_egas"
