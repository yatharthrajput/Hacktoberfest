def search(pat, txt): 
    M = len(pat) 
    N = len(txt) 
  
    # A loop to slide pat[] one by one */ 
    for i in range(N - M + 1): 
        j = 0
          
        # For current index i, check  
        # for pattern match */ 
        while(j < M): 
            if (txt[i + j] != pat[j]): 
                break
            j += 1
  
        if (j == M):  
            print("Pattern Found at Index ", i) 
        
# Driver Code 
if _name_ == '_main_': 
    txt = str(input(""))
    pat = str(input(""))
    search(pat, txt)
