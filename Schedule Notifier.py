import datetime
import time
from plyer import notification
import os
from playsound import playsound
print("ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ꜱᴄʜᴇᴅᴜʟᴇʀ ɴᴏᴛɪꜰɪᴇʀ")
print("ʜᴇʀᴇ ʏᴏᴜ ᴄᴀɴ ᴀᴅᴅ ʏᴏᴜʀ ꜱᴄʜᴇᴅᴜʟᴇꜱ ᴛᴏ ʀᴇᴍɪɴᴅ ʏᴏᴜ")
print("ᴛʏᴘᴇ ᴇɴᴛᴇʀ ᴛᴏ ꜱᴛᴀʀᴛ")
user = str(input())
a = user.lower()
alarmH2 = 000
alarmM2 = 000
alarmH3 = 000
alarmM3 = 000
alarmH4 = 000
alarmM4 = 000
enter = "enter"
pm = "pm"
y = "y"
n = "n"
if(a == enter):
    print("[ꜱᴛᴀʀᴛɪɴɢ]............................ ")
    task1 = input("ᴇɴᴛᴇʀ ʏᴏᴜʀ ꜱᴄʜᴇᴅᴜʟᴇ 1 :")
    alarmH1 = int(input("ᴡʜᴀᴛ ʜᴏᴜʀ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
    alarmM1 = int(input("ᴡʜᴀᴛ ᴍɪɴᴜᴛᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
    alarmampm = input("ᴀᴍ ᴏʀ ᴘᴍ :")
    ampm1 = alarmampm.lower()
    if(alarmH1 == 12 and ampm1 == pm):
        alarmH1 = alarmH1-12
    else:
        pass
    if(ampm1 == pm):
        alarmH1 = alarmH1+12
        pass
    add1 = input("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴᴏᴛʜᴇʀ ? ᴛʜᴇɴ ᴛʏᴘᴇ (ʏ/ɴ) :")
    t1 = add1.lower()
    if(t1 == n):
        print("ʏᴏᴜ ᴀᴅᴅᴇᴅ ᴏɴᴇ ᴛᴀꜱᴋ")
    elif(t1 == y):
        task2 = input("ᴇɴᴛᴇʀ ʏᴏᴜʀ ꜱᴄʜᴇᴅᴜʟᴇ 2 :")
        alarmH2 = int(input("ᴡʜᴀᴛ ʜᴏᴜʀ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
        alarmM2 = int(input("ᴡʜᴀᴛ ᴍɪɴᴜᴛᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
        alarmampm = input("ᴀᴍ ᴏʀ ᴘᴍ :")
        ampm2 = alarmampm.lower()
        if(alarmH1 == 12 and ampm2 == pm):
            alarmH1 = alarmH1-12
        else:
            pass
        if(ampm2 == pm):
            alarmH2 = alarmH2+12
            pass
        add2 = input("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴᴏᴛʜᴇʀ ? ᴛʜᴇɴ ᴛʏᴘᴇ (ʏ/ɴ) :")
        t2 = add2.lower()
        if(t2 == n):
            print("ʏᴏᴜ ᴀᴅᴅᴇᴅ ᴛᴡᴏ ᴛᴀꜱᴋꜱ")
        elif(t2 == y):
            task3 = input("ᴇɴᴛᴇʀ ʏᴏᴜʀ ꜱᴄʜᴇᴅᴜʟᴇ 3 :")
            alarmH3 = int(input("ᴡʜᴀᴛ ʜᴏᴜʀ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
            alarmM3 = int(input("ᴡʜᴀᴛ ᴍɪɴᴜᴛᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
            alarmampm = input("ᴀᴍ ᴏʀ ᴘᴍ :")
            ampm3 = alarmampm.lower()
            if(alarmH1 == 12 and ampm3 == pm):
                alarmH1 = alarmH1-12
            else:
                pass
            if(ampm3 == pm):
                alarmH3 = alarmH3+12
                pass
            add3 = input("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴᴏᴛʜᴇʀ ? ᴛʜᴇɴ ᴛʏᴘᴇ (ʏ/ɴ) :")
            t3 = add3.lower()
            if(t3 == n):
                print("ʏᴏᴜ ᴀᴅᴅᴇᴅ ᴛʜʀᴇᴇ ᴛᴀꜱᴋꜱ")
            elif(t3 == y):
                task4 = input("ᴇɴᴛᴇʀ ʏᴏᴜʀ ꜱᴄʜᴇᴅᴜʟᴇ 4 :")
                alarmH4 = int(input("ᴡʜᴀᴛ ʜᴏᴜʀ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
                alarmM4 = int(input("ᴡʜᴀᴛ ᴍɪɴᴜᴛᴇ ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ɴᴏᴛɪꜰʏ ʏᴏᴜ? "))
                alarmampm = input("ᴀᴍ ᴏʀ ᴘᴍ :")
                ampm4 = alarmampm.lower()
                if(alarmH1 == 12 and ampm4 == pm):
                    alarmH1 = alarmH1-12
                else:
                    pass
                if(ampm4 == pm):
                    alarmH4 = alarmH4+12
                    pass
                add4 = input("ᴅᴏ ʏᴏᴜ ᴡᴀɴᴛ ᴛᴏ ᴀᴅᴅ ᴀɴᴏᴛʜᴇʀ ? ᴛʜᴇɴ ᴛʏᴘᴇ (ʏ/ɴ) :")
                t4 = add4.lower()
                if(t4 == n):
                    print("ʏᴏᴜ ᴀᴅᴅᴇᴅ ꜰᴏᴜʀ ᴛᴀꜱᴋꜱ")
                elif(t4 == y):
                    print("ʏᴏᴜ ᴀᴅᴅᴇᴅ ꜰᴏᴜʀ ᴛᴀꜱᴋꜱ")
                    print("ᴍᴀx ʟɪᴍɪᴛ ɪꜱ ʀᴇᴀᴄʜᴇᴅ")
                    print("ᴋɪɴᴅʟʏ ᴄʜᴇᴄᴋᴏᴜᴛ ᴍʏ ɢɪᴛʜᴜʙ ᴘᴀɢᴇ ꜰᴏʀ ᴜᴘᴅᴀᴛᴇᴅ ᴠᴇʀꜱɪᴏɴ ᴀɴᴅ ᴀᴅᴅɪᴛɪᴏɴᴀʟ ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ")
                    print("ɢɪᴛʜᴜʙ ᴘʀᴏꜰɪʟᴇ : https://github.com/shansaju ")
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass
    while(1 == 1):
        if(alarmH1 == datetime.datetime.now().hour and alarmM1 == datetime.datetime.now().minute):
            print("ᴛɪᴍᴇ ᴛᴏ ᴅᴏ")
            notification.notify(title = "ꜱᴄʜᴇᴅᴜʟᴇ ɴᴏᴛɪꜰɪᴇʀ", message = task1, timeout = 25 ) 
            playsound("alarm1.wav")
            time.sleep(25)
        elif(alarmH2 == datetime.datetime.now().hour and alarmM2 == datetime.datetime.now().minute):
            print("ᴛɪᴍᴇ ᴛᴏ ᴅᴏ")
            notification.notify(title = "ꜱᴄʜᴇᴅᴜʟᴇ ɴᴏᴛɪꜰɪᴇʀ", message = task2, timeout = 25 ) 
            playsound("alarm2.wav")
            time.sleep(25)
        elif(alarmH3 == datetime.datetime.now().hour and alarmM3 == datetime.datetime.now().minute):
            print("ᴛɪᴍᴇ ᴛᴏ ᴅᴏ")
            notification.notify(title = "ꜱᴄʜᴇᴅᴜʟᴇ ɴᴏᴛɪꜰɪᴇʀ", message = task3, timeout = 25 ) 
            playsound("alarm3.wav")
            time.sleep(25)
        elif(alarmH4 == datetime.datetime.now().hour and alarmM4 == datetime.datetime.now().minute):
            print("ᴛɪᴍᴇ ᴛᴏ ᴅᴏ")
            notification.notify(title = "ꜱᴄʜᴇᴅᴜʟᴇ ɴᴏᴛɪꜰɪᴇʀ", message = task4, timeout = 25 ) 
            playsound("alarm4.wav")
            time.sleep(25)
        else:
            pass  
else:
    print("ɪᴛ'ꜱ ɴᴏᴛ ᴇɴᴛᴇʀ")
    print("ᴛʜᴀɴᴋ ʏᴏᴜ ꜰᴏʀ ᴜꜱɪɴɢ")
    print("[ᴄʟᴏꜱɪɴɢ]........................................")
