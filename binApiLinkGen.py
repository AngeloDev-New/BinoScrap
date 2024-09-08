from datetime import datetime, timezone , timedelta

# Exibir a hora no formato desejado
def getLinkApi(nivel):
    time,date = getTimeDate(nivel)
    return 'https://api.binomo.com/candles/v1/Z-CRY%2FIDX/DATETTIME/5?locale=br'.replace("TIME",time).replace("DATE",date)
    
def getTimeDate(nivel):
    datetime_utc = datetime.now(timezone.utc)
    datetimeR = datetime_utc-timedelta(hours=nivel-1)
    date , time = str(datetimeR).split(" ")
    time = time.split(":")[0]
    if len(time)==1:
        time = f"0{time}"
    time = f"{time}:00:00"

    return (time,date)

if __name__ in "__main__":
    print(*getTimeDate(1))
    print(*getTimeDate(2))
    print(*getTimeDate(3))
    print(*getTimeDate(4))
    print(*getTimeDate(5))