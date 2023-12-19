from unittest.mock import patch, Mock
from dotenv import load_dotenv
import os
from datetime import datetime
from src.sportsradar.extract.gamefeeds import GameFeeds
from src.sportsradar.workspace.datastore import DataStore

load_dotenv('../../../../../.env')


class TestConstants():
    BASE_URL = 'https://api.sportradar.us/nfl/official'
    ACCESS_LEVEL = 'trial'
    VERSION = 'v7'
    LANGUAGE_CODE = 'en'
    FORMAT = 'json'
    API_KEY = f'{os.environ.get("APIKEY")}'


@patch('os.getenv', return_value=TestConstants.API_KEY)
@patch('src.sportsradar.extract.gamefeeds.GameFeeds')
def test_game_feeds_with_box_score(mock_data_store, mock_getenv):
    # Execute
    game_feeds = GameFeeds(base_url=TestConstants.BASE_URL)
    game_id = '251ac0cf-d97d-4fe8-a39e-09fc4a95a0b2'
    result = game_feeds.get_game_boxscore(access_level=TestConstants.ACCESS_LEVEL,
                                          language_code=TestConstants.LANGUAGE_CODE, version=TestConstants.VERSION,
                                          game_id=game_id, file_format=TestConstants.FORMAT,
                                          api_key=TestConstants.API_KEY)
    # Check
    assert result.status_code == 200

@patch('os.getenv', return_value=TestConstants.API_KEY)
@patch('src.sportsradar.extract.gamefeeds.GameFeeds')
def test_game_feeds_with_game_roster(mock_data_store, mock_getenv):
    # Execute
    game_feeds = GameFeeds(base_url=TestConstants.BASE_URL)
    game_id = '251ac0cf-d97d-4fe8-a39e-09fc4a95a0b2'
    result = game_feeds.get_game_roster(access_level=TestConstants.ACCESS_LEVEL,
                                        language_code=TestConstants.LANGUAGE_CODE, version=TestConstants.VERSION,
                                        game_id=game_id, file_format=TestConstants.FORMAT,
                                        api_key=TestConstants.API_KEY)
    assert result.status_code == 200


@patch('os.getenv', return_value=TestConstants.API_KEY)
@patch('src.sportsradar.extract.gamefeeds.GameFeeds')
def test_game_feeds_with_game_statistics(mock_data_store, mock_getenv):
    # Execute
    game_feeds = GameFeeds(base_url=TestConstants.BASE_URL)
    game_id = '251ac0cf-d97d-4fe8-a39e-09fc4a95a0b2'
    result = game_feeds.get_game_statistics(access_level=TestConstants.ACCESS_LEVEL,
                                        language_code=TestConstants.LANGUAGE_CODE, version=TestConstants.VERSION,
                                        game_id=game_id, file_format=TestConstants.FORMAT,
                                        api_key=TestConstants.API_KEY)
    assert result.status_code == 200

@patch('os.getenv', return_value=TestConstants.API_KEY)
@patch('src.sportsradar.extract.gamesfeeds.GameFeeds')
def test_game_feeds_with_current_season_schedule(mock_data_store, mock_getenv):
    #Execute
    result = game_feeds.get_current_season_schedule(access_level=TestConstants.ACCESS_LEVEL,
                                                    language_code=TestConstants.LANGUAGE_CODE, version=TestConstants.VERSION,
                                                    game_id=game_id, file_format=TestConstants.FORMAT,
                                                    api_key=TestConstants.API_KEY)
    assert result.status_code == 200

@patch('os.getenv', return_value=TestConstants.API_KEY)
@patch('src.sportsradar.extract.gamesfeeds.GamesFeeds')
def test_game_feeds_with_current_week_schedule(mock_data_store, mock_getenv):
    #Execute
    result = game_feeds.get_current_week_schedule(access_level=TestConstants.ACCESS_LEVEL,
                                                language_code=TestConstants.LANGUAGE_CODE, version=TestConstants.VERSION,
                                                game_id=game_id, file_format=TestConstants.FORMAT,
                                                api_key=TestConstants.API_KEY)
    assert result.status_code == 200

@patch('os.getenv', return_value=TestConstants.API_KEY)
@patch('src.sportsradar.extract.gamesfeeds.GamesFeeds')
def test_game_feeds_with_season_schedule(mock_data_store, mock_getenv):
    #Execute
    year = 2022
    season_type = 'REG'
    result = game_feeds.current_season(access_level=TestConstants.ACCESS_LEVEL,
                                           language_code=TestConstants.LANGUAGE_CODE, version=TestConstants.VERSION,
                                           year=year, season_type=season_type,
                                           file_format=TestConstants.FORMAT,
                                           api_key = TestConstants.API_KEY
                                        )

    assert result.status_code == 200


@patch('os.getenv', return_value=TestConstants.API_KEY)
@patch('src.sportsradar.extract.gamesfeeds.GameFeeds')
def test_game_feeds_with_weekly_schedule(mock_data_store, mock_getenv):
    #Execute
    year = 2022
    season_type = 'REG'
    week_number = datetime.now().isocalendar()[1] -7
    result= game_feeds.current_week(access_level = TestConstants.ACCESS_LEVEL,
                                    language_code=TestConstants.LANGUAGE_CODE,  version=TestConstants.VERSION,
                                    year=year, season_type=season_type, week_number=week_number,
                                    file_format=TestConstants.FORMAT,
                                    api_key = TestConstants.API_KEY
                                    )
    assert result.status_code == 200
