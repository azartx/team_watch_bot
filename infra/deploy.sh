#!/bin/bash
cd /root/team_watch_bot || exit 1
git fetch
git pull origin main
sudo systemctl daemon-reload
sudo systemctl restart team_watch_bot.service