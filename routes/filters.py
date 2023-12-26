from datetime import datetime

def time_ago_filter(created_at):
  now = datetime.utcnow()
  delta = now - created_at

  print("tme is:", now)

  if delta.days > 0:
    return f"{delta.days} {'day' if delta.days == 1 else 'days'} ago"
  elif delta.seconds >= 3600:
    hours = delta.seconds // 3600
    return f"{hours} {'hour' if hours == 1 else 'hours'} ago"
  elif delta.seconds >=60:
    minutes = delta.seconds // 60
    return f"{minutes} {'min' if minutes == 1 else 'mins'} ago"
  else:
    return f"{delta.seconds} {'sec' if delta.seconds == 1 else 'secs'} ago"

