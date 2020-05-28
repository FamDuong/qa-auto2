import re


def check_game_url_format_for_game(iframe, game_url):
    if iframe == 0:
        if re.match('^.*\\?game_id=\\d', game_url):
            return True
        else:
            return False
    elif iframe == 1:
        if re.match('^.*\\?game_url=\\w(.*?)&game_id=\\d', game_url):
            return True
        else:
            return False
    else:
        raise ValueError


def check_game_url_format_for_event(iframe, game_url_for_event):
    if iframe == 0:
        if re.match('^.*\\?game_id=\\d(.*?)&event_code=\\w', game_url_for_event):
            return True
        else:
            return False
    elif iframe == 1:
        if re.match('^.*\\?game_url=\\w(.*?)&game_id=\\w(.*?)&event_code=\\w', game_url_for_event):
            return True
        else:
            return False
    else:
        raise ValueError



