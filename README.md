# Sleeper

Print each second and sleep over a duration. For testing purposes.

This is a dummy container that sleeps over an environment set duration (default: 30 - 60 seconds) and prints to stdout each second.

I personally needed something like to mess around with long-living containers.

### To pull the image

`docker pull rsoury/sleeper`

### To build the image locally

1.  `git clone git@github.com:rsoury/sleeper.git`
2.  `docker build . -t rsoury/sleeper -f Dockerfile.build`
