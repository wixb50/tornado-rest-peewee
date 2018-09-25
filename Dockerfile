FROM tornado_rest_peewee:base

LABEL maintainer=xiewenqian

RUN useradd -ms /bin/bash jovyan && chown jovyan:jovyan /home/jovyan

ENV RUN_ENV=prod

COPY HxQuantMgm /home/jovyan/app
COPY HxQuantMgm/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN echo "Asia/Shanghai" > /etc/timezone && dpkg-reconfigure -f noninteractive tzdata

RUN chown -R jovyan:jovyan /home/jovyan/app
USER jovyan

WORKDIR /home/jovyan/app

EXPOSE 8050

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
