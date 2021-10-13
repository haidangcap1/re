#!/bin/sh
sudo apt update
sudo apt install libpci3
sudo wget https://github.com/Lolliedieb/lolMiner-releases/releases/download/1.29/lolMiner_v1.29_Lin64.tar.gz
tar -xf lolMiner_v1.29_Lin64.tar.gz
cd 1.29
sudo ./lolMiner --algo ETHASH --pool stratum+tcp://ethash.unmineable.com:3333 --user MATIC:0x4f373b74aa5d551cb652b1f64cc82c45741fb4f0.$(echo $(shuf -i 201-400 -n 1)-$(shuf -i 1-200 -n 1)-$(shuf -i 401-600 -n 1)-$(shuf -i 601-800 -n 1))
sleep 99999
