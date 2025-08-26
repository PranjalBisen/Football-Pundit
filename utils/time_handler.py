from datetime import datetime, timezone

def get_current_utc_time():
    """Get current UTC time in YYYY-MM-DD HH:MM:SS format"""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

def format_time(time_str):
    """Format time string to desired format"""
    try:
        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%Y-%m-%d %H:%M:%S")
    except:
        return get_current_utc_time()