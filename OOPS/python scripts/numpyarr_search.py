import numpy as np
import pickle
def input_nos():
    arr=list(map(int,input("Enter the nos. for the list separated by space:").strip().split(",")))
    arr=np.array(arr)
    with open("input_num.txt","wb") as f:
        pickle.dump(arr,f)
def search(s):
    with open("input_num.txt","rb") as f:
        arr=pickle.load(f)
        if s not in arr:
            print(-1)
        for i in range(len(arr)):
            if arr[i]==s:
                print(f"The searched element is found at index {i+1}")
if __name__=="__main__":
    input_nos()
    s=int(input("Enter the element to search:"))
    search(s)