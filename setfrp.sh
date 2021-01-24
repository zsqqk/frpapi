#!/bin/bash
# frp外穿


echo "["$1"]
type = tcp
local_ip = "$2"
local_port = "$3"
remote_port = "$4"
">>frpc.ini
systemctl stop frpc
systemctl start frpc

