def compress(uncompressed):
    """Compress a string to a list of output symbols."""
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {chr(i): i for i in range(dict_size)}
 
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
 
    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result
 
 
def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO
 
    # Build the dictionary.
    dict_size = 256
    dictionary = {i: chr(i) for i in range(dict_size)}
 
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
 
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
 
        w = entry
    return result.getvalue()
 
#compressed = compress('TOBEORNOTTOBEORTOBEORNOT')
import numpy as np
a = np.array([[25,66,83,75],
              [37,22,41,89],
              [15,22,55,67],
              [75,88,255,254]]).reshape(1,16)
print(a)
b = np.array2string(a)
print(b)
#Using function "compressed" as above
compressed = compress(b)
print(compressed)
decompressed = decompress(compressed)
#oneDArray = np.array(decompressed)
#twoDArray = np.reshape(oneDArray,(4,4))
print('dcom:' ,decompressed)

#print(twoDArray)

