import ast
import functools
import itertools
count = 0

def compare_mesg_pair2(mesg1, mesg2) -> bool|None:
    result = 0
    for left,right in itertools.zip_longest(mesg1,mesg2):
        if isinstance(left,int) and isinstance(right,int):
            if right < left:
                result = -1
            if left < right:
                result = 1

        elif left is None and right is not None:
            result = 1
        elif right is None and left is not None:
            result = -1

        else:
            if isinstance(left,int):
                left = [left]
            if isinstance(right,int):
                right = [right]
            result = compare_mesg_pair2(left,right)
        if result != 0:
            break
    return result

packets = [[[2]],[[6]]]
with open('input', mode='r') as f:
    messages_input = [ x.strip() for x in f.readlines()]
    for x in range(0,len(messages_input),3):
        mesg1 = messages_input[x]
        mesg2 = messages_input[x+1]
        message1 = ast.literal_eval(mesg1)
        message2 = ast.literal_eval(mesg2)
        packets.append(message1)
        packets.append(message2)
        good_order = compare_mesg_pair2(message1,message2)
        # print(f"PAIR{1+x/3} {good_order=} {mesg1,mesg2} ")
        if good_order>0:

            count +=1+x/3

print(f"PART1: {count=}")

packets2=sorted(packets,key=functools.cmp_to_key(compare_mesg_pair2), reverse=True)
decoderkey=(1+packets2.index([[2]]))*(1+packets2.index([[6]]))
print(f"PART2: {decoderkey=}")
