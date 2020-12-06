from skpy import Skype

from config.credentials import SKYPE_BOT_ACCOUNT_NAME, SKYPE_BOT_PASSWORD


class SkypeLocalUtils:

    def __new__(cls):

        if not hasattr(cls, 'instance'):
            cls.instance = super(SkypeLocalUtils, cls).__new__(cls)

        return cls.instance

    @staticmethod
    def access_skype():
        return Skype(SKYPE_BOT_ACCOUNT_NAME, SKYPE_BOT_PASSWORD)

    def __init__(self):
        self.skype = self.access_skype()

    def __enter__(self):
        return self

    def access_group(self, skype_group_id):
        return self.skype.chats[skype_group_id]

    def send_message_group_skype(self, skype_group_id, message):
        return self.access_group(skype_group_id).sendMsg(message)

    # image_path (file): file-like object to retrieve the attachment's body
    # image_name (str): filename displayed to other clients
    # is_image (bool): whether to treat the file as an image
    def send_message_group_skype_with_image(self, skype_group_id, message, image_path, image_name = "image_error.png", is_image = True):
        skype_group = self.access_group(skype_group_id)
        skype_group.sendMsg(message)
        skype_group.sendFile(open(image_path, "rb"), image_name, is_image)
        return skype_group


