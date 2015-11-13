from copy import deepcopy
from samplePython.asd import AircraftMsg, ThirdParty, Aircraft, Certificate, AircraftNode 
import time 
_arg_in = deepcopy(Aircraft.select(AircraftMsg.retry_count, Aircraft.tailnum,
                             Aircraft.id.alias('aircraft_id'),  # @UndefinedVariable
                             AircraftNode.id.alias('ac_node_id'), AircraftNode.imei,  # @UndefinedVariable
                             AircraftMsg.ts_received, AircraftMsg.msg_id, AircraftMsg.payload).join(AircraftNode).join(AircraftMsg).where((AircraftMsg.id == 2)).limit(1).dicts().first())  # @UndefinedVariable
_arg_out = deepcopy(Certificate.select(Certificate.active.alias('certificate_active'), Certificate.not_before, Certificate.not_after, Certificate.commonname, # @UndefinedVariable
                                       Certificate.id.alias('certificate_id'), ThirdParty.id.alias('thirdparty_id'), ThirdParty.active.alias('thirdparty_active'), ThirdParty.sor_retry_delay.alias('retry_delay'), ThirdParty.sor_retry_times.alias('retry_times'), ThirdParty.sor_timeout.alias('timeout')).join(ThirdParty).join(AircraftMsg).where(AircraftMsg.id == 2).limit(1).dicts().first())  # @UndefinedVariable


print _arg_in
print "==================================="
print _arg_out

time.sleep(5)
_arg_in2 = deepcopy(Aircraft.select(AircraftMsg.retry_count, Aircraft.tailnum,
                             Aircraft.id.alias('aircraft_id'),  # @UndefinedVariable
                             AircraftNode.id.alias('ac_node_id'), AircraftNode.imei,  # @UndefinedVariable
                             AircraftMsg.ts_received, AircraftMsg.msg_id, AircraftMsg.payload).join(AircraftNode).join(AircraftMsg).where((AircraftMsg.id == 2)).limit(1).dicts().first())  # @UndefinedVariable
_arg_out2 = deepcopy(Certificate.select(Certificate.active.alias('certificate_active'), Certificate.not_before, Certificate.not_after, Certificate.commonname, # @UndefinedVariable
                                       Certificate.id.alias('certificate_id'), ThirdParty.id.alias('thirdparty_id'), ThirdParty.active.alias('thirdparty_active'), ThirdParty.sor_retry_delay.alias('retry_delay'), ThirdParty.sor_retry_times.alias('retry_times'), ThirdParty.sor_timeout.alias('timeout')).join(ThirdParty).join(AircraftMsg).where(AircraftMsg.id == 2).limit(1).dicts().first())  # @UndefinedVariable

print _arg_in2
print "==================================="
print _arg_out2

time.sleep(5)
_arg_in3 = deepcopy(Aircraft.select(AircraftMsg.retry_count, Aircraft.tailnum,
                             Aircraft.id.alias('aircraft_id'),  # @UndefinedVariable
                             AircraftNode.id.alias('ac_node_id'), AircraftNode.imei,  # @UndefinedVariable
                             AircraftMsg.ts_received, AircraftMsg.msg_id, AircraftMsg.payload).join(AircraftNode).join(AircraftMsg).where((AircraftMsg.id == 2)).limit(1).dicts().first())  # @UndefinedVariable
_arg_out3 = deepcopy(Certificate.select(Certificate.active.alias('certificate_active'), Certificate.not_before, Certificate.not_after, Certificate.commonname, # @UndefinedVariable
                                       Certificate.id.alias('certificate_id'), ThirdParty.id.alias('thirdparty_id'), ThirdParty.active.alias('thirdparty_active'), ThirdParty.sor_retry_delay.alias('retry_delay'), ThirdParty.sor_retry_times.alias('retry_times'), ThirdParty.sor_timeout.alias('timeout')).join(ThirdParty).join(AircraftMsg).where(AircraftMsg.id == 2).limit(1).dicts().first())  # @UndefinedVariable

print _arg_in3
print "==================================="
print _arg_out3

time.sleep(5)