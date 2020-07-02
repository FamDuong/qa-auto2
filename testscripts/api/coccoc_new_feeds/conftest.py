import pytest

from utils_automation.database import MySQL

mysql_drive = MySQL()


@pytest.fixture(scope='session')
def coccoc_new_feeds_db_interact():
    from config.environment import COCCOC_NEW_FEED_DATA_DB_SERVER
    from config.environment import COCCOC_NEW_FEED_DATA_DB_NAME
    from config.environment import COCCOC_NEW_FEED_DATA_DB_USERNAME
    from config.environment import COCCOC_NEW_FEED_DATA_DB_PASSWORD
    connection = mysql_drive.connect(host_name=COCCOC_NEW_FEED_DATA_DB_SERVER, database_name=COCCOC_NEW_FEED_DATA_DB_NAME
                                     , user_name=COCCOC_NEW_FEED_DATA_DB_USERNAME
                                     , password=COCCOC_NEW_FEED_DATA_DB_PASSWORD)
    yield connection
    mysql_drive.close(connection)



