from skpy import Skype, SkypeChats


class SkypeLocalUtils:

    @staticmethod
    def access_skype():
        return Skype('ledinhcuong_99', 'maxim')

    def access_group(self, skype_group_id):
        return self.access_skype().chats[skype_group_id]

    def send_message_group_skype(self, skype_group_id, message):
        return self.access_group(skype_group_id).sendMsg(message)












