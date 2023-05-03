cd tests

RED="\033[0;31m"
GREEN="\033[0;32m"
BOLD="\033[1m"
NC="\033[0m" # No Color
BLUE="\033[0;34m"
UL="\e[4;30m"


echo "${UL}test\tresult\truntime${NC}"
for test in *
do
    cd $test

    start=`python3 -c 'import time; print(time.time())'`
    python3 ../../approximation.py < input > output
    end=`python3 -c 'import time; print(time.time())'`
    runtime=$( echo "$end - $start" | bc -l )

    if [ "$(head -n 1 expected)" = "$(head -n 1 output)" ]
    then
        echo -e "${test}\t${GREEN}passed\t${BLUE}${runtime}s${NC}"
    else
        echo -e "${test}\t${RED}failed\t${BLUE}${runtime}s${NC}"
    fi
    cd ../
done


cd ../