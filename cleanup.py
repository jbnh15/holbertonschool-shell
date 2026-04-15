import os
def fix_file(path, content):
    with open(path, "wb") as f:
        f.write(content.encode("utf-8").replace(b"\r\n", b"\n"))

# Fix task 0 in basics
fix_file("basics/0-current_working_directory", "#!/bin/bash\npwd\n")

# Cleanup init_files
if os.path.exists("init_files_variables_and_expansions/1-hello_betty") and os.path.exists("init_files_variables_and_expansions/1-hello_you"):
    os.remove("init_files_variables_and_expansions/1-hello_betty")

if os.path.exists("init_files_variables_and_expansions/10-love_exponent_ans") and os.path.exists("init_files_variables_and_expansions/10-love_exponent_breath"):
    os.remove("init_files_variables_and_expansions/10-love_exponent_ans")
