def print_comma(txtfilename):
    import re

    f = open(txtfilename, 'r', encoding='utf-8')
    while True:
        line = f.readline()
        if len(line) <= 0:
            break
        x = line.strip()
        x1 = ''
        x2 = x
        p = x2.find(' ')
        if p >= 1:
            x1 = x2[0:p]
            x2 = x2[p:]
            
        x21org = x2+'/'
        x22 = ''
        q = x21org.find('(=')
        x21 = x21org
        if q >= 1:
            x21 = x21org[:q]+'/'
            x22 = x21org[q:-1]
        """print(x21+x22)"""
        while True:
            if re.search(r'([0-9])([0-9][0-9][0-9][^0-9])', x21) is not None:
                x21 = re.sub(r'([0-9])([0-9][0-9][0-9][^0-9])', r'\1,\2', x21)
            else:
                x21 = x21[:-1]
                break
                
        """"""
        print(x1+x21+x22)
        """print(x1+x21)"""
        
if __name__ == '__main__':
    print_comma('savings_2507.txt')
    