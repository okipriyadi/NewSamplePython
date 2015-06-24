# Name of the library, or application
SPAWNER_NAME = spawner
MAJOR_NUM = 0
MINOR_NUM = 1
REV_NUM = 0
target=$(SPAWNER_NAME)

#====================================================================================
#=== Changeable Setting For Different Platform, Library Path and Installation Path.


PREPOCESSOR = 
STAGING_DIR =


# Crosscompile.
# For compilation on the host, CROSS_COMPILE should be set to empty.
# For cross compiler, the value should be set to the appropriate tool chain prefixes.
# eg. for ELDK the value would be set to.
#
BUILD=$(shell uname -m)

STAGING_DIR=$(shell cd ~;pwd)/staging

ifeq ($(host),)

	CROSS_COMPILE=
	INCLUDE_DIR=/usr/include/
	INCLUDE_LIB=/usr/lib/i386-linux-gnu/
	ROOT_PATH=
	# Translated g++ command
	CXX = $(CROSS_COMPILE)gcc
	# Translated gcc command.
	CC = $(CROSS_COMPILE)gcc
	AS = $(CROSS_COMPILE)as
	STAGING_DIR_LIB=$(STAGING_DIR)/usr/lib
	STAGING_DIR_INCLUDE=$(STAGING_DIR)/usr/include	
	
	TARGET = native
	TARGET_ARCH = i386
else
	ifeq ($(host),armel)
		CROSS_COMPILE=arm-linux-gnueabi-
		INCLUDE_DIR=/usr/arm-linux-gnueabi/include/
		INCLUDE_LIB=/usr/arm-linux-gnueabi/lib/
	    STAGING_DIR_LIB=$(STAGING_DIR)/usr/arm-linux-gnueabi/lib
        STAGING_DIR_INCLUDE=$(STAGING_DIR)/usr/arm-linux-gnueabi/include
		ROOT_PATH=
		# Translated g++ command
		CXX = $(CROSS_COMPILE)gcc 
		# Translated gcc command.
		CC = $(CROSS_COMPILE)gcc
		AS = $(CROSS_COMPILE)as
		LIBS=-Wl,-rpath -Wl,/usr/arm-linux-gnueabi/lib
		
		TARGET = cs
		TARGET_ARCH = $(host)
	endif
	
	ifeq ($(host),armhf)
		CROSS_COMPILE=arm-linux-gnueabihf-
		INCLUDE_DIR=/usr/arm-linux-gnueabihf/include/
		INCLUDE_LIB=/usr/arm-linux-gnueabihf/lib/
		STAGING_DIR_INCLUDE=$(STAGING_DIR)/usr/arm-linux-gnueabihf/include
        STAGING_DIR_LIB=$(STAGING_DIR)/usr/arm-linux-gnueabihf/lib
		ROOT_PATH=
		# Translated g++ command
		CXX = $(CROSS_COMPILE)gcc 
		# Translated gcc command.
		CC = $(CROSS_COMPILE)gcc
		AS = $(CROSS_COMPILE)as
		LIBS=-Wl,-rpath -Wl,/usr/arm-linux-gnueabihf/lib

		TARGET = cs
		TARGET_ARCH = $(host)

	endif
	
	ifeq ($(host),amd64)
		ifeq ($(BUILD),"x86_64")
			CROSS_COMPILE=
			INCLUDE_DIR=/usr/include/
			INCLUDE_LIB=/usr/lib/x86_64-linux-gnu/
	        STAGING_DIR_INCLUDE=$(STAGING_DIR)/usr/include
            STAGING_DIR_LIB=$(STAGING_DIR)/usr/lib
			ROOT_PATH=
			# Translated g++ command
			CXX = $(CROSS_COMPILE)gcc
			# Translated gcc command.
			CC = $(CROSS_COMPILE)gcc
			AS = $(CROSS_COMPILE)as
			LIBS=-Wl,-rpath -Wl,/usr/lib/x86_64-linux-gnu
		else
			CROSS_COMPILE=-m64
			INCLUDE_DIR=/usr/x86_64-linux-gnu/include/
			INCLUDE_LIB=/usr/x86_64-linux-gnu/lib/
			ROOT_PATH=
	        STAGING_DIR_INCLUDE=$(STAGING_DIR)/usr/x86_64-linux-gnu/include
            STAGING_DIR_LIB=$(STAGING_DIR)/usr/x86_64-linux-gnu/lib
			# Translated g++ command
			CXX = gcc $(CROSS_COMPILE)
			# Translated gcc command.
			CC = gcc $(CROSS_COMPILE)
			LIBS=-Wl,-rpath -Wl,/usr/x86_64-linux-gnu/lib
		endif
		
		TARGET = hs
		TARGET_ARCH = $(host)
	endif
endif

PREFIX=$(ROOT_PATH)

##################################################
## name of Debian package to be created
##################################################
VERSION = $(MAJOR_NUM).$(MINOR_NUM).$(REV_NUM)
PackageName = $(TARGET)-$(SPAWNER_NAME)_$(VERSION)_$(TARGET_ARCH)


#====================================================================================

# Set the file mode for all installed files.
CHMOD_MODE=g+w

# Includes parameters that is not in standard include paths

INCLUDE=-I./ 

ifeq ($(dummy),)
	DEFINE_SYMBOL=
else
	ifeq ($(dummy),true)
		DEFINE_SYMBOL=-DDUMMY_AID_LIB
	else
		DEFINE_SYMBOL=
	endif
endif

# Library search path that is not in standard library paths
LIB_PATHS= 

# Libraries that is need for compilation.
LIBS=

# Default library and include lookups
LD_FLAGS=  -L$(INCLUDE_LIB) -L$(STAGING_DIR_LIB)

CFLAGS= $(PREPROCESSOR) -O0 -g3 -Wall -c -fmessage-length=0 -funwind-tables -rdynamic

# PREFIXES
#PREFIX_LOCAL_LIB=$(PREFIX)/usr/local/lib
#PREFIX_INCLUDE=$(PREFIX)/include
#PREFIX_BIN=$(PREFIX)/usr/local/bin
PREFIX_LOCAL_LIB=usr/local/lib
PREFIX_INCLUDE=include
PREFIX_BIN=usr/local/bin


# Translated ranlib command
RANLIB = $(CROSS_COMPILE)ranlib

# List of all .cpp source files that part of the main source tree.
CXX_SOURCES = $(shell find ./src -name "*.cpp")
# List of all .c source files that part of the main source tree
CC_SOURCES = $(shell find . -name "*.c")
# List of all header files that part of the main source tree.
HEADER_FILES = $(shell find . -name "*.h")


PWD=$(shell pwd)
PackageDir=$(PWD)/$(PackageName)
INITDFile=
GAPINI=
STAPCFG=
VQARCFG=
VQARRAW=
RSYSLOG_CFG=


# Dynamic target definitions. Do not change.
CXX_OBJECTS=$(CXX_SOURCES:.cpp=.o)
CC_OBJECTS=$(CC_SOURCES:.c=.o)
TEST_OBJECTS = $(TEST_SOURCES:.cpp=.o)


# Unix Command List
CD=cd
CP=cp
CHMOD=chmod
MKDIR=mkdir
RM=rm
TOUCH=touch
SYMLNK=ln -s
DPKG-DEB=dpkg-deb
ECHO=echo
SED=sed


.PHONY : all install install-lib install-bintest uninstall fixowner clean package

all: $(target)

install: install-lib
install-dev: install-lib install-bintest install-header
install-lib: install-dir
	

install-header:install-dir 
	
	
install-bintest: install-dir


install-dir:
	$(MKDIR) -p $(PREFIX_INCLUDE)
	$(MKDIR) -p $(PREFIX_BIN)
	$(MKDIR) -p $(PREFIX_LOCAL_LIB)
	
uninstall:
	$(RM) -f $(PREFIX_BIN)/$(target)


fixowner:

	
clean:
	@$(RM) -f $(CXX_OBJECTS)  $(CC_OBJECTS) $(TEST_OBJECTS) 
	@$(RM) -f $(target) $(targettest)
	@$(RM) -rf $(TARGET)-$(SPAWNER_NAME)*
	
package: $(target)
	@$(MKDIR) -p $(PackageDir)/usr/sbin
	@$(MKDIR) -p $(PackageDir)/usr/lib
	@$(MKDIR) -p $(PackageDir)/usr/share/doc
	@$(MKDIR) -p $(PackageDir)/etc/init.d
	@$(MKDIR) -p $(PackageDir)/etc/$(target)
	
	#@$(CHMOD) 644 $(PackageDir)/etc/$(target)/*
		
	# Copying binary file ...
	@$(CP) $(target) $(PackageDir)/usr/sbin
	@$(CHMOD) +x $(PackageDir)/usr/sbin/$(target)
	
	# Copy DEBIAN files and rename the package name
	
	$(MKDIR) -p $(PackageDir)/DEBIAN
	
	@$(SED) 's/<PACKAGE-NAME>/$(TARGET)-$(SPAWNER_NAME)/g' <./DEBIAN/postinst > $(PackageDir)/DEBIAN/postinst
	
	@$(SED) 's/<PACKAGE-NAME>/$(TARGET)-$(SPAWNER_NAME)/g' <./DEBIAN/postrm > $(PackageDir)/DEBIAN/postrm
	
	@$(SED) 's/<PACKAGE-NAME>/$(TARGET)-$(SPAWNER_NAME)/g' <./DEBIAN/prerm > $(PackageDir)/DEBIAN/prerm
		
	# Updating the control file
	@$(SED) '/Package:/s/<PACKAGE>/$(TARGET)-$(SPAWNER_NAME)/g' <./DEBIAN/control > temp
	
	@$(SED) '/Version:/s/<VERSION>/$(VERSION)/g' <temp > temp1

	@$(SED) '/Architecture:/s/<ARCH>/$(TARGET_ARCH)/g' <temp1 > $(PackageDir)/DEBIAN/control
		
	@$(RM) -f temp*
	
	$(CHMOD) +x $(PackageDir)/DEBIAN/*
	
	$(CHMOD) 644 $(PackageDir)/DEBIAN/control
	
	dpkg-deb --build $(PackageDir)

$(STATICLIB) :

$(targetlib) :
	
	
$(target) : $(CC_OBJECTS) $(CXX_OBJECTS)
	$(CXX) $(DEFINE_SYMBOL) $(LD_FLAGS) $(LIB_PATHS) -o $@ $^ $(LIBS)

$(targettest) : $(TEST_OBJECTS) 



%.o : %.cpp
	$(CXX) $(CFLAGS) $(INCLUDE) -c $< -o $@

%.o : %.c
	$(CC) $(CFLAGS) $(INCLUDE) $(DEFINE_SYMBOL) -c $< -o $@

%.lo : %.c
	$(CC) $(CFLAGS) $(INCLUDE) -fpic -c $< -o $@
