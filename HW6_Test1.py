import HW6_Task1 as task1


def test_get_created_instances():
    assert task1.User.get_created_instances() == 0


def test_instances_up():
    user, _, _ = task1.User(), task1.User(), task1.User()
    assert user.get_created_instances() == 3


def test_reset_instances_counter():
    user, _, _ = task1.User(), task1.User(), task1.User()
    assert user.reset_instances_counter() == 3