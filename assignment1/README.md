Docker file creates volume of the app directory.

The instruction of in Docker file VOLUME /serverdata will create the volume inside the container.

To run the image, use the following command:
docker run -it -v servervol:/serverdata assignment1:latest