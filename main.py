import utilities.logic as logic
from decouple import config

start_capital = int(config('START_CAPITAL'))
attempts = int(config('ATTEMPS'))
number1 = int(config('NUMBER_START'))
number2 = int(config('NUMBER_END'))

logic.play_game(start_capital, attempts, number1, number2)
