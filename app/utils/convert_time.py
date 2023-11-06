import datetime


async def hms_time_convert(spend_time):
    """
    Convert spend time to HH:MM:SS format
    :param spend_time: spend time that get from DB
    :return Hour:07 Minutes:08 Seconds:20
    """
    # Convert the time difference to a timedelta object
    time_delta = datetime.timedelta(seconds=spend_time)

    # Extract days, hours, minutes, and seconds from the timedelta
    days = time_delta.days
    seconds = time_delta.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the time delta as "DD:HH:MM:SS"
    formatted_time_delta = f"Hour:{hours:02} Minutes:{minutes:02} Seconds:{seconds:02}"
    return formatted_time_delta


async def dhms_time_convert(spend_time):
    """
    Convert spend time to DD:HH:MM:SS format
    :param spend_time: spend time that get from DB
    :return Day:227 Hour:07 Minutes:08 Seconds:20
    """
    # Convert the time difference to a timedelta object
    time_delta = datetime.timedelta(seconds=spend_time)

    # Extract days, hours, minutes, and seconds from the timedelta
    days = time_delta.days
    seconds = time_delta.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    # Format the time delta as "DD:HH:MM:SS"
    formatted_time_delta = f"Day:{days:02} Hour:{hours:02} Minutes:{minutes:02} Seconds:{seconds:02}"
    return formatted_time_delta
