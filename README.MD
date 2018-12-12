Instrumentation/Prometheus Sample
---------------------------------

This project serves the purpose of serving as a reference for use of prometheus instrumentation in both a vanilla (falcon) mode and the use of django-prometheus.

Requirements
------------

Docker and docker-compose installed and working.

Starting
--------

After the repository cloning, use `docker-compose up -d` to start the services. After a few seconds, the following services should be started:

 * app: A falcon app listening in the port 5000, with the /products and /metrics endpoints;
 * django: A django app listening the port 8000, with the /products and /metrics endpoints;
 * prometheus: A  prometheus running on port 9090, configured to scrap `app` and `django` apps;
 * grafana: A grafana installation that can be used to plot visualizations using prometheus data.

In all cases, you can access the application using the `localhost:<PORT>` in the browser.

Author
------

Author: Gabriel Abdalla Cavalcante Silva (gabriel.cavalcante88@gmail.com)
