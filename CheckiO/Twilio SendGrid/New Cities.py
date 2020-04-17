"""
    Your mission is to figure out how many Mayors you need to control the entire city when some nodes are crushed.
In other words, you need to figure out how many sub-networks will be formed after some nodes are crush and not recovered.

Input: Two arguments: the network structure (as a list of connections between the nodes) and the list of crashed nodes.
Output: Int. The amount of sub-networks formed after some nodes were crushed.
"""


def subnetworks(net, crushes):
    data = net, crushes
    new_list = []
    for i in net:
        if crushes[0] in i:
            i.remove(crushes[0])
            new_list.append(i)
            if len(data[1]) > 1 and crushes[1] in i:
                i.remove(crushes[1])
                i.append("")
        elif crushes[0] not in i:
            new_list.append(i)
    for i in new_list:
        if len(i) == 1:
            for j in new_list:
                if i[0] in j and len(j) > 1:
                    i[0] = ""
    count = 0
    for i in new_list:
        if i[0]:
            count += 1
    return count


if __name__ == '__main__':
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['B']) == 2, "First"
    assert subnetworks([
        ['A', 'B'],
        ['A', 'C'],
        ['A', 'D'],
        ['D', 'F']
    ], ['A']) == 3, "Second"
    assert subnetworks([
        ['A', 'B'],
        ['B', 'C'],
        ['C', 'D']
    ], ['C', 'D']) == 1, "Third"
    print('Done! Check button is waiting for you!')
