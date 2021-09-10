from datetime import datetime
from habit_tool import break_habit
import pandas as pd
from tabulate import tabulate

habits = [
    break_habit('Coffee', datetime(2021, 7, 20, 18, 20), cost_per_day=2, minutes_wasted=15),
    break_habit('Social Media', datetime(2021, 7, 20, 18, 20), cost_per_day=3, minutes_wasted=15),
    break_habit('Cola', datetime(2021, 7, 20, 18, 20), cost_per_day=4, minutes_wasted=15),
]

df = pd.DataFrame(habits)

print(tabulate(df, headers='keys', tablefmt='psql'))
