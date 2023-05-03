import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main ():
    tests = ["case1", "case2", "case3", "case4", "case5", "case6", "suboptimal"]
    runtimes_approx = [.101819, .090042, .087920, .100856, .084128, .088143, .0924602]
    runtimes_exact = [.112969, .1172528, .1273398, 3.697802, 55, 999, .6279171]
    df = pd.DataFrame (np.c_[runtimes_approx, runtimes_exact], index=tests)
    df.plot.bar ()
    #plt.bar (tests - 0.5, runtimes_approx)
    #plt.bar (tests + 0.5, runtimes_exact)
    plt.tight_layout ()
    plt.legend (['approximation', 'exact'])
    plt.xlabel ("Test Case")
    plt.ylabel ("Runtime (seconds)")
    plt.ylim (0, 4)
    plt.show ()


if __name__ == "__main__":
    main ()