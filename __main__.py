from pathlib                      import Path
from rohdeschwarz.instruments.vna import Vna


# paths
root_path = Path(__file__).parent.resolve()
log_file  = str(root_path / 'vna.log')
set_file  = str(root_path / 'sets' / 'set.znxml')


# IP address
address = '192.168.86.192'


# create Vna instance
vna = Vna()

# log
vna.open_log(log_file)
vna.print_info()

# connect to instrument (no visa)
vna.open_tcp(address)

# alternatively, using pyvisa:
# vna.open('gpib', 20)

# preset and clear errors
vna.clear_status()
vna.preset()
vna.pause()

# create an interesting setup
# to save
ch1 = vna.channel(1)
ch1.start_frequency_Hz = 1.0e9
ch1.stop_frequency_Hz  = 2.0e9
ch1.points             = 401

trc1 = vna.trace('Trc1')
trc1.parameter = 'S11'

index = vna.create_diagram()

name = vna.create_trace()
trc2 = vna.trace(name)
trc2.parameter = 'S21'
trc2.diagram   = index

# save
vna.save_active_set_locally(set_file)
vna.pause()

# preset (again)
vna.preset()
vna.pause()

# open
vna.open_set_locally(set_file)

# errors?
errors = vna.errors
for error in errors:
    code    = error[0]
    message = error[1]
    print(f"error {code}: '{message}'")
vna.clear_status()
