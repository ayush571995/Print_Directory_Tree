import sys,os
def print_dir(path):
    for root,dirs,file in os.walk(path):
        for file_ in file:
            temp=os.path.join(root,file_)
            print(temp)
            print_dir(temp)
if __name__=='__main__':
    print_dir(path)
