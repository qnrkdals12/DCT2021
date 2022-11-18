from datetime import datetime, timedelta
# 시작일,종료일 설정
start = "2020-01-01"
last = "2020-12-31"
# 시작일, 종료일 datetime 으로 변환
start_date = datetime.strptime(start, "%Y-%m-%d")
last_date = datetime.strptime(last, "%Y-%m-%d")
# 종료일 까지 반복
while start_date <= last_date:
    dates = start_date.strftime("%Y-%m-%d")
    print(dates)
    start_date += timedelta(days=1)
