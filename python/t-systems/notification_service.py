import copy
import threading

def synchronized_method(method):
	
	outer_lock = threading.Lock()
	lock_name = "__"+method.__name__+"_lock"+"__"

	def sync_method(self, *args, **kws):
		with outer_lock:
			if not hasattr(self, lock_name): setattr(self, lock_name, threading.Lock())
			lock = getattr(self, lock_name)
			with lock:
				return method(self, *args, **kws)  

	return sync_method


# SINGLETON FOR THE PLAN CONFIG
class PlanConfig:

	shared_state = {}

	def __init__(self):
		if PlanConfig.shared_state:
			pass
		else:
			# CREATE A MAP OF THE PLAN CONFIG HERE. IN CASE OF SPRING BOOT, THIS CAN BE DONE 
			# IN THE @POSTCONSTRUCT STEP AND A GLOBAL MAP CAN BE with @COMPONENT
			# Query the Models Table to find the different subscription models herePlanConfig
			plans = {
				1 : { 
				'name': '$49/Month Silver',
				'notification_types' : ['email'],
				'total_notification': 1000000
				},
				2 : { 
				'name': '$99/Month Silver',
				'notification_types' : ['email', 'sms'],
				'total_notification': 10000000
				}
			}
			PlanConfig.shared_state = plans


class Notification:

	notifications = []

	def __init__(self, data, to_user, from_user, notification_type):
		self.data = data
		self.to_user = to_user
		self.from_user = from_user
		self.notification_type = notification_type

	def send(self):
		print "Sent Notification"



class Client:

	def __init__(self):
		self.id = None
		self.plan = None

	def set_id(self, id):
		self.id = id

	def set_plan(self, plan_id):
		plans = PlanConfig.shared_state
		# POST
		# {  'plan_id':  }
		self.plan = copy.deepcopy(plans.get(plan_id))

	@synchronized_method
	def check_if_plan_active(self):
		status = True
		if not self.plan.get('total_notification'):
			status = False
		return status

	@synchronized_method
	def decrement_count(self):
		self.plan['total_notification'] -= 1

	def check_if_notification_type_allowed(self, notification_type):
		status = True
		if plan_type not in self.plan.get('notification_type'):
			status = False
		return status
			

	def send_notification(self, data, to_user, from_user, notification_type):
		if self.check_if_plan_active():
			notification = Notification(data, to_user, from_user, notification_type)
			notification.send()
			self.decrement_count()
			print self.plan
		else:
			print "Plan Exhausted"

PlanConfig()
client = Client()
client.set_id(1)
client.set_plan(1)
client.send_notification('a', 1, 2, 'email')
client.send_notification('a', 1, 2, 'email')
client.send_notification('a', 1, 2, 'email')