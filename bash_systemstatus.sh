#!/bin/bash

# Get CPU usage as a percentage and as a progress bar
cpu_usage=$(top -bn1 -o "PID" | grep '%cpu' | awk '{print $2 + $4}')
cpu_usage=${cpu_usage%.*}
cpu_bar=""
for (( i=0; i<=10; i++ )); do
  if [ $((cpu_usage / 10)) -ge $i ]; then
    cpu_bar="${cpu_bar}="
  else
    cpu_bar="${cpu_bar}-"
  fi
done

# Get RAM usage as a percentage and in GB, and as a progress bar
ram_total=$(free -m | awk 'NR==2{printf "%.1f",$2/1024 }')
ram_used=$(free -m | awk 'NR==2{printf "%.1f",$3/1024 }')
ram_usage=$(awk "BEGIN {printf \"%.0f\", ${ram_used}/${ram_total}*100}")
ram_formatted=$(printf "%.1f/%.1f GB" $ram_used $ram_total)
ram_progress=$((ram_usage/10))
ram_bar=""
for (( i=0; i<=10; i++ )); do
  if [ $ram_progress -ge $i ]; then
    ram_bar="${ram_bar}="
  else
    ram_bar="${ram_bar}-"
  fi
done

# Get disk usage for each mounted partition
disk_usage=$(df -h | grep '^/dev/' | awk '{print $1 ": " $3 " used, " $4 " available, " $5 " used%"}

# Print formatted output
echo "CPU: [$cpu_bar] $cpu_usage%"
echo "RAM: [$ram_bar] $ram_usage% ($ram_formatted)"
echo "$disk_usage"
