import Character_Dictionary as CD
import datetime as dt

stage1= dt.timedelta(minutes=1)
stage2= dt.timedelta(minutes=5)
stage3= dt.timedelta(minutes=15)
stage4= dt.timedelta(days=1)
stage5= dt.timedelta(days=2)
stage6= dt.timedelta(days=3)
stage7= dt.timedelta(days=5)
stage8= dt.timedelta(days=7)
stage9= dt.timedelta(days=14)
stage10=dt.timedelta(days=21)

queue = []
now = dt.datetime.now()

def status_check():
    for nihon in CD.hiragana_dataset:
        if nihon["due_time"] == None or nihon["due_time"] > now :
            queue.append(nihon)
    print(queue)

