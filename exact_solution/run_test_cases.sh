cd tests

RED="\033[0;31m"
GREEN="\033[0;32m"
NC="\033[0m" # No Color

for case in case*
do
    cd $case
    python3 ../../solution.py < input > output
    diff expected output > diff
    if [ -s diff ]
    then
        echo -e "$case: ${RED}failed${NC}"
    else
        echo -e "$case: ${GREEN}passed${NC}"
    fi
    rm diff
    cd ../
done

cd ../