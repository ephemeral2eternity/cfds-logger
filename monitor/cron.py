from django_cron import CronJobBase, Schedule
from monitor.monitor_utils import *

class client_monitor_job(CronJobBase):
	"""
	Cron Job that checks the availability of clients's agent mode and update the availability of clients into the db.
	"""

	# Run every 20 minutes
	run_every = 60
	schedule = Schedule(run_every_mins=run_every)
	code = 'monitor.cron.client_monitor_job'

	# This will be executed every 20 minutes
	def do(self):
		check_client_availability()
