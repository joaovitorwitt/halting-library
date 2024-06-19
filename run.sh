#!/bin/bash
PARAMS="${*:2}"


# define the TESTS value if none is passed
if [[ -z ${PARAMS} ]]; then
    TESTS="src.halting.tests"
else
    TESTS="${PARAMS}"
fi



EXIT_CODE=0
case $1 in
    shell)

        # python shell implementation
        ipython
    ;;

    coverage)

        export PYTHONWARNINGS="ignore"

        python -m coverage run -m unittest -f ${TESTS}
        python -m coverage report
        EXIT_CODE=$?
        # coverage measurament
        # report

    ;;

    tests)

        # test
        python -m unittest ${TESTS}
        EXIT_CODE=$?
    ;;

    *)
        echo "Option not found, use one of these: build, covereage, shell, tests."

        exit 1

    ;;

esac
exit $EXIT_CODE
        
