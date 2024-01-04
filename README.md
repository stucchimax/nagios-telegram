# nagios-telegram
Nagios to telegram notify script

Use this script to add fancy notifications to your nagios monitoring system.

You need to setup a virtualenv for this to run:

```shell
python3 -m venv /usr/local/venv
```

Then you need to set up the specific command - usually in commands.cfg:

```
define command{
	command_name    notify-by-telegram-service
	command_line    /usr/local/venv/bin/python3 /usr/local/venv/nagios-telegram.py --chat_id "{{Your Chat ID}}" --notification_type "$NOTIFICATIONTYPE$" --service_desc "$SERVICEDESC$" --hostname "$HOSTNAME$" --state "$SERVICESTATE$" --address "$HOSTADDRESS$" --moreinfo "$SERVICEOUTPUT$" --datetime "$LONGDATETIME$" --token "{{Bot Token}}"
}

define command{
	command_name    notify-by-telegram-host
	command_line    /usr/local/venv/bin/python3 /usr/local/venv/nagios-telegram.py --chat_id "{{Your Chat ID}}" --notification_type "$NOTIFICATIONTYPE$" --service_desc "$SERVICEDESC$" --hostname "$HOSTNAME$" --state "$HOSTSTATE$" --address "$HOSTADDRESS$" --moreinfo "$HOSTOUTPUT$" --datetime "$LONGDATETIME$" --token "{{Bot Token}}"
}

```

Of course you need a Telegram Bot, its associated token, and then a valid Chat ID. 

In my example, I have setup the virtualenv in /usr/local/venv, and copied the nagios-telegram.py script there.

Last, but not least, you should configure the templates for your services to use this notification method, such as this:

```
define contact {
    name                            generic-contact         ; The name of this contact template
    service_notification_period     24x7                    ; service notifications can be sent anytime
    host_notification_period        24x7                    ; host notifications can be sent anytime
    service_notification_options    w,u,c,r,f,s             ; send notifications for all service states, flapping events, and scheduled downtime events
    host_notification_options       d,u,r,f,s               ; send notifications for all host states, flapping events, and scheduled downtime events
    service_notification_commands   notify-by-telegram-service ; send service notifications via email
    host_notification_commands      notify-by-telegram-host    ; send host notifications via email
    register                        0                       ; DON'T REGISTER THIS DEFINITION - ITS NOT A REAL CONTACT, JUST A TEMPLATE!
}

```

You should start getting notifications such as these:

```
💚 -- RECOVERY

Host: storage
Service: Load
State: OK
Address: 192.168.1.10
Time: Thu Jan 4 09:30:54 UTC 2024
Info:
OK - load average per CPU: 0.07, 0.05, 0.05
```

