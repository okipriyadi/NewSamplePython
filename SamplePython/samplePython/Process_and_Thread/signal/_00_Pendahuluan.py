"""
signal adalah fitur dari system operasi yang menyediakan pemberitahuan kepada sebuah program 
terhadap sebuah event dan membuatnya terhandle dengan asynchronously. signal dapat digenerate dari 
sistem itu sendiri atau dikirim dari satu process ke process yang lain. Signal akan meng-interupt
aliran (regular-flow) program, ini akan memungkinkan beberapa operasi (terutama I/O) menghasilkan error
jika sebuah signal didapat di tengah sebuah process.

signal diidentifikasi sebagai sebuah integer yang didefinisikan di system operasi, tepatnya C header.


Cari tau perbedaan
SIGHUP     ( 1): SIG_DFL
SIGINT     ( 2): <built-in function default_int_handler>             (signal INTERUPT)
SIGQUIT    ( 3): SIG_DFL
SIGILL     ( 4): SIG_DFL
SIGTRAP    ( 5): SIG_DFL
SIGIOT     ( 6): SIG_DFL
SIGBUS     ( 7): SIG_DFL
SIGFPE     ( 8): SIG_DFL
SIGKILL    ( 9): SIG_DFL
SIGUSR1    (10): SIG_DFL
SIGSEGV    (11): SIG_DFL
SIGUSR2    (12): SIG_DFL
SIGPIPE    (13): SIG_IGN 
SIGALRM    (14): <function alarm_received at 0x7fcbd0b75f50>        (signal ALARM)
SIGTERM    (15): SIG_DFL
SIGCLD     (17): SIG_DFL
SIGCONT    (18): SIG_DFL
SIGSTOP    (19): SIG_DFL
SIGTSTP    (20): SIG_DFL
SIGTTIN    (21): SIG_DFL
SIGTTOU    (22): SIG_DFL
SIGURG     (23): SIG_DFL
SIGXCPU    (24): SIG_DFL
SIGXFSZ    (25): SIG_IGN 
SIGVTALRM  (26): SIG_DFL
SIGPROF    (27): SIG_DFL
SIGWINCH   (28): SIG_DFL
SIGPOLL    (29): SIG_DFL
SIGPWR     (30): SIG_DFL
SIGSYS     (31): SIG_DFL
SIGRTMIN   (34): SIG_DFL
SIGRTMAX   (64): SIG_DFL
SIGIGN                                                                (signal IGNORE)

"""