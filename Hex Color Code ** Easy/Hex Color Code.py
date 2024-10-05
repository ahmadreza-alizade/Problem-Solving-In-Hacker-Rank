import re
css = [input().strip() for _ in range(int(input()))]
colors = [re.findall(r'#([\dA-F]{6}|[\dA-F]{3})(?=.*;)',
            line,re.IGNORECASE) for line in css]
[print(f"#{hx}") for group in colors for hx in group]
