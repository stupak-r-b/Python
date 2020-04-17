"""
Input: Four arguments: network structure (as a list of connections between the nodes),
       users of each node (as dict where keys are the node-names and values are the amounts of users),
       name of the node that sends email, and the list of crashed nodes.

Output: Int. The amount of users that won't receive an email.
"""


def disconnected_users(net, users, source, crushes):
    data = net, users, source, crushes
    new_list = []
    count = 0
    for i in data:
        if type(i) == list and len(i) > 2:
            for j in i:
                if j[0] == source or j[1] == source:
                    count += 1

    if count == 1:
        for i in data:
            if type(i) == list and len(i) > 1:
                if not new_list:
                    new_list.append([source])
                    for j in i:
                        if j[0] not in new_list[0]:
                            new_list[0].append(j[0])
                        else:
                            new_list[0].append(j[1])
        SUM = 0
        for i in new_list[0]:
            if i != crushes[0]:
                SUM += users[i]
            else:
                break
        return sum(users.values()) - SUM

    if count == 2:
        for i in data:
            if type(i) == list and len(i) > 1:
                for j in i:
                    if not crushes[0] in j:
                        if j[0] not in new_list:
                            new_list.append(j[0])
                        if j[1] not in new_list:
                            new_list.append(j[1])
        SUM = 0
        for i in new_list:
            SUM += users[i]
        return sum(users.values()) - SUM

    if count == len(net):
        for i in data:
            if type(i) == list and len(i) > 1:
                if not new_list:
                    new_list.append([source])
                    for j in i:
                        if j[0] not in new_list[0]:
                            new_list[0].append(j[0])
                        else:
                            new_list[0].append(j[1])
        for i in crushes:
            new_list[0].remove(i)
        SUM = 0
        for i in new_list[0]:
            if i != crushes[0]:
                SUM += users[i]
            else:
                break
        return sum(users.values()) - SUM


if __name__ == '__main__':

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 20,
        'C': 30,
        'D': 40
    },
        'A', ['C']) == 70, "First"

    assert disconnected_users([
        ['A', 'B'],
        ['B', 'D'],
        ['A', 'C'],
        ['C', 'D']
    ], {
        'A': 10,
        'B': 0,
        'C': 0,
        'D': 40
    },
        'A', ['B']) == 0, "Second"

    assert disconnected_users([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['A', 'E'],
        ['A', 'F']
    ], {
        'A': 10,
        'B': 10,
        'C': 10,
        'D': 10,
        'E': 10,
        'F': 10
    },
        'C', ['A']) == 50, "Third"

    print('Done. Try to check now. There are a lot of other tests')
