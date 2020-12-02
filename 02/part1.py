def structured_policy(policy, pwd):
    frequencies, letter = policy.split(' ')
    min, max = frequencies.split('-')
    return {'min': int(min),
            'max': int(max),
            'letter': letter,
            'pwd': pwd
            }
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    policies = []
    for line in lines:
        policy, pwd = line.split(': ')
        policies.append(structured_policy(policy, pwd))
    valid_pwds = 0
    for policy in policies:
        frequency = list(policy['pwd']).count(policy['letter'])
        if frequency >= policy['min'] and frequency <= policy['max']:
            valid_pwds = valid_pwds + 1
    print("There are {} valid passwords".format(valid_pwds))
