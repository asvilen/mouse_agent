# Mouse Agent

## Overview

This project is a mouse tracking application designed to display real-time mouse coordinates on a webpage and capture a photo from a connected webcam when the left mouse button is pressed. The application utilizes popular Python libraries, including `aiohttp` for the web server, `pynput` for mouse tracking, and `openCV` for webcam image capture. All collected data, including mouse coordinates and image paths, is stored in an SQLite database.

## How It Works

The application operates by utilizing an aiohttp-based web server that offers a WebSocket endpoint for seamless real-time communication with the client-side. The server continually tracks mouse coordinates using `pynput` and communicates updates to connected clients. Upon pressing the left mouse button, the application captures an image from the webcam using `openCV`. The acquired data is then stored in an SQLite database for future reference.

## Instructions

To run the program, execute the provided shell script (`run_program.sh`). This script automates the installation of necessary Python libraries, starts the main Python program (`main.py`), and opens the HTML file in the default web browser. Follow the on-screen instructions to gracefully terminate the program.

## Termination

To stop the program, press `Ctrl+C` in the terminal.

## License

This project is licensed under the [MIT License](LICENSE).
