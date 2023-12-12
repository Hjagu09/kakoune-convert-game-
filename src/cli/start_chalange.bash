#/bin/bash

cd $1
cp $2 "../../rc/working/input"
cd ../../rc/working/
\time -f "%E" kak -ui terminal input
