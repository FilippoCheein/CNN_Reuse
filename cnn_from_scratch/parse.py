# parse matrix_out script
# result pairs of operands used in convolution

def format(str):
    str = str.replace("[", " ")
    str = str.replace("]", " ")
    str = str.split()
    return str

def run():
    with open('matrix_out2', 'r') as f:

        with open('operands_out2', 'w+') as o:
            while(1):
                im1 = format(f.readline())
                if(len(im1) <= 1):
                    break
                im2 = format(f.readline())
                im3 = format(f.readline())
                i = 0
                while i < 8:
                    f1 = format(f.readline())
                    f2 = format(f.readline())
                    f3 = format(f.readline())
                    o.write(im1[0] + " " + f1[0] + "\n")
                    o.write(im1[0] + " " + f1[1] + "\n")
                    o.write(im1[0] + " " + f1[2] + "\n")
                    o.write(im1[1] + " " + f2[0] + "\n")
                    o.write(im1[1] + " " + f2[1] + "\n")
                    o.write(im1[1] + " " + f2[2] + "\n")
                    o.write(im1[2] + " " + f3[0] + "\n")
                    o.write(im1[2] + " " + f3[1] + "\n")
                    o.write(im1[2] + " " + f3[2] + "\n")
                    o.write(im2[0] + " " + f1[0] + "\n")
                    o.write(im2[0] + " " + f1[1] + "\n")
                    o.write(im2[0] + " " + f1[2] + "\n")
                    o.write(im2[1] + " " + f2[0] + "\n")
                    o.write(im2[1] + " " + f2[1] + "\n")
                    o.write(im2[1] + " " + f2[2] + "\n")
                    o.write(im2[2] + " " + f3[0] + "\n")
                    o.write(im2[2] + " " + f3[1] + "\n")
                    o.write(im2[2] + " " + f3[2] + "\n")
                    o.write(im3[0] + " " + f1[0] + "\n")
                    o.write(im3[0] + " " + f1[1] + "\n")
                    o.write(im3[0] + " " + f1[2] + "\n")
                    o.write(im3[1] + " " + f2[0] + "\n")
                    o.write(im3[1] + " " + f2[1] + "\n")
                    o.write(im3[1] + " " + f2[2] + "\n")
                    o.write(im3[2] + " " + f3[0] + "\n")
                    o.write(im3[2] + " " + f3[1] + "\n")
                    o.write(im3[2] + " " + f3[2] + "\n")

                    i += 1
            
