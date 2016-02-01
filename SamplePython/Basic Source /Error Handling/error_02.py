try:
    kamus = {'TailNum':}
    peer = self.transport.getPeer()
    tailnum = request.kwargs['TailNum']
    ack = request.kwargs['Ack']
    payload = request.kwargs['Payload']

    assert isinstance(tailnum, (str, unicode)), 'TailNum'
    assert isinstance(ack, bool), 'Ack'
    assert isinstance(payload, (str, unicode)), 'Payload'

    if not tailnum : raise ValueError('TailNum')
    if not payload:  raise ValueError('Payload')

    decoded = b64decode(payload)
    if len(decoded) > MAX_SBD_SEND_LENGTH:
        raise SBDErrorLength()
    elif self.transport.getPeerCertificate().has_expired():
        raise CertificateErrorExpired()
    else:
        self.processMessage(request, tailnum, ack, payload)
except KeyError as e:
    message = 'Bad sbd_send request from (commonname = %s, addr = %s:%d), missing %s'
    self.log.warning(message % (self.commonname, peer.host, peer.port, e))
    self.storeSBDMessage(line, 'missing parameter %s' % e)
    self.sendError(request, errcode.JSONRPCErrorCode(errcode.JSONRPC_ERRCODE__SBD_SEND__MISING_ARGUMENT))
    self.disconnectLater()
except AssertionError as e:
    message = 'bad sbd_send request from (commonname = %s, addr = %s:%d), bad argument type'
    self.log.warning(message % (self.commonname, peer.host, peer.port))
    self.storeSBDMessage(line, 'bad parameter type %s' % e)
    self.sendError(request, errcode.JSONRPCErrorCode(errcode.JSONRPC_ERRCODE__SBD_SEND__ARGUMENT_TYPE))
    self.disconnectLater()
except ValueError as e:
    message = 'bad sbd_send request from (commonname = %s, addr = %s:%d), bad argument value %s'
    self.log.warning(message % (self.commonname, peer.host, peer.port, e))
    self.storeSBDMessage(line, 'bad argument value %s' % e)
    self.sendError(request, errcode.JSONRPCErrorCode(errcode.JSONRPC_ERRCODE__SBD_SEND__ARGUMENT_VALUE))
    self.disconnectLater()
except TypeError as e:
    message = 'bad sbd_send request from (commonname = %s, addr = %s:%d), bad payload value'
    self.log.warning(message % (self.commonname, peer.host, peer.port))
    self.storeSBDMessage(line, 'bad payload')
    self.sendError(request, errcode.JSONRPCErrorCode(errcode.JSONRPC_ERRCODE__SBD_SEND__PAYLOAD))
    self.disconnectLater()
except CertificateErrorExpired as e:
    message = 'bad sbd_send request from (commonname = %s, addr = %s:%d), certificate expired'
    self.log.warning(message % (self.commonname, peer.host, peer.port))
    self.storeSBDMessage(payload, 'certificate expired')
    self.sendError(request, errcode.JSONRPCErrorCode(errcode.JSONRPC_ERRCODE__SBD_SEND__CERT_EXPIRED))
    self.disconnectLater()
except SBDErrorLength as e:
    message = 'bad sbd_send request from (commonname = %s, addr = %s:%d), length exceeded'
    self.log.warning(message % (self.commonname, peer.host, peer.port))
    self.storeSBDMessage(payload, 'length exceeded')
    self.sendError(request, errcode.JSONRPCErrorCode(errcode.JSONRPC_ERRCODE__SBD_SEND__LENGTH))
    self.disconnectLater()
except Exception as e:
    notify_exception(self.log, 'failed to process sbd_send')
    self.sendError(request, errcode.JSONRPCErrorCode(errcode.JSONRPC_ERRCODE__SBD_SEND__SERVER_FAULT))
    self.disconnectLater()
