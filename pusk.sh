#!/bin/bash
rm data.txt
echo "Hi" > data.txt
python servo.py
sleep 2
nom_beats=0
python3 likes.py &
python3 tags.py &
while :
do
	nom_beats_prev=$nom_beats
	nom_beats=$(wc -l data.txt)
	if [[ $nom_beats > $nom_beats_prev ]]
	then
		python servo.py
	fi
	sleep 0.5
done
