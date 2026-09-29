#!/bin/bash
clear
echo "=================================="
echo "    VENOM DANGEROUS TOOL V6.0    "
echo "=================================="
echo "1. Show System Info"
echo "2. Digital Matrix Rain"
echo "3. Check Battery Status"
echo "4. Print Name Art"
echo "5. Local Chat with Friends"
echo "6. Network Ping Test"
echo "7. Advanced Port Scanner"
echo "8. Network Interfaces Info"
echo "9. Local Connected Devices Scanner"
echo "10. Open Wi-Fi Settings"
echo "11. SMS Bomber Tool Setup"
echo "12. Exit"
echo "=================================="
read -p "Enter your choice (1-12): " choice

if [[ $choice -eq 1 ]]; then
    neofetch
elif [[ $choice -eq 2 ]]; then
    cmatrix
elif [[ $choice -eq 3 ]]; then
    termux-battery-status
elif [[ $choice -eq 4 ]]; then
    figlet "Preethu"
elif [[ $choice -eq 5 ]]; then
    echo "Starting Chat Room..."
    echo "If you want to host, type: nc -l -p 1234"
    echo "If you want to join, type: nc <friend_ip> 1234"
    read -p "Press Enter to continue..."
elif [[ $choice -eq 6 ]]; then
    read -p "Enter website or IP to ping (e.g. google.com): " target
    ping -c 4 $target
    read -p "Press Enter to continue..."
elif [[ $choice -eq 7 ]]; then
    read -p "Enter IP or Domain to scan ports: " ip_target
    echo "Scanning open ports for $ip_target..."
    nc -z -v $ip_target 21 22 80 443 8080
    read -p "Press Enter to continue..."
elif [[ $choice -eq 8 ]]; then
    echo "Fetching Network Interface details..."
    ifconfig
    read -p "Press Enter to continue..."
elif [[ $choice -eq 9 ]]; then
    echo "Scanning devices on your network..."
    arp -a
    read -p "Press Enter to continue..."
elif [[ $choice -eq 10 ]]; then
    echo "Opening Wi-Fi Settings..."
    am start -a android.settings.WIFI_SETTINGS
    read -p "Press Enter to continue..."
elif [[ $choice -eq 11 ]]; then
    echo "Setting up SMS Bomber dependencies..."
    pkg update -y && pkg install git python -y
    echo "You can now clone a bomber tool using git clone!"
    read -p "Press Enter to continue..."
else
    echo "Exiting... Bye Preethu!"
fi
