SRC_OUT="src/day$1.py"
if [ -f "$SRC_OUT" ]; then
    echo "$SRC_OUT already exists."
else 
    echo "Copying source file $SRC_OUT"
    cp template/dayx.py "$SRC_OUT"
fi

TEST_OUT="tests/test_day$1.py"
if [ -f "$TEST_OUT" ]; then
    echo "$TEST_OUT already exists."
else 
    echo "Copying test file $TEST_OUT"
	sed "s/x/$1/g" template/test_dayx.py > "$TEST_OUT"
fi

code -a "$SRC_OUT"
code -a "$TEST_OUT"
code -a "data/day$1_ex"