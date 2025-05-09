FROM ros:humble

RUN apt-get update && apt-get install -y \
    ros-humble-turtlesim \
    x11vnc \
    xvfb \
    fluxbox \
    xterm \
    wget \
    netcat \
    python3-websockify \
    build-essential \
    && apt-get clean

RUN mkdir -p /opt/novnc && \
    wget -qO- https://github.com/novnc/noVNC/archive/refs/tags/v1.4.0.tar.gz | tar xz --strip-components=1 -C /opt/novnc

COPY start.sh /start.sh
RUN chmod +x /start.sh

EXPOSE 8080
CMD ["/start.sh"]