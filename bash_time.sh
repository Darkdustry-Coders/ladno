#!/bin/bash



start_time=$(date +%s)
$1
end_time=$(date +%s)
echo "$(($end_time - $start_time)) seconds"
