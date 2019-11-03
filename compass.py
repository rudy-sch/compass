import sys
import time
import requests
from urllib.request import urlopen

url = ['https://sepatucompass.com/collections/all/products/gazelle-hi-black?variant=30324990443629',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black?variant=30324990476397',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black?variant=30324990509165',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black?variant=30324990541933',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black?variant=30324990574701',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black?variant=30324990607469',
'https://sepatucompass.com/collections/all/products/gazelle-low-black?variant=30324985987181',
'https://sepatucompass.com/collections/all/products/gazelle-low-black?variant=30324986019949',
'https://sepatucompass.com/collections/all/products/gazelle-low-black?variant=30324986052717',
'https://sepatucompass.com/collections/all/products/gazelle-low-black?variant=30324986085485',
'https://sepatucompass.com/collections/all/products/gazelle-low-black?variant=30324986118253',
'https://sepatucompass.com/collections/all/products/gazelle-low-black?variant=30324986151021',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black-black?variant=30324989952109',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black-black?variant=30324989984877',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black-black?variant=30324990017645',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black-black?variant=30324990148717',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black-black?variant=30324990050413',
'https://sepatucompass.com/collections/all/products/gazelle-hi-black-black?variant=30324990083181',
'https://sepatucompass.com/collections/all/products/gazelle-hi-cappuccino?variant=30324990738541',
'https://sepatucompass.com/collections/all/products/gazelle-hi-cappuccino?variant=30324990771309',
'https://sepatucompass.com/collections/all/products/gazelle-hi-cappuccino?variant=30324990804077',
'https://sepatucompass.com/collections/all/products/gazelle-hi-cappuccino?variant=30324990836845',
'https://sepatucompass.com/collections/all/products/gazelle-hi-cappuccino?variant=30324990869613',
'https://sepatucompass.com/collections/all/products/gazelle-hi-cappuccino?variant=30324990902381',
'https://sepatucompass.com/collections/all/products/gazelle-low-pink?variant=30411899928685',
'https://sepatucompass.com/collections/all/products/gazelle-low-pink?variant=30324992606317',
'https://sepatucompass.com/collections/all/products/gazelle-low-pink?variant=30324992639085',
'https://sepatucompass.com/collections/all/products/gazelle-low-pink?variant=30324992704621',
'https://sepatucompass.com/collections/all/products/gazelle-low-grey?variant=30324989001837',
'https://sepatucompass.com/collections/all/products/gazelle-low-grey?variant=30324989034605',
'https://sepatucompass.com/collections/all/products/gazelle-low-grey?variant=30324989067373',
'https://sepatucompass.com/collections/all/products/gazelle-low-grey?variant=30324989100141',
'https://sepatucompass.com/collections/all/products/gazelle-low-grey?variant=30324989132909',
'https://sepatucompass.com/collections/all/products/gazelle-low-grey?variant=30324989165677',
'https://sepatucompass.com/collections/all/products/rd-low?variant=30324992802925',
'https://sepatucompass.com/collections/all/products/rd-low?variant=30324992835693',
'https://sepatucompass.com/collections/all/products/rd-low?variant=30324992868461',
'https://sepatucompass.com/collections/all/products/rd-low?variant=30324992901229',
'https://sepatucompass.com/collections/all/products/rd-low?variant=30324992933997',
'https://sepatucompass.com/collections/all/products/rd-low?variant=30324992966765',
'https://sepatucompass.com/collections/all/products/rd-hi?variant=30324992999533',
'https://sepatucompass.com/collections/all/products/rd-hi?variant=30324993032301',
'https://sepatucompass.com/collections/all/products/rd-hi?variant=30324993065069',
'https://sepatucompass.com/collections/all/products/rd-hi?variant=30324993097837',
'https://sepatucompass.com/collections/all/products/rd-hi?variant=30324993130605',
'https://sepatucompass.com/collections/all/products/rd-hi?variant=30324993163373',
'https://sepatucompass.com/collections/all/products/gazelle-low-white?variant=30324987887725',
'https://sepatucompass.com/collections/all/products/gazelle-low-white?variant=30324987920493',
'https://sepatucompass.com/collections/all/products/gazelle-low-white?variant=30324987953261',
'https://sepatucompass.com/collections/all/products/gazelle-low-white?variant=30324987986029',
'https://sepatucompass.com/collections/all/products/gazelle-low-white?variant=30324988018797',
'https://sepatucompass.com/collections/all/products/gazelle-low-white?variant=30324988051565',
'https://sepatucompass.com/collections/all/products/gazelle-low-red?variant=30324989329517',
'https://sepatucompass.com/collections/all/products/gazelle-low-red?variant=30324989362285',
'https://sepatucompass.com/collections/all/products/gazelle-low-red?variant=30324989395053',
'https://sepatucompass.com/collections/all/products/gazelle-low-red?variant=30324989427821',
'https://sepatucompass.com/collections/all/products/gazelle-low-red?variant=30324989460589',
'https://sepatucompass.com/collections/all/products/gazelle-low-red?variant=30324989493357',
'https://sepatucompass.com/collections/all/products/gazelle-low-navy?variant=30324986937453',
'https://sepatucompass.com/collections/all/products/gazelle-low-navy?variant=30324986970221',
'https://sepatucompass.com/collections/all/products/gazelle-low-navy?variant=30324987002989',
'https://sepatucompass.com/collections/all/products/gazelle-low-navy?variant=30324987035757',
'https://sepatucompass.com/collections/all/products/gazelle-low-navy?variant=30324987068525',
'https://sepatucompass.com/collections/all/products/gazelle-low-navy?variant=30324987101293',
'https://sepatucompass.com/collections/all/products/gazelle-low-cappuccino?variant=30324988510317',
'https://sepatucompass.com/collections/all/products/gazelle-low-cappuccino?variant=30324988543085',
'https://sepatucompass.com/collections/all/products/gazelle-low-cappuccino?variant=30324988575853',
'https://sepatucompass.com/collections/all/products/gazelle-low-cappuccino?variant=30324988608621',
'https://sepatucompass.com/collections/all/products/gazelle-low-cappuccino?variant=30324988641389',
'https://sepatucompass.com/collections/all/products/gazelle-low-cappuccino?variant=30324988674157',
'https://sepatucompass.com/collections/all/products/gazelle-low-black-black?variant=30324988182637',
'https://sepatucompass.com/collections/all/products/gazelle-low-black-black?variant=30324988215405',
'https://sepatucompass.com/collections/all/products/gazelle-low-black-black?variant=30324988248173',
'https://sepatucompass.com/collections/all/products/gazelle-low-black-black?variant=30324988280941',
'https://sepatucompass.com/collections/all/products/gazelle-low-black-black?variant=30324988313709',
'https://sepatucompass.com/collections/all/products/gazelle-low-black-black?variant=30324988346477',
'https://sepatucompass.com/collections/all/products/gazelle-hi-white?variant=30324987428973',
'https://sepatucompass.com/collections/all/products/gazelle-hi-white?variant=30324987461741',
'https://sepatucompass.com/collections/all/products/gazelle-hi-white?variant=30324987494509',
'https://sepatucompass.com/collections/all/products/gazelle-hi-white?variant=30324987527277',
'https://sepatucompass.com/collections/all/products/gazelle-hi-white?variant=30324987560045',
'https://sepatucompass.com/collections/all/products/gazelle-hi-white?variant=30324987592813',
'https://sepatucompass.com/collections/all/products/gazelle-hi-red?variant=30324991033453',
'https://sepatucompass.com/collections/all/products/gazelle-hi-red?variant=30324991066221',
'https://sepatucompass.com/collections/all/products/gazelle-hi-red?variant=30324991098989',
'https://sepatucompass.com/collections/all/products/gazelle-hi-red?variant=30324991131757',
'https://sepatucompass.com/collections/all/products/gazelle-hi-red?variant=30324991164525',
'https://sepatucompass.com/collections/all/products/gazelle-hi-red?variant=30324991197293',
'https://sepatucompass.com/collections/all/products/gazelle-hi-blue-sky?variant=30324991557741',
'https://sepatucompass.com/collections/all/products/gazelle-hi-blue-sky?variant=30324991623277',
'https://sepatucompass.com/collections/all/products/gazelle-hi-blue-sky?variant=30324991688813',
'https://sepatucompass.com/collections/all/products/gazelle-hi-blue-sky?variant=30324991950957',
'https://sepatucompass.com/collections/all/products/gazelle-hi-blue-sky?variant=30324991754349',
'https://sepatucompass.com/collections/all/products/gazelle-hi-blue-sky?variant=30324991852653']

def telegram_bot_sendtext(bot_message):
    
    bot_token = '911197908:AAGVnihXeEFK8reZJlUgYFCu-8DhPnEEkWU'
    bot_chatID = ['629104143', '752312439']
    for i in bot_chatID:    
        send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + i + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
    return response.json()


while True:
    for i in url:
        f = urlopen(i).read().decode('utf-8')
        if not "Sold Out" in f:
            tmp = str('READY!!!!!! ' + i)
            telegram_bot_sendtext(tmp)
        time.sleep(0.5)    


