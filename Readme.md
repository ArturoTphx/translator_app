docker image build -t translator .
SI HAY ERROR: sudo chmod 666 /var/run/docker.sock
docker run -p 5000:5000 -d translator
PARA VER REGISTROS: docker logs CONTAINER_ID
