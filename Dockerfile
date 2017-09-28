FROM ubuntu:17.10
USER root

ENV LC_ALL C
ENV DEBIAN_FRONTEND noninteractive
ENV DEBCONF_NONINTERACTIVE_SEEN true

MAINTAINER Jorge Useche <juusechec@gmail.com>
RUN apt-get -qqy update
RUN apt-get -qqy --no-install-recommends install \
  wget \
  firefox \
  x11vnc \
  xvfb \
  xfonts-100dpi \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  openjdk-8-jre-headless \
  python3-pip \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*
RUN pip3 install selenium
RUN useradd -d /home/seleuser -m seleuser
RUN mkdir -p /home/seleuser/chrome
RUN chown -R seleuser /home/seleuser
RUN chgrp -R seleuser /home/seleuser

RUN wget https://selenium-release.storage.googleapis.com/3.6/selenium-server-standalone-3.6.0.jar
RUN mv selenium-server-standalone-*.jar /home/seleuser/selenium-server-standalone.jar

ADD ./scripts/ /home/root/scripts
EXPOSE 4444 5999
ENTRYPOINT ["sh", "/home/root/scripts/start.sh"]

RUN useradd uduser \
         --shell /bin/bash  \
         --create-home \
  && usermod -a -G sudo uduser \
  && echo 'ALL ALL = (ALL) NOPASSWD: ALL' >> /etc/sudoers \
&& echo 'uduser:secret' | chpasswd

USER uduser
