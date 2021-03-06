#!/bin/bash

set -e

basename="$(dirname $0)"

if [ -z CC ]; then
	JUDYCC=$CC
else
	JUDYCC=cc
fi

if [ ! -z COPT ]; then
	COPT="-DJU_64BIT -O0 -fPIC -fno-strict-aliasing"
fi


if $JUDYCC -v 2>&1 >/dev/null | egrep "clang|gcc version 4.6"; then
	COPT+=""
else
	COPT+=" -fno-aggressive-loop-optimizations"
fi

(cd $basename; cd judy-1.0.5/src; CC=$JUDYCC COPT="$COPT" sh ./sh_build)
