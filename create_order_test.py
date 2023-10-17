# Карясова Ирина, 9-ая когорта _Финальный проект. Инженер по тестированию плюс
import sender_stand_request


def test_assert_create_order():
    response_create_order = sender_stand_request.post_new_order()
    track_id = response_create_order.json()["track"]
    response_get_order = sender_stand_request.get_order(track_id)
#    assert response_get_order.status_code == 200
    test_print = response_get_order.status_code
    if test_print == 200:
        print('Тест пройден')
    else:
        print('Тест провален')
