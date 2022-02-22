import time
import requests as req
import threading
from configdata import *



update_id=0


def start_req(post_id):

    link='https://t.me/'+CHANNEL_LINK+'/'+str(post_id)
    T_PARA=PARA
    T_PARA['link']=link

    if TEST_VALUE==True:
        tmr=5
    else:
        tmr=3600

    count=0
    sum=0
    start_time=time.time()
    val={1:'100',2:'100',3:'100',4:'100',5:'100',6:'200',7:'200',8:'200',9:'200',10:'400',11:'400',12:'400',13:'400',14:'800'}

    time_loop={1:5,4:7}
    for i in [1,4]:
        for j in range(time_loop[i]):
            count+=1
            sum+=int(val[count])

            T_PARA['quantity']=val[count]
            try:
                res=req.post(API_URL,data=T_PARA)
                print('Return Data :- \n',res.json())
            except:
                print('FAIL :- ',link,'  QTY= ',T_PARA["quantity"])

            time.sleep(i*tmr)


        time.sleep(3*tmr)
    time.sleep(9*tmr)

    for i in range(2):
        count+=1
        sum+=int(val[count])

        T_PARA['quantity']=val[count]
        try:
            res=req.post(API_URL,data=T_PARA)
            print('Return Data :- \n',res.json())
        except:
            print('FAIL :- ',link,'  QTY= ',T_PARA["quantity"])

        if i!=1:
            time.sleep(48*tmr)

    end_time = time.time()
    time_diff =end_time - start_time
    print('FINISHED :- ',link,'\t REQ COUNT = ',count,'\t QTY = ',sum,'\t TIME TAKEN = ',time_diff)

    #print(T_PARA)
    #print(link)




def get_post_update():
    global update_id
    base_link='https://api.telegram.org/bot'+BOT_API_KEY+'/getUpdates?offset=-1'
    res=req.post(base_link)
    a=res.json()
    try:
        latest_post=a['result'][-1]
        #print(latest_post['update_id'])

        if update_id==0:
            update_id=latest_post['update_id']
        elif update_id==latest_post['update_id']:
            pass
        else:
            update_id=latest_post['update_id']
            if "channel_post" in latest_post:
                req_data=latest_post['channel_post']
                user=req_data["sender_chat"]["username"]
                #print(user,':',CHANNEL_LINK)
                if user==CHANNEL_LINK:
                    post_id=req_data["message_id"]
                    th=threading.Thread(target=start_req,args=(post_id,))
                    th.start()
            else:
                pass

    except:
        pass

    #print(latest_post)

while True:

    get_post_update()
