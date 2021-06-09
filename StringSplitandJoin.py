def split_and_join(line):
    # write your code here
    spl=line.split(" ")
    jn="-".join(spl)
    return jn

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)