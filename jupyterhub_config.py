from oauthenticator.github import GitHubOAuthenticator
c.JupyterHub.authenticator_class = GitHubOAuthenticator
c.Authenticator.whitlist = {'menahappy', 'Menshawi', 'menshawi'}
c.Authenticator.admin_users = {'Menshawi', 'menshawi'}

from dockerspawner import DockerSpawner
c.JupyerHub.spawner_class = DockerSpawner

import netifaces
docker0 = netifaces.ifaddresses('docker0')
docker0_ipv4 = docker0[netifaces.AF_INET][0]
c.JupyterHub.hub_ip = docker0_ipv4['addr']

DockerSpawner.container_image = 'jupyterhub/singleuser'
