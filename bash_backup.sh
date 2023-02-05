#!/bin/bash
#######################################
#                                     #
# Backup users home folder to /backup #
#                                     #
#######################################

# What to backup. 
backup_files="/home" # you can add your own folders to backup them too

# Where to backup to.
dest="/backup" # change this string to change backup destination

# Create archive filename.
day=$(date +%A)
hostname=$(hostname -s)
archive_file="$hostname-$day.tgz"

# Print start status message.
echo "Backing up $backup_files to $dest/$archive_file"
date
echo

# Backup the files using tar.
tar czf $dest/$archive_file $backup_files

# Print end status message.
echo
echo "Backup finished"
date

# Long listing of files in $dest to check file sizes.
ls -lh $dest
