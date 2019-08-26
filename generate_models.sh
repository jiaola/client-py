#!/bin/bash

if [ ! -e fhir-parser ]; then
	git submodule update --init --recursive
fi

cp fhir-parser-resources/settings.py fhir-parser/settings.py
for file in fhir-parser-resources/*.j2
do
  cp "$file" "${file%.j2}.py"
done
pushd fhir-parser
pipenv run python ./generate.py $1
popd

for file in fhir-parser-resources/*.j2
do
  rm "${file%.j2}.py"
done
