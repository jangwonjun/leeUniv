import schedule
import time
from schedule_email import Send_Email
from leeUniv import extract_data
from env import EMAIL

def send_competition_rate():
    email_content = extract_data()

    Send_Email(EMAIL.LEE_Univ, str(email_content), "한양대학교 타겟학과 실시간 경쟁률 알림")

schedule.every().day.at("11:00").do(send_competition_rate)
schedule.every().day.at("16:00").do(send_competition_rate)
schedule.every().day.at("18:00").do(send_competition_rate)

while True:
    schedule.run_pending()
    time.sleep(60) 
