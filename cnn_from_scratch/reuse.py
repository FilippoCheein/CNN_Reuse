# parse operands_out file
# result: frequency of operands
from parse import run

def form(opstr):
    str = opstr.split()
    if(len(str) == 0):
        return None
    else:
        op1 = float(str[0])
        op2 = float(str[1])
        if op1 < op2:
            result = [op1, op2]
        else:
            result = [op2, op1]

    return result


def main():
    
    # run() 

    list = []
    # in list: [operand_pair, freq]
    # operand pair: [a, b]

    with open('operands_out2', 'r') as o:
        with open('reuse_out2', 'w+') as r:
            while(1):
                ops = form(o.readline())
                if ops == None:
                    break
                found = False
                for entry in list:
                    if (entry[0][0] == ops[0] and entry[0][1] == ops[1]):
                        entry[1] += 1
                        found = True
                        break
                if found == False:
                    list.append([ops, 1])
            
            for e in list:
                r.write("("+ str(e[0][0]) + "," + str(e[0][1]) + ") "  + str(e[1])+ "\n")
       
if __name__ == "__main__":
    main()        