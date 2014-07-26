#!/bin/bash
#A System Information Gathering Script

#Command 1
function uname_func()
{
    UNAME="uname -a"
    printf "Gathering system imformation with the $UNAME command:\n\n"
    $UNAME
}

#Command 2
function disk_func()
{
    DISKSPACE="df -h"
    printf "Gathering diskspace information with the $DISKSPACE commamd:\n\n"
    $DISKSPACE
}

function main()
{
    uname_func
    disk_func
}

main
