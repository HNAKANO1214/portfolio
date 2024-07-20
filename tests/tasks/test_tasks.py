from tasks import dummy_request


def test_index_view_get():
    '''ダミーリクエストのテスト
    '''
    try:
        dummy_request()
        assert True
    except Exception:
        assert False
