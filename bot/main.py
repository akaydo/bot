#!/usr/local/bin/python
# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api
from datetime import datetime


token = "570622413ab98962ffbf414293b043accf047fb3ee31ed2405fb907cab6268a1f4d222762596a8811303f"
vk_session = vk_api.VkApi(token=token)

session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)

while True:
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            print('Сообщение пришло в: ' + str(datetime.strftime(datetime.now(), "%H:%M:%S")))
            print('Текст сообщения: ' + str(event.text))
            response = event.text.lower()
            if event.from_user and not (event.from_me):
                if response == "привет":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Привет, дружок!', 'random_id': 0})
                elif response == "пока":
                    vk_session.method('messages.send', {'user_id': event.user_id, 'message': 'Пока, мур :3', 'random_id': 0})