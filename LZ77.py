
## define helper functions here



def error_(len_seq,win_size):
    if len_seq == 0:
        print("usage: The sequence must be of length larger than zero")
        return 1
    elif win_size <= 0:
        print("usage: Window size must be larger than zero")
        return 1
    return 0


### returns the starting index of past_symbol and the past symbols
def extract_past_symbols(i,win_len,seq):
    if i < win_len:
        return (0,seq[0:i])
    else:
        return (i - win_len, seq[(i - win_len):i])


def no_match(past_symbols,curr_symbol):
    return (past_symbols == '') or (curr_symbol not in past_symbols)


def all_past_symb_found(past_symbols,seq,i):
    past_symbol_len = len(past_symbols)
    next_index = i + past_symbol_len - 1
    return (next_index < len(seq)) and (past_symbols == seq[i:next_index + 1])


## returns updated index and also the appropriate tuple 
def compute_all_found(start_index,i,past_sym,seq):
    past_seq_len,initial_index = len(past_sym), i
    match_len,i = past_seq_len, i + past_seq_len

    while all_past_symb_found(past_sym,seq,i):
        match_len,i =  match_len + past_seq_len, i + past_seq_len
    
    seq_len = len(seq)
    if (i < seq_len) and (seq[i] == past_sym[0]):
        if (i + past_seq_len) > seq_len: # end out of bounds
            partial_match_str = seq[i:seq_len]
        else:
            partial_match_str = seq[i:i + past_seq_len]
        
        while partial_match_str != past_sym[:len(partial_match_str)]: ## will atleast match with length 1
            partial_match_str = partial_match_str[:-1]

        match_len, i = match_len + len(partial_match_str), i + len(partial_match_str)
        return i,('1',str(initial_index - start_index),str(match_len))
        
    else: ## finished matching
        return i,('1',str(initial_index - start_index),str(match_len))

### returns the length of the match
def find_match_len(start,past_sym,seq,i,indice):
    j = 1
    ps_l,s_l = len(past_sym),len(seq)
    while ((indice - start) + j < ps_l) and (i + j < s_l) and (past_sym[(indice - start): (indice - start) + j + 1] == seq[i: i + j + 1]):
        j += 1
    return j


    


## returns updated index and also the appropriate tuple 
def compute_partial_match(start,i,past_sym,seq):
    store_indice = []
    store_length = []

    running_index = start
    while running_index < start + len(past_sym):
        if past_sym[running_index - start] == seq[i]:
            store_indice.append(running_index)
        running_index += 1

    assert(len(store_indice)) ### there must be some indice that matches

    for indice in store_indice:
        store_length.append(find_match_len(start,past_sym,seq,i,indice))

    max_len_match = max(store_length)
    start_i = store_indice[store_length.index(max_len_match)]


    return ((i + max_len_match),('1',str(i - start_i),str(max_len_match)))


def tuple_to_encoded_str(tup):
    res_str = ""
    for elem in tup:
        if len(elem) == 2:
            a,b = elem
            res_str = res_str + a + b
        else:
            a,b,c = elem
            res_str = res_str + a + b + c
    return res_str







class MyLZ77(object):
    '''
    encodes a binary string using the LZ77 algorithm
    '''
    def encode(self,bin_seq,win_size):
        len_seq = len(bin_seq)
        res_encoded_tup = []

        if error_(len_seq,win_size):
            exit(1)
        
        index = 0 
        while index < len_seq:
            ### store past symbols
            start,past_seq = extract_past_symbols(index,win_size,bin_seq)
            res = None # variable to hold the result


            ### check cases
            if no_match(past_seq,bin_seq[index]):
                res_encoded_tup.append(('0',bin_seq[index])) ### No past symbols, so matches (0,bin) case
                index += 1
            elif all_past_symb_found(past_seq,bin_seq,index):
                index,res = compute_all_found(start,index,past_seq,bin_seq) 
                res_encoded_tup.append(res)
            else:  ### find the largest matching pattern
                index,res = compute_partial_match(start,index,past_seq,bin_seq)
                res_encoded_tup.append(res)

        ### finally return the concatenation of the strings inside the tuples
        return tuple_to_encoded_str(res_encoded_tup)


    '''
    decodes a binary string that is encoded using LZ77 algorithm
    '''
    def decode(self,encoded_seq,win_size):
        pass



def main():
    sol = MyLZ77()
    print('\n')
    print(sol.encode('1001001000110101',4))
    print('\n')

main()

