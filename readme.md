<h2>Task Scheduler</h2>
<p>Simple task scheduler app created using Django, a python web framework</p>

<br><h2>Table of contents</h2>
<ul>
    <li>Introduction</li>
    <li>Technologies</li>
    <li>Installation</li>
    <li>Usage</li>
</ul>

<br><h2>Introduction</h2>
<p>The Task Scheduler application is like a digital to-do list and a remainder combined. It allows users to add all the tasks that are to be accomplished.<br> Along with it, remainder can be set for events to be transpiring in near future. If set, an email remainder is sent to the provided email at a particular <br>date and time. In addition to this, different priorities can be assigned to different tasks, and on the basis of that, an analysed chart is displayed<br> depicting proportions of task on the basis of priorities assigned</p>

<br><h2>Technologies</h2>
Project is created with:
<ul>
    <li>python version: 3.8.10</li>
    <li>django-admin version: 3.2.4</li>
    <li>celery version: 5.0.5</li>
    <li>erlang version: 23.1.2</li>
    <li>rabbitmq_server version: 3.8.17</li>
</ul>
<br>Overview of above mentioned technologies:
<ul>
    <li>celery: A library for queueing task and asynchronous execution of task</li>
    <li>RabbitMQ server: Software that assits celery to implement task queuing and runs in background</li>
    <li>erlang version: A programming language with built-in concurrency and distributed support, required as RabbitMQ is written in erlang</li>
    <li>django: python web framework</li>
</ul>


<br><h2>Installation</h2>
Following is the installtion guide in Windows enviornment for the above mentioned technologies:
> pip install django=3.2.4<br>
> pip install celery=5.0.5

<br>For downloading rabbitmqserver and erlang visit below mentioned links:
> erlang : https://erlang.org/download/otp_versions_tree.html<br>
> rabbitmq_server: https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.8.17/rabbitmq-server-3.8.17.exe

<br><h2>Usage</h2>
To run this project in Windows enviornment:
> Run **rabbitmq-server.bat** file as administrator, locate this file in:   Drive_letter:\RabbitMQ Server\rabbitmq_server-3.8.17\sbin\<br>

On terminal
> (venv)> celery -A task_scheduler worker -l info<br>
> (venv)> python manage.py runserver
