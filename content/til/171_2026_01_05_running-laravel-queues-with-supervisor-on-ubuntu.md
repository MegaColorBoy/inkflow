title: Running Laravel queues with Supervisor on Ubuntu
date: January 4th, 2026
slug: running-laravel-queues-with-supervisor-on-ubuntu
category: Laravel + Ubuntu + DevOps + Supervisor
status: active

Laravel queues aren’t new to me, but I realized I’d never really written down how I usually set them up on a fresh Ubuntu server.

Whenever I need queue workers to run continuously — and survive restarts or crashes — I almost always reach for **Supervisor**. It’s simple, boring, and gets the job done.

First, install it on your server:

```bash
sudo apt update
sudo apt install supervisor
```

Then create a small config file for the queue worker:

```bash
sudo vim /etc/supervisor/conf.d/laravel-worker.conf
```

This is the setup I generally start with:

```ini
[program:laravel-worker]
process_name=%(program_name)s_%(process_num)02d
command=php /var/www/project/artisan queue:work --sleep=3 --tries=3 --max-time=3600
autostart=true
autorestart=true
user=www-data
numprocs=2
redirect_stderr=true
stdout_logfile=/var/www/project/storage/logs/laravel-worker.log
stopwaitsecs=600
```

A few quick notes on what this does:

* It runs `queue:work` instead of `queue:listen`, so the worker stays in memory
* Two worker processes are started in parallel (`numprocs=2`)
* If the queue is empty, the worker sleeps for a few seconds instead of spinning
* Failed jobs are retried a limited number of times
* The worker is force-restarted every hour to avoid memory leaks
* If a worker crashes, Supervisor brings it back up automatically

Once the file is saved, reload Supervisor’s config:

```bash
sudo supervisorctl reread
sudo supervisorctl update
```

Start the workers:

```bash
sudo supervisorctl start laravel-worker:*
```

And check their status:

```bash
sudo supervisorctl status
```

Whenever I deploy new code or change environment variables, I just restart them:

```bash
sudo supervisorctl restart laravel-worker:*
```

Logs end up in Laravel’s `storage/logs`, which is usually the first place I look when something feels off.

This setup has been reliable for me across multiple projects. No dashboards, no extra moving parts — just queue workers quietly doing their job in the background.

Hope you found this useful!