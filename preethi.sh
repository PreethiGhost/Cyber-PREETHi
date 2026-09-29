#!/bin/bash
clear
echo "=================================="
echo "    PREETHI ULTIMATE TOOL V1.0    "
echo "=================================="
echo "1. Show System & Device Info"
echo "2. Digital Matrix Rain"
echo "3. Check Battery Status"
echo "4. Advanced Port Scanner"
echo "5. Network Devices Scan (ARP)"
echo "6. Launch TBomb (SMS Bomber)"
echo "7. Open Wi-Fi Settings"
echo "8. Exit"
echo "=================================="
read -p "Enter your choice (1-8): " choice

if [[ $choice -eq 1 ]]; then
    neofetch
elif [[ $choice -eq 2 ]]; then
    cmatrix
elif [[ $choice -eq 3 ]]; then
    termux-battery-status
elif [[ $choice -eq 4 ]]; then
    read -p "Enter IP or Domain to scan: " ip_target
    nc -z -v $ip_target 21 22 80 443 8080
    read -p "Press Enter to continue..."
elif [[ $choice -eq 5 ]]; then
    arp -a
    read -p "Press Enter to continue..."
elif [[ $choice -eq 6 ]]; then
    cd ~/TBomb && bash TBomb.sh
elif [[ $choice -eq 7 ]]; then
    am start -a android.settings.WIFI_SETTINGS
else
    echo "Exiting... Bye Preethu!"
fi
