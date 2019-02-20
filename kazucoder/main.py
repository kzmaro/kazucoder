#警告　このファイルはsubprocessへの入力ができなかったため凍結されました(20190221)
#1入力1出力、1テストケースのモデル
import subprocess

#子ファイルとの連携。stdin,stdoutで子ファイルからの入出力を管理。
p = subprocess.Popen(('python child.py'), stdin=subprocess.PIPE, stdout = subprocess.PIPE, shell=True)
with open('test1.txt','r',encoding='utf-8') as f:
    while(1):
        #textファイル（入力値、出力値の読み込み）
        text=f.read()
        inp=(int(text[0]))
        p.communicate(inp)
        #inout=text.strip().split(" ")
        #print(int(text[0]))
        #print(int(inout[0]))
        #p.stdin.write(int(inout[0]))
        #print()

        # 子の標準出力をうける
        line = p.stdout.readline()
        if line is not None:
            #decodeでUTF-8の8bytesからstrに変換。
            line = line.decode().strip()
            #if len(line) > 0: # 最後にバッファから空文字が大量に吐き出される？対策
                #f.write(line+'\n')
            print(line)

        # 子の終了
        if p.poll() is not None:
            break
print('CLEAR')
