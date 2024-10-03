FROM solr:8.1.1

#WORKDIR /opt/solr-8.1.1/server/

USER root

RUN precreate-core ctf

RUN touch /opt/solr-8.1.1/server/CTF{S0lr_Inj3cti0n_Is_BAd}

RUN chown -R solr /opt/solr/server/solr

USER solr

# RUN /opt/solr/bin/solr start && /opt/solr/bin/solr create_core -c avatar && /opt/solr/bin/solr stop

