

# Functions 
def make_graph(percent: float):
    '''Make progress graph from API graph'''
    done_block = '█'
    empty_block = '░'
    pc_rnd = round(percent)
    return f"{done_block * int(pc_rnd / 4)}{empty_block * int(25 - int(pc_rnd / 4))}"

def make_commit_list(data: list):
    '''Make List'''
    data_list = []
    for l in data[:7]:
        ln = len(l['name'])
        ln_text = len(l['text'])
        op = f"{l['name']}{' ' * (13 - ln)}{l['text']}{' ' * (15 - ln_text)}{make_graph(l['percent'])}   {l['percent']}%"
        data_list.append(op)
    return ' \n'.join(data_list)



hour= 3
weekday="Monday"

string =""

morning = 0  # 6 - 12
daytime = 0  # 12 - 18
evening = 0  # 18 - 24
night = 0  # 0 - 6

Monday = 0
Tuesday = 0
Wednesday = 0
Thursday = 0
Friday = 0
Saturday = 0
Sunday = 0

if 6 <= hour < 12:
    morning += 1
if 12 <= hour < 18:
    daytime += 1
if 18 <= hour < 24:
    evening += 1
if 0 <= hour < 6:
    night += 1

if weekday == "Monday":
    Monday += 1
if weekday == "Tuesday":
    Tuesday += 1
if weekday == "Wednesday":
    Wednesday += 1
if weekday == "Thursday":
    Thursday += 1
if weekday == "Friday":
    Friday += 1
if weekday == "Saturday":
    Saturday += 1
if weekday == "Sunday":
    Sunday += 1

sumAll = morning + daytime + evening + night
sum_week = Sunday + Monday + Tuesday + Friday + Saturday + Wednesday + Thursday

title = 'I am an Early' if morning + daytime >= evening + night else 'I am a Night'
one_day = [
    {"name": "🌞 " + 'Morning', "text": str(morning) + " commits",
        "percent": round((morning / sumAll) * 100, 2)},
    {"name": "🌆 " + 'Daytime', "text": str(daytime) + " commits",
        "percent": round((daytime / sumAll) * 100, 2)},
    {"name": "🌃 " + 'Evening', "text": str(evening) + " commits",
        "percent": round((evening / sumAll) * 100, 2)},
    {"name": "🌙 " + 'Night', "text": str(night) + " commits",
        "percent": round((night / sumAll) * 100, 2)},
]

dayOfWeek = [
        {"name": 'Monday', "text": str(Monday) + " commits", "percent": round((Monday / sum_week) * 100, 2)},
        {"name": 'Tuesday', "text": str(Tuesday) + " commits",
         "percent": round((Tuesday / sum_week) * 100, 2)},
        {"name": 'Wednesday', "text": str(Wednesday) + " commits",
         "percent": round((Wednesday / sum_week) * 100, 2)},
        {"name": 'Thursday', "text": str(Thursday) + " commits",
         "percent": round((Thursday / sum_week) * 100, 2)},
        {"name": 'Friday', "text": str(Friday) + " commits", "percent": round((Friday / sum_week) * 100, 2)},
        {"name": 'Saturday', "text": str(Saturday) + " commits",
         "percent": round((Saturday / sum_week) * 100, 2)},
        {"name": 'Sunday', "text": str(Sunday) + " commits", "percent": round((Sunday / sum_week) * 100, 2)},
    ]

string = string + '**' + title + '** \n\n' + '```text\n' + make_commit_list(one_day) + '\n\n```\n'

title="### 📅 **I'm Most Productive on Sunday**"

string = string + '**' + title + '** \n\n' + '```text\n' + make_commit_list(dayOfWeek) + '\n\n```\n'

print(string)
print("succesfully ended")

