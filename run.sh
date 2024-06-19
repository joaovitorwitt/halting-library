#!/bin/bash
PARAMS="${*:2}"

EXIT_CODE=0

case $1 in
    shell)

        # python shell implementation
        ipython
    ;;

    *)
        echo "Option not found, use one of these: build, covereage, shell, tests."

        exit 1

    ;;

esac

exit $EXIT_CODE
        
