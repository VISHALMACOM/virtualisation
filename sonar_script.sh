#!/bin/bash

# Pattern to search for processes
pattern="java"  # Replace 'your_pattern_here' with the actual pattern

# Use pgrep to find process IDs (PIDs) matching the pattern
pids=$(pgrep "$pattern")

if [ -z "$pids" ]; then
    echo "No processes found matching the pattern '$pattern'"
else
    echo "Processes found matching the pattern '$pattern':"
    echo "$pids"
    # Kill the processes
    pkill "$pattern"
    echo "Processes killed."
fi
