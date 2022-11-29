x = set
def prep_calculate(*some_set):
    global x
    some_set = x
    sim = {'(', ')', '/', '*', '+', '-'}
    for ch in sim:
        if some_set.intersection('('):
            index_in = str(some_set).find('(')
            new_x = ' '.join(str(x).partition(ch)[index_in + 1:])
            if new_x.find('('):
                index_second_in = new_x.find('(')
                new_x = ' '.join(new_x.partition(ch)[index_second_in:])
                if str(some_set).find(')'):
                    index_second_end = new_x.find(')')
                    new_x = ' '.join(new_x.partition(ch)[:index_second_end - 1:])
            return new_x
    if some_set == None:
        return None

