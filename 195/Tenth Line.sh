#!/usr/bin/env bash

head -n 10 file.txt | tail -n+10

sed -n 10p file.txt