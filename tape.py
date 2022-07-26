'''tape'''

def main():
    '''dddddd'''
    long_tape = int(input())
    count = []
    if long_tape < 1:
        print('No Tape Measure')
    while True:
        stop = input()
        if stop == 'No more!':
            break
        if stop.isnumeric and int(stop) <= long_tape:
            count.append(int(stop))
    count = sum(count)
    if count == 0:
        print('Not Found Number')
    else:
        print('Sum of Found Number = %d'%(count))

main()
