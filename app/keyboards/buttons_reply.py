from aiogram.types import KeyboardButton

start_buttons = [
    [KeyboardButton(text="Help"), KeyboardButton(text="Begin")]
]

begin_buttons = [
    [KeyboardButton(text="Choose activity"), KeyboardButton(text="Statistics")]
]

activity_buttons = [
    [KeyboardButton(text="Rest"), KeyboardButton(text="Health")],
    [KeyboardButton(text="Routine"), KeyboardButton(text="Study")],
    [KeyboardButton(text="Job"), KeyboardButton(text="Road to")],
    [KeyboardButton(text="Back")]
]

rest_buttons = [
    [KeyboardButton(text="watching"), KeyboardButton(text="read")],
    [KeyboardButton(text="game"), KeyboardButton(text="sleep")],
    [KeyboardButton(text="food"), KeyboardButton(text="party")],
    [KeyboardButton(text="hobby"), KeyboardButton(text="short break")],
    [KeyboardButton(text="Back")]
]

health_buttons = [
    [KeyboardButton(text="meditation"), KeyboardButton(text="sports exercises")],
    [KeyboardButton(text="routine"), KeyboardButton(text="health care")],
    [KeyboardButton(text="Back")]
]

health_sports_buttons = [
    [KeyboardButton(text="yoga"), KeyboardButton(text="fitness")],
    [KeyboardButton(text="warm-up"), KeyboardButton(text="outdoor")],
    [KeyboardButton(text="Back")]
]

health_routine_buttons = [
    [KeyboardButton(text="morning"), KeyboardButton(text="evening")],
    [KeyboardButton(text="Back")]
]

health_care_buttons = [
    [KeyboardButton(text="doctor"), KeyboardButton(text="analyses")],
    [KeyboardButton(text="Back")]
]

routine_buttons = [
    [KeyboardButton(text="cooking"), KeyboardButton(text="cleaning")],
    [KeyboardButton(text="repairing"), KeyboardButton(text="shopping")],
    [KeyboardButton(text="Back")]
]

study_buttons = [
    [KeyboardButton(text="reading"), KeyboardButton(text="videos")],
    [KeyboardButton(text="learning"), KeyboardButton(text="lectures")],
    [KeyboardButton(text="Back")]
]

job_buttons = [
    [KeyboardButton(text="at work"), KeyboardButton(text="at home")],
    [KeyboardButton(text="Back")]
]

road_buttons = [
    [KeyboardButton(text="to work"), KeyboardButton(text="to home")],
    [KeyboardButton(text="to study"), KeyboardButton(text="to meeting")],
    [KeyboardButton(text="to party / hobby / fun")],
    [KeyboardButton(text="Back")]
]