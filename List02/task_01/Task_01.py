class Program(object):
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        with open(self.filepath) as fp, \
                open("out", "wb") as op:
            line = fp.readline()
            wordsQuantity = 0
            maxLineLength = len(line)
            lineCounter = 1
            res = ''
            while line:
                if maxLineLength < len(line):
                    maxLineLength = len(line)

                wordsQuantity += len(line.split())

                res = ''.join(
                    format(i, 'b') for i in bytearray(
                        line, encoding='utf-8')
                )
                op.write(res.encode())
                line = fp.readline()
                lineCounter += 1
            print('Lines:', lineCounter)
            print('MaxLineLength:', maxLineLength)
            print('Words:', wordsQuantity)
            print('Bytes:', len(res))


prg = Program("/task_01/input.txt")
prg.read()
