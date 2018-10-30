#app_python_stamp

FROM python:3

WORKDIR /usr/src/ps3838

# Add crontab file in the cron directory
COPY crontab /etc/cron.d/ps-cron
# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/ps-cron
# Create the log file to be able to run tail
RUN touch /var/log/cron.log


# Install any needed packages specified in requirements.txt
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Install Mitmproxy
RUN pip install mitmproxy

# Install Phantomjs
# RUN mkdir -p /srv/var && \
#     wget -q --no-check-certificate -O /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
#     tar -xjf /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 -C /tmp && \
#     rm -f /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64.tar.bz2 && \
#     mv /tmp/phantomjs-$PHANTOMJS_VERSION-linux-x86_64/ /usr/local/share/phantomjs && \
#     ln -s /usr/local/share/phantomjs/bin/phantomjs /usr/local/bin/phantomjs

COPY . .
# Define environment variable
ENV NAME ps38

# Run the command on container startup
# CMD ["cron", "-f"]

# Run Crawler
CMD [ "python", "spider/ps_main.py" ]
# CMD [ "sh", "./re_header.sh" ]
# CMD ["sh","./rePS.sh"]