import csv
import pandas as pd

def handle(prev_line):
    each_list = []
    each_list.append(prev_line[2])
    if(prev_line[3] not in region):
        each_list.append(prev_line[3])
    else:
        each_list.append(region[prev_line[3]])
    each_list.append(prev_line[5])
    each_list.append(prev_line[7])
    try:
        death_rate = float(prev_line[7]) / float(prev_line[5])
        each_list.append("{:.2f}".format(100 * death_rate))
    except:
        each_list.append(0)
    found = False
    for i in range(len(countryCode)):
        if(countryCode[i][0] in prev_line[2]):
            each_list.append(countryCode[i][1])
            found = True
            countryCode.remove(countryCode[i])
            break
    if not found:
        each_list.append("NA")
    try:
        int(prev_line[4])
        each_list.append(prev_line[4])  # New Cases
    except:
        each_list.append(0)  # New Cases
    each_list.append(prev_line[6])  # Death Cases
    return each_list


countryCode = []
with open("Country and Code.csv") as code:
    temp = code.readline()
    for line in code:
        tempList = []
        line = line.replace("\n", "")
        line = line.split(",")
        tempList.append(line[0])
        tempList.append(line[1])
        countryCode.append(tempList)

region = {}
region["AFRO"] = "Africa"
region["AMRO"] = "Americas"
region["EMRO"] = "Eastern Mediterranean"
region["EURO"] = "Europe"
region["SEARO"] = "South East Asia"
region["WPRO"] = "Western Pacific"

url = "WHO-COVID-19-global-data.csv"
final = []
with open(url, "r", encoding="UTF-8") as data:
    temp = data.readline()
    prev_line = data.readline()
    prev_line = prev_line.replace("\n", "")
    prev_line = prev_line.split(",")
    for line in data:
        line = line.replace("\n", "")
        line = line.split(",")
        if(line[2] != prev_line[2]):
            final.append(handle(prev_line))
        prev_line = line


# 處理最後一行
with open(url, "r", encoding="UTF-8") as data:
    lines = data.readlines()
    last_line = lines[-1]
    last_line = last_line.replace("\n", "")
    last_line = last_line.split(",")
    final.append(handle(last_line))
    lastRecordDate = last_line[0]

# 排列各國確診數，從大到小排
final = sorted(final, key=lambda x: int(x[2]), reverse=True)

# 計算總確診人數
total_cumulative_cases = 0
for i in range(len(final)):
    total_cumulative_cases += int(final[i][2])

# 計算各國確診人數並加入各國的資料區
for i in range(len(final)):
    final[i].append("{:.2f}".format(100 * float(final[i][2]) / total_cumulative_cases))

# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    # 寫入第一列title
    writer.writerow(['Country', 'WHO_region', "Cumulative_cases", "Cumulative_deaths", "Death / Cases", "Code", "New_Cases", "Death_Cases", "allPercent"])
    # 寫入另外幾列資料
    for i in range(len(final)):
        writer.writerow(final[i])

df = pd.read_csv("output.csv")
countryDrop = ""
NewCases = 0
new_death_cases = 0
world_total_confirmed = 0
world_total_death = 0
with open("output.csv") as f:
    temp = f.readline()  # 讀掉第一行
    for lines in f:
        lines = lines.split(",")
        world_total_confirmed += int(lines[2])
        world_total_death += int(lines[3])
        NewCases += int(lines[6])
        new_death_cases += int(lines[7])
        countryDrop += lines[0] + ","  # 國家列表

countryDrop = countryDrop.split(",")
countryDrop.remove("")  # 把特例刪除
countryDrop.pop(168)
countryDrop.pop(219)