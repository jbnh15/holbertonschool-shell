import os
def fix_file(path, content):
    with open(path, "wb") as f:
        f.write(content.encode("utf-8").replace(b"\r\n", b"\n"))

# Root README
fix_file("README.md", "# holbertonschool-shell\n")

# Basics
if not os.path.exists("basics"): os.makedirs("basics")
fix_file("basics/README.md", "# basics\n")

# Permissions
if not os.path.exists("permissions"): os.makedirs("permissions")
fix_file("permissions/README.md", "# permissions\n")

# I/O Redirections
if not os.path.exists("io_redirections_and_filters"): os.makedirs("io_redirections_and_filters")
fix_file("io_redirections_and_filters/README.md", "# io_redirections_and_filters\n")

# Init files
if not os.path.exists("init_files_variables_and_expansions"): os.makedirs("init_files_variables_and_expansions")
fix_file("init_files_variables_and_expansions/README.md", "# init_files_variables_and_expansions\n")
