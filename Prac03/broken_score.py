def main():
    result = ''
    score = float(input("Enter score: "))
    result = check_score(score)
    print(result)

def check_score(score):
    if score < 0:
        return 'invalid score'
    elif score > 100:
        return 'invalid score'
    elif score >= 90:
        return 'excellent'
    elif 50 <= score:
        return 'passable'
    else:
        return 'bad'


main()
