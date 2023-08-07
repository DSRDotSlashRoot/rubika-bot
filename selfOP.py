from pyrubi import Bot
import requests ,json
# from PIL import Image, ImageDraw, ImageFont
# import arabic_reshaper
# from bidi.algorithm import get_display
import random

key = '!'
bot = Bot("session")
def err(chat_id , message_id) :
    pass
    # bot.send_text(chat_id=chat_id , 'متاسفانه خطایی رخ داده است ! \nمجدد امتحان کنید و در صورت ادامه داشتن خطا به پشتیبانی [@Vi_Russ] مراجعه کنید .' , message_id=message_id)
bot.send_text('u0EjTH10e93dfc0b48149016f6ab0ac4', 'srar')
for update in bot.on_message(chat_filter=['Channel'] , message_filter=['Gif', 'Video', 'Music', 'Image', 'Voice' , 'Other' , 'Edit' , 'FileInline' ,'Event' , 'FileInlineCaption' , 'RubinoStoryRubinoStory']):
    try :
        msg = update.data
        if update.author_id() == 'u0EjTH10e93dfc0b48149016f6ab0ac4' : # or update.chat_id()  == 
            text_mess = update.text()
            if text_mess[0] == key :
                ai_list = ['AI ' , ' AI' , 'ai ' , ' ai' , ' Ai' , 'Ai ']
                logo_list = ['LOGO ' , ' LOGO' , 'logo ' , ' logo' , 'Logo ' , ' Logo']
                stat_list = ['on' , 'off']
                if text_mess[1] + text_mess[2] == stat_list[0] :
                    stat_file = open('stat.txt')
                    stat_check = stat_file.readlines()[0]
                    stat_file.close()
                    if stat_check == 'on' :
                        bot.send_text('u0EjTH10e93dfc0b48149016f6ab0ac4' , 'ربات از قبل روشن بود !')
                    elif stat_check == 'off' :
                        edit_file = open('stat.txt' , 'w')
                        edit_file.write('on')
                        edit_file.close()
                        bot.send_text('u0EjTH10e93dfc0b48149016f6ab0ac4' , 'ربات روشن شد ! \nسرور ها در وضعیت عادی به سر میبرند ')
                    else :
                        edit_file = open('stat.txt' , 'w')
                        edit_file.write('on')
                        edit_file.close()
                        bot.send_text('u0EjTH10e93dfc0b48149016f6ab0ac4' , 'ربات روشن شد ! \nسرور ها در وضعیت عادی به سر میبرند \nاخطار : ربات فاقد وضعیت قبلی بود !')
                elif text_mess[1]+text_mess[2]+text_mess[3] == stat_list[1] :
                    stat_file = open('stat.txt')
                    stat_check = stat_file.readlines()[0]
                    stat_file.close()
                    if stat_check == 'off' :
                        bot.send_text('u0EjTH10e93dfc0b48149016f6ab0ac4' , 'ربات از قبل خاموش بود !')
                    elif stat_check == 'on' :
                        edit_file = open('stat.txt' , 'w')
                        edit_file.write('off')
                        edit_file.close()
                        bot.send_text('u0EjTH10e93dfc0b48149016f6ab0ac4' , 'ربات خاموش شد ! \nسرور ها در وضعیت عادی به سر میبرند :white_check_mark:')
                    else :
                        edit_file = open('stat.txt' , 'w')
                        edit_file.write('on')
                        edit_file.close()
                        bot.send_text('u0EjTH10e93dfc0b48149016f6ab0ac4' , 'ربات خاموش شد ! \nسرور ها در وضعیت عادی به سر میبرند :white_check_mark:\nاخطار : ربات فاقد وضعیت قبلی بود !')
                elif text_mess[1]+text_mess[2]+text_mess[3] in ai_list :
                    string = text_mess
                    try :
                        new_string = string[:0] + string[4:]
                        # req = requests.get(f'https://nahanabzar.ir/ai?text={new_string}') ## API V2
                        req = requests.get(f'https://api.fasttube.ir/?text={new_string}&key=RayaxKey') ## API V1
                        js = json.loads(req.text)
                        if js['status'] == True :
                            if js['code'] == 200 :
                                # bot.send_text(update.chat_id(), js["answer"] , update.message_id()) ## API V2
                                bot.send_text(update.chat_id(), js["message"] , update.message_id()) ## API V1
                            else :
                                err(update.chat_id , update.message_id)
                        else :
                            err(update.chat_id , update.message_id)
                    except :
                        err(update.chat_id , update.message_id)
                elif text_mess[1]+text_mess[2]+text_mess[3]+text_mess[4]+text_mess[5] in logo_list  :
                    string = text_mess
                    new_string = string[:0] + string[6:]
                    # img = Image.new('RGB', (100, 100), color='black')
                    # draw = ImageDraw.Draw(img)
                    # text = new_string
                    # reshaped_text = arabic_reshaper.reshape(text)
                    # display_text = get_display(reshaped_text)
                    # text_size = draw.textsize(display_text)
                    # x = (img.width - text_size[0]) / 2
                    # y = (img.height - text_size[1]) / 2
                    # draw.text((x, y), display_text, fill='red')
                    # img.save(r'logo.png')
                    num = random.randint(1, 138)
                    req = requests.get(f'https://haji-api.ir/ephoto360/?type=text&id={num}&text={new_string}')
                    if req.status_code == 200 :
                        res= req.content
                        with open('logo.png','wb')as f:
                            f.write(res)
                        bot.send_image(update.chat_id(), 'logo.png' , f'لوگوی شما با متن {new_string} ساخته شد !' ,update.message_id())
                    else :
                        err(update.chat_id , update.message_id)
                else :
                    pass
            else :
                pass
        else :
            pass
    except :
        # print(update.data)
        pass

# print(bot.get_chat_messages('g0CksyM0574514a7c27bb5b87b666e81',True))

# {
#   'chat_updates': 
#       [
#           {
#               'object_guid': 'g0ClgeQ00793223915a5f5c4cf217e88',
#               'action': 'Edit',
#               'chat': 
#                   {
#                       'time_string': '169019494700000651154405238887',
#                       'last_message': 
#                           {
#                               'message_id': '651154405238887', 
#                               'type': 'Text', 
#                               'text': 'ت بدبختری😂', 
#                               'author_object_guid': 'u0ChtcS08c2fe8d75e6888203bb9c85c', 
#                               'is_mine': False, 
#                               'author_title': '\u200c', 
#                               'author_type': 'User'
#                           }, 
#                       'last_seen_peer_mid': '651153404959887', 
#                       'time': 1690194947, 
#                       'last_message_id': '651154405238887'
#                   }, 
#               'updated_parameters': 
#                   [
#                       'time_string', 'last_message', 'last_message_id', 'last_seen_peer_mid', 'time'
#                   ], 
#               'timestamp': '1690194947', 
#               'type': 'Group'
#         }
#      ],
#  'message_updates': [{'message_id': '651154405238887', 'action': 'New', 'message': {'message_id': '651154405238887', 'text': 'ت بدبختری😂', 'reply_to_message_id': '651153404959887', 'time': '1690194947', 'is_edited': False, 'type': 'Text', 'author_type': 'User', 'author_object_guid': 'u0ChtcS08c2fe8d75e6888203bb9c85c'}, 'updated_parameters': [], 'timestamp': '1690194947', 'prev_message_id': '651153404959887', 'object_guid': 'g0ClgeQ00793223915a5f5c4cf217e88', 'type': 'Group', 'state': '1690194887'}], 'show_notifications': [], 'remove_notifications': [], 'edit_notifications': [], 'user_guid': 'u0EjTH10e93dfc0b48149016f6ab0ac4'}