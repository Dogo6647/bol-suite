#!/bin/bash

#Splash
USER=$(whoami)
echo Hi $USER, welcome to GitUnite!
echo -----------------------------------------------

# Sets variables
PROJECTNAME=$(cat projectname.txt)

# Asks for the platform to build for
echo Available platforms to build for:
ls pforms
echo ''
read -p 'Build for: ' PLATFORM

echo -----------------------------------------------
echo Building $PROJECTNAME for $PLATFORM...
cd pforms
sh $PLATFORM
