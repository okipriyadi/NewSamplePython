def __transfer(self, source, target, listener):
        done = False
        try:
            fsource = open(source, "rb")
            ftarget = open("{0}{1}".format(target, repository.PARTIALLY_DOWNLOADED_EXT), "wb")
            
            # total size of files
            size = os.stat(source).st_size
            
            if size / repository.BUFFER_SIZE == 0:
                buffer_size = repository.MIN_BUFFER_SIZE
            else:
                buffer_size = repository.BUFFER_SIZE
            
            if(listener is not None):
                listener.start(source, target, size)
    
            block_pos = 0
            while True and not self.close:
                cur_block = fsource.read(buffer_size)
    
                if cur_block:
                    block_pos += len(cur_block)
                    ftarget.write(cur_block)
                    if(listener is not None):
                        listener.update(block_pos)
                else:
                    ftarget.flush()
                    os.fsync(ftarget.fileno())
                    done = True
                    break
    
            if(listener is not None):
                listener.end()
        finally:
            try:
                fsource.close()
            except:
                pass
            try:
                ftarget.close()
            except:
                pass
            if done:
                # check size
                if os.stat(ftarget.name).st_size != size:
                    try:
                        os.remove(ftarget.name)
                    except:
                        pass
                    raise Exception("Size doesn't match")
                
                try:
                    os.remove(target)
                except:
                    pass
                os.rename(ftarget.name, target)
                
        # force to remove .part file
        part_file = "{0}{1}".format(target, repository.PARTIALLY_DOWNLOADED_EXT)
        if os.path.exists(part_file):
            try:
                os.remove(part_file)
            except Exception as e:
                pass
    pass
    # end transfer
