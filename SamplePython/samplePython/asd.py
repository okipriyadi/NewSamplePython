mo_header = Struct('mo_header',
UBInt32('cdrref'),
Bytes  ('imei', 15),
Enum(Byte('mo_status'),
                              success=0,
                                  truncated=1,
                                  bad_quality=2,
                                  timeout=10,
                                  too_large=12,
                                  link_loss=13,
                                  proto_anomaly=14,
                                  imei_prohibited=15),
                             UBInt16('momsn'),
                             UBInt16('mtmsn'),
                             UBInt32('tstamp'))

cdrref=randint(0, max_32), 
imei=self.imei, 
mo_status='success',
momsn=randint(0, max_16), 
mtmsn=randint(0, max_16),
tstamp=int(time())))


mo_location = Struct('mo_location',
                     
BitStruct('flags',
                               BitField('reserved', 4),
                               BitField("format_code", 2),
                               Flag('nsi'),
                               Flag('ewi')),
                     UBInt8   ('lat_deg'),  # 0 .. 90
                     UBInt16  ('lat_min'),  # 0 .. 59999
                     UBInt8   ('lon_deg'),  # 0 .. 120
                     UBInt16  ('lon_min'),  # 0 .. 59999
                     UBInt32  ('radius'))

(flags=Container(reserved=0, format_code=0, nsi=randint(0, 1), ewi=randint(0, 1)),
                                                          lat_deg=randint(0, 90), lat_min=randint(0, 59999),
                                                          lon_deg=randint(0, 180), lon_min=randint(0, 59999),
                                                          radius=randint(1, 2000)))


elements = GreedyRange(Struct('elements',
                              Enum(Byte('identifier'),
                                   mo_header=0x01,
                                   mo_payload=0x02,
                                   mo_location=0x03,
                                   mt_header=0x41,
                                   mt_payload=0x42,
                                   mt_confirm=0x44),
                              UBInt16('length'),
                              Bytes  ('payload', lambda ctx:ctx.length)))


encoded_elements = elements.build([Container(
                                             identifier='mo_header', 
                                             length=len(encoded_mo_header),
                                             payload=encoded_mo_header),
                                           
                                    Container(
                                              identifier='mo_payload', 
                                              length=len(self.payload),
                                              payload=self.payload),
                                    Container(
                                              identifier='mo_location', 
                                              length=len(encoded_mo_location),
                                              payload=encoded_mo_location)])


sbd_msg = Struct('message',
                 UBInt8 ('version'),
                 UBInt16('length'),
                 Bytes  ('payload', lambda ctx: ctx.length))


sbd_msg.build(Container(
                        version=1, 
                        length=len(encoded_elements), 
                        payload=encoded_elements))

        