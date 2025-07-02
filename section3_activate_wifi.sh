#!/bin/bash
#Script to ativate alfa awus1900 in monito mode autmatically

#Look for wireless interface that starts with wlan(e.g. wlan0, wlan1. wlan2)

IFACE=$(iw dev | awk '$1=="Interface"{print $2}' | grep -E '^wlan[0-9]+$')

#if no interface found shows error
if [ -z "$IFACE" ]; then
	echo "No wireles interface found"
	exit 1
fi

echo "Wireless interface found: $IFACE"

#enabling monitor mode
sudo ip link set $IFACE down

sudo iw dev $IFACE set type monitor

sudo ip link set $IFACE up

echo "Monitor mode enabled in $IFACE"

#Shows state to confirm
iwconfig $IFACE 
