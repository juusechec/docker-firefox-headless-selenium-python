export DISPLAY=:99
Xvfb :99 -shmem -screen 0 1366x768x16 &
x11vnc -passwd secret -display :99 -N -forever &
# selenium must be started by a non-root user otherwise chrome can't start
su - seleuser -c "java -jar /home/seleuser/selenium-server-standalone.jar &"
# Loop until selenium server is available
# link: http://phptest.club/t/how-to-know-if-selenium-server-is-ready/277/3
printf 'Waiting Selenium Server to load\n'
until $(curl --output /dev/null --silent --head --fail http://localhost:4444/wd/hub); do
    printf '.'
    sleep 1
done
printf '\n'
bash
