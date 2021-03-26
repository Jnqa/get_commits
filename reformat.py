import json
import sys
report = ""
with open('test.json', 'r', encoding='utf-8') as t:
    all_commits = json.load(t)
for i in all_commits:
    # report.append({'name':i['commit']['author']['name'],'message':i['commit']['message']})
    report=f"{report}{i['commit']['author']['name']}:{i['commit']['message']}\n"
    # print(f"{i['commit']['author']['name']}: {i['commit']['message']}")
print(report)