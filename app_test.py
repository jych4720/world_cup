from app import app


def test_search_player_not_found():
    with app.test_client() as client:
        response = client.post('/search_player', data={'player_name': 'Nonexistent Player'})
        assert b"Player Nonexistent Player not found." in response.data

def test_search_player_messi():
    with app.test_client() as client:
        response = client.post('/search_player', data={'player_name': 'Messi'})
        assert response.status_code == 200
        assert b"Messi" in response.data  
        assert b"Goals scored" in response.data  
        assert b"Matches played" in response.data
        assert b"Goals per match" in response.data
