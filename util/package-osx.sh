#!/usr/bin/env bash
#COMM_TAG=$(git describe --tags $(git rev-list --tags --max-count=1))
#COMM_COUNT=$(git rev-list --count HEAD)
#BUILD="steemdesktop-${COMM_TAG}-${COMM_COUNT}_osx.dmg"
BUILD="steemdesktop_osx.dmg"
echo -e $BUILD
mv target/steemdesktop.dmg "$BUILD"
curl --upload-file ./steemdesktop_osx.dmg https://transfer.sh/steemdesktop_osx.dmg
# Required for a newline between the outputs
echo -e "\n"
md5 -r "$BUILD"
echo -e "\n"
shasum -a 256 "$BUILD"
