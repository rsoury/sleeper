# Sleeper

Print each second and sleep over a duration. For testing purposes.

This is a dummy container that sleeps over an environment set duration (default: 30 - 60 seconds) and prints to stdout each second.

I personally needed something like to mess around with long-living containers.

### Change duration

Change the environment variables to alter the duration in which the sleeper sleeps.
`SLEEP_START=100`
`SLEEP_STOP=120`
This example will decided to sleep for a randomised duration between 100 seconds and 120 seconds.

### To pull the image

`docker pull rsoury/sleeper`

### To build the image locally

1.  `git clone git@github.com:rsoury/sleeper.git`
2.  `docker build . -t rsoury/sleeper -f Dockerfile.build`

### To run the sleeper inside Docker

`docker run --rm rsoury/sleeper`

### To run the sleeper outside a container

`python -u ./sleeper.py`
