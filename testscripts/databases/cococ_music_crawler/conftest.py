import pytest

from utils_automation.database import MySQL

mysql_drive = MySQL()


@pytest.fixture(scope='session')
def cococ_music_crawler_db_interact():
    from config.environment import COCOC_MUSIC_CRAWLER_DB_SERVER
    from config.environment import COCCOC_MUSIC_CRAWLER_DB_NAME
    from config.environment import COCOC_MUSIC_CRAWLER_DB_USER_NAME
    from config.environment import COCCOC_MUSIC_CRAWLER_DB_PASS_WORD
    connection = mysql_drive.connect(COCOC_MUSIC_CRAWLER_DB_SERVER, COCCOC_MUSIC_CRAWLER_DB_NAME
                                     , COCOC_MUSIC_CRAWLER_DB_USER_NAME, COCCOC_MUSIC_CRAWLER_DB_PASS_WORD)
    yield connection
    mysql_drive.close(connection)









