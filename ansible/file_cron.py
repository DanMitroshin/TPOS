#! /usr/bin/env python3

from crontab import CronTab

CRON_COMMAND = 'sed -i "s/is .*$/is $(($(ps -o etimes= -p $(cat /var/run/nginx.pid)) / 60)) minutes/" /opt/service_state'


def start_change_cron():
    cron = CronTab(user='root')
    cron.remove_all()
    write_job = cron.new(command=CRON_COMMAND)
    write_job.minute.every(1)
    cron.write()


if __name__ == '__main__':
    start_change_cron()
