from fabric.api import run
import time
from helpers import conf
import digitalocean
from bitbucket.bitbucket import Bitbucket


def do_create_new(name=None):
	if name is None:
		name = 'test'
	
	droplet = digitalocean.Droplet(client_id=conf.do_client_id, api_key=conf.do_api_key,
                               name=name,
                               region_id=conf.region_id,  
                               image_id=conf.image_id,  
                               size_id=conf.size_id,  
                               backup_active=conf.backup_active)
	droplet.create()
	time.sleep(10)
	print(droplet)

def do_stop(name=None):
	if name is None:
		name = "test"

	_do_action(name, 'power_off')


def do_remove(name=None):
	if name is None:
		name = "test"

def _do_action(name, action, status = "active"):
	do_manager = digitalocean.Manager(client_id=conf.do_client_id, api_key=conf.do_api_key)
	droplets = do_manager.get_all_droplets()
	for droplet in droplets:
		if name == droplet.name and droplet.status == status:
			getattr(droplet,"action").__call__()
			

def do_backup():
	pass


# ['_Droplet__call_api', '__class__', '__delattr__', '__dict__', '__doc__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'api_key', 'backup_active', 'call_reponse', 'call_response', 'client_id', 'create', 'destroy', 'disable_backups', 'enable_backups', 'events', 'get_events', 'id', 'image_id', 'ip_address', 'load', 'name', 'power_cycle', 'power_off', 'power_on', 'private_ip_address', 'reboot', 'rebuild', 'region_id', 'reset_root_password', 'resize', 'restore', 'shutdown', 'size_id', 'ssh_key_ids', 'status', 'take_snapshot']