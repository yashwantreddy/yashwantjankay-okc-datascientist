def check_ip(ip):
    listed_ip = ip.split('.')
    que=[]
    if len(listed_ip) > 4:
        return 'IP address is invalid; The IP address is too long and possibly contains unecessary periods.'
    else:
        for seq in listed_ip:
            if int(seq) < 0:
                return 'IP address is invalid; It has a negative segment.'
            if 0 <= int(seq) <= 255:
                que.append(seq)
            else:
                return 'IP address is invalid; One of the segements is larger than 255.'
    printer = []
    if len(que) == 4:
        printer.append('The IP address is valid, printing the segments: ')
        for q in que:
            printer.append('Length of segment is {} and numbers are {}'.format(len(q),q))
        return printer