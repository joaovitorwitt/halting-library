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
        
        echo "Running coverage..."

        python -m coverage run -m unittest -f ${TESTS}
        python -m coverage report -m
        EXIT_CODE=$?
        # coverage measurament
        # report

    ;;

    tests)

        # test
        
        echo "Running tests..."
        
        python -m unittest -v ${TESTS}
        EXIT_CODE=$?
    ;;

    build)

    # build command to deploy a new version of the library
    echo "Preparing deployment..."

    ;;

    deploy)

    echo "Deploying Library...."

    ;;

    *)
        echo "Option not found, use one of these: build, covereage, shell, tests."

        exit 1

    ;;

esac
exit $EXIT_CODE
        
