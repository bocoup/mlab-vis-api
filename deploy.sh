#!/bin/bash

USAGE="$0 [production|staging|arbitrary-string-sandbox] travis?"
if [[ -n "$2" ]] && [[ "$2" != travis ]]; then
  echo The second argument can only be the word travis or nothing at all.
  echo $USAGE
  exit 1
fi

set -e
set -x

if [[ $2 == travis ]]; then
  cd $TRAVIS_BUILD_DIR
  GIT_COMMIT=${TRAVIS_COMMIT}
else
  GIT_COMMIT=$(git log -n 1 | head -n 1 | awk '{print $2}')
fi

source "${HOME}/google-cloud-sdk/path.bash.inc"

# Adapted from the one from ezprompt.net
function git_is_dirty {
    status=`git status 2>&1 | tee`
    dirty=`echo -n "${status}" 2> /dev/null | grep "modified:" &> /dev/null; echo "$?"`
    newfile=`echo -n "${status}" 2> /dev/null | grep "new file:" &> /dev/null; echo "$?"`
    renamed=`echo -n "${status}" 2> /dev/null | grep "renamed:" &> /dev/null; echo "$?"`
    deleted=`echo -n "${status}" 2> /dev/null | grep "deleted:" &> /dev/null; echo "$?"`
    bits=''
    if [ "${renamed}" == "0" ]; then
        bits=">${bits}"
    fi
    if [ "${newfile}" == "0" ]; then
        bits="+${bits}"
    fi
    if [ "${deleted}" == "0" ]; then
        bits="x${bits}"
    fi
    if [ "${dirty}" == "0" ]; then
        bits="!${bits}"
    fi
    [[ -n "${bits}" ]]
}

# Initialize correct environment variables based on type of deployment
if [[ "$1" == production ]]; then
  source ./environments/production.sh
  if git_is_dirty ; then
    echo "We won't deploy to production with uncommitted changes"
    exit 1
  fi
elif [[ "$1" == staging ]]; then
  source ./environments/staging.sh
  if git_is_dirty ; then
    echo "We won't deploy to staging with uncommitted changes"
    exit 1
  fi
elif [[ "$1" == sandbox-* ]]; then
  source ./environments/sandbox.sh
else
  echo "BAD ARGUMENT TO $0"
  exit 1
fi

if [[ $2 == travis ]]; then
  gcloud auth activate-service-account --key-file ${KEY_FILE}
fi


