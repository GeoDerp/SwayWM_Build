#!/bin/bash
#
# Simple Hue Light script to control one group/room/Light, by GeoDerp https://github.com/GeoDerp/SwayWM_Build
# Instructions to Hue api: https://developers.meethue.com/develop/get-started-2/ (find how to generate Key and light/group Id here)
#

#Instance Varibles
#Bridge IP
IP="<IP address>"
#Hash
userKey="<user key>"
#Unique Light/Room/Group ID
LightID="<Light ID>"

#off,Low,Medium,Hight Examples
Low='{"on":true, "sat":199, "bri":42,"hue":5000}'
medium='{"on":true, "sat":199, "bri":5,"hue":7688}'
hight='{"on":true, "sat":199, "bri":52,"hue":65535}'

#Get satus
  curl -X PUT -d $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1

#Move Up/Down interval if args selected
if  [ $1 = "-e" ] ; then
if  [ $2 = "up" ] ; then
  curl -X PUT -d $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1
  curl -X PUT -d '{"on":false}'  $next https://$IP/api/$userKey/lights/$LightID/state > /dev/null 2>&1
fi
if  [ $2 = "down" ] ; then
fi
fi

#if (curl -X GET -s)

#https://$IP/api/$userKey/lights/$LightID/state

#reachable=`curl -X GET -s "http://$bridge/api/$hash/lights/$light" |cut -d, -f10 |cut -d: -f2 |sed 's/}//'`
#    curl -X PUT -d '{"on":false}' http://$bridge/api/$hash/lights/$light/state > /dev/null 2>&1

#Get satus
asdadasdas

# echo status
asdadasdasda
