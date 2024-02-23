# import loraplus

# depending where you run it from, loraplus could be refer to the repo dir, the "loraplus" dir in that, or the loraplus.py in that.
import loraplus as lp 
import loraplus.loraplus as lplp 
# import loraplus.loraplus.loraplus as lplplp #.py IN the dir in the repo

if __name__ == "__main__":
    print(dir(lp))
    print(dir(lplp))
    # print(dir(lplplp))


    # print(dir(lp.arguments))
    # print(dir(loraplus))