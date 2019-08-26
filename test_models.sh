#!/bin/bash

# set this to a relative path, from inside the fhirclient/models directory, to the downloaded FHIR spec directory
DOWNLOAD_DIR="fhir-parser/downloads"
FHIR_UNITTEST_DATADIR=$(cd "$DOWNLOAD_DIR"; echo "$PWD")

if [ ! -e $FHIR_UNITTEST_DATADIR ]; then
	echo Unit tests depend on the downloaded FHIR spec, which is not present at $FHIR_UNITTEST_DATADIR. Cannot run unit tests.
	return
fi

#python -m unittest discover ./models 'test_*.py'		# ImportError
model_tests=(tests/test_models/test_*.py)

pipenv run python -m unittest "${model_tests[@]}"

# custom tests
custom_tests=(tests/test_client/test_*.py)
pipenv run python -m unittest "${custom_tests[@]}"

