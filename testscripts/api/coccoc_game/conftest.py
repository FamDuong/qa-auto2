import pytest

from utils_automation.database import MySQL

mysql_drive = MySQL()


@pytest.fixture(scope='session')
def coccoc_game_api_db():
    from config.environment import COCCOC_GAME_API_DB_SERVER
    from config.environment import COCCOC_GAME_API_DB_NAME
    from config.environment import COCCOC_GAME_API_DB_USER_NAME
    from config.environment import COCCOC_GAME_API_DB_PASSWORD
    connection = mysql_drive.connect(host_name=COCCOC_GAME_API_DB_SERVER, database_name=COCCOC_GAME_API_DB_NAME
                                     , user_name=COCCOC_GAME_API_DB_USER_NAME
                                     , password=COCCOC_GAME_API_DB_PASSWORD)
    yield connection
    mysql_drive.close(connection)


