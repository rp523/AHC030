#coding: utf-8
from subprocess import getoutput
from pathlib import Path
import sys, os
from tqdm import tqdm

def main():
    seed_num = int(sys.argv[1])
    getoutput("cargo build -r")
    scan_bin = Path("scan")
    if scan_bin.exists():
        os.remove(scan_bin)
    getoutput("cp target/release/start scan")
    score_sum = 0
    score_worst = -1
    score_worst_case = 0
    norm = 0
    assert(scan_bin.exists())
    with open("score1.csv", "w") as f:
        for i in tqdm(range(seed_num)):
            cmd = "./tester ./{}".format(scan_bin) + " < tools/in/{0:04d}.txt > tools/out/{0:04d}.txt".format(i, i)
            ret = getoutput(cmd)
            score = int(ret[ret.rfind(" ") + 1:])
            norm += 1
            score_sum += score
            if score_worst < 0:
                score_worst = score
                score_worst_case = i
            elif score_worst < score:
                score_worst = score
                score_worst_case = i
            f.write("{}\n".format(score))
    score_ave = score_sum / norm
    print("ave", score_ave, "worst", score_worst, score_worst_case)

if __name__ == "__main__":
    main()
