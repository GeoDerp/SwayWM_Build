#!/bin/bash
#
# Simple Hue Light script to control one group/room/Light, by GeoDerp https://github.com/GeoDerp/SwayWM_Build
# Instructions to Hue api: https://developers.meethue.com/develop/get-started-2/ (find how to generate Key and light/group Id here)
# Used danradom's https://github.com/danradom/hue as an exmple

#Instance Varibles
#Bridge IP
IP="<IP address here>"
#Hash
userKey="<user key here>"
#Unique Light/Room/Group ID
LightID="<Light ID here>"

# current state [dont change]
cstate=0

#off,Low,Medium,Hight Examples
Low='{"on":true, "sat":199, "bri":42,"hue":5000}' #int 1
medium='{"on":true, "sat":199, "bri":5,"hue":7688}' #int 2
hight='{"on":true, "sat":199, "bri":52,"hue":65535}' #int 3

#Get satus
 ## get satus
  #curl -X PUT -d $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1

#Move Up/Down interval if args selected
if  [ $1 = "-e" ] ; then
if  [ $2 = "up" ] ; then
interate up
fi
if  [ $2 = "down" ] ; then
interate down
fi
fi
if  [ $2 = "switch" ] ; then
interate switch
fi
else 
status eho # check status and echo (no iteration)
fi

#reachable=`curl -X GET -s "https://$IP/api/$userKey/lights/$LightID/state" |cut -d, -f10 |cut -d: -f2 |sed 's/}//'`
#    curl -X PUT -d '{"on":false}' https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1

#Get satus
function status {
     curl -X GET -s "https://$IP/api/$userKey/lights/$LightID/state"
    # incert switch statment here
    if ($1 == "eho") {
        echo (text cstate)
        exit #dont need to iterate, just "ping" and check status
    }
}

function interate { #interate up, down or switch (on/off)
elif ($1 == "up" || $1 == "down" || $1 == "switch") 
# incert switch statment here, "switch" will need to have a temp of number stored somewhere, if file is empty them populate and 
# switch (on/off) if not then return to last case 
fi
else #return current int value 
fi
# waybar echo status
status text
}

function putState {
    # incert switch here
}

function text { #convert int to text (is there a smarter way of doing this, probally)
    # incert switch here
}

##curl -X PUT -d $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1
  ##curl -X PUT -d '{"on":false}'  $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1
