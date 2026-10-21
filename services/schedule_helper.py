from datetime import datetime, timedelta
from typing import Tuple

CLASS_DAYS = [1, 3, 5]  # Tuesday=1, Thursday=3, Saturday=5
CLASS_START_HOUR = 20    # 8:00 PM (20:00)
CLASS_END_HOUR = 21      # 9:00 PM (21:00)
CLASS_JOIN_URL = "https://operation.fastinfoclass.in/zoomMaster/classLobby_Dev.php"
CLASS_NAME = "English Fluency Live Class"

def get_next_class_info(now: datetime = None) -> Tuple[str, str, bool]:
    """Calculate the next class datetime string, relative label, and whether class is live right now.
    
    Returns:
        (class_label, date_str, is_live_now)
    """
    if now is None:
        now = datetime.now()

    # Check if a class is happening right now today
    today_weekday = now.weekday()
    if today_weekday in CLASS_DAYS:
        class_start_today = now.replace(hour=CLASS_START_HOUR, minute=0, second=0, microsecond=0)
        class_end_today = now.replace(hour=CLASS_END_HOUR, minute=0, second=0, microsecond=0)
        if class_start_today <= now <= class_end_today:
            return ("LIVE NOW (8:00 PM - 9:00 PM)", "Today", True)
        elif now < class_start_today:
            return ("Today, 8:00 PM - 9:00 PM", now.strftime("%A, %d %b"), False)

    # Otherwise find the next upcoming class date
    days_ahead = 1
    while True:
        target_date = now + timedelta(days=days_ahead)
        if target_date.weekday() in CLASS_DAYS:
            target_class_time = target_date.replace(hour=CLASS_START_HOUR, minute=0, second=0, microsecond=0)
            day_name = "Tomorrow" if days_ahead == 1 else target_date.strftime("%A, %d %b")
            return (f"{day_name}, 8:00 PM - 9:00 PM", target_date.strftime("%d %b %Y"), False)
        days_ahead += 1
