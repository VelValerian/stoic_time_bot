from app.database import db_activ_name
from app.utils import hms_time_convert, dhms_time_convert

async def hms_convert_id_to_value(lst: list) -> dict:
    """
    Convert list(id,value) to dict(name,HH:MM:SS)
    example: (8,5) to (Activ_name:Hours:00 Minutes:00 Seconds:5)
    :param lst: list of id and time spend by the user
    :return: Dictionary of Activ_name:Hours:00 Minutes:00 Seconds:5
    """
    print(f"List in hms_convert_id_to_value(): {lst}")
    new_dict = {}
    for k, v in lst:
        key = await db_activ_name(int(k))
        value = await hms_time_convert(v)

        new_dict[key] = value
    return new_dict


async def dhms_convert_id_to_value(lst: list) -> dict:
    """
    Convert list(id,value) to dict(name,HH:MM:SS)
    example: (8,5) to (Activ_name:Hours:00 Minutes:00 Seconds:5)
    :param lst: list of id and time spend by the user
    :return: Dictionary of Activ_name:Hours:00 Minutes:00 Seconds:5
    """
    new_dict = {}
    for k, v in lst:
        key = await db_activ_name(int(k))
        value = await dhms_time_convert(v)

        new_dict[key] = value
    return new_dict


async def format_msg(new_dict: dict) -> str:
    new_str = str(new_dict)
    new_str = new_str.replace("{", "")
    new_str = new_str.replace("}", "")
    new_str = new_str.replace("'", "")
    new_str = new_str.replace(",", "\n")
    return new_str