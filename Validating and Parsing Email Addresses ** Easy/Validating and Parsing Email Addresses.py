from email.utils import parseaddr
import re


def validate_email_address(test_email):
    name, addr = parseaddr(test_email)

    if addr and re.match(r'^[a-zA-Z][a-zA-Z0-9._-]*@[a-zA-Z]+\.[a-zA-Z]{1,3}$', addr):
        return True
    return False


if __name__ == "__main__":
    res = []
    n = int(input())
    for _ in range(n):
        email = input().strip()
        result = validate_email_address(email)
        if result:
            res.append(email)
        # else:
            # res.append("")
            

    for r in res:
        print(r)
