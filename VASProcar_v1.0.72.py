
from _printMessages import PrintMessages

PrintMessages.authors_information()
PrintMessages.minimal_requirement_to_run()

# src directory to the main python codes
main_dir = 'src/'
run = main_dir + '_settings.py'
exec(open(run).read())
