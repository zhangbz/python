#!/bin/bash
#A System Information Gathering Script

#Command 1
UNAME="uname -a"
printf "Gathering system imformation with the $UNAME command:\n\n"
$UNAME

#Command 2
DISKSPACE="df -h"
printf "Gathering diskspace information with the $DISKSPACE commamd:\n\n"
$DISKSPACE
