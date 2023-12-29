#!/bin/bash

pip3 install -r requirements.txt
python3 main.py &
PID=$!

# Sleep to ensure the server has loaded
sleep 2

cleanup() {
    echo " Stopping the program..."
    kill $PID
    exit
}
trap cleanup SIGINT SIGTERM

if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open http://localhost:8080
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    xdg-open http://localhost:8080
else
    echo "Unsupported operating system"
    cleanup
fi

echo ""
echo "Running..."
echo "To terminate the program press Ctrl+C"
echo ""
wait $PID
