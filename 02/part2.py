def structured_policy(policy, pwd):
    frequencies, letter = policy.split(' ')
    indexes = [int(i) for i in frequencies.split('-')]
    return {'indexes': indexes,
            'letter': letter,
            'pwd': pwd
            }
def letter_at_exactly_one_position(policy):
    indexes, expected_letter, pwd = policy.values()
    matches = 0
    for index in indexes:
        try:
            letter = pwd[index-1]
            if letter == expected_letter:
                matches = matches + 1
        except IndexError:
            print('Index out of range')
    return matches == 1

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    policies = []
    for line in lines:
        policy, pwd = line.split(': ')
        policies.append(structured_policy(policy, pwd))
    valid_pwds = 0
    for policy in policies:
        if letter_at_exactly_one_position(policy):
            valid_pwds = valid_pwds + 1
    print("There are {} valid passwords".format(valid_pwds))
