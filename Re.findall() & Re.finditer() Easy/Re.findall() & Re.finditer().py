import re

if __name__ == "__main__":
    
    text = input()
    
    pattern = r'(?<=[^aeiouAEIOU])[aeiouAEIOU]{2,}(?=[^aeiouAEIOU])'

    matches = re.findall(pattern, text)
    if len(matches)  == 0:
        print(-1)
    else:
        for match in matches:
            print(match)
    
