FROM pamarthid/voterlist

RUN apt-get update && apt-get install gcc && rm -rf /var/lib/apt/lists/*
