########################################################################################################################
# IMPORTS
########################################################################################################################
from datetime import datetime
from peewee import SqliteDatabase, Model, CharField, IntegerField, DateTimeField, TextField, ForeignKeyField, \
    FloatField, BigIntegerField, Check, BooleanField
    
########################################################################################################################
# Peewee init
########################################################################################################################
db_connection = SqliteDatabase("igg.db")
db_connection.connect()


fn_sql_auto_update = """
CREATE OR REPLACE FUNCTION update_modified_column()    
RETURNS TRIGGER AS $$
BEGIN
    NEW.ts_modified = (now() at time zone 'utc');
    RETURN NEW;    
END;
$$ language 'plpgsql';
"""


########################################################################################################################
# CLASSES
########################################################################################################################

class BaseModel(Model):
    class Meta:
        database = db_connection

class RudicsPipeNode(BaseModel):
    """Model for RUDICS client
    ts_created -- Pipe entry timestamp
    ts_modified -- Pipe modification timestamp
    address -- address of rudics-pipe client
    active  -- whether rudics pipe is valid
    """
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    address = CharField(max_length=64, unique=True)
    active = BooleanField(default=True)

class Certificate(BaseModel):
    """Model for certificates
    ts_created    -- Timestamp of certificate entry
    ts_modified   -- Timestamp of certificate modification
    commonname    -- common name of certificate taken from subject element
    not_before    -- certificate date usage boundary
    not_after     -- certificate date usage boundary
    digest        -- SHA1 digest of certificate
    active        -- status of certificate
    dest_id       -- Airborne destination id.
    """
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    commonname = CharField(unique=True)
    not_before = DateTimeField(default=datetime.utcnow)
    not_after = DateTimeField()
    digest = CharField(unique=True, null = True)
    active = BooleanField(default=False)
    dest_id = IntegerField(unique=True, null = True)

class GroundNode(Model):
    """Model for ground nodes

    address  -- address of ground node
    interface -- interface used by ground node
    """
    address = CharField(max_length=64)
    interface = CharField()

    class Meta:
        database = db_connection
        indexes = ((('address', 'interface'), True),)


class ADBUser(Model):
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    address = CharField(max_length=64)
    password = CharField()
    active = BooleanField(default=True)
    class Meta:
        database = db_connection
        indexes = ((('address', 'password'), True),)

class ThirdParty(BaseModel):
    """Model for third party entity
    ts_created      -- timestamp of thirdparty entry
    ts_modified     -- timestamp of thirdparty modification
    certificate     -- certificate used by this third party
    cipherkey       -- cipherkey of message
    initvector      -- initial vector used during enciphering
    quota           -- monthly quota for this thirdparty
    priority        -- priority of messages coming form this thirdparty
    sbd_retry_delay -- sbd_receive retry delay attempt
    sbd_retry_times -- sbd_receive count of maximum retry
    sbd_timeout     -- sbd_receive message lifetime in seconds
    sor_retry_delay -- sor_send retry delay attempt
    sor_retry_times -- sor_send count of maximum retry
    sor_timeout     -- sor_send message lifetime in seconds
    active          -- thirdparty activation flag
    """
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    certificate = ForeignKeyField(Certificate)
    cipherkey = CharField(max_length=8)
    initvector = CharField(max_length=8)
    quota = IntegerField(default=4194304)
    priority = IntegerField(default=50, constraints=[Check('priority >= 1'), Check('priority <= 100')])
    sbd_retry_delay = IntegerField(default=30)
    sbd_retry_times = IntegerField(default=100)
    sbd_timeout = IntegerField(default=3600, constraints=[Check('sbd_timeout <= 86400')])
    sor_retry_delay = IntegerField(default=30)
    sor_retry_times = IntegerField(default=100)
    sor_timeout = IntegerField(default=3600, constraints=[Check('sor_timeout <= 86400')])
    active = BooleanField(default=True)

class ThirdPartyNode(Model):
    """Model for third-party nodes
    ts_started -- time-stamp of node entry
    ts_modified -- time-stamp of node update
    address    -- address of a third-party node
    group      -- name of third-party entity where this node belong to
    active     -- activation of third-party-node
    """
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    address = CharField(max_length=64)
    group = ForeignKeyField(ThirdParty)
    active = BooleanField(default=False)

    class Meta:
        database = db_connection
        indexes = ((('address', 'group'), True),)

class Airline(BaseModel):
    """Model for airline
    ts_created -- airline entry timestamp
    ts_modified -- airline modify timestamp
    name -- name of airline
    """
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    name = CharField(unique=True)

class Aircraft(Model):
    """Model for aircrafts
    ts_created -- aircraft entry timestamp
    ts_updated -- aircraft update timestamp
    tailnum   -- tail number of aircraft
    group     -- reference to airline
    sbd_mode  -- SBD API mode of aircraft
    sbd_thres -- messages longer than this value will be sent using RUDICS API
    active    -- aircraft entry activation flag
    """
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    tailnum = CharField()
    group = ForeignKeyField(Airline)
    sbd_mode = IntegerField(default=2,
                            choices=((0, 'always disabled'),
                                     (1, 'enabled but subject to quota'),
                                     (2, 'always enabled')))
    sbd_thres = IntegerField(default=240)
    active = BooleanField(default=False)

    class Meta:
        database = db_connection
        indexes = ((('tailnum', 'group'), True),)

class MessageCounter(BaseModel):
    dst = ForeignKeyField(Aircraft)
    counter = IntegerField(default=1, constraints=[Check('counter >= 1'), Check('counter <= 65535')])

class AircraftNode(BaseModel):
    """Model for aircraft communication nodes
    ts_created -- Timestamp of aircraft-node entry
    ts_modified -- Timestamp of aircraft-node update
    imei       -- IMEI number of the aircraft-communication-node
    msisdn     -- MSISDN number of the aircraft-communication-node
    group      -- aircraft where this communication-node belong to
    mode       -- mode of ISU
    """
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    group = ForeignKeyField(Aircraft, null=True)
    imei = CharField(unique=True, max_length=15)
    msisdn = CharField(null=True, max_length=15)
    mode = IntegerField(default=0,
                                choices=((0, 'ISU is inactive'),
                                         (1, 'ISU is primary'),
                                         (2, 'ISU is secondary')))

class AircraftMsg(BaseModel):
    """Model for messages received from aircraft

    ts_received  -- time the message received from aircraft
    ts_sent      -- time the message sent to third-party    
    src          -- communication-node of aircraft used to send this message
    dst          -- third-party destination of this message
    msg_id       -- identification number of the message
    ack          -- acknowledge flag
    payload      -- message payload
    method       -- the method used while receiving this message
    status       -- status of the message
    unique_id    -- the unique id of sbd_receive sent to thirdparty client
    raw_length   -- raw length of PDU
    retry_count  -- count of retry done by IGG
    remarks      -- additional remark
    """
    #ts_received = DateTimeField(default=datetime.utcnow)
    ts_received = DateTimeField(default=datetime.now)
    ts_sent = DateTimeField(null=True)
    src = ForeignKeyField(AircraftNode)
    dst = ForeignKeyField(ThirdParty, null=True)
    msg_id = IntegerField(null=True, constraints=[Check('msg_id >= 0'), Check('msg_id <= 65535')])
    ack = BooleanField(default=False, null=True)
    payload = TextField()
    rx_method = CharField(max_length=1, default='S', choices=(('R', 'RUDICS'), ('S', 'SBD')))
    status = IntegerField(default=0, choices=((0, 'not sent'),
                                                           (1, 'sending'),
                                                           (2, 'sent and replied'),
                                                           (3, 'failed'),
                                                           (45, 'timeout')))
    unique_id = IntegerField(default=1)
    raw_length = IntegerField()
    retry_count = IntegerField(default=0)
    remarks = CharField(null=True)

class ThirdPartyMsg(BaseModel):
    """Model for messages received from third-party

    ts_received    -- time the message received from aircraft
    ts_sent        -- time the message sent to aircraft
    ts_fwd         -- time SOR_SENT received
    ts_ack         -- time SOR_ACK received
    src            -- third-party node used to send this message
    dst            -- aircraft destination of this message
    msg_id         -- identification number of the message
    ack            -- indicating this message requires acknowledge
    payload        -- message payload
    status         -- status of the message
    error          -- indicating that the message is error
    retry_count    -- count of sending attempt
    remarks        -- additional remark
    """
    ts_received = DateTimeField(default=datetime.utcnow)
    ts_sent = DateTimeField(null=True)
    ts_fwd = DateTimeField(null=True)
    ts_ack = DateTimeField(null=True)
    src = ForeignKeyField(ThirdPartyNode)
    dst = ForeignKeyField(Aircraft, null=True)
    msg_id = IntegerField(null=True, constraints=[Check('msg_id >= 0'), Check('msg_id <= 65535')])
    ack = BooleanField(default=False, null=True)
    payload = TextField()
    tx_method = CharField(max_length=1, default='S', choices=(('R', 'RUDICS'), ('S', 'SBD')))
    status = IntegerField(default=0, choices=((0, 'not sent'),
                                              (1, 'sent and replied'),
                                              (2, 'forwarded'),
                                              (3, 'forwarded and acknowledged'),
                                              (4, 'failed'),
                                              (5, 'expired')))
    retry_count = IntegerField(default=1)
    remarks = CharField(null=True)

class UplinkTraffic(BaseModel):
    """Model for thirdparty trafic
    ts_received -- the time message being received
    ts_sent     -- the time message being sent
    src         -- third-party-node sending the traffic
    dst         -- aircraft-node receiving the traffic
    usage       -- traffic length
    method      -- sending method
    """
    ts_received = DateTimeField()
    ts_sent = DateTimeField(default=datetime.utcnow)
    src = ForeignKeyField(ThirdPartyNode)
    dst = ForeignKeyField(AircraftNode)
    usage = IntegerField()
    method = CharField(max_length=1,
                            default='S',
                            choices=(('R', 'RUDICS'),
                                        ('S', 'SBD')))

class DownlinkTraffic(BaseModel):
    """Model for aircraft traffic usage

    ts_sent        -- the time message being sent
    src            -- aircraft-node sending the traffic
    dst            -- third-party-node receiving the traffic
    usage          -- traffic length
    method         -- reception method used
    """
    ts_received = DateTimeField()
    ts_sent = DateTimeField(default=datetime.utcnow)
    src = ForeignKeyField(AircraftNode)
    dst = ForeignKeyField(ThirdPartyNode)
    usage = IntegerField()
    method = CharField(max_length=1,
                               default='S',
                               choices=(('R', 'RUDICS'),
                                        ('S', 'SBD')))

class AircraftTrigger(BaseModel):
    """Model for aircraft trigger event
    ts_triggered    --- trigger requested time-stamp
    ts_connected    --- aircraft connected time-stamp
    aircraft        --- aircraft being triggered
    timeout         --- whether trigger entry is timeout
    """
    ts_triggered = DateTimeField(default=datetime.utcnow)
    ts_connect = DateTimeField(null=True)
    aircraft = ForeignKeyField(Aircraft)
    timeout = BooleanField(default=False)

class TriggerCounter(BaseModel):
    aircraft = ForeignKeyField(Aircraft)
    counter = IntegerField(default=0)

class DhcpLease(BaseModel):
    """Model for DHCP leasing

    ip         -- integer representation of IP address
    ip_str     -- dotted representation of IP address
    host       -- link to AircraftNode / GroundNode model
    ts_set     -- timestamp the ip starts being leased
    ts_removed -- timestamp the ip starts being collected
    type       -- type of IP address leasing recepient
    tx_bytes   -- transmitted bytes
    rx_bytes   -- received bytes
    """
    ip = IntegerField()
    ip_str = CharField(max_length=64)
    host = IntegerField()
    ts_set = DateTimeField(default=datetime.utcnow)
    ts_removed = DateTimeField(null=True)
    type = CharField(max_length=1,
                            choices=(('G', 'Ground'),
                                     ('A', 'Aircraft')))
    tx_bytes = IntegerField(default=0)
    rx_bytes = IntegerField(default=0)

class SBDEventCache(BaseModel):
    ts_received = DateTimeField(default=datetime.utcnow)
    src = ForeignKeyField(ThirdParty)
    msg = ForeignKeyField(ThirdPartyMsg)
    event = CharField(choices=(('SBD_SENT', 'message sent'),
                                 ('SBD_ACK', 'message sent and replied'),
                                 ('SBD_FAILED', 'failed'),))
    fetched = BooleanField(default=False)
    class Meta:
        database = db_connection
        indexes = ((('src', 'msg', 'event'), True),)

class SOREventCache(Model):
    ts_received = DateTimeField(default=datetime.utcnow)
    src = ForeignKeyField(Aircraft)
    msg = ForeignKeyField(AircraftMsg)
    event = CharField(choices=(('SOR_SENT', 'message sent'),
                               ('SOR_ACK', 'message sent and replied'),
                               ('SOR_FAILED', 'mesage failed')))
    fetched = BooleanField(default=False)

    class Meta:
        database = db_connection
        indexes = ((('src', 'msg', 'event'), True),)

class ExceptionNotifications(BaseModel):
    host_name = CharField()
    host_addr = CharField()
    ts_created = DateTimeField()
    ts_sent = DateTimeField(null=True)
    filename = CharField()
    module = CharField()
    reason = CharField()
    dump = TextField(null=True)

class AllocationNotifications(BaseModel):
    aircraft = ForeignKeyField(Aircraft)
    ts_created = DateTimeField()
    ts_sent = DateTimeField(null=True)
    pri_isu = ForeignKeyField(AircraftNode, related_name='primary')
    sec_isu = ForeignKeyField(AircraftNode, related_name='secondary', null=True)
    mode = CharField()

class OperationalNotifications(BaseModel):
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_sent = DateTimeField(null=True)
    remark = TextField()

class MOMessages(BaseModel):
    ts_created = DateTimeField(default=datetime.utcnow)
    msg_type = CharField(null = True)
    version = IntegerField()
    cdrref = BigIntegerField()
    imei = CharField(max_length=15)
    mo_status = CharField()
    momsn = IntegerField()
    mtmsn = IntegerField()
    tstamp = IntegerField()
    latitude = FloatField(null=True)
    longitude = FloatField(null=True)
    radius = FloatField(null=True)
    payload = TextField()

class MTMessages(BaseModel):
    ts_created = DateTimeField(default=datetime.utcnow)
    msg_type = CharField()
    dst = ForeignKeyField(AircraftNode)
    tp_msg = ForeignKeyField(ThirdPartyMsg, null=True)
    ac_msg = ForeignKeyField(AircraftMsg, null=True) 
    mt_msg_id = IntegerField()
    auto_id = IntegerField()
    mt_status = IntegerField()
    payload = TextField()

class FTPUsers(BaseModel):
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    username = CharField(unique=True)
    password = CharField()

class FTPClients(BaseModel):
    ts_created = DateTimeField(default=datetime.utcnow)
    ts_modified = DateTimeField(null = True)
    address = CharField(max_length=64, unique=True)

class SBDAPISessions(BaseModel):
    ts_connected = DateTimeField(default = datetime.utcnow)
    ts_closed    = DateTimeField(null = True)
    node = ForeignKeyField(ThirdPartyNode)
    remark = TextField(null = True)

class RUDICSSessions(BaseModel):
    ts_connected = DateTimeField(default = datetime.utcnow)
    ts_closed    = DateTimeField(null = True)
    node = ForeignKeyField(AircraftNode)
    ip_gnd = CharField()
    ip_ac = CharField()
    tx_bytes = IntegerField(default = 0)
    rx_bytes = IntegerField(default = 0)   
    remark = TextField(null = True) 
    
def create_tables():
    RudicsPipeNode.create_table(True)
    Certificate.create_table(True)
    GroundNode.create_table(True)
    ADBUser.create_table(True)
    ThirdParty.create_table(True)
    ThirdPartyNode.create_table(True)
    Airline.create_table(True)
    Aircraft.create_table(True)
    MessageCounter.create_table(True)
    AircraftNode.create_table(True)
    AircraftMsg.create_table(True)
    ThirdPartyMsg.create_table(True)
    UplinkTraffic.create_table(True)
    DownlinkTraffic.create_table(True)
    AircraftTrigger.create_table(True)
    TriggerCounter.create_table(True)
    DhcpLease.create_table(True)
    SBDEventCache.create_table(True)
    SOREventCache.create_table(True)
    ExceptionNotifications.create_table(True)
    AllocationNotifications.create_table(True)
    OperationalNotifications.create_table(True)
    MOMessages.create_table(True)
    MTMessages.create_table(True)
    FTPUsers.create_table(True)
    FTPClients.create_table(True)
    SBDAPISessions.create_table(True)
    RUDICSSessions.create_table(True)
    
    try:
        db_connection.execute_sql(fn_sql_auto_update)
    except Exception as e:
        print "failed to create function, %s" % e
        db_connection.rollback()
    
    print "adding ts_modified auto trigger"
    for name in ('rudicspipenode', 'certificate', 'adbuser', 'thirdparty', 'thirdpartynode', 'airline', 'aircraft', 
                 'aircraftnode', 'ftpusers', 'ftpclients'):
        cmd = 'CREATE TRIGGER update_%s_modtime BEFORE UPDATE ON %s FOR EACH ROW EXECUTE PROCEDURE update_modified_column();'
        try:
            db_connection.execute_sql(cmd % (name, name))
        except Exception as e:  # @UnusedVariable
            db_connection.rollback()
            print 'failed to add ts_modified auto trigger, %s' % e

    db_connection.close()

#create_tables()