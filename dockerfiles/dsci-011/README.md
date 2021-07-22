When using the `dsci-011` Docker image with JupyterHub and DockerSpawner, 
be sure to set `c.DockerSpawner.post_start_cmd = 'sh -c "cp -a /tmp/user-settings/. /home/jupyter/.jupyter/lab/user-settings"'` 
in `/srv/jupyterhub/jupyterhub_config.py`. This will disable the merging cells keyboard shortcut.
