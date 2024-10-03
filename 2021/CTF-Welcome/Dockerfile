# start from base
FROM ubuntu:18.04

RUN apt update -y 
RUN apt install -y git libssl-dev libpam0g-dev zlib1g-dev dh-autoreconf

#Creating flag for the Challenge
RUN cd /home && mkdir Desktop  
RUN cd /home/Desktop && echo "CTF{Welcome_To_CTF_2021}" > - 

WORKDIR /

RUN  git clone https://github.com/shellinabox/shellinabox.git && cd shellinabox

RUN  autoreconf -i

RUN  ./configure && make

# Add a new user "carlos" with user id 8877
RUN useradd -u 8877 carlos
# Change to non-root privilege
USER carlos
