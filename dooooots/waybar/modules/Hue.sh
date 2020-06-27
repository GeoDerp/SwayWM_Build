#!/bin/bash
#
# Simple Hue Light script to control one group/room/Light, by GeoDerp https://github.com/GeoDerp/SwayWM_Build
# Instructions to Hue api: https://developers.meethue.com/develop/get-started-2/ (find how to generate Key and light/group Id here)
# Used danradom's https://github.com/danradom/hue bash code as an exmple
#

#Instance Varibles
#Bridge IP
IP="<IP address here>"
#Hash
userKey="<user key here>"
#Unique Light/Room/Group ID
LightID="<Light ID here>"

#off,Low,Medium,Hight Examples
Low='{"on":true, "sat":199, "bri":42,"hue":5000}'    #cState=1
medium='{"on":true, "sat":199, "bri":5,"hue":7688}'  #cState=2
hight='{"on":true, "sat":199, "bri":52,"hue":65535}' #cState=3

# current state variables [dont change]
cState=0
cStateText=null




#main function
function main {

#Move Up/Down interval if args selected
# if [ "$2" == "" ]; then
# usage
# fi

case "$1" in

    -e)
        
        case "$2" in
        up) iterate up ;;
        down) iterate down ;;
        switch) iterate switch ;;
        esac
    ;;

    -u) status eho ;;

    -h|--help) usage ;;

    *) usage ;;

esac    

}

#reachable=`curl -X GET -s "https://$IP/api/$userKey/lights/$LightID/state" |cut -d, -f10 |cut -d: -f2 |sed 's/}//'`
#curl -X PUT -d '{"on":false}' https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1


# Fuction Usage
function usage {
printf "usage: \n$0 -e [up,down,switch] \n OR \n$0 -u [to get light status]" 
exit
}

#Get satus
function status {
    curl -X GET -s "https://$IP/api/$userKey/lights/$LightID/state"
    # incert switch statment here
    if [ "$1" == "eho" ] ; then
        text & echo cStateText # grab state as text thene echo out
        exit #dont need to iterate, just "ping" and check status
    fi
}

function iterate { #iterate up, down or switch (on/off)
if [ "$1" == "up" || "$1" == "down" || "$1" == "switch" ] ; then
echo "put something here"
fi
}

function putState {
    echo "put something here"
    # incert switch here
}

function text { #convert int to text (is there a smarter way of doing this...probally)
echo "put something here"
    # incert switch here
}

##curl -X PUT -d $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1
##curl -X PUT -d '{"on":false}'  $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1

function switch {
    # incert switch statment here, "switch" will need to have a temp of number stored somewhere (if not off), if file is empty them populate and 
# switch (on/off) if not then return to last case
echo "put something here"
}

#Run main
main "$@"